# distill-note

> Distill raw material into a concise, self-contained, evidenced knowledge node.

## When to use

- Turning raw notes (from [excavate-experience](excavate-experience.md)) or
  researched sources into a permanent knowledge node.
- Autonomous mode (the user asked you to write it up). In Assistive mode, the
  user writes the note; you only carry load around it.

## Naming rules

- The name reflects the actual entity/concept of the knowledge.
- Keep it short and to the point; no negation words.
- No counting numbers or ordinals in the name.

## Content rules

- No vague pointers ("this thing", "that one"); do not explain a concept via an
  unnamed referent.
- Use consistent terminology within a document (do not mix two words for the
  same idea).
- For terms more common in English, use the English term rather than translating.
- Use the domain's technical vocabulary as much as possible.
- Limit nesting — at most 3 levels of structure within a note.
- Split knowledge so each part can be understood independently.
- **Every claim needs evidence from a reputable source; do not reason beyond the
  sources found.**
- Use bullet points only when each item is already very clear.
- If a fragment is tiny and very close to existing knowledge, fold it into the
  existing node instead of creating a new one.
- Rich components (code blocks, mermaid, images) may support explanation.

## Markdown rules

- Do not draw figures in ASCII; use mermaid for diagrams (keep them small to
  avoid overload).
- File structure: title (the node name) → body sections → a links list → tags.
- Links list: use markdown `[]()` to connect to other nodes; the link label has
  the form `<Node name> - <linking reasoning>` (see
  [build-knowledge-graph](build-knowledge-graph.md)).
- Tags: tag for classification/statistics; reuse the vault's tag list and add new
  tags to it.
- Add the new node to the vault index.

### Template

```markdown
# Node name (heading 1)

# Body sections developing the knowledge

# Sources
<list of sources consulted>

# Links
<list of links within the vault>

# Tags
<list of tags>
```

## Provenance (when distilling from memory)

Carry the three markers from [excavate-experience](excavate-experience.md) —
**[Memory] / [Added — source] / [Uncertain]** — or split the personal experience
into its own section, so the line between memory and background knowledge stays
clear.

## Reporting back

- Do not over-explain inside the note itself.
- After writing, tell the user where the new node sits in the vault.

## Canonical example

The `add-knowledge` skill in `wiki` is the full method: the research steps, the
naming/content/markdown rules above, and the final "report where it landed" step.

## Reminder

Report back to the user in Vietnamese; keep widely-used technical terms in
English. Note bodies follow the vault's own language convention.
