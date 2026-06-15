# discover-sources

> Find *where to read* and hand the user the original links. Do not read or
> summarize for them.

## When to use

- "Find me sources on X", "where can I read about Y?", "find sources on…".
- The opening phase of a research session, when the raw material is original
  sources.

## Principle

Finding sources is **load** — give it to the assistant. Reading, weighing, and
synthesizing into understanding is **thinking** — it belongs to the user. If the
assistant reads the pages and returns a tidy summary, the user gets an answer
they never built: borrowed understanding that collapses the moment it is probed.

## Method

1. Use the built-in web search (WebSearch) to locate sources for the topic.
2. Return **only the original links** with their title/source, enough for the
   user to choose which to open.
3. Stop there. Do NOT open pages, read, summarize, compare, rank, or synthesize.
4. If the user asks you to "summarize" / "digest": in Assistive mode, stop and
   hand it back (see [principles](principles.md)); only read/synthesize once in
   Autonomous mode.

## Canonical example

The `source-finder` skill in `kb-client` (`allowed-tools: WebSearch`): it finds
public sources, returns **exactly the original links** for the user to read, and
refuses to open/read/summarize/rank them. That is the model for the stance
"finding is load, reading is thinking".

## Anti-patterns

- Returning a summary instead of links (in Assistive mode).
- Ranking "this source is best" — that is the user's judgment.
- Inventing links or unchecked citations.

## Connects to

- Once you have sources, use [select-sources](select-sources.md) to choose
  trustworthy ones by object type.

## Reminder

Reply to the user in Vietnamese; keep widely-used technical terms in English.
