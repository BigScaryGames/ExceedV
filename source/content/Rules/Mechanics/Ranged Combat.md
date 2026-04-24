Ranged attacks must overcome a **Distance DC** before the defender rolls.

| Range Increment | Distance DC |
| --------------- | ----------- |
| 0 (point blank) | 10          |
| 1               | 12          |
| 2               | 14          |
| 3               | 16          |
| 4               | 18          |
| 5               | 20          |

Attacks that roll below the Distance DC miss automatically - the shot goes wide before reaching the target.

If the attack equals or exceeds the Distance DC, the defender may use Block or Dodge against the attack roll as normal.

The **[[Aim]]** action reduces the Distance DC by 2.

## Range Increment Calculation

Each weapon defines its own **Range Increment** in meters (e.g., a shortbow might have 15m increments, while a longbow has 25m).

**To determine your range increment:**

| Situation | Range Increment |
| --------- | --------------- |
| Target is in the same [[Skirmish]] as you | 0 (point blank) |
| Target is in the same zone but not in your skirmish | 1 |
| Target is in a different zone | `ceil(Total Distance / Weapon Range Increment)` |

**Total Distance:** Sum of line distances from your zone to the target's zone.

### Example
- Your longbow has a 25m range increment
- Target is in zone C, you are in zone A
- Lines: A→B is 15m, B→C is 15m
- Total Distance = 30m
- Range Increment = ceil(30 / 25) = 2
- Distance DC = 14
