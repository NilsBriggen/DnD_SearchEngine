l = [
    {
        "index": "fireball",
        "name": "Fireball",
        "desc": [
            "A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.",
            "The fire spreads around corners. It ignites flammable objects in the area that aren't being worn or carried.",
        ],
        "higher_level": [
            "When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd."
        ],
        "range": "150 feet",
        "components": ["V", "S", "M"],
        "material": "A tiny ball of bat guano and sulfur.",
        "ritual": False,
        "duration": "Instantaneous",
        "concentration": False,
        "casting_time": "1 action",
        "level": 3,
        "damage": {
            "damage_type": {
                "index": "fire",
                "name": "Fire",
                "url": "/api/damage-types/fire",
            },
            "damage_at_slot_level": {
                "3": "8d6",
                "4": "9d6",
                "5": "10d6",
                "6": "11d6",
                "7": "12d6",
                "8": "13d6",
                "9": "14d6",
            },
        },
        "dc": {
            "dc_type": {
                "index": "dex",
                "name": "DEX",
                "url": "/api/ability-scores/dex",
            },
            "dc_success": "half",
        },
        "area_of_effect": {"type": "sphere", "size": 20},
        "school": {
            "index": "evocation",
            "name": "Evocation",
            "url": "/api/magic-schools/evocation",
        },
        "classes": [
            {"index": "sorcerer", "name": "Sorcerer", "url": "/api/classes/sorcerer"},
            {"index": "wizard", "name": "Wizard", "url": "/api/classes/wizard"},
        ],
        "subclasses": [
            {"index": "lore", "name": "Lore", "url": "/api/subclasses/lore"},
            {"index": "fiend", "name": "Fiend", "url": "/api/subclasses/fiend"},
        ],
        "url": "/api/spells/fireball",
    },
    {
        "index": "fire",
        "name": "Fire",
        "desc": [
            "Red dragons breathe fire, and many spells conjure flames to deal fire damage."
        ],
        "url": "/api/damage-types/fire",
    },
    {
        "index": "wand-of-fireballs",
        "name": "Wand of Fireballs",
        "equipment_category": {
            "index": "wand",
            "name": "Wand",
            "url": "/api/equipment-categories/wand",
        },
        "rarity": {"name": "Rare"},
        "variants": [],
        "variant": False,
        "desc": [
            "Wand, rare (requires attunement by a spellcaster)",
            "This wand has 7 charges. While holding it, you can use an action to expend 1 or more of its charges to cast the fireball spell (save DC 15) from it. For 1 charge, you cast the 3rd-level version of the spell. You can increase the spell slot level by one for each additional charge you expend.",
            "The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the wand's last charge, roll a d20. On a 1, the wand crumbles into ashes and is destroyed.",
        ],
        "url": "/api/magic-items/wand-of-fireballs",
    },
]

l1 = [
    {
        "Index": "fireball",
        "Name": "Fireball",
        "Desc": [
            "A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.",
            "The fire spreads around corners. It ignites flammable objects in the area that aren't being worn or carried.",
        ],
        "Higher level": [
            "When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd."
        ],
        "Range": "150 feet",
        "Components": ["V", "S", "M"],
        "Material": "A tiny ball of bat guano and sulfur.",
        "Ritual": "False",
        "Duration": "Instantaneous",
        "Concentration": "False",
        "Casting time": "1 action",
        "Level": "3",
        "Damage": {
            "damage_type": ["fire", "/api/damage-types/fire"],
            "damage_at_slot_level": {
                "3": "8d6",
                "4": "9d6",
                "5": "10d6",
                "6": "11d6",
                "7": "12d6",
                "8": "13d6",
                "9": "14d6",
            },
        },
        "Dc": {
            "dc_type": {
                "index": "dex",
                "name": "DEX",
                "url": "/api/ability-scores/dex",
            },
            "dc_success": "half",
        },
        "Area of effect": {"type": "sphere", "size": 20},
        "School": ["evocation", "/api/magic-schools/evocation"],
        "Classes": [
            ["sorcerer", "/api/classes/sorcerer"],
            ["wizard", "/api/classes/wizard"],
        ],
        "Subclasses": [
            ["lore", "/api/subclasses/lore"],
            ["fiend", "/api/subclasses/fiend"],
        ],
    },
    {
        "Index": "fire",
        "Name": "Fire",
        "Desc": [
            "Red dragons breathe fire, and many spells conjure flames to deal fire damage."
        ],
    },
    {
        "Index": "wand-of-fireballs",
        "Name": "Wand of Fireballs",
        "Equipment category": ["wand", "/api/equipment-categories/wand"],
        "Rarity": {"name": "Rare"},
        "Variants": [],
        "Variant": "False",
        "Desc": [
            "Wand, rare (requires attunement by a spellcaster)",
            "This wand has 7 charges. While holding it, you can use an action to expend 1 or more of its charges to cast the fireball spell (save DC 15) from it. For 1 charge, you cast the 3rd-level version of the spell. You can increase the spell slot level by one for each additional charge you expend.",
            "The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the wand's last charge, roll a d20. On a 1, the wand crumbles into ashes and is destroyed.",
        ],
    },
]
