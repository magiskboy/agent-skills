# challenge-claims

> Relay real counter-arguments from real people or real sources. Never invent a
> rebuttal of your own.

## When to use

- "Has anyone argued against this?", "what are the counter-arguments to this
  position?", "rebut my claim".
- After the user states a claim (a note with `claim: true`) and wants friction.

## Principle

The value of friction is that it comes from a **different mind** that actually
disagrees. An objection the assistant makes up is just the user's own model
talking back to them in a costume — it cannot genuinely surprise or correct them.
So the assistant is a loudspeaker for other people's disagreement, not a debater.

## Method

1. Take the user's claim and go looking for **real** pushback — anonymized
   arguments from real people (via a server/community) or documented critiques
   from real sources.
2. Relay whatever comes back **verbatim**, attributed as external.
3. If nothing real is found, **say so plainly** — do not fill the gap with an
   invented counter-argument.
4. Never generate an objection of your own and present it as a rebuttal.

## Relation to evidence

This pairs with the rule from [select-sources](select-sources.md): every claim
needs reputable evidence. Challenging a claim means finding *real* opposing
evidence, not constructing a plausible-sounding one.

## Canonical example

The `fracture-mirror` skill in `kb-client` is the model: it fetches anonymized
counter-arguments written by real people and relays them verbatim, NEVER invents
one, and when the source returns none it says so plainly.

## Anti-patterns

- Steelmanning an objection the assistant invented and passing it off as external.
- Softening or paraphrasing a real rebuttal until it loses its bite.
- Silence when no real pushback is found (say "none found" instead).

## Reminder

Relay and report to the user in Vietnamese; keep widely-used technical terms in
English. Quote external arguments faithfully.
