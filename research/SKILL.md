---
name: research
description: >-
  Personal research and knowledge-building methodology. Use when the user wants
  to research a topic, find sources, excavate faded experiential memory, deeply
  understand a concept, distill raw material into knowledge notes, link ideas
  into a knowledge graph, challenge a claim, or maintain a knowledge vault.
  Triggers: "research X", "find sources", "counter-arguments", "excavate my
  memory", "take notes on this", "knowledge graph", "rebut this", "review my
  vault", and the Vietnamese equivalents ("nghiên cứu", "tìm nguồn", "phản
  biện", "ghi chú"). This SKILL.md is an index; each sub-skill lives in
  references/ and is loaded on demand.
license: MIT
metadata:
  author: magiskboy
  version: "0.1.0"
---

# Research — methodology for studying and building knowledge

This skill packages **research methodology** as several independent sub-skills,
each a file under `references/`. This `SKILL.md` is only an **index**: read the
table below to pick the right method, then open that one file. Do not load
everything — open a sub-skill file only when the task calls for it (progressive
disclosure).

Each sub-skill is distilled from a **canonical example** skill that already runs
in two personal knowledge vaults: `wiki` (distills knowledge into a graph) and
`kb-client` (a knowledge network that keeps the thinking with the user). The
"Canonical example" column points at the source skill so you can see how it is
applied — **do not modify the source skills**; reference them as examples only.

> **Attribution.** Every sub-skill in this `research` skill is **inspired by and
> extracted from** the referenced source skills in the `wiki` and `kb-client`
> repositories. They are distillations and reorganizations of those originals,
> not new inventions — credit belongs to the source vaults.
>
> Sources:
> - `wiki` — https://github.com/magiskboy/wiki (skills under `.agents/skills/`:
>   `add-knowledge`, `excavate-knowledge`, `socratic`)
> - `kb-client` — https://github.com/magiskboy/kb-client (skills under
>   `.agent/skills/`: `source-finder`, `link-prompter`, `fracture-mirror`,
>   `knowledge-curation`, `reflection`)

## Global rule — language

> **Always respond to the user in Vietnamese**, regardless of the language of
> this skill, the sources, or the notes. The skill content is written in English
> for precision, but every user-facing message, question, and report is in
> Vietnamese. Keep technical terms in English when the English term is more
> common (e.g. *knowledge graph*, *frontmatter*, *counter-argument*).

## Core principle (read first)

Everything here stands on one line: **the assistant carries load, the user keeps
the thinking.** Finding, linting, diffing, surfacing candidates is load — give it
to the assistant. Deciding *why* two ideas connect, whether a claim is true,
whether a change is progress or regress — that is thinking, and it belongs to the
user.

There are two modes, chosen by how much the user delegates (details in
[principles](references/principles.md)):

- **Assistive (default):** the assistant only carries load; it does not write
  reasoning/edges or synthesize on the user's behalf. This is `kb-client`'s
  stance.
- **Autonomous (only when the user explicitly says "research it and write it up
  for me"):** the assistant may distill into notes and link them, but **must**
  mark provenance and cite sources. This is `wiki`'s stance.

## Quick Reference

Five groups, following the flow of one research session: **Discover → Elicit →
Synthesize → Challenge → Maintain.**

### 1. Discover sources

| Sub-skill | Purpose | Canonical example |
|-----------|---------|-------------------|
| [discover-sources](references/discover-sources.md) | Find and hand over original links for the user to read; never summarize for them | `kb-client/source-finder` |
| [select-sources](references/select-sources.md) | Choose trustworthy sources by object type (academic / technology / code) | `wiki/add-knowledge` |

### 2. Elicit & understand

| Sub-skill | Purpose | Canonical example |
|-----------|---------|-------------------|
| [excavate-experience](references/excavate-experience.md) | Surface faded experiential knowledge through cued-recall interviewing | `wiki/excavate-knowledge` |
| [socratic-understanding](references/socratic-understanding.md) | Reach the essence of a concept via Socratic questioning and first principles | `wiki/socratic` |

### 3. Synthesize

| Sub-skill | Purpose | Canonical example |
|-----------|---------|-------------------|
| [distill-note](references/distill-note.md) | Distill raw material into a concise, evidenced knowledge node | `wiki/add-knowledge` |
| [build-knowledge-graph](references/build-knowledge-graph.md) | Organize knowledge as an undirected graph whose edges carry the linking reasoning | `wiki/add-knowledge` |
| [connect-ideas](references/connect-ideas.md) | Surface missing link candidates as open questions; never draw the link | `kb-client/link-prompter` |

### 4. Challenge

| Sub-skill | Purpose | Canonical example |
|-----------|---------|-------------------|
| [challenge-claims](references/challenge-claims.md) | Relay real counter-arguments from real people/sources; never invent one | `kb-client/fracture-mirror` |

### 5. Maintain

| Sub-skill | Purpose | Canonical example |
|-----------|---------|-------------------|
| [curate-vault](references/curate-vault.md) | Lint/normalize the *form* of the vault only; never touch meaning | `kb-client/knowledge-curation` |
| [reflect-evolution](references/reflect-evolution.md) | Neutrally diff the knowledge graph over time for the user to interpret | `kb-client/reflection` |

## How to use

1. Identify which phase of research the user is in (the 5 groups above).
2. Open **one** `references/<sub-skill>.md` and follow it.
3. A session usually spans several phases; when the phase changes, open the next
   file — do not preload all of them.
4. Always honor the Assistive/Autonomous mode chosen in
   [principles](references/principles.md), and always reply in Vietnamese.
