﻿# Ren'Py script for "The Last Briefing" scene with a starting label

# Character Definitions
define e = Character("Dr. Elara Vaestrom", color="#88CFF1")
define j = Character("Captain Jarek Duval", color="#FFA07A")
define a = Character("Dr. Amara Li", color="#98FB98")
define v = Character("Tech Specialist Voss", color="#DAA520")
define z = Character("Zara Trent", color="#FFC0CB")

# Initialize `message_choice` variable to avoid errors later
default message_choice = ""

# Define images for scenes if not defined elsewhere
image briefing_room = "briefing_room.png"
image hangar_bay = "hangar_bay.png"
image decrypted_message = "decrypted_message.png"

# Start label to initiate the game
label start:
    # Go to the last briefing scene at the start of the game
    jump last_briefing

# Scene: The Last Briefing
label last_briefing:
    scene briefing_room with fade
    
    e "Alright, team. This is it. We've got one shot to track down that alien signal."
    e "Helion Dynamics thinks it might hold the key to our survival."
    
    j "Survival. Isn’t that what they said back when the first reactors blew?"
    j "What’s this signal supposed to do anyway? Disintegrate us faster?"
    
    a "Or it could help us find something we lost long ago, Jarek. Hope. A cure. There’s always a chance."
    
    v "Did you get any data regarding the signal’s origin? If it’s been out there long enough, we could face… unexpected challenges."
    
    z "Helion believes the signal is emitted from a point in the Nebula X-23. It’s risky, but the rewards outweigh the dangers."
    z "Your mission is to collect samples and data at all costs."
    
    # Elara notices the encrypted message
    e "(noticing something odd) Uh, Zara, what’s this?"
    
    z "(deflecting) Just standard updates. The mission parameters are of utmost importance. Focus on the signal."
    
    j "(noticing Elara's distraction) What’s on your mind, Doc?"
    
    e "What if there’s something we’re missing? Something that could... change how we approach this mission?"
    
    a "You’ve always said to trust instinct. What’s your instinct telling you now?"
    
    v "Whatever that message is, it could reveal important information. Or it could be a distraction."
    
    z "(interrupting) Enough speculation. The mission is the priority. We must depart within the hour."
    
    e "Alright, everyone. It’s time to gear up for launch. Just… keep your eyes open. That signal won’t decipher itself."
    
    # Choice: Ignore or Decrypt the Message
    menu:
        "Ignore the encrypted message and trust the crew.":
            $ message_choice = "ignore"
            e "(to herself) Let’s focus on the mission. We need to work together."
            e "Just some standard security protocols. Nothing we can’t handle. We trust each other, right?"
            e "We’ve got to work as a team."
            
            jump departure
    
        "Decrypt the message to discover more about possible betrayals.":
            $ message_choice = "decrypt"
            e "(after a pause, reaching out to the encrypted message)"
            e "Alright… Let's decrypt it. We face the truth together, come what may."
            
            # Transition to decrypted message reveal
            scene decrypted_message with dissolve
            e "It... it contains warnings. Potential betrayals, even from our own team."
            e "(to herself) This changes things. I need to keep an eye on Zara."
            
            jump departure

# Continuation of "The Last Briefing" scene
# Scene: Act 1, Scene 1 - Departure

label departure:
    # Scene setup for the hangar bay
    scene hangar_bay with fade
    
    # Description for the atmosphere in the hangar
    narrator "The hangar is filled with the low hum of machinery. Various crew members move about, preparing a sleek spacecraft for launch."
    "Dr. Elara Vaestrom stands at the entrance, taking a deep breath. The atmosphere is tense but filled with an undercurrent of excitement."
    
    e "Alright, everyone! This is it. We leave behind everything we know for a chance at survival. Let’s make it count."
    
    # Jarek approaches with a smirk
    j "You sure you're ready for this, Doc? Space isn’t exactly a walk in the park."
    
    if message_choice == "decrypt":
        e "(hesitant, suspicious) Are you with me, Jarek? No matter what happens out there?"
        j "(raising an eyebrow) Of course, Elara. I wouldn’t dream of letting you down."
    
    else:
        e "(raising an eyebrow) I’ve never been more ready, Jarek. We need to focus on the mission."
    
    # Amara joins the conversation, serious yet hopeful
    a "This could be our chance to discover something groundbreaking. Let’s just remember to stick together out there."
    
    # Voss calibrates equipment nearby, occasionally glancing at the crew
    v "And let’s not forget to double-check our systems. We can’t afford any slip-ups. Not now."
    
    # Zara enters the hangar with a commanding demeanor
    z "You’re all aware of the stakes. Helion Dynamics is counting on us to collect data from the alien signal. We mustn’t deviate from our objectives."
    
    "Elara exchanges a wary look with her crew, sensing the underlying tension."
    
    e "Understood. But before we launch, I want to talk to each of you. We need to be prepared for anything."
    
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
        e "(nervously) Jarek… if anything goes wrong out there, you’ll back me up, right?"
        j "(seriously) Always, Elara. If you have doubts, just say the word."
        e "(relieved but cautious) Thanks. I know I can trust you."
    
    else:
        j "What’s on your mind, Elara? You’re not having second thoughts, are you?"
        e "(hesitating) No, just thinking about our past missions. We’ve had our share of close calls. I need to know you’re with me on this."
        j "(sincerely) Always. Just don’t forget to keep your head in the game."
    
    e "(nodding) Thanks, Jarek. I’ll do my best."
    
    jump crew_gathering

# Conversation with Amara
label amara_conversation:
    "Elara turns to Amara, who is examining a sample container thoughtfully."
    
    if message_choice == "decrypt":
        e "(carefully) Amara, how do you feel about the rest of the team? Can we really rely on everyone?"
        a "(surprised but calm) Elara, we’ve been through a lot together. I believe in our team. We have to work together if we want to survive."
        e "(softly) You’re right. Trust is key. Let’s stay vigilant, though."
    
    else:
        a "This is an incredible opportunity. If we find what we’re looking for, it could change everything."
        e "(curious) What are your thoughts on alien biology? Do you think we’re ready for whatever we might encounter?"
        a "(determined) We’ll adapt. We always do. Let’s just remember to keep an open mind."
    
    e "Agreed. Let’s make sure we’re prepared for anything."
    
    jump crew_gathering

# Conversation with Zara
label zara_conversation:
    "Elara approaches Zara, who is reviewing mission data on her tablet with a focused expression."
    
    if message_choice == "decrypt":
        e "(coldly) Zara, I came across a message. It mentioned… potential betrayals. Care to comment?"
        z "(with a faint smile) Betrayals? You should focus on the mission, Elara, not on distractions. Paranoia won’t get us far."
        e "(suspiciously) Maybe. But I’ll be watching, just in case."
    
    else:
        e "Zara, can we discuss Helion’s expectations? I want to ensure we’re not missing any critical information."
        z "(coldly) Our objective is straightforward. Collect data and samples. Anything beyond that is not your concern."
        e "(narrowing her eyes) But what if there’s more at stake? We need to be prepared for hidden agendas."
        z "(dismissively) Focus on the mission, Elara. That’s all that matters."

    "Elara feels a sense of unease but decides to let it go for now."

    jump crew_gathering

# After conversations, the crew gathers for departure
label crew_gathering:
    "As the conversations conclude, Elara gathers her crew. Their expressions are a mix of determination and anxiety."

    if message_choice == "decrypt":
        e "(to herself) I know what that message warned about... But who among us can I truly trust?"
        e "(addressing the team) Alright, everyone. Before we head out, I just want to say... stay sharp. And watch each other's backs."
        
        # Jarek responds with reassurance, sensing Elara’s underlying concern
        j "We’re a team, Elara. If anyone tries anything, they'll have to get through me first."
        
        # Amara, sensing the tension, chimes in thoughtfully
        a "We’ve come this far together. Let’s focus on the mission and not let doubt tear us apart."

        # Zara’s reaction remains neutral, yet controlled
        z "(coolly) Helion is counting on us. Let’s not waste time with unnecessary worries."

    else:
        e "(inspiring) Alright, team. Let’s gear up and head out. Remember, trust each other, and stay alert. We’re facing the unknown together."

        # Jarek’s light-hearted response
        j "Nothing we can’t handle. Let’s get this done and head back in one piece."

        # Amara’s optimistic response
        a "The possibilities are endless. Just imagine what we might find out there."

        # Zara’s formal response
        z "Our objective is clear. Let’s not deviate from it."

    "The crew nods, a shared resolve forming among them. They move toward the ship, ready to embark on their journey into the abyss."

    # Transition to the next scene
    scene spaceship_departure with dissolve
    narrator "The engines hum as the crew boards the sleek, advanced spacecraft. The hangar bay doors open, revealing the stars outside."
    narrator "As the ship lifts off, the vast expanse of space stretches before them, both beautiful and terrifying."

    "Elara sits in the captain’s seat, her mind racing with thoughts about the decrypted message and the possible betrayals it hinted at. She glances at her team, wondering who—if anyone—might betray her trust."

    jump first_contact

# Scene: Act 1, Scene 2 - First Contact
label first_contact:
    scene spaceship_departure with fade

    # Opening narration for the new scene
    narrator "The crew has embarked on their journey, heading towards Nebula X-23. As the ship approaches the edge of the nebula, the atmosphere inside the cockpit is tense, each crew member preparing for the unknown."

    scene cockpit_view with dissolve

    # Description of the cockpit with the crew
    "The cockpit is filled with the soft glow of various control panels and the swirling, ominous hues of Nebula X-23 visible through the viewport."
    "Dr. Elara Vaestrom sits in the pilot’s seat, monitoring the signal’s coordinates. Captain Jarek Duval stands nearby, a cautious but eager look on his face."
    "The rest of the team is strapped in behind them, their expressions a mix of anticipation and unease."

    e "Alright, everyone. We’re approaching the source of the signal. Remember, we need to proceed carefully."
    
    j "(glancing at the readouts skeptically) Carefully? You know these signals can be pretty volatile, right? We push through, we might catch them off guard."

    v "(monitoring the systems) But if we push too hard, we risk triggering a defensive response. We don’t know what we’re dealing with here."

    a "(watching the swirling nebula) A cautious approach might allow us to gather more data without alarming whatever is out there."

    z "(leaning forward with a cold tone) We’re on a deadline. Helion expects results. We can’t afford to waste time being cautious."

    # Choice: Cautious or Aggressive Approach
    menu:
        "Order a cautious approach":
            $ approach_choice = "cautious"
            e "(decisively) I’m ordering a cautious approach. We can’t risk escalating the situation. Let’s monitor the signals and gather as much data as we can before making any moves."
            
            # Crew reactions to cautious approach
            "The crew exchanges glances, some relieved, others apprehensive."
            
            j "(sighing) Fine. But if we end up sitting here doing nothing, it’s on you, Doc."
            
            v "(nodding) I’ll run a full scan of the area. Let’s see if we can pinpoint the source of that signal without drawing attention."

            # Transition to the next scene within the cautious approach
            jump cautious_approach

        "Push forward aggressively":
            $ approach_choice = "aggressive"
            e "(resolutely) No, we’re pushing forward. We need to make contact now. Jarek, increase speed."

            # Crew reactions to aggressive approach
            "Jarek nods, a glint of excitement in his eyes as he accelerates the ship."
            
            j "(grinning) You got it! Let’s show them we mean business."
            
            v "(warningly) Careful, Elara! We’re entering uncharted territory. We could trigger a defensive response."
            
            a "(anxiously) This could get dangerous! We should be cautious!"
            
            # Transition to the next scene within the aggressive approach
            jump aggressive_approach

# Cautious Approach Path
label cautious_approach:
    # Scene setup for cautious approach within the nebula
    scene nebula_approach with dissolve
    narrator "The view outside the ship shifts as they glide deeper into the nebula, taking slow, calculated moves to avoid alarming any potential threats."

    # Crew detects the signal
    a "(pointing at the screen) There! The signal’s stronger now. If we can triangulate its position…"
    
    # Sudden interference interrupts their scans
    "Suddenly, the ship shakes violently, and alarms begin to blare."
    
    v "(frantically) We’re getting interference! They know we’re here!"

    e "(shouting over the alarms) Hold steady! We’re not done yet!"

    "The crew scrambles to stabilize the ship, working in unison to manage the interference and keep the ship under control. Their cautious approach has bought them some time to react to the disturbance without triggering an immediate threat."

    # Next steps based on the cautious approach
    narrator "With a coordinated effort, the crew manages to stabilize the ship. They exchange glances, realizing they may have only moments to decide on their next course of action."

    # Transition to next possible choices in Act 1, Scene 3 or other events
    jump next_scene

# Aggressive Approach Path
label aggressive_approach:
    # Scene setup for aggressive approach within the nebula
    scene nebula_rush with dissolve
    narrator "The ship barrels forward, cutting through the nebula with newfound speed as the crew’s expressions shift from tension to exhilaration."

    # Crew detects the signal but faces backlash
    v "(concerned, watching the readings) Elara, we’re approaching uncharted territory. This could trigger a defensive response!"
    
    a "(gripping her seat, eyes wide) This could get dangerous! We should have been cautious!"

    e "(determined) We need to take risks if we want to find answers. Let’s make history!"

    # Unexpected energy pulse shakes the ship
    "Suddenly, a massive energy pulse erupts from within the nebula, shaking the ship violently. The alarms blare louder as the crew is thrown against their restraints."

    z "(shouting over the noise) What did I tell you? We’re in over our heads!"

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
    scene common_area_dim with fade
    
    # Description for setting the mood in the common area
    narrator "The common area is dimly lit, the glow from holographic displays casting eerie shadows across the room."
    "The crew—Dr. Elara Vaestrom, Captain Jarek Duval, Dr. Amara Li, Tech Specialist Voss, and Helion Representative Zara Trent—are gathered, the tension palpable."
    
    # Elara addresses the crew about Helion’s motives
    e "(determined) We need to discuss what we’ve discovered. There’s something unsettling about Helion’s true motives for sending us here."
    
    # Zara’s guarded response
    z "(dismissively) What’s done is done, Elara. We’re on a mission, and we need to focus on the objectives at hand."

    # Jarek challenges Zara
    j "(challenging) But what if the objectives are just a cover? We deserve to know what Helion is really after."
    
    # Elara agrees with Jarek, emphasizing safety concerns
    e "Exactly. If there’s hidden information, it could compromise our safety and the mission itself."
    
    # Amara glances at Zara with concern
    a "(supportively) Zara, you’ve been with Helion longer than any of us. What do you know about their covert missions?"
    
    # Conditional: Additional dialogue if Elara questioned Zara in The Last Briefing
    if message_choice == "decrypt":
        z "(sighing, reluctantly) Helion has been involved in operations that extend beyond what you can imagine. They’re not just looking for technology; they want control over it."
        
        # Voss’s anxious reaction to Zara’s revelation
        v "(anxiously) Control how? Are we just pawns in their game?"
        
        "Zara looks uneasy but stands her ground."
        z "(defensively) You have to understand, the stakes are incredibly high. Helion’s interests in alien technology are about power and survival."
    
    # The crew’s reaction to Zara’s response varies based on the First Contact approach
    if approach_choice == "cautious":
        "The atmosphere is tense, but Elara senses that the crew is still managing to keep their emotions in check."
    else:
        "The crew’s aggression is heightened, with Jarek visibly clenching his fists and Amara watching Zara with mistrust."
    
    # Jarek’s frustration
    j "(accusingly) So we’re just supposed to follow orders blindly? This isn’t right!"
    
    # Elara takes a deep breath to maintain control of the escalating tension
    e "(calming) We need to decide how to handle this information. Confronting Zara could lead to a division among us."
    
    # Choice: Confront Zara or Keep Knowledge Secret
    menu:
        "Confront Zara about Helion’s secrets":
            jump confront_zara

        "Keep the knowledge secret":
            jump keep_secret

# Choice Path 1: Confront Zara
label confront_zara:
    e "(firmly) Zara, we can’t ignore this. You need to come clean about Helion’s true intentions. Are we just expendable assets?"
    
    "Zara’s composure falters, revealing her inner conflict."
    
    z "(defensively) You don’t understand the bigger picture! This isn’t just about us; it’s about humanity’s future!"
    
    j "(sarcastically) Right. And your loyalty to Helion means more than our lives?"
    
    "Elara steps closer to Zara, her voice lowering, her gaze intense."
    
    e "(intensely) I trusted you, Zara. If you’re not with us, you’re against us."
    
    "Zara’s eyes flash with anger, and the tension in the room escalates into a confrontation."
    
    # Escalated aggression based on First Contact approach
    if approach_choice == "aggressive":
        narrator "The crew’s aggression flares, with voices raised and accusations flying. Elara can feel the group teetering on the edge of mutiny."
        jump mutiny  # Placeholder for mutiny scene
    else:
        narrator "Though tense, the crew manages to restrain themselves. Zara’s silence speaks volumes, and Elara knows this conflict is far from over."
        return  # Ends the scene, to be continued in the next part of the story

# Choice Path 2: Keep the Knowledge Secret
label keep_secret:
    e "(cautiously) Maybe we should hold off on confronting Zara for now. Let’s keep this information under wraps and focus on our mission."
    
    # The crew’s response to keeping the knowledge secret
    "The crew looks uncertain but slowly nods, the tension easing slightly."
    
    a "(relieved) That might be wise. We can’t afford to fracture the team at this stage."
    
    # Zara’s subtle relief
    z "(gratefully) Thank you, Elara. We need to be united. Our lives depend on it."
    
    # Voss remains skeptical, however
    v "(tentatively) But we can’t ignore potential threats. If Helion is hiding something, we need to be prepared."
    
    # Elara’s response to keep the team focused
    e "(resolutely) We will stay vigilant. But for now, let’s focus on the mission. We need each other more than ever."
    
    narrator "The crew returns to the holographic displays, but the atmosphere remains charged with unresolved tension and the weight of secrets."
    return
