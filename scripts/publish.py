#!/usr/bin/env python3
"""Pack skill directories, generate the well-known discovery index, and build the Pages site."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tarfile
from pathlib import Path

import yaml

from skill_pages import SkillPage, generate_site, parse_skill_page

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"
MAX_DESCRIPTION_LEN = 1024
SKIP_DIRS = {".github", "deploy", "dist", "scripts"}


def discover_skills(root: Path) -> list[Path]:
    skills: list[Path] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if child.name in SKIP_DIRS:
            continue
        if (child / "SKILL.md").is_file():
            skills.append(child)
    return skills


def parse_frontmatter(skill_dir: Path) -> dict:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{skill_dir.name}/SKILL.md is missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{skill_dir.name}/SKILL.md has invalid frontmatter")

    meta = yaml.safe_load(parts[1])
    if not isinstance(meta, dict):
        raise ValueError(f"{skill_dir.name}/SKILL.md frontmatter must be a mapping")

    return meta


def normalize_description(description: str, skill_name: str) -> str:
    text = " ".join(description.split())
    if not text:
        raise ValueError(f"{skill_name}: description is empty")
    if len(text) > MAX_DESCRIPTION_LEN:
        raise ValueError(
            f"{skill_name}: description is {len(text)} chars (max {MAX_DESCRIPTION_LEN})"
        )
    return text


def pack_skill(skill_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(output_path, "w:gz") as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                archive.add(path, arcname=path.relative_to(skill_dir).as_posix())


def sha256_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def release_asset_url(repo: str, tag: str, skill_name: str) -> str:
    return f"https://github.com/{repo}/releases/download/{tag}/{skill_name}.tar.gz"


def build_index(skills: list[dict], repo: str) -> dict:
    return {
        "$schema": SCHEMA,
        "releases": f"https://github.com/{repo}/releases",
        "skills": skills,
    }


def publish(version: str, repo: str, root: Path, dist_dir: Path, deploy_dir: Path) -> dict:
    skill_dirs = discover_skills(root)
    if not skill_dirs:
        raise RuntimeError("No skills found (expected top-level directories with SKILL.md)")

    index_skills: list[dict] = []
    site_skills: list[SkillPage] = []

    for skill_dir in skill_dirs:
        skill_page = parse_skill_page(skill_dir)
        meta = skill_page.meta
        skill_name = meta.get("name") or skill_dir.name
        if skill_name != skill_dir.name:
            print(
                f"warning: {skill_dir.name} frontmatter name={skill_name!r} "
                f"differs from directory name",
                file=sys.stderr,
            )

        description = normalize_description(skill_page.description, skill_dir.name)
        site_skills.append(
            SkillPage(
                dir_name=skill_page.dir_name,
                name=str(skill_name),
                description=description,
                meta=meta,
                body_md=skill_page.body_md,
            )
        )

        archive_path = dist_dir / f"{skill_dir.name}.tar.gz"
        pack_skill(skill_dir, archive_path)
        digest = sha256_digest(archive_path)

        index_skills.append(
            {
                "name": skill_dir.name,
                "type": "archive",
                "description": description,
                "url": release_asset_url(repo, version, skill_dir.name),
                "digest": digest,
            }
        )
        print(f"packed {skill_dir.name} -> {archive_path.name} ({digest})")

    index = build_index(index_skills, repo)
    index_path = deploy_dir / ".well-known" / "agent-skills" / "index.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {index_path.relative_to(root)}")

    generate_site(deploy_dir, site_skills, repo)

    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version",
        required=True,
        help="Release tag (with or without leading v), e.g. v0.1.0",
    )
    parser.add_argument(
        "--repo",
        default="magiskboy/agent-skills",
        help="GitHub repository in owner/name form",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root",
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        default=ROOT / "dist",
        help="Output directory for skill archives",
    )
    parser.add_argument(
        "--deploy-dir",
        type=Path,
        default=ROOT / "deploy",
        help="Output directory for GitHub Pages / well-known files",
    )
    args = parser.parse_args()

    try:
        publish(
            version=args.version,
            repo=args.repo,
            root=args.root,
            dist_dir=args.dist_dir,
            deploy_dir=args.deploy_dir,
        )
    except (RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
