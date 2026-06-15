# curate-vault

> Tidy and check the *form* of the vault — frontmatter, links, structure. Never
> touch the meaning of any note, link, or reasoning.

## When to use

- "Tidy up the frontmatter on this note."
- "Are there any broken links / bad relation types in my vault?"
- "Which of my notes aren't connected to anything yet?"

## Principle

This is **pure load-carrying** — formatting and structure only. It never writes
the content of a note, a wikilink, or the reasoning on an edge — that is the
user's thinking, and doing it for them would hollow out the one thing the vault
exists to protect.

## Method

Form-and-structure operations only:

1. **Normalize frontmatter** — consistent fields, types, and ordering.
2. **Lint** — broken links, bad relation types, schema slips, too many relations
   per pair.
3. **Find orphans** — notes not connected to anything yet (report them; do not
   auto-connect — that is [connect-ideas](connect-ideas.md), still as questions).

Report findings; apply only mechanical, meaning-preserving fixes.

## Canonical example

The `knowledge-curation` skill in `kb-client` (with scripts `normalize_frontmatter.py`,
`lint_vault.py`, `find_orphans.py`) is exactly this: it carries formatting load
and touches structure/form only, never the meaning.

## Anti-patterns

- "Fixing" a note by rewriting its content.
- Auto-creating links to clear orphans.
- Changing a relation type because it "reads better" — that is meaning.

## Connects to

- Orphans found here become open questions in [connect-ideas](connect-ideas.md).

## Reminder

Report findings to the user in Vietnamese; keep widely-used technical terms in
English.
