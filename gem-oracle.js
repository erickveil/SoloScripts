#!/usr/bin/env node

const rolls = {
    approach: [
        "Gracefully", "Unexpectedly", "Quickly", "Unnaturally", "Adamantly", "Noisily", "Seemingly", "Arrogantly", "Wisely", "Recklessly",
        "Maliciously", "Scientifically", "Mysteriously", "Smoothly", "Calmly", "Evenly", "Selfishly", "Innocently", "Simply", "Loudly",
        "Foolishly", "Artificially", "Lovingly", "Faithfully", "Sharply", "Potentially", "Tenaciously", "Oddly", "Bluntly", "Subtly",
        "Partially", "Adventurously", "Awkwardly", "Utterly", "Annoyingly", "Officially", "Painfully", "Superficially", "Persistently", "Angrily",
        "Hopelessly", "Weakly", "Energetically", "Dreamily", "Insatiably", "Obviously", "Randomly", "Cruelly", "Proudly", "Theatrically",
        "Wrongly", "Politely", "Offensively", "Diligently", "Tearfully", "Tactfully", "Inquisitively", "Nervously", "Thoughtfully", "Clearly",
        "Immediately", "Obediently", "Playfully", "Rebelliously", "Freely", "Sarcastically", "Glibly", "Distinctly", "Fatally", "Transparently",
        "Openly", "Courageously", "Safely", "Correctly", "Rudely", "Jealously", "Cleverly", "Devastatingly", "Discreetly", "Bravely",
        "Menacingly", "Elegantly", "Crudely", "Optimistically", "Slowly", "Unethically", "Wickedly", "Neatly", "Flagrantly", "Knowingly",
        "Mostly", "Flatteringly", "Lazily", "Zealously", "Equally", "Greedily", "Blindly", "Fairly", "Naively", "Ruthlessly"
    ],
    intent: [
        "Combine", "Acquire", "Become", "Shatter", "Copy", "Navigate", "Befriend", "Create", "Run", "Share",
        "Predict", "Crush", "Obscure", "Entertain", "Retreat", "Help", "Regenerate", "Grow", "Kill", "Trample",
        "Pierce", "Win", "Banish", "Exploit", "Ruin", "Track", "Retract", "Block", "Spoil", "Store",
        "Dodge", "Deplete", "Overrun", "Craft", "Catch", "Suffocate", "Mourn", "Change", "Decimate", "Enhance",
        "Ascend", "Question", "Annoy", "Achieve", "Disarm", "Fortify", "Trust", "Protect", "Build", "Betray",
        "Overcome", "Deceive", "Slash", "Enchant", "Demand", "Carve", "Forget", "Transform", "Force", "Destroy",
        "Advance", "Break", "Display", "Replace", "Avoid", "Anticipate", "Lacerate", "Enslave", "Purchase", "Reveal",
        "Convince", "Exhaust", "Follow", "Preach", "Preserve", "Promise", "Revive", "Bless", "Reverse", "Curse",
        "Expand", "Summon", "Ward", "Unleash", "Explore", "Annoy", "Devour", "Overshadow", "Heal", "Allow",
        "Ambush", "Discuss", "Float", "Rotate", "Remember", "Observe", "Soften", "Annihilate", "Conquer", "Abandon"
    ],
    theme: [
        "Death", "Heritage", "Spectacle", "Beauty", "Hatred", "Revenge", "Learning", "Perseverance", "Stability", "Shame",
        "Arrogance", "Comfort", "Desire", "Maturity", "Burden", "Destiny", "Pressure", "Memory", "Mistake", "Poverty",
        "Sacrifice", "Armor", "Warmth", "Destruction", "Patience", "Utility", "War", "Rebirth", "Wonder", "Friendship",
        "Failure", "Forgiveness", "Family", "Madness", "Honor", "Paradise", "Surprise", "Property", "Light", "Instinct",
        "Rejection", "Duel", "Weakness", "Completion", "Growth", "Duty", "Volatility", "Language", "Oblivion", "Cure",
        "Bloodshed", "Tool", "Empathy", "Art", "Despair", "Joy", "Life", "Proof", "Progress", "Blackmail",
        "Time", "Promise", "Loss", "Game", "Oath", "Insecurity", "Legacy", "Nature", "Existence", "Wrath",
        "Murder", "Allies", "Culture", "Mentorship", "Conflict", "Tradition", "Cruelty", "Hope", "Aggression", "Knowledge",
        "Production", "Decay", "Suffering", "Sickness", "Starvation", "Solitude", "Clarity", "Protection", "Eternity", "Frustration",
        "Normalcy", "Love", "Truth", "Morality", "Darkness", "Companionship", "Cooperation", "Weapon", "Communication", "Reason"
    ]
};

function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

const approach = getRandomElement(rolls.approach);
const intent = getRandomElement(rolls.intent);
const theme = getRandomElement(rolls.theme);

console.log(`${approach} ${intent} ${theme}`);
