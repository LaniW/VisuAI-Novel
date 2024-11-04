# Ren'Py script for "The Last Briefing" scene with a starting label

# Character Definitions
define e = Character("Dr. Elara Vaestrom", color="#88CFF1")
define j = Character("Captain Jarek Duval", color="#FFA07A")
define a = Character("Dr. Amara Li", color="#98FB98")
define v = Character("Tech Specialist Voss", color="#DAA520")
define z = Character("Zara Trent", color="#FFC0CB")

# Initialize `message_choice` variable to avoid errors later
default message_choice = ""
default jarek_support = ""
default amara_support = ""
default zara_confronted = ""
default approach_choice = ""
default diplomacy_mutiny = ""
default authority_mutiny = ""
default kept_secret = ""
default betray_helion = ""

# Start label to initiate the game
label start:
    # Go to the last briefing scene at the start of the game
    jump last_briefing

# Scene: The Last Briefing
label last_briefing:
    scene bg briefing_room with fade
    
    show e upset
    e "Alright, team. This is it. We've got one shot to track down that alien signal."
    show e neutral
    e "Helion Dynamics thinks it might hold the key to our survival."
    hide e
    
    show j neutral
    j "Survival. Isn’t that what they said back when the first reactors blew?"
    show j neutral
    j "What’s this signal supposed to do anyway? Disintegrate us faster?"
    hide j
    
    show a neutral
    a "Or it could help us find something we lost long ago, Jarek. Hope. A cure. There’s always a chance."
    hide a
    
    show v neutral
    v "Did you get any data regarding the signal’s origin? If it’s been out there long enough, we could face… unexpected challenges."
    hide v
    
    show z neutral
    z "Helion believes the signal is emitted from a point in the Nebula X-23. It’s risky, but the rewards outweigh the dangers."
    show z neutral
    z "Your mission is to collect samples and data at all costs."
    hide z
    
    # Elara notices the encrypted message
    show e upset
    e "(noticing something odd) Uh, Zara, what’s this?"
    hide e
    
    show z neutral
    z "(deflecting) Just standard updates. The mission parameters are of utmost importance. Focus on the signal."
    hide z
    
    show j neutral
    j "(noticing Elara's distraction) What’s on your mind, Doc?"
    hide j

    show e upset
    e "What if there’s something we’re missing? Something that could... change how we approach this mission?"
    hide e
    
    show a neutral
    a "You’ve always said to trust instinct. What’s your instinct telling you now?"
    hide a
    
    show v neutral
    v "Whatever that message is, it could reveal important information. Or it could be a distraction."
    hide v
    
    show z neutral
    z "(interrupting) Enough speculation. The mission is the priority. We must depart within the hour."
    hide z
    
    show e neutral
    e "Alright, everyone. It’s time to gear up for launch. Just… keep your eyes open. That signal won’t decipher itself."
    hide e
    
    # Choice: Ignore or Decrypt the Message
    menu:
        "Ignore the encrypted message and trust the crew.":
            $ message_choice = "ignore"
            show e neutral
            e "(to herself) Let’s focus on the mission. We need to work together."
            show e neutral
            e "Just some standard security protocols. Nothing we can’t handle. We trust each other, right?"
            show e neutral
            e "We’ve got to work as a team."
            hide e
            
            jump departure
    
        "Decrypt the message to discover more about possible betrayals.":
            $ message_choice = "decrypt"
            show e neutral
            e "(after a pause, reaching out to the encrypted message)"
            show e neutral
            e "Alright… Let's decrypt it. We face the truth together, come what may."
            hide e
            
            # Transition to decrypted message reveal
            scene decrypted_message with dissolve
            e "It... it contains warnings. Potential betrayals, even from our own team."
            e "(to herself) This changes things. I need to keep an eye on Zara."
            
            jump departure

# Continuation of "The Last Briefing" scene
# Scene: Act 1, Scene 1 - Departure

label departure:
    # Scene setup for the hangar bay
    scene bg hangar_bay with fade
    
    # Description for the atmosphere in the hangar
    narrator "The hangar is filled with the low hum of machinery. Various crew members move about, preparing a sleek spacecraft for launch."
    "Dr. Elara Vaestrom stands at the entrance, taking a deep breath. The atmosphere is tense but filled with an undercurrent of excitement."
    
    show e upset
    e "Alright, everyone! This is it. We leave behind everything we know for a chance at survival. Let’s make it count."
    hide e
    
    # Jarek approaches with a smirk
    show j neutral
    j "You sure you're ready for this, Doc? Space isn’t exactly a walk in the park."
    hide j
    
    if message_choice == "decrypt":
        show e neutral
        e "(hesitant, suspicious) Are you with me, Jarek? No matter what happens out there?"
        hide e
        show j upset
        j "(raising an eyebrow) Of course, Elara. I wouldn’t dream of letting you down."
        hide j
    
    else:
        show e neutral
        e "(raising an eyebrow) I’ve never been more ready, Jarek. We need to focus on the mission."
        hide e
    
    # Amara joins the conversation, serious yet hopeful
    show a neutral
    a "This could be our chance to discover something groundbreaking. Let’s just remember to stick together out there."
    hide a
    
    # Voss calibrates equipment nearby, occasionally glancing at the crew
    show v neutral
    v "And let’s not forget to double-check our systems. We can’t afford any slip-ups. Not now."
    hide v
    
    # Zara enters the hangar with a commanding demeanor
    show z neutral
    z "You’re all aware of the stakes. Helion Dynamics is counting on us to collect data from the alien signal. We mustn’t deviate from our objectives."
    hide z
    
    "Elara exchanges a wary look with her crew, sensing the underlying tension."
    
    show e neutral
    e "Understood. But before we launch, I want to talk to each of you. We need to be prepared for anything."
    hide e
    
    # Choice to converse with different crew members
    menu:
        "Converse with Jarek":
            jump jarek_conversation

        "Spend time with Amara":
            jump amara_conversation

        "Question Zara":
            jump zara_conversation

# Conversation with Jarek
label jarek_conversation:
    "Elara steps closer to Jarek, who is smirking, trying to lighten the mood despite the high stakes of the mission."
    
    if message_choice == "decrypt":
        show e neutral
        e "(nervously) Jarek… if anything goes wrong out there, you’ll back me up, right?"
        hide e
        show j upset
        j "(seriously) Always, Elara. If you have doubts, just say the word."
        hide j
        show e neutral
        e "(relieved but cautious) Thanks. I know I can trust you."
        hide e
    
    else:
        show j neutral
        j "What’s on your mind, Elara? You’re not having second thoughts, are you?"
        hide j
        show e upset
        e "(hesitating) No, just thinking about our past missions. We’ve had our share of close calls. I need to know you’re with me on this."
        hide e
        show j neutral
        j "(sincerely) Always. Just don’t forget to keep your head in the game."
        hide j
    
    show e neutral
    e "(nodding) Thanks, Jarek. I’ll do my best."
    hide e
    $ jarek_support = "yes"
    $ amara_support = "no"
    
    jump crew_gathering

# Conversation with Amara
label amara_conversation:
    "Elara turns to Amara, who is examining a sample container thoughtfully."
    
    if message_choice == "decrypt":
        show e neutral
        e "(carefully) Amara, how do you feel about the rest of the team? Can we really rely on everyone?"
        hide e
        show a neutral
        a "(surprised but calm) Elara, we’ve been through a lot together. I believe in our team. We have to work together if we want to survive."
        hide a
        show e neutral
        e "(softly) You’re right. Trust is key. Let’s stay vigilant, though."
        hide e
    
    else:
        show a neutral
        a "This is an incredible opportunity. If we find what we’re looking for, it could change everything."
        hide a
        show e neutral
        e "(curious) What are your thoughts on alien biology? Do you think we’re ready for whatever we might encounter?"
        hide e
        show a neutral
        a "(determined) We’ll adapt. We always do. Let’s just remember to keep an open mind."
        hide a
    
    show e neutral
    e "Agreed. Let’s make sure we’re prepared for anything."
    hide e
    $ amara_support = "yes"
    $ jarek_support = "no"
    
    jump crew_gathering

# Conversation with Zara
label zara_conversation:
    "Elara approaches Zara, who is reviewing mission data on her tablet with a focused expression."
    
    if message_choice == "decrypt":
        show e upset
        e "(coldly) Zara, I came across a message. It mentioned… potential betrayals. Care to comment?"
        hide e
        show z neutral
        z "(with a faint smile) Betrayals? You should focus on the mission, Elara, not on distractions. Paranoia won’t get us far."
        hide z
        show e neutral
        e "(suspiciously) Maybe. But I’ll be watching, just in case."
        hide e
    
    else:
        show e neutral
        e "Zara, can we discuss Helion’s expectations? I want to ensure we’re not missing any critical information."
        hide e
        show z neutral
        z "(coldly) Our objective is straightforward. Collect data and samples. Anything beyond that is not your concern."
        hide z
        show e neutral
        e "(narrowing her eyes) But what if there’s more at stake? We need to be prepared for hidden agendas."
        hide e
        show z neutral
        z "(dismissively) Focus on the mission, Elara. That’s all that matters."
        hide z

    "Elara feels a sense of unease but decides to let it go for now."

    jump crew_gathering

# After conversations, the crew gathers for departure
label crew_gathering:
    "As the conversations conclude, Elara gathers her crew. Their expressions are a mix of determination and anxiety."

    if message_choice == "decrypt":
        show e neutral
        e "(to herself) I know what that message warned about... But who among us can I truly trust?"
        hide e
        show e upset
        e "(addressing the team) Alright, everyone. Before we head out, I just want to say... stay sharp. And watch each other's backs."
        hide e
        
        # Jarek responds with reassurance, sensing Elara’s underlying concern
        show j neutral
        j "We’re a team, Elara. If anyone tries anything, they'll have to get through me first."
        hide j
        
        # Amara, sensing the tension, chimes in thoughtfully
        show a neutral
        a "We’ve come this far together. Let’s focus on the mission and not let doubt tear us apart."
        hide a

        # Zara’s reaction remains neutral, yet controlled
        show z neutral
        z "(coolly) Helion is counting on us. Let’s not waste time with unnecessary worries."
        hide z

    else:
        show e neutral
        e "(inspiring) Alright, team. Let’s gear up and head out. Remember, trust each other, and stay alert. We’re facing the unknown together."
        hide e

        # Jarek’s light-hearted response
        show j neutral
        j "Nothing we can’t handle. Let’s get this done and head back in one piece."
        hide j

        # Amara’s optimistic response
        show a upset
        a "The possibilities are endless. Just imagine what we might find out there."
        hide a

        # Zara’s formal response
        show z neutral
        z "Our objective is clear. Let’s not deviate from it."
        hide z

    "The crew nods, a shared resolve forming among them. They move toward the ship, ready to embark on their journey into the abyss."

    # Transition to the next scene
    scene bg spaceship_departure with dissolve
    narrator "The engines hum as the crew boards the sleek, advanced spacecraft. The hangar bay doors open, revealing the stars outside."
    narrator "As the ship lifts off, the vast expanse of space stretches before them, both beautiful and terrifying."

    "Elara sits in the captain’s seat, her mind racing with thoughts about the decrypted message and the possible betrayals it hinted at. She glances at her team, wondering who—if anyone—might betray her trust."

    jump first_contact

# Scene: Act 1, Scene 2 - First Contact
label first_contact:
    scene spaceship_departure with fade

    # Opening narration for the new scene
    narrator "The crew has embarked on their journey, heading towards Nebula X-23. As the ship approaches the edge of the nebula, the atmosphere inside the cockpit is tense, each crew member preparing for the unknown."

    scene bg cockpit_view with dissolve

    # Description of the cockpit with the crew
    "The cockpit is filled with the soft glow of various control panels and the swirling, ominous hues of Nebula X-23 visible through the viewport."
    "Dr. Elara Vaestrom sits in the pilot’s seat, monitoring the signal’s coordinates. Captain Jarek Duval stands nearby, a cautious but eager look on his face."
    "The rest of the team is strapped in behind them, their expressions a mix of anticipation and unease."

    show e neutral
    e "Alright, everyone. We’re approaching the source of the signal. Remember, we need to proceed carefully."
    hide e
    
    show j neutral
    j "(glancing at the readouts skeptically) Carefully? You know these signals can be pretty volatile, right? We push through, we might catch them off guard."
    hide j

    show v upset
    v "(monitoring the systems) But if we push too hard, we risk triggering a defensive response. We don’t know what we’re dealing with here."
    hide v

    show a neutral
    a "(watching the swirling nebula) A cautious approach might allow us to gather more data without alarming whatever is out there."
    hide a

    show z upset
    z "(leaning forward with a cold tone) We’re on a deadline. Helion expects results. We can’t afford to waste time being cautious."
    hide z

    # Choice: Cautious or Aggressive Approach
    menu:
        "Order a cautious approach":
            $ approach_choice = "cautious"
            show e neutral
            e "(decisively) I’m ordering a cautious approach. We can’t risk escalating the situation. Let’s monitor the signals and gather as much data as we can before making any moves."
            hide e
            
            # Crew reactions to cautious approach
            "The crew exchanges glances, some relieved, others apprehensive."
            
            show j neutral
            j "(sighing) Fine. But if we end up sitting here doing nothing, it’s on you, Doc."
            hide j
            
            show v neutral
            v "(nodding) I’ll run a full scan of the area. Let’s see if we can pinpoint the source of that signal without drawing attention."
            hide v

            # Transition to the next scene within the cautious approach
            jump cautious_approach

        "Push forward aggressively":
            $ approach_choice = "aggressive"
            show e neutral
            e "(resolutely) No, we’re pushing forward. We need to make contact now. Jarek, increase speed."
            hide e

            # Crew reactions to aggressive approach
            "Jarek nods, a glint of excitement in his eyes as he accelerates the ship."
            
            show j upset
            j "(grinning) You got it! Let’s show them we mean business."
            hide j
            
            show v upset
            v "(warningly) Careful, Elara! We’re entering uncharted territory. We could trigger a defensive response."
            hide v
            
            show a upset
            a "(anxiously) This could get dangerous! We should be cautious!"
            hide a
            
            # Transition to the next scene within the aggressive approach
            jump aggressive_approach

# Cautious Approach Path
label cautious_approach:
    # Scene setup for cautious approach within the nebula
    scene bg nebula_approach with dissolve
    narrator "The view outside the ship shifts as they glide deeper into the nebula, taking slow, calculated moves to avoid alarming any potential threats."

    # Crew detects the signal
    show a neutral
    a "(pointing at the screen) There! The signal’s stronger now. If we can triangulate its position…"
    hide a
    
    # Sudden interference interrupts their scans
    "Suddenly, the ship shakes violently, and alarms begin to blare."
    
    show v neutral
    v "(frantically) We’re getting interference! They know we’re here!"
    hide v

    show e neutral
    e "(shouting over the alarms) Hold steady! We’re not done yet!"
    hide e

    "The crew scrambles to stabilize the ship, working in unison to manage the interference and keep the ship under control. Their cautious approach has bought them some time to react to the disturbance without triggering an immediate threat."

    # Next steps based on the cautious approach
    narrator "With a coordinated effort, the crew manages to stabilize the ship. They exchange glances, realizing they may have only moments to decide on their next course of action."

    # Transition to next possible choices in Act 1, Scene 3 or other events
    jump next_scene

# Aggressive Approach Path
label aggressive_approach:
    # Scene setup for aggressive approach within the nebula
    scene bg nebula_rush with dissolve
    narrator "The ship barrels forward, cutting through the nebula with newfound speed as the crew’s expressions shift from tension to exhilaration."

    # Crew detects the signal but faces backlash
    show v neutral
    v "(concerned, watching the readings) Elara, we’re approaching uncharted territory. This could trigger a defensive response!"
    hide v
    
    show a upset
    a "(gripping her seat, eyes wide) This could get dangerous! We should have been cautious!"
    hide a

    show e neutral
    e "(determined) We need to take risks if we want to find answers. Let’s make history!"
    hide e

    # Unexpected energy pulse shakes the ship
    "Suddenly, a massive energy pulse erupts from within the nebula, shaking the ship violently. The alarms blare louder as the crew is thrown against their restraints."

    show z neutral
    z "(shouting over the noise) What did I tell you? We’re in over our heads!"
    hide z

    # Crew attempts to stabilize the ship amidst the chaos
    "Elara fights to regain control as the crew scrambles to manage the unexpected energy wave surging through the ship’s systems."

    # Next steps based on the aggressive approach
    narrator "The crew braces for impact as the ship veers through the nebula’s volatile currents. Their aggressive approach has brought them closer to the signal, but at a perilous cost."

    # Transition to next possible choices in Act 1, Scene 3 or other events
    jump next_scene

# Placeholder label for the next part of the story
label next_scene:
    if approach_choice == "cautious":
        jump secrets_unveiled
    else:
        jump mutiny

# Scene: Act 2, Scene 3 - Secrets Unveiled
label secrets_unveiled:
    scene bg common_area_dim with fade
    
    # Description for setting the mood in the common area
    narrator "The common area is dimly lit, the glow from holographic displays casting eerie shadows across the room."
    "The crew—Dr. Elara Vaestrom, Captain Jarek Duval, Dr. Amara Li, Tech Specialist Voss, and Helion Representative Zara Trent—are gathered, the tension palpable."
    
    # Elara addresses the crew about Helion’s motives
    show e neutral
    e "(determined) We need to discuss what we’ve discovered. There’s something unsettling about Helion’s true motives for sending us here."
    hide e
    
    # Zara’s guarded response
    show z neutral
    z "(dismissively) What’s done is done, Elara. We’re on a mission, and we need to focus on the objectives at hand."
    hide z

    # Jarek challenges Zara
    show j neutral
    j "(challenging) But what if the objectives are just a cover? We deserve to know what Helion is really after."
    hide j
    
    # Elara agrees with Jarek, emphasizing safety concerns
    show e neutral
    e "Exactly. If there’s hidden information, it could compromise our safety and the mission itself."
    hide e
    
    # Amara glances at Zara with concern
    show a neutral
    a "(supportively) Zara, you’ve been with Helion longer than any of us. What do you know about their covert missions?"
    hide a
    
    # Conditional: Additional dialogue if Elara questioned Zara in The Last Briefing
    if message_choice == "decrypt":
        show z neutral
        z "(sighing, reluctantly) Helion has been involved in operations that extend beyond what you can imagine. They’re not just looking for technology; they want control over it."
        hide z
        
        # Voss’s anxious reaction to Zara’s revelation
        show v upset
        v "(anxiously) Control how? Are we just pawns in their game?"
        hide v
        
        "Zara looks uneasy but stands her ground."
        show z neutral
        z "(defensively) You have to understand, the stakes are incredibly high. Helion’s interests in alien technology are about power and survival."
        hide z
    
    # The crew’s reaction to Zara’s response varies based on the First Contact approach
    if approach_choice == "cautious":
        "The atmosphere is tense, but Elara senses that the crew is still managing to keep their emotions in check."
    else:
        "The crew’s aggression is heightened, with Jarek visibly clenching his fists and Amara watching Zara with mistrust."
    
    # Jarek’s frustration
    show j neutral
    j "(accusingly) So we’re just supposed to follow orders blindly? This isn’t right!"
    hide j
    
    # Elara takes a deep breath to maintain control of the escalating tension
    show e neutral
    e "(calming) We need to decide how to handle this information. Confronting Zara could lead to a division among us."
    hide e
    
    # Choice: Confront Zara or Keep Knowledge Secret
    menu:
        "Confront Zara about Helion’s secrets":
            jump confront_zara

        "Keep the knowledge secret":
            jump keep_secret

# Choice Path 1: Confront Zara
label confront_zara:
    show e neutral
    e "(firmly) Zara, we can’t ignore this. You need to come clean about Helion’s true intentions. Are we just expendable assets?"
    hide e
    
    "Zara’s composure falters, revealing her inner conflict."
    
    show z neutral
    z "(defensively) You don’t understand the bigger picture! This isn’t just about us; it’s about humanity’s future!"
    hide z
    
    show j neutral
    j "(sarcastically) Right. And your loyalty to Helion means more than our lives?"
    hide j
    
    "Elara steps closer to Zara, her voice lowering, her gaze intense."
    
    show e neutral
    e "(intensely) I trusted you, Zara. If you’re not with us, you’re against us."
    hide e
    
    "Zara’s eyes flash with anger, and the tension in the room escalates into a confrontation."
    $ zara_confronted = "yes"
    $ kept_secret = "no"
    
    # Escalated aggression based on First Contact approach
    if approach_choice == "aggressive":
        narrator "The crew’s aggression flares, with voices raised and accusations flying. Elara can feel the group teetering on the edge of mutiny."
        jump mutiny  # Placeholder for mutiny scene
    else:
        narrator "Though tense, the crew manages to restrain themselves. Zara’s silence speaks volumes, and Elara knows this conflict is far from over."
        jump mutiny

# Choice Path 2: Keep the Knowledge Secret
label keep_secret:
    show e neutral
    e "(cautiously) Maybe we should hold off on confronting Zara for now. Let’s keep this information under wraps and focus on our mission."
    hide e
    
    # The crew’s response to keeping the knowledge secret
    "The crew looks uncertain but slowly nods, the tension easing slightly."
    
    show a neutral
    a "(relieved) That might be wise. We can’t afford to fracture the team at this stage."
    hide a
    
    # Zara’s subtle relief
    show z neutral
    z "(gratefully) Thank you, Elara. We need to be united. Our lives depend on it."
    hide z
    
    # Voss remains skeptical, however
    show v neutral
    v "(tentatively) But we can’t ignore potential threats. If Helion is hiding something, we need to be prepared."
    hide v
    
    # Elara’s response to keep the team focused
    show e neutral
    e "(resolutely) We will stay vigilant. But for now, let’s focus on the mission. We need each other more than ever."
    hide e
    
    narrator "The crew returns to the holographic displays, but the atmosphere remains charged with unresolved tension and the weight of secrets."
    $ zara_confronted = "no"
    $ kept_secret = "yes"
    jump scene_abys_awakens

label mutiny:
    # Scene setup
    scene bg common_area_day
    with dissolve

    # Initial dialogue
    "The atmosphere is thick with tension as the crew of the spaceship gathers in the common area. Holographic displays flicker with data, but the crew's focus is on each other rather than their mission."
    
    "Dr. Elara Vaestrom stands at the forefront, flanked by Helion Representative Zara Trent, who appears guarded. The rest of the crew—Captain Jarek Duval, Dr. Amara Li, and Tech Specialist Voss—are visibly agitated."

    if message_choice == "decrypt": # Check if the message was decrypted in "The Last Briefing"
        "Tension is heightened by the recent revelations. The crew’s aggression is palpable."
    else:
        "Tension lingers in the air as unspoken words hang heavily between them."

    show e neutral
    e "We need to address what’s happening here. We’re a team, and I refuse to let Helion’s agenda tear us apart."
    hide e

    show z neutral
    z "What’s done is done, Elara. We’re on a mission, and we need to focus on the objectives at hand."
    hide z

    show a neutral
    a "But we can’t ignore the fact that we might be expendable to them. If we don’t act now, we could lose everything."
    hide a

    show v neutral
    v "Consequences? We’re already facing them! We’re risking our lives while Helion sits back and watches!"
    hide v

    "The crew's emotions boil over, and Jarek looks conflicted, glancing between Elara and the dissenting crew."

    if jarek_support == "yes":
        show j neutral
        j "Elara’s right. We need to stick together. If we don’t, we’re playing directly into Helion’s hands."
        hide j
    else:
        # Jarek remains silent
        show j neutral
        j "..."
        hide j

    show z neutral
    z "I won’t let you jeopardize this mission over your paranoia. You think you can just turn against your own?"
    hide z

    "The crew begins to turn on each other, voices rising."

    if zara_confronted == "yes":
        show z neutral
        z "This is exactly what Helion feared—a fractured crew. If you want a mutiny, fine. Just know the consequences."
        hide z

    show e neutral
    e "Everyone, please! We’re all in this together. Fighting amongst ourselves won’t solve anything. We need a plan, not a divide."
    hide e

    # Choices for the player
    menu:
        "Use diplomacy to calm tensions":
            show e neutral
            e "Let’s focus on what we can do together. We can’t let Helion win by turning against each other."
            hide e
            
            "The crew hesitates, their anger faltering as they listen to Elara."
            if jarek_support == "yes":
                show j neutral
                j "Elara’s right. We need to unite for our mission."
                hide j
            
            show a neutral
            a "We can find a way to navigate this. We’ve overcome challenges before. Let’s unite our strengths."
            hide a

            "Gradually, the crew’s tension eases as they remember their shared purpose. Zara, though still wary, seems to relent slightly."
            show z neutral
            z "Fine. But we need to operate with caution. No more reckless decisions."
            hide z
            
            "The crew exchanges glances, a renewed sense of unity forming."
            $ authority_mutiny = "no"
            $ diplomacy_mutiny = "yes"
            $ betray_helion = "no"

        "Exercise authority to quash the mutiny":
            show e neutral
            e "I am the leader here, and I won’t tolerate this insubordination. We have a mission, and I expect everyone to follow orders!"
            hide e
            
            "The crew stares at her, shock and anger flashing across their faces."
            if not jarek_support == "yes":
                show j neutral
                j "Elara, this isn’t how you lead. We need to be a team, not a dictatorship!"
                hide j

            show v upset
            v "So we’re just supposed to bow down while Helion pulls the strings? That’s not teamwork!"
            hide v

            "Elara’s authority creates rifts among the crew, and the tension escalates."
            show z neutral
            z "You’ve just sealed your fate, Elara. This is exactly what Helion wanted—a divided crew."
            hide z

            "The crew’s trust in Elara diminishes, sowing seeds of resentment that will lead to future betrayals."
            $ authority_mutiny = "yes"
            $ diplomacy_mutiny = "no"
            $ betray_helion = "no"

        "Side with dissenting crew":
            show e neutral
            e "You’re right! We can’t let Helion dictate our fate. I stand with you against their agenda!"
            hide e

            "The crew erupts in a mixture of cheers and disbelief, rallying behind Elara."
            if jarek_support == "yes":
                show j neutral
                j "Finally! This is what we need! Let’s take control of our mission!"
                hide j

            show z neutral
            z "You’ll regret this betrayal, Elara. You’re playing into Helion’s hands by defying them."
            hide z

            show e neutral
            e "No more secrets. We’ll create our own path."
            hide e

            "The crew, emboldened by Elara’s words, begins to form a united front against Zara and Helion’s agenda. The tension is thick with the promise of rebellion."
            $ authority_mutiny = "no"
            $ diplomacy_mutiny = "no"
            $ betray_helion = "yes"

    # End of scene
    jump scene_abys_awakens

label scene_abys_awakens:
    # Scene setup
    scene bg alien_structure_day
    with dissolve

    # Initial atmosphere and character introduction
    "The crew stands in awe within a vast, organic-like alien structure, illuminated by bioluminescent patterns. The air is thick with an otherworldly energy."

    "Dr. Elara Vaestrom leads her crew—Captain Jarek Duval, Dr. Amara Li, Tech Specialist Voss, and Helion Representative Zara Trent—into the chamber, their expressions a mix of fear and wonder."

    if approach_choice == "cautious": # If cautious approach was taken in "First Contact"
        "The atmosphere feels less hostile, the alien technology humming gently rather than surging with aggression."
    else:
        "A tension hangs in the air, as the alien tech pulses ominously around them."

    show a neutral
    a "Look at this! The structure seems to resonate with the energy patterns we detected. It’s almost like a living organism."
    hide a

    if amara_support == "yes":
        show a neutral
        a "I have a theory! The alien technology might be linked to Earth’s ecosystem. It’s possible that they’ve developed a symbiotic relationship with their environment."
        hide a
        
        "The crew listens intently, the tension in the air easing slightly."
        
    show e neutral
    e "That’s a fascinating perspective, Amara. If we can understand how they interact with their ecosystem, it might help us figure out how to approach this technology."
    hide e

    show j neutral
    j "Let’s not forget why we’re here. We need to decide how to handle this tech before we get in over our heads."
    hide j

    show v neutral
    v "The energy levels are stable… for now. But we need to act quickly."
    hide v

    show z upset
    z "We can’t afford to let our guard down. Helion expects results, and we need to make a decision about this technology."
    hide z

    if diplomacy_mutiny == "yes": # If diplomacy was chosen in "Mutiny"
        "The crew feels more united as they face the new challenge."

    if kept_secret == "yes": # If the secret was kept in "Secrets Unveiled"
        # Elara has fewer allies, leading to a more strained dynamic
        "However, the air is thick with unspoken tensions. The crew's trust in Elara is shaky, and she feels the weight of their skepticism."
    else:
        # Normal dynamics if the secret was not kept
        "There’s a sense of camaraderie, but uncertainty still lingers."
    
    # Choices for the player
    menu:
        "Attempt to reprogram the technology":
            show e neutral
            e "I say we attempt to reprogram it. If we can tap into its systems, we might be able to control it."
            hide e
            
            "The crew looks at each other, some hesitant but intrigued."
            show a neutral
            a "If we can understand its functions, we might be able to use it to our advantage."
            hide a

            show v upset
            v "But what if it reacts negatively? We’ve seen how unpredictable it can be."
            hide v

            show e neutral
            e "It’s a risk we have to take. We’ll need to work together."
            hide e

            "The crew sets to work, interfacing with the alien technology. The atmosphere is charged with tension as they focus on the task at hand."

            # Transition to the next scene
            jump scene_ultimate_choice

        "Prepare to destroy the alien tech":
            show e neutral
            e "I think we should prepare to destroy it. If we can’t control it, it poses a risk to us and possibly to Earth."
            hide e

            "The crew exchanges worried glances, the weight of the decision heavy in the air."
            show j neutral
            j "That’s a drastic step, Elara. We might be losing out on something that could help us."
            hide j

            show z upset
            z "But if it’s dangerous, we can’t afford to take that chance."
            hide z

            show v neutral
            v "Let’s just make sure we have a way out if this goes south."
            hide v

            "The crew prepares themselves, the tension thickening as they ready their equipment."

            # Transition to the next scene
            jump scene_ultimate_choice

        "Leave the technology untouched":
            show e neutral
            e "You know what? Let’s leave the technology untouched for now. We need more information before making a decision."
            hide e

            "The crew looks at each other, some surprised but relieved."
            show a neutral
            a "That might be wise. We don’t fully understand its capabilities yet."
            hide a

            show j neutral
            j "Let’s return to the ship and regroup. We can analyze the data we’ve collected."
            hide j

            show z neutral
            z "Fine. But we need to keep moving. Helion won’t wait forever."
            hide z

            "The crew begins to back away from the alien technology, a sense of uncertainty hanging in the air as they prepare to leave the chamber."

            # End of scene transition
            "As they exit the alien structure, there’s an underlying tension, but also a flicker of hope as they consider their next steps and the choices ahead."

    jump scene_ultimate_choice

label scene_ultimate_choice:
    # Setting up the environment and atmosphere
    scene bg spaceship_control_room
    with dissolve

    "The control room is dimly lit, the tension palpable as Elara and her crew gather around the holographic display of the alien technology. The hum of the technology pulses, reflecting the weight of their decision."

    show e neutral
    e "We’ve come so far... but we’re out of time. This is it. We decide now or risk everything."
    hide e

    show j neutral
    j "If we take control, we could achieve something monumental, but... what if we lose ourselves in the process?"
    hide j

    show a neutral
    a "We’ve seen what it can do. This tech could wipe us out if we’re not careful."
    hide a

    show z neutral
    z "Helion expects results. We can't leave here with nothing."
    hide z

    "Elara glances at her crew, gauging their reactions. Past choices weigh heavily here; each crewmember's loyalty or skepticism is written on their face."

    if authority_mutiny == "yes":
        "Elara feels a distance from some of the crew members, especially those who resented her taking authority earlier. The unspoken tension is thick, and Elara realizes that trust is fragile here."
    
    if diplomacy_mutiny  == "yes":
        "The crew feels more united after Elara's decision to balance authority and diplomacy, though tensions remain high as they face the alien technology."

    if kept_secret == "yes":
        "The secret Elara kept earlier has weakened some of her allies' trust, and she can sense lingering skepticism from those who felt betrayed."

    # Player's final choice
    menu:
        "Sacrifice herself to shut down the alien technology":
            show e neutral
            e "I can’t ask any of you to risk yourselves further. I'll shut it down myself."
            hide e

            show j upset
            j "Elara, don’t! We need you, and we need each other."
            hide j

            show a neutral
            a "No! There has to be another way."
            hide a

            "Elara places her hands on the control interface, preparing to shut down the technology. Alarms blare, and the system reacts violently, discharging energy across the room."

            show v upset
            v "Please, Elara, be careful!"
            hide v

            show e neutral
            e "If this technology threatens everything, I won’t let it take any of you. This is on me."
            hide e

            "She feels the energy surging through her, visions of alien worlds and the universe flashing before her eyes. Her final act resonates deeply with the crew, each one watching in awe and sorrow as the room fills with blinding light."

            centered "Ending 1: Sacrifice and Freedom"

            "The crew returns to Earth, forever changed by Elara's bravery, determined to honor her memory by pursuing a future of peace and wisdom."
            return

        "Gain control of the technology, risking human freedom":
            show e neutral
            e "We can't destroy something with so much potential. I’ll take control, even if it’s a risk."
            hide e

            "The crew exchanges uneasy glances. Some support her choice, while others appear deeply concerned about the consequences."

            if diplomacy_mutiny  == "yes":
                show a neutral
                a "If we do this carefully, it could change everything for humanity. I’m with you, Elara."
                hide a
            else:
                show a neutral
                a "Elara, I know you believe in this, but what if we end up being controlled by it?"
                hide a

            show z neutral
            z "A wise decision. Helion would approve."
            hide z

            "Elara connects with the alien system, a rush of power flooding through her. The technology starts to respond, stabilizing and syncing with her commands."

            if kept_secret == "yes":
                "Suddenly, an error flashes on the control panel, and Elara realizes the risk has grown; a security system overloads, endangering the entire structure."
            
            "Alarms sound as the system begins to destabilize, sending waves of energy into the room."

            show v neutral
            v "Elara! It’s too powerful. We’re triggering something!"
            hide v

            show e upset
            e "We have to keep going. It’s too late to stop now!"
            hide e

            "With a final surge, Elara locks in the controls, fully activating the alien system. The technology's defenses surge, sending out a blinding pulse that engulfs the entire chamber in chaos."

            centered "Ending 2: Power and Control"

            "The crew barely escapes with their lives, carrying with them the immense, perilous knowledge that they attempted to wield a power far beyond human understanding."
            return

        "Destroy the alien tech and abandon the project":
            show e neutral
            e "If we can’t control it safely, we need to destroy it. We can’t take the chance."
            hide e

            "Her tone is final, and the crew’s expressions shift to concern and reluctant agreement."

            show j neutral
            j "If that’s what you think is best, Elara. Let's end this here."
            hide j

            "Voss initiates the self-destruct sequence, his hands shaking as he enters the final command. The alien structure begins to tremble, and alarms blare around them as the countdown starts."

            if betray_helion:
                show z neutral
                z "You’ll regret this decision. Helion doesn’t forgive so easily."
                hide z

            "As the countdown reaches its final moments, the alien system’s defenses activate, hurling energy beams across the chamber."

            show a neutral
            a "Everyone, get back to the ship, now!"
            hide a

            "The crew races towards the exit, dodging energy blasts as the alien structure collapses. They make it back to the ship just as a massive explosion erupts behind them."

            centered "Ending 3: The Void’s Warning"

            "As they return to Earth, the crew reflects on the unknown dangers they encountered, forever reminded of the fragility of human understanding in the face of cosmic power."
            return

        "Attempt to harness the tech with the crew":
            show e neutral
            e "We’ll work together to harness its power. We’ve come this far as a team."
            hide e

            "Some crew members step forward, encouraged, while others remain cautious, unsure of the path Elara has chosen."

            if diplomacy_mutiny  == "yes":
                show j neutral
                j "If we work together, maybe we can understand it without triggering its defenses. I'm with you, Elara."
                hide j
            else:
                show j neutral
                j "Are you sure this is wise? We’re dealing with something we don’t fully understand."
                hide j

            show a neutral
            a "There’s a real risk, but maybe we can do it."
            hide a

            "They gather around the control interface, each member working on a different aspect of the technology. As they proceed, the alien system begins to power up, glowing with an intense energy."

            "The system's defenses activate suddenly, and a blinding energy wave fills the room."

            show v upset
            v "Everyone, get down!"
            hide v

            "Energy surges around them, and in the chaos, the crew struggles to keep the technology stable. But the intensity becomes overwhelming."

            show e neutral
            e "Hold on! We’re almost there!"
            hide e

            "As the energy wave reaches its peak, the crew is engulfed in a blinding flash, and they feel themselves slipping into a strange, unfamiliar realm, lost in the technology’s vast, incomprehensible depths."

            centered "Ending 4: Vanished in the Abyss"

            "The crew’s ambition to harness the unknown led them into a place beyond human understanding, their fates left uncertain as they disappear into the alien void."
            return
