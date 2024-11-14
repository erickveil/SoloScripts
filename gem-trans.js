#!/usr/bin/env node

const process = require('process');

// Define the scene transitions and focuses
const sceneTransitions = [
  { range: [1, 20], transition: "No Change" },
  { range: [21, 30], transition: "No Change" },
  { range: [31, 40], transition: "Positive Replacement" },
  { range: [41, 50], transition: "Positive Alteration" },
  { range: [51, 60], transition: "Positive Interruption" },
  { range: [61, 65], transition: "Random Event" },
  { range: [66, 75], transition: "Negative Interruption" },
  { range: [76, 85], transition: "Negative Alteration" },
  { range: [86, 95], transition: "Negative Replacement" },
  { range: [96, 100], transition: "Random Event" }
];

const focuses = [
  { range: [1, 20], focus: "Character List" },
  { range: [21, 30], focus: "New Character" },
  { range: [31, 40], focus: "Adventure Goal" },
  { range: [41, 50], focus: "Quest Giver" },
  { range: [51, 60], focus: "Player Character" },
  { range: [61, 65], focus: "Location List" },
  { range: [66, 75], focus: "Scene Goal" },
  { range: [76, 85], focus: "Quest Target" },
  { range: [86, 95], focus: "Campaign Goal" },
  { range: [96, 100], focus: "Faction List" }
];

// Function to roll a die
function rollDie(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

// Function to get the result from a range
function getResultFromRoll(roll, table) {
  for (let entry of table) {
    if (roll >= entry.range[0] && roll <= entry.range[1]) {
      return entry;
    }
  }
  return null;
}

// Main function
function main() {
  const argument = process.argv[2] ? parseInt(process.argv[2], 10) : 0;
  if (isNaN(argument)) {
    console.error('Please provide a valid integer argument.');
    process.exit(1);
  }

  // Roll d100 and apply the argument
  let transitionRoll = rollDie(100) + argument;

  // Ensure the roll is within 1-100
  if (transitionRoll < 1) transitionRoll = 1;
  if (transitionRoll > 100) transitionRoll = 100;

  const transitionResult = getResultFromRoll(transitionRoll, sceneTransitions);

  if (transitionResult) {
    if (transitionResult.transition === "No Change") {
      console.log(`Transition: ${transitionResult.transition}`);
    } else {
      const focusRoll = rollDie(100);
      const focusResult = getResultFromRoll(focusRoll, focuses);

      if (focusResult) {
        console.log(`Transition: ${transitionResult.transition} - Focus: ${focusResult.focus}`);
      } else {
        console.error('Error in focus roll or table lookup.');
      }
    }
  } else {
    console.error('Error in transition roll or table lookup.');
  }
}

main();
