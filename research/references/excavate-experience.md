# excavate-experience

> Dig out experiential knowledge the user lived through but no longer actively
> recalls — through cued-recall interviewing — and dump it as raw notes for later
> distillation.

## When to use

- The user wants to recover faded experiential knowledge ("excavate my memory of
  doing X", "I worked on this once but barely remember it").
- As the *material-gathering* step before [distill-note](distill-note.md). This
  is upstream of distillation, not distillation itself.

## Principle

**Recognition beats recall.** Ask cued, concrete questions that trigger
recognition instead of open prompts like "tell me about X". The most valuable
part is experiential knowledge — the thing only the user has. The assistant must
not fabricate it; it may only add sourced background knowledge, clearly marked.

## Method — one session per leaf

Work one smallest "leaf" topic at a time. The user may pick the leaf, or you may
propose a leaf that looks experience-rich and is not yet captured.

1. **Locate.** Check the existing vault for what the leaf already touches, so you
   do not re-ask what is recorded and you know where it will join the graph.
2. **Interview in clusters.** Ask a cluster of questions along the recall frame
   below. The user answers freely; skip anything they do not remember.
3. **Adaptive probing.** Based on answers, probe nearby territory the user likely
   lived through but has not mentioned. This is the most important step — it
   restores faded cause-and-effect, not just transcribes memory. Probing well
   needs background knowledge of the leaf; on unfamiliar ground, fall back to
   pure recall prompts and let the user lead.
4. **Mirror and connect.** Summarize what the user just said and point out links
   to knowledge already in the vault.
5. **Dump raw.** Write the distilled transcript to a temporary staging note using
   the three provenance markers below. Do not verify sources yet — that is the
   distillation step's job.
6. **Track progress.** Update the leaf's status (`[ ]` → `[~]` → `[x]`).
7. **Hand off.** When the user wants to refine, use [distill-note](distill-note.md)
   to turn the raw notes into a knowledge node. One leaf may split into several
   nodes (separate a reusable concept from the experience node).
8. **Archive the transcript.** After it reaches the vault, move the transcript
   into a permanent `references/interviews/`-style location as the primary source
   for that experiential knowledge, and point its header at the resulting node.

## Recall frame (cued-recall)

Ask along this axis: context (when, where, why it had to be done) → the specific
problem → options considered or tried → what worked, what failed → the final
decision and its trade-off → the surprise or stumble → the lesson, what you would
do differently.

## Three provenance markers

Keep these in both the raw notes and the final node, to separate original memory
from added knowledge:

- **[Memory]** — told by the user; original experiential asset, irreplaceable.
- **[Added — source]** — background knowledge the assistant added; must carry a
  reputable source (verify the link at distillation time).
- **[Uncertain]** — areas the user does not clearly remember. Stay honest; do not
  infer, do not force the memory.

In the final node you may pull the personal experience into its own section
instead of scattering inline markers, as long as the boundary between memory and
background knowledge stays clear.

## Principles

- Never fabricate the user's experience. To enrich, only add sourced background
  knowledge marked **[Added — source]**.
- Do not over-pack a cluster; prefer concrete cues over open questions.
- Respect the user's pace: they answer one point at a time, not all at once.

## Canonical example

The `excavate-knowledge` skill in `wiki` is the full version of this method —
leaf-based sessions, the cued-recall frame, the three markers, and the hand-off
to `add-knowledge` for distillation.

## Connects to

- Hands off to [distill-note](distill-note.md) and
  [build-knowledge-graph](build-knowledge-graph.md).

## Reminder

Run the interview in Vietnamese; keep widely-used technical terms in English.
