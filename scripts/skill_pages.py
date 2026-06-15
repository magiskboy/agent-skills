"""Generate static HTML pages for the skills GitHub Pages site."""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path

import markdown

GITHUB_BRANCH = "main"


@dataclass(frozen=True)
class SkillPage:
    dir_name: str
    name: str
    description: str
    meta: dict
    body_md: str


def parse_skill_page(skill_dir: Path) -> SkillPage:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{skill_dir.name}/SKILL.md is missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{skill_dir.name}/SKILL.md has invalid frontmatter")

    import yaml

    meta = yaml.safe_load(parts[1])
    if not isinstance(meta, dict):
        raise ValueError(f"{skill_dir.name}/SKILL.md frontmatter must be a mapping")

    body_md = parts[2].lstrip("\n")
    skill_name = str(meta.get("name") or skill_dir.name)
    description = str(meta.get("description", ""))

    return SkillPage(
        dir_name=skill_dir.name,
        name=skill_name,
        description=description,
        meta=meta,
        body_md=body_md,
    )


def read_site_url(deploy_dir: Path, default: str = "https://skills.nkthanh.dev") -> str:
    cname = deploy_dir / "CNAME"
    if cname.is_file():
        host = cname.read_text(encoding="utf-8").strip()
        if host:
            return f"https://{host}"
    return default


def install_command(site_url: str, skill_name: str) -> str:
    return f"npx skills add {site_url} --skill {skill_name}"


def github_install_command(repo: str, skill_name: str) -> str:
    return f"npx skills add https://github.com/{repo} --skill {skill_name}"


def rewrite_relative_links(body_md: str, skill_dir_name: str, repo: str) -> str:
    base = f"https://github.com/{repo}/tree/{GITHUB_BRANCH}/{skill_dir_name}"

    def replace_link(match: re.Match[str]) -> str:
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith(("#", "/")):
            return match.group(0)
        return f"{prefix}{base}/{url}{suffix}"

    return re.sub(r"(\]\()([^)#]+)(\))", replace_link, body_md)


def markdown_to_html(body_md: str) -> str:
    converter = markdown.Markdown(
        extensions=["extra", "tables", "sane_lists", "toc"],
        extension_configs={"toc": {"permalink": False}},
    )
    return converter.convert(body_md)


def _truncate(text: str, max_len: int = 200) -> str:
    collapsed = " ".join(text.split())
    if len(collapsed) <= max_len:
        return collapsed
    return collapsed[: max_len - 1].rstrip() + "…"


SITE_CSS = """
/* --- Theme tokens: light (default) — white / black --- */
:root,
[data-theme="light"] {
  color-scheme: light;
  --bg: #ffffff;
  --bg-elevated: #ffffff;
  --bg-subtle: #f5f5f5;
  --bg-hero: linear-gradient(160deg, #ffffff 0%, #fafafa 55%, #f0f0f0 100%);
  --text: #000000;
  --text-secondary: #171717;
  --text-muted: #525252;
  --border: #e5e5e5;
  --border-strong: #d4d4d4;
  --accent: #000000;
  --accent-hover: #404040;
  --accent-on: #ffffff;
  --accent-soft: rgba(0, 0, 0, 0.06);
  --accent-ring: rgba(0, 0, 0, 0.2);
  --code-bg: #f5f5f5;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.1);
  --sidebar-bg: #ffffff;
  --card-hover: #fafafa;
  --success: #16a34a;
}

/* --- Theme tokens: dark (explicit) --- */
[data-theme="dark"] {
  color-scheme: dark;
  --bg: #000000;
  --bg-elevated: #0a0a0a;
  --bg-subtle: #171717;
  --bg-hero: linear-gradient(160deg, #000000 0%, #0a0a0a 55%, #171717 100%);
  --text: #ffffff;
  --text-secondary: #e5e5e5;
  --text-muted: #a3a3a3;
  --border: #262626;
  --border-strong: #404040;
  --accent: #ffffff;
  --accent-hover: #e5e5e5;
  --accent-on: #000000;
  --accent-soft: rgba(255, 255, 255, 0.08);
  --accent-ring: rgba(255, 255, 255, 0.25);
  --code-bg: #171717;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.5);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.55);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.65);
  --sidebar-bg: #0a0a0a;
  --card-hover: #141414;
  --success: #4ade80;
}

/* --- Theme tokens: dark (system preference) --- */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --bg: #000000;
    --bg-elevated: #0a0a0a;
    --bg-subtle: #171717;
    --bg-hero: linear-gradient(160deg, #000000 0%, #0a0a0a 55%, #171717 100%);
    --text: #ffffff;
    --text-secondary: #e5e5e5;
    --text-muted: #a3a3a3;
    --border: #262626;
    --border-strong: #404040;
    --accent: #ffffff;
    --accent-hover: #e5e5e5;
    --accent-on: #000000;
    --accent-soft: rgba(255, 255, 255, 0.08);
    --accent-ring: rgba(255, 255, 255, 0.25);
    --code-bg: #171717;
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.5);
    --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.55);
    --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.65);
    --sidebar-bg: #0a0a0a;
    --card-hover: #141414;
    --success: #4ade80;
  }
}

*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.65;
  color: var(--text);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

a { color: var(--accent); text-decoration: none; transition: color 0.15s; }
a:hover { color: var(--accent-hover); }

.shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.container {
  width: min(1120px, calc(100% - 2.5rem));
  margin-inline: auto;
}

/* --- Header --- */
.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(12px);
  background: color-mix(in srgb, var(--bg-elevated) 82%, transparent);
  border-bottom: 1px solid var(--border);
}

.site-header__inner {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 1rem;
  padding: 0.85rem 0;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.header-link {
  font-size: 0.875rem;
  color: var(--text-muted);
  padding: 0.35rem 0.65rem;
  border-radius: 0.45rem;
  border: 1px solid transparent;
}
.header-link:hover {
  color: var(--text);
  background: var(--bg-subtle);
  text-decoration: none;
}

/* --- Theme switcher --- */
.theme-switcher {
  display: inline-flex;
  padding: 0.2rem;
  border-radius: 0.65rem;
  border: 1px solid var(--border);
  background: var(--bg-subtle);
  gap: 0.15rem;
}

.theme-switcher button {
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  padding: 0;
  border: none;
  border-radius: 0.45rem;
  background: transparent;
  color: var(--text-muted);
  cursor: pointer;
  transition: background 0.15s, color 0.15s, box-shadow 0.15s;
}
.theme-switcher button:hover { color: var(--text); background: var(--bg-elevated); }
.theme-switcher button.is-active {
  color: var(--accent);
  background: var(--bg-elevated);
  box-shadow: var(--shadow-sm);
}
.theme-switcher svg { width: 1rem; height: 1rem; }

/* --- Hero (index) --- */
.hero {
  padding: 3.5rem 0 2.5rem;
  background: var(--bg-hero);
  border-bottom: 1px solid var(--border);
}

.hero__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.85rem;
}

.hero h1 {
  margin: 0 0 0.75rem;
  font-size: clamp(2rem, 4vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.03em;
  font-weight: 700;
  max-width: 18ch;
}

.hero__lead {
  margin: 0;
  max-width: 42rem;
  color: var(--text-secondary);
  font-size: 1.05rem;
}

.hero__stats {
  display: flex;
  gap: 1.5rem;
  margin-top: 1.75rem;
  flex-wrap: wrap;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.stat__value {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.stat__label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* --- Skill grid (index) --- */
.catalog {
  padding: 2.5rem 0 4rem;
}

.catalog__heading {
  margin: 0 0 1.25rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.skill-card {
  display: flex;
  flex-direction: column;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 0.85rem;
  padding: 1.35rem;
  box-shadow: var(--shadow-sm);
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s, background 0.2s;
  min-height: 100%;
}
.skill-card:hover {
  border-color: var(--border-strong);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  background: var(--card-hover);
}

.skill-card__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.skill-card__name {
  margin: 0;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: -0.01em;
}
.skill-card__name a { color: var(--text); }
.skill-card__name a:hover { color: var(--accent); text-decoration: none; }

.skill-card__arrow {
  flex-shrink: 0;
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  border-radius: 0.45rem;
  color: var(--text-muted);
  font-size: 1.1rem;
  line-height: 1;
  border: 1px solid transparent;
  transition: transform 0.2s, color 0.2s, background 0.2s, border-color 0.2s;
}
.skill-card__arrow:hover {
  color: var(--accent);
  background: var(--accent-soft);
  border-color: var(--border);
  text-decoration: none;
  transform: translate(2px, -2px);
}
.skill-card:hover .skill-card__arrow {
  color: var(--text-muted);
  transform: none;
}
.skill-card:hover .skill-card__arrow:hover {
  color: var(--accent);
  transform: translate(2px, -2px);
}

.skill-card__desc {
  margin: 0 0 1.25rem;
  flex: 1;
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.55;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.skill-card__footer {
  margin-top: auto;
}
.install-snippet {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  min-width: 0;
}

.install-snippet__cmd {
  flex: 1;
  min-width: 0;
  margin: 0;
  padding: 0.45rem 0.65rem;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 0.45rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.72rem;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* --- Buttons & code blocks --- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.5rem 0.85rem;
  font-size: 0.82rem;
  font-weight: 500;
  border-radius: 0.5rem;
  border: 1px solid var(--border);
  background: var(--bg-elevated);
  color: var(--text);
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s, background 0.15s;
  white-space: nowrap;
}
.btn:hover { border-color: var(--accent); color: var(--accent); }
.btn--primary {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--accent-on);
}
.btn--primary:hover {
  background: var(--accent-hover);
  border-color: var(--accent-hover);
  color: var(--accent-on);
}
.btn--ghost {
  background: transparent;
}
.btn--sm { padding: 0.4rem 0.65rem; font-size: 0.78rem; }
.btn--block { width: 100%; }

.code-block {
  position: relative;
  margin: 0;
}
.code-block pre {
  margin: 0;
  padding: 0.55rem 0.75rem;
  padding-right: 3.25rem;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 0.55rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.72rem;
  line-height: 1.4;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.code-block pre code {
  white-space: nowrap;
}
.code-block .btn-copy {
  position: absolute;
  top: 50%;
  right: 0.35rem;
  transform: translateY(-50%);
  padding: 0.3rem 0.5rem;
  font-size: 0.72rem;
}

/* --- Detail page layout --- */
.detail-page {
  padding: 1.75rem 0 4rem;
}

.detail-back {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  color: var(--text-muted);
}
.detail-back:hover { color: var(--accent); text-decoration: none; }

.detail-layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(240px, 280px);
  gap: 1.75rem;
  align-items: start;
}

.detail-sidebar {
  position: sticky;
  top: 5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sidebar-panel {
  background: var(--sidebar-bg);
  border: 1px solid var(--border);
  border-radius: 0.85rem;
  padding: 1.25rem;
  box-shadow: var(--shadow-sm);
}

.sidebar-panel h2 {
  margin: 0 0 0.35rem;
  font-size: 1rem;
  font-weight: 650;
  letter-spacing: -0.02em;
}

.sidebar-panel__sub {
  margin: 0 0 1rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.45;
}

.install-group { display: flex; flex-direction: column; gap: 1rem; }

.install-group label {
  display: block;
  margin-bottom: 0.4rem;
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}

.meta-kv {
  margin: 0.85rem 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.meta-kv__row {
  display: grid;
  grid-template-columns: 7.5rem minmax(0, 1fr);
  gap: 0.35rem 0.65rem;
  align-items: baseline;
  font-size: 0.8rem;
  line-height: 1.4;
}

.meta-kv__key {
  color: var(--text-muted);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.72rem;
}

.meta-kv__val {
  color: var(--text);
  word-break: break-word;
}

/* --- Prose --- */
.detail-main { min-width: 0; }

.prose {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 0.85rem;
  padding: clamp(1.25rem, 3vw, 2rem) clamp(1.25rem, 3vw, 2.25rem);
  box-shadow: var(--shadow-sm);
}

.prose h1, .prose h2, .prose h3, .prose h4 {
  margin-top: 1.75rem;
  margin-bottom: 0.65rem;
  line-height: 1.3;
  letter-spacing: -0.02em;
  color: var(--text);
}
.prose h1 { font-size: 1.65rem; margin-top: 0; }
.prose h2 { font-size: 1.25rem; padding-bottom: 0.35rem; border-bottom: 1px solid var(--border); }
.prose h3 { font-size: 1.05rem; }

.prose p, .prose ul, .prose ol, .prose table { margin: 0 0 1rem; }
.prose ul, .prose ol { padding-left: 1.35rem; }
.prose li { margin-bottom: 0.35rem; }

.prose blockquote {
  margin: 0 0 1rem;
  padding: 0.75rem 1rem;
  border-left: 3px solid var(--accent);
  color: var(--text-secondary);
  background: var(--accent-soft);
  border-radius: 0 0.55rem 0.55rem 0;
}

.prose pre {
  overflow-x: auto;
  padding: 1rem;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 0.55rem;
  font-size: 0.84rem;
  line-height: 1.5;
}

.prose code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.86em;
  background: var(--code-bg);
  padding: 0.12em 0.38em;
  border-radius: 0.3rem;
  border: 1px solid var(--border);
}
.prose pre code { background: none; border: none; padding: 0; }

.prose table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  display: block;
  overflow-x: auto;
}
.prose th, .prose td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.75rem;
  text-align: left;
}
.prose th { background: var(--code-bg); font-weight: 600; }
.prose tr:nth-child(even) td { background: color-mix(in srgb, var(--code-bg) 50%, transparent); }

.prose a { text-decoration: underline; text-underline-offset: 2px; }
.prose a:hover { text-decoration-thickness: 2px; }

/* --- Footer --- */
.site-footer {
  margin-top: auto;
  padding: 1.5rem 0 2rem;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.82rem;
  text-align: center;
}
.site-footer a { color: var(--text-muted); }
.site-footer a:hover { color: var(--accent); }

/* --- Responsive --- */
@media (max-width: 860px) {
  .detail-layout {
    grid-template-columns: 1fr;
  }
  .detail-sidebar {
    position: static;
  }
  .hero { padding-top: 2.5rem; }
  .container { width: min(100%, calc(100% - 1.5rem)); }
}
"""

SITE_JS = """
(function () {
  const STORAGE_KEY = 'agent-skills-theme';

  function readStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY) || 'system';
    } catch {
      return 'system';
    }
  }

  function writeStoredTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch {
      /* private browsing */
    }
  }

  function applyTheme(preference) {
    const pref = preference || 'system';
    if (pref === 'system') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', pref);
    }
    document.documentElement.dataset.themePreference = pref;

    document.querySelectorAll('[data-theme-set]').forEach((btn) => {
      const active = btn.getAttribute('data-theme-set') === pref;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise((resolve, reject) => {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.top = '-1000px';
      ta.style.left = '-1000px';
      document.body.appendChild(ta);
      ta.select();
      ta.setSelectionRange(0, text.length);
      try {
        const ok = document.execCommand('copy');
        document.body.removeChild(ta);
        ok ? resolve() : reject(new Error('execCommand failed'));
      } catch (err) {
        document.body.removeChild(ta);
        reject(err);
      }
    });
  }

  function initTheme() {
    applyTheme(readStoredTheme());

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (readStoredTheme() === 'system') applyTheme('system');
    });

    document.querySelectorAll('[data-theme-set]').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const theme = btn.getAttribute('data-theme-set') || 'system';
        writeStoredTheme(theme);
        applyTheme(theme);
      });
    });
  }

  function initCopy() {
    document.querySelectorAll('[data-copy]').forEach((btn) => {
      btn.addEventListener('click', async (e) => {
        e.preventDefault();
        const text = btn.getAttribute('data-copy') || '';
        const label = btn.getAttribute('data-label') || 'Copy';
        try {
          await copyText(text);
          btn.textContent = 'Copied';
          btn.classList.add('is-copied');
          setTimeout(() => {
            btn.textContent = label;
            btn.classList.remove('is-copied');
          }, 2000);
        } catch {
          btn.textContent = 'Failed';
          setTimeout(() => { btn.textContent = label; }, 2000);
        }
      });
    });
  }

  initTheme();
  initCopy();
})();
"""

ICON_SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>'
ICON_MOON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
ICON_SYSTEM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>'


def _theme_switcher() -> str:
    return f"""
<div class="theme-switcher" role="group" aria-label="Color theme">
  <button type="button" data-theme-set="light" aria-label="Light theme" aria-pressed="false">{ICON_SUN}</button>
  <button type="button" data-theme-set="dark" aria-label="Dark theme" aria-pressed="false">{ICON_MOON}</button>
  <button type="button" data-theme-set="system" aria-label="System theme" aria-pressed="false">{ICON_SYSTEM}</button>
</div>
"""


def _page_paths(depth: int = 0) -> tuple[str, str]:
    prefix = "../" * depth
    home = f"{prefix}" if depth else "./"
    assets = f"{prefix}assets"
    return home, assets


def _header(repo: str) -> str:
    github_url = f"https://github.com/{repo}"
    return f"""
<header class="site-header">
  <div class="container site-header__inner">
    <div class="header-actions">
      <a class="header-link" href="https://agentskills.io" target="_blank" rel="noopener">Specification</a>
      <a class="header-link" href="{html.escape(github_url)}" target="_blank" rel="noopener">GitHub</a>
      {_theme_switcher()}
    </div>
  </div>
</header>
"""


def _footer(site_url: str, repo: str) -> str:
    github_url = f"https://github.com/{repo}"
    return f"""
<footer class="site-footer">
  <div class="container">
    <a href="{html.escape(site_url)}">{html.escape(site_url)}</a>
    &nbsp;&middot;&nbsp;
    <a href="{html.escape(github_url)}">{html.escape(repo)}</a>
  </div>
</footer>
"""


def _layout(title: str, body: str, site_url: str, repo: str, *, depth: int = 0) -> str:
    safe_title = html.escape(title)
    _, assets_href = _page_paths(depth)
    return f"""<!DOCTYPE html>
<html lang="en" data-theme-preference="system">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{safe_title} · Agent Skills</title>
  <script>
    (function () {{
      try {{
        var t = localStorage.getItem('agent-skills-theme');
        if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
      }} catch (e) {{}}
    }})();
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{html.escape(assets_href)}/site.css">
</head>
<body>
  <div class="shell">
    {_header(repo)}
    <main>{body}</main>
    {_footer(site_url, repo)}
  </div>
  <script src="{html.escape(assets_href)}/site.js"></script>
</body>
</html>
"""


def _copy_button(command: str, label: str = "Copy") -> str:
    safe_cmd = html.escape(command)
    safe_label = html.escape(label)
    return (
        f'<button type="button" class="btn btn--ghost btn--sm" '
        f'title="{safe_cmd}" data-copy="{safe_cmd}" data-label="{safe_label}">'
        f"{safe_label}</button>"
    )


def _code_block(command: str, btn_label: str = "Copy") -> str:
    safe_cmd = html.escape(command)
    safe_label = html.escape(btn_label)
    return f"""
<div class="code-block">
  <pre title="{safe_cmd}"><code>{safe_cmd}</code></pre>
  <button type="button" class="btn btn--sm btn-copy" title="{safe_cmd}" data-copy="{safe_cmd}" data-label="{safe_label}">{safe_label}</button>
</div>
"""


def _install_group(primary_label: str, primary_cmd: str, secondary_label: str, secondary_cmd: str) -> str:
    return f"""
<div class="install-group">
  <div>
    <label>{html.escape(primary_label)}</label>
    {_code_block(primary_cmd)}
  </div>
  <div>
    <label>{html.escape(secondary_label)}</label>
    {_code_block(secondary_cmd)}
  </div>
</div>
"""


def _meta_row(key: str, value: str) -> str:
    return (
        f'<li class="meta-kv__row">'
        f'<span class="meta-kv__key">{html.escape(key)}</span>'
        f'<span class="meta-kv__val">{html.escape(value)}</span>'
        f"</li>"
    )


def _meta_info(skill: SkillPage) -> str:
    rows: list[str] = []
    if skill.meta.get("license"):
        rows.append(_meta_row("license", str(skill.meta["license"])))
    metadata = skill.meta.get("metadata")
    if isinstance(metadata, dict):
        if metadata.get("version"):
            rows.append(_meta_row("metadata.version", str(metadata["version"])))
        if metadata.get("author"):
            rows.append(_meta_row("metadata.author", str(metadata["author"])))
    if not rows:
        return ""
    return f'<ul class="meta-kv">{"".join(rows)}</ul>'


def render_index(skills: list[SkillPage], site_url: str, repo: str) -> str:
    cards: list[str] = []
    for skill in skills:
        detail_url = f"skills/{skill.dir_name}/"
        primary = install_command(site_url, skill.dir_name)
        short_desc = html.escape(_truncate(skill.description, 220))
        safe_cmd = html.escape(primary)
        cards.append(
            f"""
<article class="skill-card">
  <div class="skill-card__top">
    <h2 class="skill-card__name"><a href="{html.escape(detail_url)}">{html.escape(skill.dir_name)}</a></h2>
    <a class="skill-card__arrow" href="{html.escape(detail_url)}" aria-label="View {html.escape(skill.dir_name)} overview">&#8599;</a>
  </div>
  <p class="skill-card__desc">{short_desc}</p>
  <div class="skill-card__footer">
    <div class="install-snippet">
      <code class="install-snippet__cmd" title="{safe_cmd}">{safe_cmd}</code>
      {_copy_button(primary, "Copy")}
    </div>
  </div>
</article>
"""
        )

    count = len(skills)
    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero__eyebrow">Cursor &amp; compatible agents</div>
    <h1>Reusable skills for your AI workflow</h1>
    <p class="hero__lead">
      Installable <a href="https://agentskills.io">Agent Skills</a> with conventions,
      references, and templates. Pick a skill, copy the install command, or read the full overview.
    </p>
    <div class="hero__stats">
      <div class="stat">
        <span class="stat__value">{count}</span>
        <span class="stat__label">Skills</span>
      </div>
      <div class="stat">
        <span class="stat__value">npx</span>
        <span class="stat__label">One-line install</span>
      </div>
    </div>
  </div>
</section>
<section class="catalog">
  <div class="container">
    <h2 class="catalog__heading">All skills</h2>
    <div class="skill-grid">
      {"".join(cards)}
    </div>
  </div>
</section>
"""
    return _layout("Catalog", body, site_url, repo)


def render_skill_detail(skill: SkillPage, site_url: str, repo: str) -> str:
    linked_md = rewrite_relative_links(skill.body_md, skill.dir_name, repo)
    content_html = markdown_to_html(linked_md)
    primary = install_command(site_url, skill.dir_name)
    secondary = github_install_command(repo, skill.dir_name)
    meta_info = _meta_info(skill)

    body = f"""
<div class="detail-page">
  <div class="container">
    <a class="detail-back" href="../../">&#8592; All skills</a>
    <div class="detail-layout">
      <div class="detail-main">
        <article class="prose">
          {content_html}
        </article>
      </div>
      <aside class="detail-sidebar" aria-label="Install and metadata">
        <div class="sidebar-panel">
          <h2>{html.escape(skill.dir_name)}</h2>
          <p class="sidebar-panel__sub">{html.escape(_truncate(skill.description, 280))}</p>
          {meta_info}
        </div>
        <div class="sidebar-panel">
          <h2>Install</h2>
          <p class="sidebar-panel__sub">Run in your project directory.</p>
          {_install_group("Registry", primary, "GitHub", secondary)}
          <a class="btn btn--primary btn--block" style="margin-top: 1rem" href="{html.escape(f"https://github.com/{repo}/tree/{GITHUB_BRANCH}/{skill.dir_name}")}" target="_blank" rel="noopener">View source on GitHub</a>
        </div>
      </aside>
    </div>
  </div>
</div>
"""
    return _layout(skill.dir_name, body, site_url, repo, depth=2)


def generate_site(deploy_dir: Path, skills: list[SkillPage], repo: str) -> None:
    site_url = read_site_url(deploy_dir)
    assets_dir = deploy_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / "site.css").write_text(SITE_CSS.strip() + "\n", encoding="utf-8")
    (assets_dir / "site.js").write_text(SITE_JS.strip() + "\n", encoding="utf-8")

    (deploy_dir / "index.html").write_text(
        render_index(skills, site_url, repo),
        encoding="utf-8",
    )

    for skill in skills:
        skill_dir = deploy_dir / "skills" / skill.dir_name
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "index.html").write_text(
            render_skill_detail(skill, site_url, repo),
            encoding="utf-8",
        )

    print(f"wrote {deploy_dir / 'index.html'} ({len(skills)} skill pages)")
