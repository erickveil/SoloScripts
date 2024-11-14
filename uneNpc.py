#!/usr/bin/python3

import random

modifiers = [
    "superfluous", "addicted", "conformist", "nefarious", "sensible", 
    "untrained", "romantic", "unreasonable", "skilled", "neglectful", 
    "lively", "forthright", "idealistic", "unsupportive", "rational", 
    "coarse", "foolish", "cunning", "delightful", "miserly", 
    "inept", "banal", "logical", "subtle", "reputable", 
    "wicked", "lazy", "pessimistic", "solemn", "habitual", 
    "meek", "helpful", "unconcerned", "generous", "docile", 
    "cheery", "pragmatic", "serene", "thoughtful", "hopeless", 
    "pleasant", "insensitive", "titled", "inexperienced", "prying", 
    "oblivious", "refined", "indispensable", "scholarly", "conservative", 
    "uncouth", "willful", "indifferent", "fickle", "elderly", 
    "sinful", "naive", "privileged", "glum", "likable", 
    "lethargic", "defiant", "obnoxious", "insightful", "tactless", 
    "fanatic", "plebeian", "childish", "pious", "uneducated", 
    "inconsiderate", "cultured", "revolting", "curious", "touchy", 
    "needy", "dignified", "pushy", "kind", "corrupt", 
    "jovial", "shrewd", "liberal", "compliant", "destitute", 
    "conniving", "careful", "alluring", "defective", "optimistic", 
    "affluent", "despondent", "mindless", "passionate", "devoted", 
    "established", "unseemly", "dependable", "righteous", "confident"
]

nouns = [
    "gypsy", "witch", "merchant", "expert", "commoner", 
    "judge", "ranger", "occultist", "reverend", "thug", 
    "drifter", "journeyman", "statesman", "astrologer", "duelist", 
    "jack-of-all-trades", "aristocrat", "preacher", "artisan", "rogue", 
    "missionary", "outcast", "mercenary", "caretaker", "hermit", 
    "orator", "chieftain", "pioneer", "burglar", "vicar", 
    "officer", "explorer", "warden", "outlaw", "adept", 
    "bum", "sorcerer", "laborer", "master", "ascendant", 
    "villager", "magus", "conscript", "worker", "actor", 
    "herald", "highwayman", "fortune-hunter", "governor", "scrapper", 
    "monk", "homemaker", "recluse", "steward", "polymath", 
    "magician", "traveler", "vagrant", "apprentice", "politician", 
    "mediator", "crook", "civilian", "activist", "hero", 
    "champion", "cleric", "slave", "gunman", "clairvoyant", 
    "patriarch", "shopkeeper", "crone", "adventurer", "soldier", 
    "entertainer", "craftsman", "scientist", "ascetic", "superior", 
    "performer", "magister", "serf", "brute", "inquisitor", 
    "lord", "villain", "professor", "servant", "charmer", 
    "globetrotter", "sniper", "courtier", "priest", "tradesman", 
    "hitman", "wizard", "beggar", "warrior"
]

power_levels = {
    1: {"Much Weaker": range(1, 3), "Slightly Weaker": range(3, 11), "Comparable": range(11, 91), "Slightly Stronger": range(91, 99), "Much Stronger": range(99, 101)},
    2: {"Much Weaker": range(1, 5), "Slightly Weaker": range(5, 16), "Comparable": range(16, 86), "Slightly Stronger": range(86, 97), "Much Stronger": range(97, 101)},
    3: {"Much Weaker": range(1, 6), "Slightly Weaker": range(6, 21), "Comparable": range(21, 81), "Slightly Stronger": range(81, 96), "Much Stronger": range(96, 101)},
    4: {"Much Weaker": range(1, 9), "Slightly Weaker": range(9, 26), "Comparable": range(26, 76), "Slightly Stronger": range(76, 93), "Much Stronger": range(93, 101)},
    5: {"Much Weaker": range(1, 13), "Slightly Weaker": range(13, 31), "Comparable": range(31, 71), "Slightly Stronger": range(71, 89), "Much Stronger": range(89, 101)}
}

verbs = [
    "advise", "obtain", "attempt", "spoil", "oppress", 
    "interact", "create", "abduct", "promote", "conceive", 
    "blight", "progress", "distress", "possess", "record", 
    "embrace", "contact", "pursue", "associate", "prepare", 
    "shepherd", "abuse", "indulge", "chronicle", "fulfill", 
    "drive", "review", "aid", "follow", "advance", 
    "guard", "conquer", "hinder", "plunder", "construct", 
    "encourage", "agonize", "comprehend", "administer", "relate", 
    "take", "discover", "deter", "acquire", "damage", 
    "publicize", "burden", "advocate", "implement", "understand", 
    "collaborate", "strive", "complete", "compel", "join", 
    "assist", "defile", "produce", "institute", "account", 
    "work", "accompany", "offend", "guide", "learn", 
    "persecute", "communicate", "process", "report", "develop", 
    "offend", "suggest", "weaken", "achieve", "secure", 
    "inform", "patronize", "depress", "determine", "seek", 
    "manage", "suppress", "proclaim", "operate", "access", 
    "refine", "compose", "undermine", "explain", "discourage", 
    "attend", "detect", "execute", "maintain", "realize", 
    "convey", "rob", "establish", "support", "overthrow"
]

nouns_motivation = [
    "wealth", "hardship", "affluence", "resources", "prosperity", 
    "poverty", "opulence", "deprivation", "success", "distress", 
    "contraband", "music", "literature", "technology", "alcohol", 
    "medicines", "beauty", "strength", "intelligence", "force", 
    "the wealthy", "the populous", "enemies", "the public", "religion", 
    "the poor", "family", "the elite", "academia", "the forsaken", 
    "the law", "the government", "the oppressed", "friends", "criminals", 
    "allies", "secret societies", "the world", "military", "the church", 
    "dreams", "discretion", "love", "freedom", "faith", 
    "pain", "slavery", "enlightenment", "racism", "sensuality", 
    "dissonance", "peace", "discrimination", "disbelief", "pleasure", 
    "hate", "happiness", "servitude", "harmony", "justice", 
    "gluttony", "lust", "envy", "greed", "laziness", 
    "wrath", "pride", "purity", "moderation", "vigilance", 
    "zeal", "composure", "charity", "modesty", "atrocities", 
    "cowardice", "narcissism", "compassion", "valor", "patience", 
    "advice", "propaganda", "science", "knowledge", "communications", 
    "lies", "myths", "riddles", "stories", "legends", 
    "industry", "new religions", "progress", "animals", "ghosts", 
    "magic", "nature", "old religions", "expertise", "spirits"
]

random_modifier = random.choice(modifiers)
random_noun = random.choice(nouns)

r_level = random.randint(1, 5)
d100_roll = random.randint(1, 100)

for power_level, range_values in power_levels[r_level].items():
    if d100_roll in range_values:
        selected_power_level = power_level
        break

motivations = []
for _ in range(3):
    verb = random.choice(verbs)
    noun_motivation = random.choice(nouns_motivation)
    motivations.append(f"{verb} {noun_motivation}")

result = f"A {random_modifier} {random_noun}, {selected_power_level.lower()} than the party, " + ", ".join(motivations) + "."
print(result)
