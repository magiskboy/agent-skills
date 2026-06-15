# agent-skills

Personal [Agent Skills](https://agentskills.io) — reusable instructions that teach the AI agent how to handle specific workflows, conventions, and domains.

Each skill is a self-contained directory with a `SKILL.md` entry point. The agent reads the skill when a task matches its description, then follows the linked references, assets, and scripts as needed.

Install any skill with the [skills.sh](https://www.skills.sh/) CLI:

```bash
# Browse the catalog: https://skills.nkthanh.dev

# Well-known registry (recommended after release)
npx skills add https://skills.nkthanh.dev --skill <skill-name>

# GitHub source
npx skills add https://github.com/magiskboy/agent-skills --skill <skill-name>
```

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [research](research/) | Research and knowledge-building methodology — source discovery, deep understanding, note distillation, knowledge graphs, claim challenge, and vault curation. | `npx skills add https://skills.nkthanh.dev --skill research` |
| [report-builder](report-builder/) | Build polished reports in Markdown or HTML — slides, charts, tables, diagrams, maps, math, and more via routed client libraries. | `npx skills add https://skills.nkthanh.dev --skill report-builder` |
| [tauri-apps-development](tauri-apps-development/) | Conventions and workflows for Tauri v2 desktop apps (React + TypeScript frontend, Rust backend) — IPC, state, SQLite, capabilities, testing, and release. | `npx skills add https://skills.nkthanh.dev --skill tauri-apps-development` |
| [dockerfile-builder](dockerfile-builder/) | Production-ready multi-stage Dockerfiles for Python (uv), Vite React, Next.js, and Python+Vite bundled monorepos — nginx SPA hosting, OCI labels, image size optimization. | `npx skills add https://skills.nkthanh.dev --skill dockerfile-builder` |

## Install locally

To develop or symlink skills from a local clone:

```bash
# Symlink (recommended — stays in sync with this repo)
ln -s "$(pwd)/research" ~/.cursor/skills/research
ln -s "$(pwd)/tauri-apps-development" ~/.cursor/skills/tauri-apps-development
```

Alternatively, copy a skill directory into `~/.cursor/skills/<skill-name>/`.

> **Note:** Do not put custom skills in `~/.cursor/skills-cursor/` — that directory is reserved for Cursor's built-in skills.

## Release

Publishing is automated via GitHub Actions when you publish a GitHub Release:

1. Bump version in the skill's `SKILL.md` frontmatter if needed.
2. Create and push a tag, e.g. `git tag v0.1.0 && git push origin v0.1.0`.
3. Publish a release for that tag on GitHub.

The [release workflow](.github/workflows/release.yml) will:

- Pack every top-level skill directory (any folder with `SKILL.md`) into `dist/*.tar.gz`
- Upload archives to the GitHub Release
- Generate `deploy/.well-known/agent-skills/index.json`, `deploy/index.html`, and per-skill pages under `deploy/skills/` for GitHub Pages

After the first release, enable **GitHub Pages** (`Settings → Pages → Source: GitHub Actions`) and point `skills.nkthanh.dev` to Pages (CNAME is in `deploy/CNAME`).

To validate locally before releasing:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/publish.py --version v0.1.0
```

## Add a new skill

1. Create a directory named after the skill (lowercase, hyphens for spaces).
2. Add `SKILL.md` with YAML frontmatter (`name`, `description`) and a concise body.
3. Put detailed material in `references/`, reusable files in `assets/`, and automation in `scripts/`.
4. Keep `description` specific enough that the agent knows **when** to apply the skill.
5. Update the table in this README.

See [Cursor's skill documentation](https://cursor.com/docs/agent/skills) for the full format and best practices.

## License

Unless noted otherwise in a skill's frontmatter, skills in this repository are released under the [MIT License](https://opensource.org/licenses/MIT).
