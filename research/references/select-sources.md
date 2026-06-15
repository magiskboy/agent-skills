# select-sources

> Pick trustworthy sources by what kind of object you are researching.

## When to use

- After [discover-sources](discover-sources.md) returns candidates, or whenever
  you must decide *where* authoritative information for a topic lives.

## Principle

Source quality depends on the *type* of object. Academic claims, a piece of
technology, and code each have a different "home" where the trustworthy version
lives. Go to that home rather than to the nearest aggregator.

## Method — source selection by object type

- **Academic information** (computer science, theory, results): prefer arXiv,
  Google Scholar, and the blogs/websites of leading experts in the field.
- **Technologies, libraries, software, solutions:** prefer the technology's
  official site, the blogs of its authors/contributors, and its forums or
  community.
- **Code:** always look for the source code itself on GitHub, GitLab, or the
  library's official site.

## Rules of evidence

- Every claim needs evidence from a reputable source.
- Do not reason beyond the sources you actually found — no invented inference.
- When a claim is uncertain, mark it as such rather than asserting it.

## Canonical example

The `add-knowledge` skill in `wiki` (section "Quy tắc chọn nguồn tham khảo")
codifies exactly these three buckets — academic vs technology vs code — as its
source-selection rule before any knowledge is written down.

## Anti-patterns

- Citing a content farm or SEO blog over the primary source.
- Treating an LLM's recollection as a source.
- Mixing a strong claim with a weak source and presenting both as equal.

## Connects to

- Feeds [distill-note](distill-note.md): every distilled claim carries one of
  these sources.

## Reminder

Reply to the user in Vietnamese; keep widely-used technical terms in English.
