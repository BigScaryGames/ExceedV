#THIS IS A DESIGN DOCUMENT

Actions and Traits Logic

## Core Principle
Primary trait defines mechanical template. Secondary traits modify behavior.

**Action Format:**
Action Name | AP Cost
Primary Trait, Secondary Traits
Description

---

## Primary Traits

**#Attack**
This action requires a contested attack roll.

**#Spell**
This action requires a [Casting Check] to succeed at evoking the spell. If it targets a contested check or a DC (like attack or treatment) the result of the casting check is used against that.

**#Skill**
This action requires a skill level or a skill check as per description of the action.

**#Defense**
This action is a response to an #Attack action.

**#Move**
This action involves moving through space.

**#Interact**
Broad category that includes item manipulation like moving, throwing, stawing, picking up of an item or physical interaction with other creatures like treating wounds.

---

## Secondary Traits

**Defense Types**
#Strike → Block, Parry, Dodge
#Projectile → Block, Dodge (Parry with perks)
#Burst → Dodge (Block/Parry with perks)
#Mind → Endure
#Body → Endure

**Effects**
#Boon → Beneficial
#Bane → Detrimental
#Protection → Damage mitigation
#Healing → HP restoration/consequence treatment

**Magic Categiry**
#Conjuration → Creates/summons
#Manipulation → Controls reality/objects
#Transformation → Changes form/shape
#Scrying → Information gathering
#Illusion → Sensory effects
#Ward → Defensive barriers
#Attuned -> Spells and item effects that can be maintained using the limit.

**Bonus Types**
#Competence, #Enhancement, #Morale, #Equipment → Don't stack same type
#Situational → Can stack.
#Luck -> **Advantage/Disadvantage** → Direct dice modifiers (3d10 keep 2)
---

## Basic Actions

| Action | AP | Traits | Description |
|--------|----|---------| ------------|
| [[Step]] | 1 | #Move | Move 1m, no reactions provoked |
| [[Stride]] | 1 | #Move | Move Speed/2 rounded up |
| [[Run]] | 1 | #Move | Move full speed (after stride) |
| [[Block]] | - | #Defense #Strike/#Projectile | Shield defense roll |
| [[Parry]] | - | #Defense #Strike | Weapon defense roll |
| [[Dodge]] | - | #Defense #Strike/#Projectile/#Burst | Agility defense roll |
| [[Endure]] | - | #Defense #Mind/#Body | Will/Endurance defense roll |
| [[Melee Attack]] | 2-4 | #Attack #Strike | Close combat attack |
| [[Ranged Attack]] | 2-4 | #Attack #Projectile | Ranged weapon attack |
| [[Cast A Spell]] | Variable | #Spell | Active spell casting |
| [[Demoralize]] | 1 | #Skill #Bane #Mind | Intimidation vs Endure |
| [[Deduce]] | 1 | #Skill | Knowledge skill for information |
| [[identify]] | varies | #Skill | Knowledge skill for information |
| [[First Aid]] | 4 | #Interact #Healing | Medicine skill, restore HP |
| [[Aid]] | 2+R | #Interact #Boon | Provide bonus to ally action |
