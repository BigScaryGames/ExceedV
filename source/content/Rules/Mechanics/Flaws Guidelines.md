This guideline is mainly for design purposes.

# Intro into Flaw Design

The basic formula for calculating is **Severity × Frequency**. It is calculated in different ways based on flaw type.

There are 5 flaw types. This doesn't automatically put them into #Skill or #Combat categories for XP, so tags will remain present.

1. Addictions
2. Stigmas
3. Personality
4. Bodily
5. Supernatural

---

**`Chance of appearance`** is a hidden GM roll on chances of issue coming to play during game if applicable, as per GM. This doesn't count player's play-style or what they are going to do, so it's an approximation, as well as a hidden roll at the start of session to see if it will come up if applicable.

**`Resisting a flaw`** is a flat d10 roll that is only modified by circumstances by GM and not stats. That resist roll already considers character's willpower, their endurance and other stats and perks. You have to roll above DC to resist.

---

# Addictions

Addictions are a broad category, but here we focus on substances, and not things like gambling or nymphomania - those are for Personality issues.

Addictions will be staged in later versions, but currently it's unavailable. (maybe V0.8)

When calculating **Severity** we look at 4 factors:

1. Availability, Costs and Legality (1-3 cost)
2. Severity - how much it debilitates character (1-5)
3. Withdrawal
4. Drawbacks under substance

---

## Inner Calculation for Addictions

**Availability and Legality**

| Value | Description |
|-------|-------------|
| 0 | Free |
| 1 | Legal and cheap |
| 2 | Expensive and legal, or cheap and illegal |
| 3 | Expensive and illegal |

**Severity** - 1-5 scale. We take under effect condition.

**Drawbacks** under substance and withdrawal - take highest on a scale of 1-3.

---

## Frequency Calculation

The **Frequency** in addictions is calculated as Intake Frequency Requirement (0-1) + Resist Roll (DC/10). These are character request specific.

If character skips his intake at frequency time - he rolls to resist seeking substance.
Skipping intake for second time - results in drawback activating.

**Intake Frequency Requirement**

| Frequency | Daily | Bi-daily | Every 5 days | Every 10 days |
|-----------|-------|----------|--------------|---------------|
| Value     | 1     | 0.6      | 0.4          | 0.2           |

---

## Examples

### Alcoholism - mild to severe

It's 1 available and cheap. (Yes, cheap alcohol is more harmful, add "methanol poisoning if you want to play full simulationism")

**Severity:**
- Availability: 1
- Drunk Condition: gives disadvantage on most checks, so 3
- Drawbacks: 2
- Withdrawal: 3
- **Severity Sum: 7**

**Frequency:**
- Our drinker drinks after work every day and on weekends (1.0 for frequency)
- He rarely resists his friends calling him to drink, but doesn't jump on all drinks in vicinity, only half of them (DC 5 = 0.5)
- **Frequency Sum: 1.5**

**Result:** 1.5 × 7 ≈ **10 XP**

**Effects:**
- Drunk effect when drunk
- Roll above DC 5 to resist an offer to drink (this IS modified by #Attitude and things like combat state, so a life enemy offering a drink will not be required. But taking a sip of vodka on table while burglarizing?)

---

### Meth Addict

**Severity:**
- Availability: 3 (expensive and illegal)
- Severity: same as drunk (we don't look at long-term consequences like falling teeth) - 3
- Effect is worse than withdrawal (both 3)
- **Severity Sum: 9**

**Frequency:**
- Our meth addict is likely consuming multiple times a day (1.0)
- Can't resist meth and will sell his house/do crime for it (1.0)
- **Frequency Sum: 2.0**

**Result:** 2.0 × 9 = **18 XP**

---

### Smoking

**Severity:**
- Availability: 0 (cheap, almost free - setting dependent)
- Effect condition: 1
- Drawback: 0
- Withdrawal: 1 (doesn't last that long and you can't die from it, you just get debuffs on concentration)
- **Severity Sum: 2**

**Frequency:**
- 1.0 for a daily smoker
- 0.5 to resist a random smoke when available
- **Frequency Sum: 1.5**

**Result:** 1.5 × 2 = **3 XP**

**Effects:**
- -3 points to Endurance or Charisma (your lungs are fine, but you stink of cigs)
- All running and forced march checks are rolled with -1

---

# Stigma
Stigma relates to social perception. Base price 5. Stigmas can lack an attribute penalty.

Here we rely on:
1. How often might encounter in campaign. (being a slave in a city and wilderness are different). This includes ease of hiding said stigma. (multiply by 0.2 to 2) Being a low-born in noble intrigue game is a Stigma, in an adventurer campaign isn't.
2. The consequences of stigma. e.g. a witch getting into forced into reeducation camp, slaves being brought back to owners, children being not very. (0.2 to 2)

Thus a Child can be a minor stigma.
x2 for being often encountered and hard to hide (in most social campaigns), and x0.2 for the consequences of stigma for overall -2 points. Negative effects "Adults and others will start with -1 Starting Attitude, and react with -2 on you breaching adult topics."

Known serial killer with a bounty would be -2 to -20. In a functioning society its -20. As people who are not criminal degenerates are going to report you, start with -3 to -5 negative attitude, and consequences are being hanged.

# Personality
Personality flaws are internal compulsions, biases, and emotional vulnerabilities. These include gambling, kleptomania, cowardice, greed, compulsive lying, phobias, and other behavioral issues that character struggles to control.

Personality flaws don't always carry attribute penalties, but when they do, it reflects deep-rooted psychological or physiological damage.

The formula for Personality flaws is **Frequency × Severity**.

## Frequency Calculation

Frequency = (Average appearance of trigger) + (Resist DC / 10)

| Component | Range | Description |
|-----------|--------|-------------|
| Average appearance of trigger | 0.1 to 1.0 | How often relevant situations arise in campaign |
| Resist DC / 10 | 0.1 to 1.0 | How hard to resist when triggered (DC 2 = 0.2, DC 8 = 0.8) |

**Frequency Range:** 0.2 to 2.0

## Severity Calculation

Severity = (Consequences/Legality) + (Compulsion severity) + (Triggered effects)

| Component | Range | Description |
|-----------|--------|-------------|
| Consequences/Legality | 1 to 3 | Legal/social severity - administrative punishment (1), criminal (2), severe (3) |
| Compulsion severity | 1 to 3 | Urge strength when resisted - mild (1), moderate (2), overwhelming (3) |
| Triggered effects | 1 to 3 | What happens when you give in - minor (1), significant (2), severe (3) |

**Severity Range:** 3 to 9

## Examples

### Kleptomania
Compulsion to steal small, non-essential items when opportunity presents itself.

**Frequency:**
- Trigger appears when shopping and items are poorly placed = 0.5
- Can resist 8/10 times (DC 8) = 0.2 (2/10 chance to fail)
- Frequency Sum: **0.5 + 0.2 = 0.7**

**Severity:**
- Legality: 2 (illegal, but administrative punishment, not death penalty)
- Consequences: 3 (reputation loss, possible stigma)
- Drawbacks/Effects: 1 (minor stigma if caught)
- Severity Sum: **2 + 3 + 1 = 6**

**Result:** 0.7 × 6 = **4.2 ≈ 4 XP**

**Effects:**
- Attribute: -4 points in Will (compulsion overrides rational decision)
- When triggered by opportunity to steal, must roll above DC 8 or make attempt to steal within one turn or feel increasing #Shaken

# Bodily
Bodily flaws represent physical disabilities, injuries, or limitations. These include missing limbs, organ damage, sensory impairment, chronic pain, and other permanent physical conditions.

These are the most straightforward flaws in terms of pricing - they typically include an attribute penalty reflective of the actual physical limitation, plus situational penalties.

GM will look at 2 factors.
1. **Attribute impact** - Which attributes are affected and to what degree. (-5 to -20 XP)
2. **Situational limitations** - What character cannot do, or what they do at penalty. (-5 to -20 XP)

E.g. One-Eyed.
Missing one eye. Depth perception severely affected, peripheral vision gone.
Attribute impact: -10 points in Perception (-10 XP)
Situational: -2 to #Strike attacks in melee combat and all checks relying on sight (ranged attacks, Perception checks) (-10 XP)
Total: -20 XP

E.g. Crippled Leg.
Leg damaged such that walking is painful, running impossible.
Attribute impact: -15 points in Agility (-15 XP)
Situational: Cannot Run action, -1 AP per turn, -2 on Balance/Acrobatics checks (-10 XP)
Total: -25 XP

E.g. Missing Arm.
One arm missing entirely. Cannot two-hand weapons, cannot use shields, off-hand actions impossible.
Attribute impact: -15 points in Dexterity (fine motor control reduced) (-15 XP)
Situational: Cannot use weapons requiring two hands, cannot use shields, -2 on all tasks requiring two hands (carrying, climbing) (-15 XP)
Total: -30 XP

# Supernatural
Supernatural flaws are curses, magical afflictions, unnatural traits, and conditions that exist beyond normal biology. These include curses, lycanthropy, vampirism, born magical susceptibility, pact-bound limitations, and otherworldly taints.

These flaws are often the most severe due to their unpredictable nature, visibility, and potential for escalation.

GM will look at 4 factors.
1. **Origin** - Was it chosen (pact, ritual) or inflicted (curse, born)? Inflicted flaws are worth more.
2. **Visibility** - Is it concealed or obvious? Visible flaws carry social stigma automatically.
3. **Control** - Does character have agency over it, or does it act against them?
4. **Effects** - What does it do mechanically?

Base price 10, adjusted by factors.

E.g. Witch-Blood.
Born with visible signs of magical affinity. In superstitious communities, this is dangerous.
Origin: Born (no modifier)
Visibility: Obvious (×2) - marks, faint aura, unusual eye color
Control: None - it's just what they are
Effects: Starts with -2 Attitude in religious/superstitious communities, may be accused of causing misfortune
10 × 2 = -20 XP
Attribute: -10 points in Charisma (social stigma)
Effects: #Stigma: Witch-Blood in superstitious regions

E.g. Cursed by Witch.
Hexed to always be slightly unlucky.
Origin: Inflicted (×1.5)
Visibility: Concealed (×0.5)
Control: Acts against character (×1.5)
Effects: Once per day, must re-roll a natural 10 and take second result (which may be lower)
10 × 1.5 × 0.5 × 1.5 = -11.25 ≈ -10 XP
Attribute: -10 points in Perception (things just seem to happen)
Effects: Bad Luck once per day

E.g. Pact with Dark Entity.
Sold something (voice, shadow, firstborn) for power.
Origin: Chosen (×0.5)
Visibility: Concealed usually, but entity may manifest (×1)
Control: Contractual obligations (×1.5)
Effects: Must perform services for entity periodically, entity can claim payment at any time
10 × 0.5 × 1 × 1.5 = -7.5 ≈ -8 XP
Attribute: -10 points in Will (bound to another)
Effects: Debt owed to [entity], entity can compel services
