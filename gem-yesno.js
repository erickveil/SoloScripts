#!/usr/bin/env node

const probabilities = {
    "AI": {
        name: "Almost Impossible",
        ranges: [
            { range: [1, 25], result: "No, and" },
            { range: [26, 75], result: "No" },
            { range: [76, 90], result: "No, but" },
            { range: [91, 96], result: "Yes, but" },
            { range: [97, 99], result: "Yes" },
            { range: [100, 100], result: "Yes, and" }
        ]
    },
    "VU": {
        name: "Very Unlikely",
        ranges: [
            { range: [1, 20], result: "No, and" },
            { range: [21, 70], result: "No" },
            { range: [71, 80], result: "No, but" },
            { range: [81, 90], result: "Yes, but" },
            { range: [91, 97], result: "Yes" },
            { range: [98, 100], result: "Yes, and" }
        ]
    },
    "UL": {
        name: "Unlikely",
        ranges: [
            { range: [1, 15], result: "No, and" },
            { range: [16, 55], result: "No" },
            { range: [56, 65], result: "No, but" },
            { range: [66, 80], result: "Yes, but" },
            { range: [81, 92], result: "Yes" },
            { range: [93, 100], result: "Yes, and" }
        ]
    },
    "UK": {
        name: "Unknown",
        ranges: [
            { range: [1, 10], result: "No, and" },
            { range: [11, 40], result: "No" },
            { range: [41, 50], result: "No, but" },
            { range: [51, 60], result: "Yes, but" },
            { range: [61, 90], result: "Yes" },
            { range: [91, 100], result: "Yes, and" }
        ]
    },
    "LI": {
        name: "Likely",
        ranges: [
            { range: [1, 7], result: "No, and" },
            { range: [8, 17], result: "No" },
            { range: [18, 32], result: "No, but" },
            { range: [33, 44], result: "Yes, but" },
            { range: [45, 85], result: "Yes" },
            { range: [86, 100], result: "Yes, and" }
        ]
    },
    "VL": {
        name: "Very Likely",
        ranges: [
            { range: [1, 3], result: "No, and" },
            { range: [4, 10], result: "No" },
            { range: [11, 20], result: "No, but" },
            { range: [21, 30], result: "Yes, but" },
            { range: [31, 80], result: "Yes" },
            { range: [81, 100], result: "Yes, and" }
        ]
    },
    "AC": {
        name: "Almost Certain",
        ranges: [
            { range: [1, 1], result: "No, and" },
            { range: [2, 4], result: "No" },
            { range: [5, 10], result: "No, but" },
            { range: [11, 25], result: "Yes, but" },
            { range: [26, 75], result: "Yes" },
            { range: [76, 100], result: "Yes, and" }
        ]
    }
};

function getProbabilityResult(probability) {
    const roll = Math.floor(Math.random() * 100) + 1;
    const ranges = probabilities[probability].ranges;

    for (let i = 0; i < ranges.length; i++) {
        const { range, result } = ranges[i];
        if (roll >= range[0] && roll <= range[1]) {
            return result;
        }
    }
    return "Invalid roll"; // Should not happen
}

function printHelp() {
    console.log("Usage: node script.js [probability]");
    console.log("Possible probabilities:");
    Object.keys(probabilities).forEach(abbreviation => {
        console.log(`- ${abbreviation}: ${probabilities[abbreviation].name}`);
    });
}

const args = process.argv.slice(2);
const probability = args[0] ? args[0].toUpperCase() : null;

if (!probability || probability === "--HELP" || probability === "-H") {
    printHelp();
} else if (probabilities[probability]) {
    const result = getProbabilityResult(probability);
    console.log(`Rolled on ${probabilities[probability].name} (${probability}): ${result}`);
} else {
    console.log("Invalid probability argument.");
    printHelp();
}
