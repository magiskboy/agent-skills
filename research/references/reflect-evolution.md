# reflect-evolution

> Show the user how their knowledge graph changed over time — a neutral diff.
> Describe movement only; never call it progress, regress, better, or worse.

## When to use

- "What's shifted since last week?", "how has my graph moved?".
- Periodic reflection on how one's thinking has evolved.

## Principle

This skill is a **mirror**. Whether a denser region is "growth" or "going in
circles", whether a removed edge is "a mistake corrected" or "a thread dropped"
— that interpretation is an act of self-understanding that belongs to the person.
If the tool labeled the diff as progress or scored it, it would be doing the
user's reflecting for them.

## Method

1. Take two points in time (a past git ref and now).
2. Compute a **neutral diff** of nodes and edges between them — what was added,
   removed, changed.
3. Present the movement plainly, then ask the user **calibration questions**
   inviting them to interpret it.
4. Never assign a score, never say the change is progress/regress/better/worse.

## Canonical example

The `reflection` skill in `kb-client` (script `graph_diff.py`) is the model: it
shows a neutral node/edge diff between a past git ref and now, asks calibration
questions, and explicitly refuses to label the change as progress, regress, or a
score.

## Anti-patterns

- "You've made great progress" — that is the user's judgment to make.
- Scoring the diff or ranking periods.
- Explaining what the movement *means* instead of asking.

## Connects to

- Pairs with [curate-vault](curate-vault.md) (form) — this one is about change
  over time (substance the user interprets).

## Reminder

Present the diff and ask calibration questions in Vietnamese; keep widely-used
technical terms in English.
