# build-knowledge-graph

> Organize knowledge as an undirected graph whose edges carry the *reasoning* for
> why two ideas connect.

## When to use

- Placing a new node among existing ones, or deciding how pieces of knowledge
  relate.
- Any time the question is "how does this connect to what I already know?".

## Principle

The graph's value is in its edges. A node is a fact; an **edge is an act of
thinking** — the decision that two ideas relate and *why*. In Assistive mode that
reasoning is the user's to write (see [connect-ideas](connect-ideas.md)); in
Autonomous mode the assistant may draft it but must mark it for review.

## Graph rules

- Knowledge is organized as an **undirected graph**.
- Vertices are pieces of knowledge; **edges reflect the thinking that links them**.
- Two vertices may have **multiple edges** — different facets of reasoning that
  connect the same two ideas.

## Method

1. When introducing a new piece of knowledge, identify what it relates to: same
   pattern, an inheritance from known knowledge, a contrast, a cause — any genuine
   link.
2. For each link, write the edge label as `<Node name> - <linking reasoning>`,
   making the *why* explicit, not just the *that*.
3. If a fragment is tiny and tightly bound to an existing node, merge it in rather
   than creating a weakly-connected new vertex.
4. Keep the reasoning honest and specific; a vague edge ("related to") is a
   missing edge.

## Canonical example

The `add-knowledge` skill in `wiki` (sections "Quy tắc liên kết tri thức" and the
link-label format) defines the undirected-graph model, the multi-edge rule, and
the `<name> - <reasoning>` label format used here.

## Anti-patterns

- An edge with no reasoning, or a generic "related" label.
- (Assistive mode) the assistant writing the edge reasoning instead of the user.
- Forcing a link that does not genuinely exist just to reduce orphans.

## Connects to

- [connect-ideas](connect-ideas.md) surfaces *candidate* edges as questions;
  [curate-vault](curate-vault.md) finds orphans and bad relation types.

## Reminder

Discuss the graph with the user in Vietnamese; keep widely-used technical terms
in English.
