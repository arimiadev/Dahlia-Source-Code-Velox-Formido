# The script of the game goes in this file.

## ctc="ctc", ctc_pause="ctc", ctc_position="nestled"

define narrator = nvl_narrator
define menu = nvl_menu

define d = Character("[dah]", color="#fc8bab", image="dahlia", what_prefix='\"', what_suffix='\"', kind=nvl)
define c = Character("Camellia", color="#bba3d6", image="camellia", what_prefix='\"', what_suffix='\"', kind=nvl)


layeredimage dahlia:

    group base:
        attribute base1 default:
            "dahlia base2.png"

    group brows:
        attribute up default:
            "dahlia brows1.png"
        attribute surprise:
            "dahlia brows2.png"
        attribute unsure:
            "dahlia brows3.png"
        attribute down:
            "dahlia brows3.png"
        attribute neutral:
            "dahlia brows5.png"

    attribute base3:
        "dahlia base3.png"

    group expressions:
        attribute smile default:
            "dahlia expression1.png"
        attribute happy:
            "dahlia expression2.png"
        attribute talk:
            "dahlia expression3.png"
        attribute frown:
            "dahlia expression4.png"


layeredimage camellia:

    group base:
        attribute base1 default:
            "camellia base2.png"

    group expressions:
        attribute smile default:
            "camellia expression3.png"
        attribute talk:
            "camellia expression4.png"
        attribute frown:
            "camellia expression1.png"
        attribute frowntalk:
            "camellia expression2.png"

    group brows:
        attribute up default:
            "camellia brows1.png"
        attribute surprise:
            "camellia brows2.png"
        attribute unsure:
            "camellia brows3.png"
        attribute down:
            "camellia brows3.png"

image black = "#000"

transform leftt:
    zoom 0.7 xalign -0.3 yalign 0.1

transform lefttt:
    zoom 0.5 xalign 0.3 yalign 0.05

transform leftttb:
    zoom 0.8 xalign -1.6 yalign 0.1 matrixcolor(BrightnessMatrix(-1)) xzoom -1

transform centerr:
    zoom 0.7 xalign 0.5 yalign 0.1

transform shake:
    ease 0.3 xoffset -39
    ease 0.4 xoffset 50
    ease 0.2 xoffset -10
    ease 0.3 xoffset 22
    ease 0.2 xoffset 0

transform slowshake:
    ease 0.4 xoffset -205
    linear 0.2
    ease 0.6 xoffset 140
    linear 0.14
    ease 0.5 xoffset -370
    linear 0.3    
    ease 0.7 xoffset 290
    linear 0.2
    ease 0.5 xoffset -105
    linear 0.12
    ease 0.6 xoffset 370
    linear 0.22
    ease 0.8 xoffset 0

transform dance:
    ease 0.7 xoffset -59
    linear 0.25
    ease 0.6 xoffset 74
    linear 0.19
    ease 0.76 xoffset -70
    linear 0.3    
    ease 0.7 xoffset 102
    linear 0.2
    ease 0.8 xoffset 0

transform quickshake:
    ease 0.1 xoffset -39
    ease 0.2 xoffset 50
    ease 0.11 xoffset -10
    ease 0.22 xoffset 22
    ease 0.14 xoffset 0

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -28
    easeout .175 yoffset 0
    easein .175 yoffset -14
    easeout .175 yoffset 0
    yoffset 0

transform curtsy:
    easein 0.4 yoffset 25
    easein 0.25 yoffset 0
transform customcurtsy(ypos):
    easein 0.4 yoffset (ypos+30)
    easein 0.25 yoffset (ypos+0)

transform nightcolor:
    matrixcolor TintMatrix("#8594d6") * BrightnessMatrix(0.03)

transform bedcolor:
    matrixcolor TintMatrix("#8594d6") * TintMatrix("#966585") * BrightnessMatrix(0.03)

image dahlia night = LayeredImageProxy("dahlia",nightcolor)
image camellia night = LayeredImageProxy("camellia",nightcolor)

image dahlia bed = LayeredImageProxy("dahlia",bedcolor)
image camellia bed = LayeredImageProxy("camellia",bedcolor)


default dpoint = 2
default dah = "Humanoid"

label start:
    
    scene black with fade

    "I've always wondered what eternity must feel like. Would it go by in the blink of an eye? Like a drop in the bucket of an infinitely expanding pool where the waves never crest on a shore?"

    "Or would it be that feeling of waiting for a lesson to end, where the teacher drones on and on for hours, a never-ending slew of course matter dripping from their lips?"
    "Where the reprieve of a sunny day and a mild breeze is just out of reach beyond the windowsill, only a few more minutes away forever while you wilt inside."
    nvl clear
    "I don't know what the \"real\" eternity feels like, but I know I'm in a pocket of it right now."

    nvl clear 
    scene bg balcony
    show nvlgrad:
        blend "multiply"
    show dahlia night at leftt
    with dissolve

    d talk "How do you manage with those guards? They're so brash and annoying."
    show dahlia smile
    c "They tend to like people more when they don't suck people's blood."

    d down happy "I reckon even some pigs can hate."

    nvl clear
    scene bg balcony:
        zoom 1.3 xalign 0.5 yalign 0.0
        linear 10.0 yalign 0.9
    show nvlgrad:
        blend "multiply"
    show dahlia night:
        zoom 1 xoffset -410 yalign 0.8
        linear 10.0 yalign 0.05
    with dissolve

    "Starlight clings to the lace on her dress as the girl prances away from the window. Each step is graceful on the hardwood floor, not even making a light creak."
    "With her dark tied-up hair and flowing dress, she looks more akin to a ball-jointed doll dancing."
    "But the minimal lighting betrays her, bouncing off of the trace amount of blood on her lace collar."

    scene black with fade

    "Rather than risk the chance of being seen in the window any longer, she plops down on a chair in my reading nook. My favorite chair."

    nvl clear
    scene bg bedroom
    show nvlgrad:
        blend "multiply"
    show dahlia bed at lefttt
    show camellia at leftttb
    with dissolve

    show dahlia talk at curtsy

    d "Come. Sit with me."
    show dahlia smile
    
    window show
    menu:
        ">Why?":
            c "Why should I?"
            d talk "Why not? What else do you have to do?"
            hide camellia
            show dahlia at leftttb
            show camellia bed frown down at lefttt behind dahlia:
                yoffset 10
            with dissolve
            c "Sleep. I was sleeping rather well until you interrupted."
            d "Boring! What's the appeal in sleeping your life away? Everything fun happens at night."
            nvl clear
            c "Or is that because you can't be out during the day?"
            # hide dahlia
            # show camellia at leftttb
            # show dahlia bed frown at lefttt behind camellia
            # with dissolve
            "The girl doesn't immediately retort back. Instead, she purses her lips together and turns her attention to my bookcase."
            hide camellia
            hide dahlia
            show dahlia bed frown surprise at leftt
            with dissolve

        ">Alright.":
            "There's nothing better for me to do. I'm surely not falling back asleep with her here."
            hide camellia
            show dahlia at leftttb
            show camellia bed frown at lefttt behind dahlia:
                yoffset 10
            with dissolve
            c "Alright."
            hide dahlia with dissolve
            show camellia at lefttt, customcurtsy(10)
            "I climb out of bed for the first time since she broke in. Despite willingly leaving the safety of my sheets, I still tread carefully."
            hide camellia
            show dahlia bed at leftt
            with dissolve
            "The girl pats on the pillows beside the chair and turns her attention to my bookcase."
            show dahlia talk surprise

    nvl clear

    d "There's so many books here. Can you read?"
    show dahlia smile
    "If there were a book in my hand, it would be flying towards her head at this moment."

    c "Of course I can! What do you take me for, a child?"

    d neutral "Yes."
    nvl clear
    hide dahlia
    show camellia bed down frown at leftt:
        yoffset 10
    with dissolve
    "I look her over again. She looks to be my age, but most girls my age don't have splatters of blood on them."

    c frowntalk "And you aren't?"
    show camellia frown
    d "Age is meaningless to me. I stopped counting my age when I stopped being human."
    nvl clear
    c frowntalk "How long ago was that?"
    hide camellia
    show dahlia bed happy at leftt
    with dissolve
    d "Counting in years is such a dull human trait. It's been a couple of full moons since I stopped such boring things."
    show dahlia smile
    c "..."
    nvl clear
    hide dahlia
    show dahlia bed at lefttt
    show camellia at leftttb
    with dissolve

    d happy "Are they for decoration? Surely you could decorate with something more lively, like plants or stuffed animals or art."
    show dahlia smile
    menu:
        ">Of course not.":
            c "Of course they're not decorations, they're my books!"
            d frown "All of them?"
            c "Yes! It's my room! My room that you so rudely intruded on!"
            nvl clear
            show dahlia at curtsy
            d "Huh. This big thing?"
            "She motions her hand around my room which is clearly one area, not partitioned off by anything else."
            c "It's all my bedroom, yes. I'd like to think it's a fairly typical one."
            nvl clear
            d "Not from what I've seen."

        ">Are you sure you're not the illiterate one?":
            $ dpoint -= 1
            c "Are you sure you're not the illiterate one?"
            d frown surprise "Excuse me?"
            c "Why else would you question what books are for? No one would look at a full bookcase and ask if it's decor."
            nvl clear
            d up "Not if you've seen the houses I have."

    hide dahlia
    hide camellia
    show camellia bed frown at leftt
    with dissolve

    c "Other houses don't have bookcases?"

    hide camellia
    show dahlia at leftt:
        matrixcolor BrightnessMatrix(-1) xzoom -1
    with dissolve

    d "They don't have books this well loved."
    hide dahlia with dissolve
    "Her eyes gloss over the books and back to the entrance to my room."
    "A lone alabaster doorway separates us from the hallway. Its ornate door knob rests in the locked position—not that it helps when intruders come in through the window."

    nvl clear
    show camellia bed frown at lefttt:
        yoffset 10
    show dahlia at leftttb
    with dissolve

    c "Why did you come here?"

    d "Your guards were chasing me."

    c "They're not my guards."

    d "Did they kidnap you?"

    c down "No!! They're—... They're father's."
    nvl clear
    d "Your father or someone else's?"

    c "My...My father."

    d "Tell your father he has poor judgment in staff."

    c "I'll let you file your complaint yourself."

    d "I've had enough pitchforks stuck in my face for today."

    nvl clear
    c "And why is that?"
    hide dahlia
    show dahlia bed frown down at lefttt behind camellia
    show camellia at leftttb
    with dissolve
    d "Because your kind isn't too welcoming to my kind."

    c "I was asking why you were here in the first place."

    d up happy "Obvious questions get obvious responses. I needed a snack, of course."
    show dahlia smile
    nvl clear
    c "And you chose my residence."
    d down happy "Didn't you say this was your father's?"

    hide dahlia
    hide camellia
    show dahlia bed down:
        zoom 0.8 xalign 2.2 yalign 0.1
        linear 10.0 xalign -0.6
    show camellia:
        xalign 1.5 yalign 0.0 matrixcolor BrightnessMatrix(-1)
        linear 10.0 xalign -1.0
    with dissolve

    "Her words curl around the last word, like ivy growing against a trellis. She's clearly already had a \"snack\", but was it enough to satisfy her?"

    "Or am I the main course?"

    hide camellia
    show dahlia bed surprise at bounce:
        xalign -0.6
    with dissolve
    nvl clear
    "The girl springs up to her feet. Her sudden movement sends a jolt down my spine, but she doesn't notice. Instead, she saunters to my wardrobe."
    show dahlia happy at curtsy
    d "Ooo, look at this! So many nice gowns."
    show dahlia at slowshake
    "She picks one off the hanger, taking it into her arms as you would a dance partner. Her fingers clasp the sleeve cuffs and her legs do the thinking."

    d "Say, have you ever been to a party?"
    show dahlia smile
    nvl clear
    c "Only several."

    d down talk "What a braggart! I've only been to a handful."
    show dahlia smile at dance
    "The skirt tails of the gown intermingle with her own as she twirls about. Lace on lace, the two become indistinguishable in the darkness."
    nvl clear
    d talk surprise "Ah, but aren't they so fun? Dancing the night away, stuffing your faces with delicacies..."
    show dahlia smile up
    menu:
        ">The sweets are good.":
            c "The sweets are rather tasty at any good party."
            d surprise happy "Aren't they? You can always tell how an evening is going to go by the quality of their dishes."
            show dahlia smile
            c "You sound like you've been to more than you let on."

        ">Is food all you think about?":
            $ dpoint -= 1
            c "Is food all you ever think about?"
            d frown "Mmm, not always. But isn't It natural to spend so much time contemplating food? You can't live without it."
            c "I try not to spend my time thinking about things that are guaranteed."
            nvl clear
            d talk "That's true. There's always plenty of food around, isn't there?"
            "She steps closer, evening gown clutched close to her."
            d down happy "Always plenty of piggies to try."
            show dahlia up smile
            "Her eyes stare a whole through me."
            hide dahlia
            show dahlia bed neutral:
                zoom 1.1 xpos -500 yoffset -100
            with Dissolve(0.2)
            "Before I realize it, she's only a foot away. I reflexively lean back—but it's all for nothing. Just as quickly as she pranced towards me, she turned away."
            hide dahlia with easeoutleft
            show dahlia bed at leftt with dissolve

        ">I'm not a good dancer.":
            c "I'm not a good dancer, to be honest."
            d talk "Oh, what a shame! I hope someone will teach your poor soul."
            show dahlia smile
            c "..."
            nvl clear
            d "Dancing is one of the many joys of life and it's best done under a ballroom illuminated brightly to keep nighttime at bay!"
            c "That's...rather specific."
    nvl clear

    d surprise happy "Didn't I tell you? The best things in life happen at night!"
    show dahlia at curtsy
    pause(0.5)
    scene bg balcony
    show dahlia night up smile at leftt
    with dissolve

    show dahlia up smile at bounce, dance
    "With a grand flourish, my evening gown flies into the air as she circles back towards my window. She does a low curtsy before tossing the gown across a chair."

    d talk neutral "Everything... Everything good in this world happens at nighttime."
    show dahlia smile
    "Her words are said with a quiet intensity."
    nvl clear
    d talk "Late night parties. Dinner time. No crowds on the road. Secret meetings behind hushed doors..."
    show dahlia smile at curtsy
    "She raises her hand, placing it against the glass of the window pane."

    d talk "The moon and stars come out to play..."
    d unsure "They've witnessed everything, you know? Everything that's happened in this world—every lie said, every empire destroyed, every person created."
    nvl clear
    d neutral "Imagine all of that. Seeing everything laid out before you."
    show dahlia smile
    menu:
        ">They must be rather smart.":
            c "They must be rather smart, then. That's all the knowledge of the world, all theirs."
            d surprise talk "I suppose so! No wonder they're so bright."
            show dahlia smile
        ">They must be rather lonely.":
            $ dpoint += 1
            c "They must be rather lonely, then. Seeing all of that and being unable to change anything."
            show dahlia surprise frown
            pause(0.5)
            show dahlia unsure
            pause(0.5)
            show dahlia:
                matrixcolor BrightnessMatrix(-1)
            with dissolve
            d "...I suppose so."


    nvl clear
    hide dahlia
    show camellia night smile at lefttt:
        yoffset 10
    show dahlia at leftttb
    with dissolve

    c "The stars are really pretty either way. I like to watch them as I fall asleep."

    d "So that's why your curtains weren't drawn on the balcony."

    show camellia unsure frowntalk at lefttt, shake

    c "I-I wasn't expecting company to arrive through that door..."

    show camellia frown

    "She flashes me a toothy grin. Her canines are stained red."

    nvl clear
    hide dahlia
    show dahlia night happy unsure at lefttt behind camellia
    show camellia at leftttb
    with dissolve

    d "Don't you know that pulled curtains are an open invitation?"

    c "Balconies aren't most people's first entry choice. Or a choice at all."
    show dahlia at bounce
    d "And most people are boring! What a terrible way to live a life." 

    c "So you prefer your way?"
    nvl clear
    d surprise "Of course I do. What's the point in living if you aren't living a life you love?"
    show dahlia smile

    menu:
        ">Because it's our only life.":
            c "Because it's our only life. You can't squander it."
            d neutral "Hmm, I wonder if that's true... I mean, you never know. Even if not, I wouldn't want to waste a moment of my life."
            nvl clear
            c "You can't enjoy everything in life."
            show dahlia at bounce
            d up happy "No, but I can fill my life with much more fun to make up for it! Hahahah!"
            show dahlia at curtsy, dance
            "She does a twirl in the moonlight, swinging her arms out."
            hide dahlia
            hide camellia
            with dissolve
            show camellia night frowntalk at leftt:
                yoffset 10
            with dissolve
            c "And this...Is this fun?"
            nvl clear
            hide camellia with dissolve
            show dahlia night at leftt with dissolve
            
            if dpoint <= 1:
                # >BAD END
                d "Yes... I'd say I've had fun."
                show dahlia unsure at curtsy
                pause(0.4)
                show dahlia:
                    zoom 1 xoffset -400
                with dissolve
                "A pitiful, elongated sigh escapes her. I blink and she's suddenly invading my personal space, just a foot away."
                d "I wish I could stay, but those guards look like they're still on the lookout. So..."
                show dahlia at curtsy
                "My blood turns to ice as she lifts her dainty fingers to my chin."
                nvl clear
                "For the first time tonight—for the first time in a long time—I feel the skin of another person. Her fingers are cold, making me shiver. They're not the kind of cold that I would imagine of someone undead, but rather that of a girl escaping the winter outside—despite it being a summer night."
                d neutral happy "Thank you for your time, Camellia."
                "I open my mouth—"
                scene black
                extend "but the only thing that escapes me is a singular gasp as her fangs sink into my neck."
                nvl clear
                "All of the blood rushes to my head, turning my face flush. It doesn't hurt. I can only groan."
                "One more small groan leaves my lips...as darkness takes a hold of me."

            else:
                # >GOOD END
                d "Yes... I'd say it is."
                show dahlia unsure at curtsy
                pause(0.4)
                show dahlia:
                    zoom 1 xoffset -400
                with dissolve
                "A pitiful sigh escapes her. I blink and she's suddenly invading my personal space, just a foot away."
                d "I wish I could stay, but those guards look like they're still on the lookout. So..."
                show dahlia at curtsy
                "My blood turns to ice as she lifts her dainty fingers to my chin."
                nvl clear
                "For the first time tonight—for the first time in a long time—I feel the skin of another person. Her fingers are cold, making me shiver. They're not the kind of cold that I would imagine of someone undead, but rather that of a girl escaping the winter outside—despite it being a summer night."
                d talk "Thank you for your time, Camellia."
                show dahlia smile
                "I open my mouth, to retort back, to ask how she knows my name, but the words become lost in the look of her eyes."
                nvl clear
                "For the first time, I'm able to see her clearly. Tiny freckles dot her face like a constellation. Even in the darkness, her eyes twinkle a vibrant green."
                c "What—What is your name?"
                $ dah = "Dahlia"
                d talk neutral "...Dahlia."
                show dahlia smile
                c "Will I...ever see you again...Dahlia?"
                nvl clear
                show dahlia at bounce
                d surprise happy "Hahah! A human wants to meet me again?!"
                show dahlia at bounce
                "She reels back, her laughter echoing off of the walls."
                d unsure "I really have had fun tonight! I tell you what—I'll be back a week from now. Be sure to have a tray of sweets waiting for my arrival."
                show dahlia smile
                c "Hmm...a whole week...? I'm afraid I might eat the sweets by then."
                nvl clear
                d neutral talk "Then ask your butlers for more. If there aren't any here for me...I'll have to take something else for taste."
                show dahlia smile
                "My heart skips a beat as her eyes narrow in on me, her thin fingers curling around my chin."
                c "A taste....?"
                "Her thumb traces against my bottom lip."
                d happy "A taste...of something sweet."
                nvl clear
                show dahlia smile at bounce:
                    easein 0.6 zoom 0.7 xoffset 0
                "Just as quick as she danced up to me, she pulls away, taking my breath with her."
                d happy "Be well, my Camellia."
                show dahlia smile
                pause(0.1)
                show dahlia:
                    easein 0.6 alpha 0.0 xoffset 600
                "Her words hang in the air as she unlatches the balcony door—and escapes into the night. I touch my lips. A small smile crosses my face as I stand to close the door behind her."
                scene black with fade
                "A future meeting time. A nighttime rendezvous. —A date."

        ">Because some people don't have a choice.":
            c "Because some people don't have a choice. They can't change things."
            d neutral talk "Ooo, what wise words from a rich girl. Look at the size of this estate! Have you even seen every crevice of it?"
            show dahlia smile
            pause(0.1)
            hide camellia
            show dahlia:
                zoom 1 xoffset -500
            with dissolve
            "The moonlight creeps across her face, flashing against the lace in her dress."
            nvl clear
            d talk "What do you know about not having a choice in this world?"
            show dahlia smile
            hide dahlia with dissolve
            show camellia night:
                matrixcolor BrightnessMatrix(-1) yoffset 10 xoffset -500
            with dissolve
            c "I didn't have a choice with my body."
            "My heart thuds within my chest, panging back and forth as the words leave me."
            d "Oh...do tell, my lady."
            "Her words drip out. I clutch the ends of my dress."
            nvl clear
            show camellia unsure frowntalk:
                matrixcolor BrightnessMatrix(0)
            with dissolve
            c "My body has...always been weaker than others. I become exhausted doing things others find simple. Running is a good way to make myself bedridden for days."
            c "Even with the doctors my father has hired, none were able to help me. Most didn't see anything wrong with me—the most common prescription was fresh air."
            c "My room is my home."
            show camellia frown
            pause(0.1)
            hide camellia with dissolve
            show dahlia night:
                zoom 1 xoffset -500
            with dissolve
            d talk "And tell me...how do you like that?"
            show dahlia smile
            nvl clear
            c "You can already guess the answer."
            d talk "Maybe I can, maybe I can't. But I don't know the answer to one more question."
            show dahlia night base3 with Dissolve(0.3)
            d happy "What would you do if you could leave here?"
            show dahlia smile
            nvl clear
            "Leave here?"
            hide dahlia
            show camellia night:
                yoffset 10 xoffset -500
            with dissolve
            c frowntalk "I'd love it, as long as it isn't me leaving in a casket."
            show camellia frown
            pause(0.1)
            hide camellia
            show camellia night at leftttb
            show dahlia night at lefttt behind camellia
            with dissolve
            d "I've always wanted a dancing partner. What do you say?"
            show dahlia smile
            c "You haven't even told me your name yet, and you're asking these questions?"
            $ dah = "Dahlia"
            d neutral talk "...Dahlia. That's my name."
            show dahlia smile
            nvl clear
            c "Well, Dahlia... Is it painless?"
            d talk "Is there anything in life that's painless?"
            show dahlia night base3 with Dissolve(0.3)
            d happy "Don't worry, I'll make it extra sweet."
            show dahlia:
                matrixcolor BrightnessMatrix(-1)
            with dissolve
            "I open my mouth—"
            scene black
            extend "but the only thing that escapes me is a singular gasp as her fangs sink into my neck."
            nvl clear
            "All of the blood rushes to my head, turning my face flush. It doesn't hurt. I can only groan."
            "One more small groan leaves my lips...as darkness takes a hold of me."
            nvl clear
            scene bg bed
            show dahlia bed surprise at leftt
            with fade
            show dahlia at bounce
            "When I come to, I'm in an unfamiliar place, surrounded by warmth."
            "The air doesn't feel as oppressive anymore—it's like I'm able to breath oxygen for the first time. Even my gown feels like it's not constricting me. I exhale a long, well-overdue breath."
            show dahlia up at bounce
            d happy "You must be so hungry, you've slept for days!"
            extend " Don't worry, I know just the place for a snack~"
            show dahlia smile



    return
