const readline = require("readline");

const units = {
  "Elite Riders": { cost: 6, options: { "Mounted missiles": 2, "Level Headed": 2, "Any fantasy ability": "any" } },
  "Heavy Riders": { cost: 4, options: { "Mounted missiles": 1, "Chariots": 2, "Any fantasy ability": "any" } },
  "Light Riders": { cost: 4, options: { "Short Range Missiles": -1, "Any fantasy ability": "limited" } },
  "Greater Warbeasts": { cost: 6, options: { "Flame Attack": 2, "Ponderous": 1, "Cunning": 2, "Any fantasy ability": "limited" } },
  "Lesser Warbeasts": { cost: 4, options: { "Flame Attack": 2, "Cunning": 2, "Any fantasy ability": "limited" } },
  "Elite Foot": { cost: 6, options: { "Missiles": 2, "Any fantasy ability": "any" } },
  "Heavy Foot": { cost: 4, options: { "Offensive": 2, "Any fantasy ability": "any" } },
  "Light Foot": { cost: 3, options: { "Offensive": 2, "Short Range Missiles": 1, "Mixed Weapons": 2, "Any fantasy ability": "any" } },
  "Bellicose Foot": { cost: 4, options: { "Armor": 2, "Any fantasy ability": "limited" } },
  "Heavy Missiles": { cost: 4, options: { "Weighty Projectiles": -1, "Any fantasy ability": "limited" } },
  "Light Missiles": { cost: 4, options: { "Sharpshooter": 2, "Any fantasy ability": "limited" } },
  "Scouts": { cost: 2, options: { "Any fantasy ability": "limited" } },
  "Levies": { cost: 1, options: { "Undead": 0, "Venomous": 2, "Hatred": 1, "Fear": 2 } },
};

const fantasyAbilities = {
  Slayer: 4,
  Exploder: 2,
  Fear: 2,
  Fearful: -2,
  "Flying/Burrowing": 2,
  Hatred: 1,
  Invisibility: 3,
  "Enchanted Weapons": 2,
  "Mystical Armor": 2,
  Spellcaster: 4,
  Wizardling: 2,
  Summoner: 3,
  "Were Creatures": 1,
  "Undead": 0,
};

const leaderSkills = {
  Aggressive: 1,
  Blessed: 2,
  Bloodthirsty: 3,
  Braveheart: 1,
  Brutal: 1,
  Commanding: 2,
  Courageous: 2,
  Eccentric: 1,
  Fearless: 2,
  Fearsome: 2,
  Impulsive: 1,
  Insipid: -2,
  Inspired: 3,
  Knockkneed: -1,
  Lionheart: 2,
  Patient: 1,
  Rash: 1,
  Strongbow: 1,
  Strongsword: 1,
  "The Great": 3,
  "Old Wound": -1,
  Vulnerable: -1,
  Weakling: -2,
  Wise: 1,
};

const limitedFantasyAbilities = ["Spellcaster", "Summoner", "Slayer"];
const abilityTypes = ["Celestial", "Demon", "Elemental", "Undead"];

function displayHelp() {
  console.log(`Usage: node warband.js [points]

  Arguments:
    points    The number of points available to build the warband.

  Example:
    node warband.js 20
  `);
}

// Weighted random function to decide how many leader abilities (0, 1, or 2)
function getRandomLeaderAbilitiesCount() {
  const roll = Math.random();
  if (roll < 0.5) return 0; // 50% chance of no skills
  if (roll < 0.8) return 1; // 30% chance of 1 skill
  return 2; // 20% chance of 2 skills
}

function generateWarband(points) {
  let remainingPoints = points;
  const warband = {};

  const unitsList = Object.keys(units);
  const leaderUnit = unitsList[Math.floor(Math.random() * unitsList.length)];
  warband["Leader"] = {
    unit: leaderUnit,
    skills: [],
    cost: units[leaderUnit].cost,
  };

  remainingPoints -= warband["Leader"].cost;

  // Determine how many leader skills (0, 1, or 2)
  const maxLeaderAbilities = getRandomLeaderAbilitiesCount();
  const leaderSkillsKeys = Object.keys(leaderSkills);

  // Assign leader skills, ensuring the maximum of 2 abilities
  while (warband["Leader"].skills.length < maxLeaderAbilities && remainingPoints > 0) {
    const randomSkill = leaderSkillsKeys[Math.floor(Math.random() * leaderSkillsKeys.length)];
    const skillCost = leaderSkills[randomSkill];

    if (warband["Leader"].skills.find((skill) => skill.name === randomSkill)) {
      continue;
    }

    warband["Leader"].skills.push({ name: randomSkill, cost: skillCost });
    remainingPoints -= skillCost;
  }

  // Assign other units and their options
  while (remainingPoints > 0) {
    const randomUnit = unitsList[Math.floor(Math.random() * unitsList.length)];
    const unit = { name: randomUnit, options: [], cost: units[randomUnit].cost };

    if (remainingPoints - unit.cost < 0) continue;

    remainingPoints -= unit.cost;

    const optionsKeys = Object.keys(units[randomUnit].options);
    for (let i = 0; i < optionsKeys.length; i++) {
      if (remainingPoints <= 0) break;

      const option = optionsKeys[i];
      const optionCost = units[randomUnit].options[option];

      if (option === "Any fantasy ability") {
        const fantasyAbilityKeys = Object.keys(fantasyAbilities);
        const randomFantasyAbility =
          fantasyAbilityKeys[Math.floor(Math.random() * fantasyAbilityKeys.length)];
        const fantasyAbilityCost = fantasyAbilities[randomFantasyAbility];

        if (
          limitedFantasyAbilities.includes(randomFantasyAbility) &&
          units[randomUnit].options["Any fantasy ability"] === "limited"
        ) {
          continue;
        }

        if (
          unit.options.find((opt) => opt.name === randomFantasyAbility) ||
          remainingPoints - fantasyAbilityCost < 0
        ) {
          continue;
        }

        const ability = { name: randomFantasyAbility, cost: fantasyAbilityCost };
        if (randomFantasyAbility === "Summoner" || randomFantasyAbility === "Slayer") {
          ability.type = abilityTypes[Math.floor(Math.random() * abilityTypes.length)];
        }

        unit.options.push(ability);
        remainingPoints -= fantasyAbilityCost;
      } else if (optionCost !== "any" && optionCost !== "limited") {
        if (unit.options.find((opt) => opt.name === option)) continue;
        unit.options.push({ name: option, cost: optionCost });
        remainingPoints -= optionCost;
      }
    }

    warband[randomUnit] = unit;
  }

  if (remainingPoints !== 0) {
    console.log("Unable to use all points with the current configuration. Please try again.");
    return;
  }

  console.log(`Warband Generated (Points: ${points}):\n`);

  console.log(`Leader: ${warband["Leader"].unit} (${warband["Leader"].cost} pts) with skills:`);
  warband["Leader"].skills.forEach((skill) => console.log(`  - ${skill.name} (${skill.cost} pts)`));

  for (const unitKey of Object.keys(warband)) {
    if (unitKey !== "Leader") {
      const unit = warband[unitKey];
      console.log(`${unit.name}: ${unit.cost} pts`);
      unit.options.forEach((opt) => {
        if (opt.type) {
          console.log(`  - ${opt.name} (${opt.cost} pts) [${opt.type}]`);
        } else {
          console.log(`  - ${opt.name} (${opt.cost} pts)`);
        }
      });
    }
  }
}

const points = parseInt(process.argv[2], 10);

if (isNaN(points)) {
  displayHelp();
} else {
  generateWarband(points);
}
