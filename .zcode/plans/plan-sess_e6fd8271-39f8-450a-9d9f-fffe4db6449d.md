Reorganize `Rules/Social And World/Social Interactions.md` into clean sections with verbatim text, extracting two reference files. No prose rewriting; the only word-level changes are the agreed attitude→disposition term swaps and one link-token fix.

## File 1 — `Rules/Social And World/Social Interactions.md` (reorganized)

New structure, in the draft's own order (model after scene intro, procedures after). Every block is verbatim from the current file unless noted:

```
(intro sentence: "Whether conducting negotiations…")
(two-mode bullets: Social Interaction / Social Combat Subsystem TBD)

## The Social Interaction Scene
    - scene paragraph + initial-impression paragraph + 3-activities list
      (list item 1: fix [[Asess]] → [[Assess]] to match line 76 — link-token fix only)
    - Flow opening paragraphs (initial disposition procedure, pre-encounter
      reputation, "sets the prices, NPC behavior…" line)

## NPC Values
![[NPC Values]]                      ← embed replaces inline section

## Disposition
![[Disposition System]]              ← embed replaces inline section AND the dead
                                        ![[Attitude System]] embed (file renamed)

## Social Activities
    ### [Assess]
        - gauge-the-level paragraph ("Players then can read the room…")
        - the two quoted read-example lines
    ### [Impress]
        - the 4-step procedure + "The target will either change…" line
    ### [Suggest]
        - "Players can ask for favors without assessments…" paragraph
        ### Bribes and Threats [SETTLED] - Wants and Needs   (demoted to ### —
            it declares itself part of [Suggest]; bullets verbatim)
        - Asking for a Favor block (intro paras + table + fragments)

## Social Actions
    ### Detect Falsehood
    ### Fast-Talk

## GM Guidelines                      (verbatim; term swaps only, see below)

## Example Character                  (3 examples verbatim)

## Social Combat [OPEN — sketch LATER MS]   (verbatim, incl. "sign.")

## Trading
![[Trading Rules]]
```

## File 2 — `Rules/Mechanics/Disposition System.md` (rewritten)

Replaces the stale old-attitude stub wholesale with the chapter's Disposition section, verbatim: intro line ("raw value and level following the math logic of attributes…"), the points/levels table, the two follow-up lines. Keeps the file's existing `**Tags:** #Social` line. Its old content (initial-disposition factors, "first meeting −1 to 1") is superseded by the chapter's Flow + GM Guidelines text and disappears with the rewrite.

## File 3 — `Rules/References/NPC Values.md` (new)

Verbatim move of the chapter's NPC Values section: intro paragraph, the three band lines, the six-axis table, the writing-convention line, `## A bit on aspects` (demoted from ###), and `## Traits` (Trusting/Suspicious/Vengeful/Forgiving). Adds `**Tags:** #Social`. Placed in References/ alongside Rank System / Defense Traits so NPC and Encounter Builder can embed it later.

## Term swaps (exhaustive — attitude → disposition, nothing else)

1. [Impress] skill list: "Intimidation (efficient for lowering attitude)" → "(efficient for lowering disposition)"
2. [Impress] outcome: "change attitude or resist" → "change disposition or resist"
3. Asking for a Favor table header `| Attitude |` → `| Disposition |`
4. "(+1 attitude for this favor)" → "(+1 disposition for this favor)"
5. GM Guidelines: "to set initial attitude" → "to set initial disposition"

## Left untouched, flagged for you (per verbatim instruction)

- Disposition table: −2 appears twice (Wary row reads like it should be −1)
- "−3/+3 progression" line in GM Guidelines (old-system math vs new points table)
- Stray "sign." line; "Negotiating a deal" dangling fragment; [Impress] steps 2–3 redundancy
- Typos: cicling, dothings, vlaues, Ascectic, Beind, descruction, sircumstances, workplase, Actiions
- [[Assess]] has no target file yet (forward link, expected — like other planned actions)

## Execution notes

- You edited files minutes ago (Attitude→Disposition rename landed mid-read), so I will re-read all three targets immediately before writing to capture your latest state.
- Full-file Writes via the file tools (a reorder+extract isn't a surgical section save); then run `python3 tools/consistency_check.py` per AGENTS.md and report results. No commits — diff shown for your review.