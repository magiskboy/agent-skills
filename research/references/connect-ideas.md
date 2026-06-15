# connect-ideas

> Surface link candidates the user might be missing — as open questions only.
> Never draw the link or write its reasoning.

## When to use

- "What could link to what?", "am I missing any connections?".
- Assistive mode, when the user is building their own graph and wants a spark.

## Principle

The reasoning written on an edge — *why* two ideas connect — is the exact
cognitive act the whole vault exists to protect. If the assistant drafts that
reasoning or draws the link, the user has outsourced the one thing they were
meant to keep doing, and the graph stops being a record of their thinking.

## Method

1. Find two notes that share vocabulary and are **not yet connected**.
2. Present them to the user as an **open question**: do these relate, and if so,
   how? Do not propose a relation type or reasoning.
3. Stop. Never create the wikilink, never pick the relation type, never write the
   edge reasoning.
4. If the user says "just make the links for you" → stop and hand it back (see
   [principles](principles.md)). This stays in Assistive mode by design.

## Canonical example

The `link-prompter` skill in `kb-client` does exactly this: it points at two
vocabulary-sharing, unconnected notes and asks the user an open question about
whether and how they relate — "a spark, not an author".

## Anti-patterns

- Drafting the edge reasoning "to save the user time".
- Picking the relation type for them.
- Auto-creating links to reduce the orphan count.

## Connects to

- The user's answer becomes a real edge under
  [build-knowledge-graph](build-knowledge-graph.md).

## Reminder

Ask the questions in Vietnamese; keep widely-used technical terms in English.
