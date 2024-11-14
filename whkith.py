#!/usr/bin/python3

import random

# Define trait data including descriptions and actions
traits = {
    "Artistic Traits": {
        "Crafty": {
            "description": "A crafty kith is very skilled at putting all the pieces together in an unconventional way. They are often tinkers, mongers, and magicians, among others.",
            "actions": ["Invent something totally new.", "Propose an alternate approach.", "Reveal that a plan they’ve had in motion has paid off."]
        },
        "Dramatic": {
            "description": "A dramatic kith loves to show off to impress and please others. They are often singers, harkers, and socialites, among others.",
            "actions": ["Put on a big show, with heightened emotions and histrionics.", "Distract someone with a talented display.", "Play up your emotions to absurd levels."]
        },
        "Imaginative": {
            "description": "An imaginative kith’s head is always up in the clouds. They are often artists, glaziers, and dreamers, among others.",
            "actions": ["Explain a way things could be better.", "Forget about something really important.", "Describe an everyday object in a way no one’s ever thought about it before."]
        },
        "Poetic": {
            "description": "A poetic kith has a deep love for wordplay and lyricism. They are often authors, rimesters, and astrologers, among others.",
            "actions": ["Wax metaphorical.", "Get caught up in the big picture.", "Give advice on what someone else should say."]
        },
        "Glamorous": {
            "description": "A glamorous kith has a beguiling and enchanting appearance that is both beautiful and impossible. They are often kaleidoscopic insects, flirtatious daemons, and especially skilled makeup artists, among others.",
            "actions": ["Dazzle and stun everyone who beholds you.", "Reveal the appearance you hide underneath.", "Tell someone to look at you. If they want to look away, they’re going to need to spend a token."]
        },
        "Miraculous": {
            "description": "A miraculous kith can do things no one else can do. They are often great and mighty gods, powerful wizards, and wish-granting fish, among others.",
            "actions": ["Make possible the impossible.", "Take someone’s hand and fly with them.", "Offer to grant someone’s wish, in a way that won’t work out how they want."]
        },
    },
    "Grounded Traits": {
        "Honest": {
            "description": "An honest kith always says what’s on their mind. They are often bayweavers, bookbinders, and clerks, among others.",
            "actions": ["Lay out the facts, as you see it.", "Point out the truth everyone else has been ignoring.", "Ask: 'Do you want my opinion?'"]
        },
        "Quiet": {
            "description": "A quiet kith doesn’t have much to say. They are often colporteurs, glassblowers, and wallflowers, among others.",
            "actions": ["Tap on someone’s shoulder.", "Stare at someone until they get the point.", "Non-verbally ask: 'Are you okay?'"]
        },
        "Watchful": {
            "description": "A watchful kith keeps a close eye on the world around them. They are often guards, astronomers, and scribes, among others.",
            "actions": ["Point out something people missed.", "Guard the exits.", "Ask: 'What’s that you’re hiding?'"]
        },
        "Wise": {
            "description": "A wise kith has learned a lot from listening and moving through the world. They are often monks, herbalists, and janitors, among others.",
            "actions": ["Reflect on what someone else has said.", "Propose a path quite unlike those that others have suggested.", "Ask: 'What are your feelings on the matter?'"]
        },
        "Intertwined": {
            "description": "An intertwined kith is rooted in the world around them and is just as much a part of the trees and the sky as they are themselves.",
            "actions": ["Show how two things are connected in an unexpected way.", "Take your time and move very carefully.", "Help someone ask the world around them for guidance."]
        },
        "Invisible": {
            "description": "An invisible kith cannot be seen. They are often ghostly spirits, terrified gods, and tiny scuttling creatures, among others.",
            "actions": ["Have been somewhere the whole time.", "Move right past people who should’ve spotted you.", "Vanish. If someone wants to find you again, they’re going to need to spend a token."]
        },
    },
    "Intellectual Traits": {
        "Ambitious": {
            "description": "An ambitious kith has goals and aspirations beyond where they are in life. They are often scribblers, scullions, and apprentices, among others.",
            "actions": ["Take a calculated risk.", "Explain how you’re the only person who can handle this.", "Ask: 'How would you make things better?'"]
        },
        "Cunning": {
            "description": "A cunning kith is skilled at turning events and situations in their favor. They are often guttersnipes, wainwrights, and con artists, among others.",
            "actions": ["Get somewhere you’re not supposed to be.", "Tell a compelling lie.", "Ask: 'What’s your real goal here?'"]
        },
        "Inquisitive": {
            "description": "An inquisitive kith grabs hold of all the information that they can. They are often journalists, alchemists, and enumerators, among others.",
            "actions": ["Focus on an irrelevant detail.", "Hold something up to the light.", "Ask: 'What’s this?'"]
        },
        "Learned": {
            "description": "A learned kith has spent plenty of time with texts and traditional learning. They are often professors, librarians, and apothecaries, among others.",
            "actions": ["Reference a text no one else here has read.", "Know something useful that applies to the situation.", "Ask: 'Do you want my advice?'"]
        },
        "Oracular": {
            "description": "An oracular kith can see the future, for better or for worse. They are often venerated sages, enigmatic gods, and stargazers, among others.",
            "actions": ["Make a vague and unclear reference to something that hasn’t happened yet.", "Say: 'I told you so.'", "Tell someone the bad news about what their future holds."]
        },
        "Witchy": {
            "description": "A witchy kith is skilled at quiet and tricksy magics. They are often healers, court magicians, and kind old ladies that live in the swamp, among others.",
            "actions": ["Cackle.", "Mix assorted components to create something new.", "Point out a personality flaw someone hasn’t been dealing with."]
        },
    },
    "Personal Traits": {
        "Cheerful": {
            "description": "A cheerful kith is happy and positive. They are often bakers, friars, and cooks, among others.",
            "actions": ["Look on the bright side.", "Whistle a chipper tune.", "Gallivant into an awkward situation."]
        },
        "Confident": {
            "description": "A confident kith knows exactly who they are and who they want to be. They are often blacksmiths, plumbers, and drovers, among others.",
            "actions": ["Jump headfirst into action.", "Charge into a situation without understanding the risks.", "Say: 'I’ve got it covered.'"]
        },
        "Pensive": {
            "description": "A pensive kith has a lot of heavy things on their mind. They are often printers, vintners, and bellringers, among others.",
            "actions": ["Rain on someone’s parade.", "Stare off into the distance mournfully.", "Ask: 'What else can we do?'"]
        },
        "Relaxed": {
            "description": "A relaxed kith is perpetually calm. They are often fishers, brewsters, and dilly-dalliers, among others.",
            "actions": ["Go with the flow.", "Remind everyone to take a step back.", "Ask: 'Do you wanna talk about it?'"]
        },
        "Luminescent": {
            "description": "A luminescent kith is full of light that casts a glow across the world. They are often motes of light, fallen stars, and fireflies, among others.",
            "actions": ["Shed light on the shadows of the world.", "Lead the way.", "Non-verbally ask: 'What is true about you that you keep from everyone?'"]
        },
        "Venerable": {
            "description": "A venerable kith is as old as the hills and the earth. They are often mountain gods, isopods from an ancient time, and beings deep in the old dark, among others.",
            "actions": ["Offer something that hasn’t been seen in a very long time.", "Show what things were like in more grim times.", "Tell someone how they will repeat the mistakes of the past."]
        },
    },
    "Physical Traits": {
        "Adventurous": {
            "description": "An adventurous kith always wants to be getting tangled up in something new. They are often aeronauts, sailors, and itinerants, among others.",
            "actions": ["Declare where you’re going next.", "Charge headfirst into trouble.", "Have circumstances improbably work out for you."]
        },
        "Passionate": {
            "description": "A passionate kith is full of intense and explosive emotions. They are often mail-carriers, writers, and flâuners, among others.",
            "actions": ["Explain why this matters to you.", "Say exactly what’s on your mind right now.", "Lose your temper and damage something important."]
        },
        "Resolute": {
            "description": "A resolute kith cannot be swayed from their current path, no matter what. They are often architects, caulkers, and arkwrights, among others.",
            "actions": ["Keep at something that others would give up at.", "Reject what’s right in front of your eyes.", "Refuse to yield under pressure."]
        },
        "Sturdy": {
            "description": "A sturdy kith can be depended on when times are tough. They are often carpenters, spinsters, and dockhands, among others.",
            "actions": ["Support something in danger of collapse.", "Push something concerning aside.", "Exert yourself to protect someone else."]
        },
        "Feral": {
            "description": "A feral kith rejects traditional society and embraces monstrosity. They are often fearsome insects, hungry gods, and kids raised by the wilderness itself.",
            "actions": ["Call out to the wild, and hear it respond.", "Ask: 'What’s stopping you?'", "Show all your teeth and bite."]
        },
        "Mighty": {
            "description": "A mighty kith has a strength that is beyond normal capacity. They are often great warriors, herculean gods, and beasts of forgotten legend.",
            "actions": ["Take on a heavy burden.", "Move the unmovable.", "Anchor something in the ground."]
        },
    },
    "Social Traits": {
        "Caring": {
            "description": "A caring kith is willing to die to keep someone else safe. They are often doctors, farmers, and coroners, among others.",
            "actions": ["Protect someone else from the world.", "Inconvenience yourself to help someone else.", "Ask: 'What do you need right now?'"]
        },
        "Friendly": {
            "description": "A friendly kith gets along well with folk from all over. They are often innkeeps, barbers, and bards, among others.",
            "actions": ["Start up a conversation with someone else.", "Introduce someone to an old friend of yours.", "Get really attached to an inanimate object."]
        },
        "Proper": {
            "description": "A proper kith sticks with formality and tradition. They are often butlers, grocers, and chamberlains, among others.",
            "actions": ["Explain how things have been handled in the past.", "Judge something for its inappropriateness.", "Struggle to get something new."]
        },
        "Raucous": {
            "description": "A raucous kith is always looking for a good time. They are often revelers, jesters, and roustabouts, among others.",
            "actions": ["Find the fun in a dull task.", "Get lost in the excitement.", "Know exactly where a better party is."]
        },
        "Empathetic": {
            "description": "An empathetic kith can connect with and understand things no one else can. They are often gentle teachers, affectionate spirits, and anyone with a knack for empathy.",
            "actions": ["Communicate with something that can’t normally talk.", "Express a concept in a way everyone understands.", "Non-verbally ask: 'What are you feeling?'"]
        },
        "Many-Faced": {
            "description": "A many-faced kith is a shapeshifter, who can adopt other forms. They are often trickster gods, sneaky thieves with a little bit of magic, and skilled mimics, among others.",
            "actions": ["Change dramatically, and become something new.", "Reveal another kith to have been them this whole time.", "Look exactly like another character."]
        },
    },
    "Traumatized Traits": {
        "Cautious": {
            "description": "A cautious kith spent the last of their trust a long time ago. They are often exhausted widows, cold-hearted farmers, and those who have seen firsthand the harshness of the world.",
            "actions": ["Point out a danger, real or imagined.", "Refuse to open up to someone else.", "Step out of your comfort zone, even slightly."]
        },
        "Empty": {
            "description": "An empty kith feels like there’s just not much left to them anymore. They are often war-blasted survivors, haunted veterans, and those hollowed out by pain, among others.",
            "actions": ["Sigh and gaze blankly.", "Ask: 'Does it matter?'", "Display an emotion you thought you couldn’t anymore."]
        },
        "Frantic": {
            "description": "A frantic kith is struggling to get everything done. They are often overburdened caretakers, manic intellectuals, and those desperate to please.",
            "actions": ["Agree to something dangerous or risky.", "Try to say too many things all at once.", "Push against your instincts and take a break."]
        },
        "Furious": {
            "description": "A furious kith cannot hold back their rage. They are often vengeful mothers, soldiers with fuming eyes, and those forged into a weapon by the pain in their heart.",
            "actions": ["Lash out without meaning to.", "Bottle everything up and seethe.", "Express your rage in a constructive manner."]
        },
        "Grieving": {
            "description": "A grieving kith freshly mourns the loss of their love. They are often heartbroken parents, terrified exiles, and those promised greatness, among others.",
            "actions": ["Overflow with emotion.", "Hold tight to comfort and refuse to let go.", "Ask: 'Are you in a place to listen right now?'"]
        },
        "Hurt": {
            "description": "A hurt kith nurses wounds that will never fully heal. They are often old heroes, aching patients, and those marked by pain, among others.",
            "actions": ["Flinch at someone else’s actions.", "Re-open an old wound.", "Articulate a step on the path towards healing."]
        },
        "Lost": {
            "description": "A lost kith has forgotten how to get back home. They are often lonely travelers, confused prophets, and those disassociated from this world, among others.",
            "actions": ["Wander deep into the darkness.", "Express the disconnect between yourself and the world around you.", "Seek out the help of someone else to anchor you."]
        },
        "Nervous": {
            "description": "A nervous kith is very stressed out. They are often freaked-out kids, princes out of their depth, and those overwhelmed by the many dangers of the world.",
            "actions": ["Worry about something you don’t have control over.", "Say: 'I’m sorry.'", "Ask: 'Is everything okay?'"]
        },
        "Starving": {
            "description": "A starving kith has been denied their hunger for too long, and it’s burning them up inside. They are often hungry ghouls, spiteful wardens, and shadows of monstrous gods.",
            "actions": ["Gnaw on what’s left.", "Blame the wrong person for your hunger.", "Name a person, place, object, or secret."]
        },
        "Heroic": {
            "description": "A heroic kith believes they are the savior of the world. What a cruel fate indeed. They are often dragon-slayers, leaders of the rebellion, and those arrogant enough to seek out power.",
            "actions": ["Know what’s best for everyone else.", "Present a perfect persona to the world.", "Declare someone fundamentally good or irredeemably evil."]
        },
        "Royal": {
            "description": "A royal kith rules over this land with authority and lonely gravitas. They are often arrogant kings, towering giants, or those destined to be undone by their own glory.",
            "actions": ["Engage in a petty and useless display of power.", "Inflict your will on the world around you.", "Make a sweeping proclamation."]
        },
        "Dead": {
            "description": "A dead kith was once alive, but isn’t anymore. They are often spectral lights, wandering souls, and the last remnants of a forgotten time, among others.",
            "actions": ["Provide a bridge from one life to the other.", "Send a chill down someone’s spine.", "Show someone something they truly don’t want to grapple with."]
        },
    }
}

# Determine the number of traits
def determine_trait_count():
    return random.choices([2, 3, 4], weights=[70, 25, 5], k=1)[0]

# Select random traits
def select_traits(trait_count):
    selected_traits = []
    while len(selected_traits) < trait_count:
        category = random.choice(list(traits.keys()))
        sub_trait = random.choice(list(traits[category].keys()))
        if (category, sub_trait) not in selected_traits:
            selected_traits.append((category, sub_trait))
    return selected_traits

# Create a Kith with traits
def create_kith():
    trait_count = determine_trait_count()
    kith_traits = select_traits(trait_count)
    print("Traits:\n")
    for category, sub_trait in kith_traits:
        trait_data = traits[category][sub_trait]
        description = trait_data["description"]
        actions = random.sample(trait_data["actions"], k=2)
        
        print(f"{category}: {sub_trait}")
        print(description)
        print("\nThis kith can always...\n")
        for action in actions:
            print(f"- {action}")
        print("\n")

# Generate a Kith
create_kith()
