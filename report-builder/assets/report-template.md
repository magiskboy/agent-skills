<!--
  Markdown report scaffold (GitHub-Flavored Markdown).
  - Replace the bracketed placeholders.
  - Keep one `#` title; sections are `##`, sub-points `###`.
  - Blank line before/after every heading, list, table, and code fence.
  - Lead with the answer (Summary first). Every number/quote gets a source.
-->

# [Report title]

> [One line: what this answers, for whom — as of YYYY-MM-DD]

## Summary

[The answer in 3–5 sentences or bullets. A reader can stop here and still know
the conclusion and the recommended action.]

- **Bottom line:** [the single most important takeaway].
- [Key result with a number, e.g. "p99 dropped 1.9s → 240ms (−87%)"].
- [Recommended action].

## Context

[Why this report exists, the scope, and what is explicitly out of scope.]

## Findings

### [Finding 1 stated as a claim]

[Evidence first, then detail.]

| Service  | p99 before (ms) | p99 after (ms) |     Δ |
| -------- | --------------: | -------------: | ----: |
| payments |          1,900  |          240  | −87% |
| checkout |            310  |          305  |  −2% |
| search   |            880  |          410  | −53% |

*Table 1: caption states the takeaway, not just the subject.*

### [Finding 2 stated as a claim]

[...]

> [!NOTE]
> [Context the reader needs to trust the numbers — baseline, sample size, dates.]

## Recommendations

1. [Concrete, owned, actionable next step.]
2. [...]

## Appendix

### Methodology

[How the data was collected and processed.]

### References

- [Source title](https://example.com)
