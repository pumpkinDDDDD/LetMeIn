# The script of the game goes in this file.
# cektes masuk 
# Set up LayeredImage Sprites
layeredimage eileen:

    group base auto:
        attribute casual default

    if casual:

        "eileen_headband"

    group face auto:
        attribute neutral default

# This adds Eileen's headband to her sprite when True
default casual = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#f88787", image="eileen")
define e_nvl = Character("Eileen", color="#f88787", kind=nvl, image="eileen")
define e_bubble = Character(color="#f88787", kind=bubble, image="eileen")
define nar_nvl = nvl_narrator


define MC = Character ("[mc]")    
define NO = Character ("???")
define Y = Character ("Blonde Woman")
define B = Character ("Brown Haired Woman")
define D = Character ("Bearded Man")
define BM = Character ("Howard")
define DA = Character ("Dad")
define C = Character ("Catherine")
define E = Character ("Lizzie")
define VA = Character ("Villager A")
define VB= Character ("Villager B")
define WI= Character ("Witch")
define Q = Character (" ")

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False

label splashscreen:
    
    scene black

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0
    
    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)
 
        $ persistent.seen_splash = True
    
    ## Players can skip the animation in subsequent launches of the game.
    else:
 
        if renpy.pause(8.5):
 
            jump skip_splash

    scene black
    with fade
 
    label skip_splash:
 
        pass
    
    call screen content_warning

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:

        call screen splash_settings

        call screen preferences

        ## This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True

    return








## The game starts here.

label start:
    #bgm: https://dova-s.jp/EN/bgm/play17718.html
    scene black with fade
    pause 0.5
    scene bedroomnight with fade
    "(I can’t sleep)"
    "(I’ll go take a walk)"
    scene cg1 with fade 
    #whether we use a video or not is decided later
    "(What’s that?)"
    "(A..bird?)"
    "(It’s staring right at me, I guess I might as well give it a smile?)"
    #feather drops here
    scene cg1a with fade
    pause 1
    scene cg1b
    pause 1
    scene cg1c
    pause 1
    scene cg1d
    "I could never forget the beautiful feather I saw falling out of the night sky, the way it shimmered against the moon and gently fell to my hand."
    "It’s beautiful.."
    scene black with fade
    "However, what creature did this come from?"
    "{size=+10}{color=#df1439} Was it a monster? {/color}{/size}"

    scene black with fade
    #bgm : https://dova-s.jp/EN/bgm/play22607.html
    #op lines
    #footsteps
    NO "H-hello? I know I haven’t been here for a while but I’m back?"
    #knock on window
    NO "Can you please open the window? I’m here."
    NO "Please?"
    "..."
    NO "You’re awfully silent today.. Can I assume you’ve given me permission to enter?"
    "..."
    "Alright, I’m coming in."
    #creak then stab
    NO "Ah!"
    NO "That’s new..Are these pointy things on your window a new form of decoration?"
    #stab
    NO "Ack! {size=-5} I sure hope you remove them soon, it’s starting to hurt..{/size}"
    #stab

    scene cg2 with fade
    NO "Let me in."
    scene cg2 with vpunch
    #brutal stabbing, layer w/ wood noise?
    NO "LET ME IN!"
    scene cg2 with vpunch
    #rattling, window breaking, stabbing noise
    #He starts crying here
    NO "T-that’s a lot of blood.."
    NO "H-hey, did you get sick of me already..?"
    NO "I..I thought y-you wouldn’t do that to me.."
    NO "D..do you really not care anymore? P-please..tell me.."
    NO "Why won’t you wake up..?! Pl–please help me.."
    #if possible edit blurred voices
    "..."

    scene bedroomday with fade
    #bgm: https://dova-s.jp/EN/bgm/play22000.html

    #bird sfx
    "..."
    "(That was strange..)"
    "(Why does my head hurt so much?)"
    #wood sfx
    "I stumble out of bed, squinting and frowning at the bright sun shining right in my face. While I never expected to wake up feeling refreshed, things like this make mornings feel worse."
    "(I should get some curtains)"
    #door sfx
    show y happy
    "Y Morning sleepyhead! You up yet?"
    show y smile
    "(Who..?)"
    "A blonde woman I don’t recognize beams cheerfully at me, smiling like she’s ready to outrun a horse."
    show y happy at left
    show b normal at right
    B "Don’t shout so loudly, it’s still morning."
    show b silent
    "To contrast, the next woman who entered is seemingly calm or maybe..tired? Whatever the right word is, she’s much more subdued."
    "(Who are these people?)"
    show y grumpy
    Y "Yea yea. Who cares? It’s not like we have any neighbors."
    show b normal
    B "Still, I’d like it if you’d be a bit more mindful."
    menu: 
            "Excuse me, who are you two?":
                show y grumpy:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                Y "Oh come on!"
                show b happy
                B "See, even a certain someone is embarrassed by your antics."
                "(Am I supposed to know these people?)"
                show b normal
                B "Why are you frowning like that?"
                Y "Don’t tell me.."
                B "That question was genuine?"
                show y grumpy:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                show b silent
                Y "WHAT?!"
                Y "Nonono, say that again!"
                show b normal
                B "We’re your sisters. Do you.. not remember us?"
                Y "Oh no."
                B "Do you even remember your name? Or who you are?"
                $ mc = renpy.input ("What’s my name?")
                MC "I’m..[mc]?"
                show b happy
                B "Oh thank goodness you at least remembered your name."
                show b silent
                MC "And I’m.."
                menu:
                            "A woman?":
                                $ player_gender = "she"
                                $ player_possessive = "her"
                                $ player_object = "her"
                                $ player_pronoun = "girlfriend"
                                $ player_sb =  "is"
                                $ player_sbn = "isn’t"
                                $ player_ds =  "woman"
                                $ player_fm =  "sister"
                            "A man?":
                                $ player_gender = "he"
                                $ player_possessive = "his"
                                $ player_object = "him"
                                $ player_pronoun = "boyfriend"
                                $ player_sb =  "is"
                                $ player_sbn =" isn’t"
                                $ player_ds =  "man"
                                $ player_fm =  "brother"
                            "Neither a man nor a woman?":
                                $ player_gender = "they"
                                $ player_possessive = "their"
                                $ player_object = "them"
                                $ player_pronoun = "partner"
                                $ player_sb =  "are"
                                $ player_sbn = "aren’t"
                                $ player_ds =  "person"
                                $ player_fm =  "sibling"
                
                show y happy:
                        linear 0.050 yoffset +10
                        linear 0.050 yoffset -10
                Y "Yep! That’s what you are!"
                show b happy
                B "Well, I’m glad you didn’t lose {i}all{/i} your memories."
            "(I should shut up)":
                show y happy
                Y "By the way, you’re being awfully quiet today. What’s up?"
                show b happy
                show y smile
                B "Did you have a nightmare last night?"
                show b silent
                "(Who are these people??)"
                show y grumpy:
                                linear 0.050 yoffset +10
                                linear 0.050 yoffset -10
                Y "Woa, you don’t have to back away from us like we’re strangers!"
                show b normal
                B "Actually, you’re staring at us like we are."
                #sprite moves closer to eachother
                show y grumpy:
                        parallel:
                            ease .5 zoom 1.0
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.35
                show b normal:
                        parallel:
                            ease .5 zoom 1.0
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.65
                "(What are they whispering about..?)"
                #Y jumps back to earlier position
                show y grumpy at left with vpunch
                show b silent
                Y "No way! Really?!"
                show b normal
                B "Could it be? You lost your memories?"
                "(!!)"
                B "Do you at least remember your name?"
                show b silent
                $ mc = renpy.input ("What’s my name?")
                MC "I’m..[mc]?"
                show b happy
                B "Oh thank goodness you at least remembered your name."
                MC "And I’m.."
                menu:
                        "A woman?":
                                $ player_gender = "she"
                                $ player_possessive = "her"
                                $ player_object = "her"
                                $ player_pronoun = "girlfriend"
                                $ player_sb =  "is"
                                $ player_sbn = "isn’t"
                                $ player_ds =  "woman"
                                $ player_fm =  "sister"
                        "A man?":
                                $ player_gender = "he"
                                $ player_possessive = "his"
                                $ player_object = "him"
                                $ player_pronoun = "boyfriend"
                                $ player_sb =  "is"
                                $ player_sbn = "isn’t"
                                $ player_ds =  "man"
                                $ player_fm =  "brother"
                        "Neither a man nor a woman?":
                                $ player_gender = "they"
                                $ player_possessive = "their"
                                $ player_object = "them"
                                $ player_pronoun = "partner"
                                $ player_sb =  "are"
                                $ player_sbn = "aren’t"
                                $ player_ds = "person"
                                $ player_fm =  "sibling"
                show y happy
                Y "Yep! That’s what you’ve always told us."
                show b happy
                B "Just so we can be reacquainted, we’re your sisters."
                show b silent
                Y "You better not forget us again!"

    MC "Still though if you were my sisters, why do I not remember you?"
    show y grumpy:
                linear 0.050 yoffset +10
                linear 0.050 yoffset -10
    Y "That’s what we’d like to know!"
    show b normal
    B "In all honesty, there have been some mysterious cases going around the surrounding villages.."
    B "Perhaps [player_possessive] sudden memory loss is related to it?"
    show b silent
    MC "(Well that sounds like a convenient explanation.)"
    Y "Aw man..That blows."
    show y happy
    Y "Anyway, we should go downstairs. I bet dad’s waiting for us to have breakfast with him."
    show y smile
    MC "(So I have a dad.)"
    show b normal
    B "Guessing from your expression, do you not remember him too?"
    menu:
        "Yea, I don’t remember him at all.":
            jump next1
        
        "I guess there’s bits and pieces?":
            jump next1

label next1:
    B "That’s alright, maybe having breakfast would jog your memory."
    MC "I sure hope so."

    scene kitchen with fade
    "They held my hands as they led me into the halls and down the stairs, eventually stopping at a kitchen."
    "There sat a bearded man at the table, his blank expression shifting into a smile as he saw us enter."
    show y happy:
                linear 0.050 yoffset +10
                linear 0.050 yoffset -10

    Y "Morning, dad!"
    show y smile at left
    show b happy at right
    B "Good morning father."
    show d happy
    D "Good morning you two."
    show d normal
    MC "(Uh oh, he’s staring at me.)"
    menu: 
            "Morning!":
                D "Chipper as always I see."
            "Good morning.":
                D "Oh? Taking after your older sister today?"
            "(HELP.)":
                #B closer
                scene b happy:
                    parallel:
                        ease .5 zoom 1.7
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.0 xalign 0.0
                B "{size=-10} Stay calm, just greet him as cheerfully as you can{/size}"
                MC "{size=-10} Alright{/size}"
                #sprite back
                scene b silent:
                    parallel:
                        ease .5 zoom 1.0
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.0 xalign 0.0
                D "Is anything wrong, [mc]?"
                MC "Nope, I'm good. Good Morning Dad!"

    MC "(So this is my father.)"
    show d happy
    D "Eat up [mc], I’ll bring back some more bread tonight."
    show d normal
    Y "And meat!"
    show d happy
    D "Yes, we’ll bring back some meat."
    show d normal
    show y happy:
                linear 0.050 yoffset +10
                linear 0.050 yoffset -10

    Y "WOO!"
    show b normal
    B "Careful, you’ll get your new clothes dirty."
    Y "They’re clothes. "
    extend "They’re meant to get dirty."
    #ini pk  https://www.youtube.com/watch?v=TsOM4gmW_As

    Y "Shame the fair’s already over. I wanted to ask for more things."
    show y smile
    show b happy
    B "We’ve asked for plenty."
    show b silent
    show d happy
    D "Not [mc] though, I feel a little guilty I couldn’t bring back more. Not to mention it took so long to even find it."
    D "Are you sure you were alright with what I got you?"
    show d normal
    MC "(What did I ask for??)"
    MC "Of course I’m alright."
    MC "(I DON’T KNOW)"
    B "Father, I think we’ve spoken enough about the fair these past few days."
    MC "(Wait, I want to know more about the fair.)"
    show d happy
    D "Really? But-"
    show d normal
    Y "Dad, I’m done eating! Can we go out now?"
    show d happy
    D "Very well."
    show d normal
    "Once she dragged the bearded man out the door, she waves her hands wildly back at me. "
    Y "Bye, [mc]! We’ll be back before the sun sets!"
    B "Stay safe out there!"
    show d happy
    D "We will."
    #door close

    MC "(Now it’s just me and her.)"
    B "Now [mc], shall we clean the table?"
    MC "Sure?"

    scene kitchen with fade
    #water sfx
    MC "So, what was the fair like?"
    show b silent
    "She pauses her movements for a brief moment, barely stopping herself from sighing before continuing to scrub the plates with more fury than before."
    show b normal
    B "Oh you wouldn’t want to hear about it again. We’ve spoken far too many times about it."
    MC "But I don’t remember any of it."
    B "[mc], it has been months since the fair ended. I believe we should let the topic pass."
    show b silent
    MC "Please? It might jog my memory."
    "While I try my best at a pitiful expression, it seems to have no effect as she responds with as neutral an expression as possible."
    show b normal
    B "Maybe some other time."
    show b silent
    MC "(Somethings not right here.)"
    menu:
            "(I’ll drop the topic so I can investigate without her feeling suspicious)":
                MC "(Even if I ask, can I even trust her words?)"
            "Why won’t you tell me?":
                show b normal
                B "[mc], please wash the dishes correctly."
                MC "(Fine then, keep your secrets. I’ll find out for myself!)"

    scene kitchen with fade
    show b happy
    B "Thank you for helping me clean up, [mc]."
    MC "Sure thing."
    B "Are you feeling alright?"
    MC "Who knows."
    extend "I think I’m fine but my head’s a little foggy?"
    show b normal
    B "Oh dear."
    B "Maybe it’d be best if I took over your chores for the day."
    show b silent
    MC "I have chores?"
    MC "(Wait that was really stupid.)"
    show b normal
    B "We all do. But given your current state you’re better off resting."
    MC "Shouldn’t I move around so I can start remembering things?"
    show b happy
    B "That can wait until tomorrow, I’m worried."
    MC "Alright then, I’ll return back to my room."
    menu:
            "(If she really is my sister, I’m glad I have her to care about me.)":
                jump next2

            "(I don’t trust her one bit, something’s off.)":
                jump next2

label next2:
    scene bedroomday with fade
    MC "(So this is my room.)"
    "I didn’t have time to take a good look earlier but it’s kinda..bare?"
    "I don’t know what I was like before I lost my memory but I certainly would prefer a room with more personality."
    "Well, I can always decorate."
    MC "(I’m back in my room but am I really gonna rest?)"
    menu: 
            "(Obviously not! I’m gonna search the room for hints.)":
                    MC "(Starting here!)"
                    #fabric noise
                    show mc fehand
                    MC "(?)"
                    MC "(This feather..)"
            "(Uhh..Maybe I should rest, just for a bit)":
                    MC "(Hm?)"
                    show mc fehand
                    "(What’s this feather doing here?)"

    scene cg1d with fade
    pause 2
    scene bedroomday with fade
    MC "(I’ve seen this thing before!)"
    MC "(It wasn’t just a dream.)"
    scene kitchennight with fade
    show d happy
    D "[mc]? What were you doing outside? It’s dangerous out there."
    show d normal
    MC "Sorry, I was out for a stroll."
    MC "But look! I found this feather, isn’t it pretty?"
    show d happy
    D "Yes, it is, [mc]."
    MC "You don’t mind if I decorate my bedroom window with it, right dad?"
    D "Do as you like."

    scene kitchen with fade
    show d happy
    D "Settle down, I’m going to the fair today. Is there anything you’d like?"
    show d normal
    show y happy at left:
                linear 0.050 yoffset +10
                linear 0.050 yoffset -10

    Y "Ooh! Ooh! I want new boots! Something that’ll really hold up when we’re hiking."
    show y smile
    show b happy at right
    B "I’d like a shawl if it isn’t too much."
    show b silent
    show d happy
    D "Very well. "
    D "What about you, [mc]?"
    MC "I want a feather just like this one."
    D "A feather? Are you sure? Why not boots or a coat?"
    show d normal
    MC "I’m sure. It’s so pretty I could spend a whole day staring at it! "
    show b happy
    B "[mc], we love you and all. But don’t you think you’re better off asking for a new cloak?"
    show y happy
    Y "For once I agree, don’t you want something to help survive the winter?"
    MC "I guess I won’t be going out this winter. I want this feather!"
    show d happy
    D "Well, if that’s what you want then I’ll try my best."

    scene bedroomday with vpunch
    #fallonwood sfx
    MC "(!!!)"
    MC "(Was that...my memory?)"
    show mc fehand
    "With the feather right in my hands, I observe the way its colors seemingly shift as I hold it against the window."
    "Sometimes it’s seemingly a metallic blue-ish hue, while at other times it appears as a shiny green."
    MC "(It’s beautiful that’s for sure.)"
    MC "(But why is it underneath the covers? Did a bird perch on my window and shedded a feather?)"
    MC "(Whatever, I wanna hang this on my window!)"
    hide mc
    scene bedroomday:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5

    #thump, zoom bg
    MC "(Oh? That’s strange. There’s already a hook for me to hang it.)"
    MC "(I guess I don’t change much.)"
    #door
    show b normal
    B "[mc]?!"
    scene bedroomday with vpunch
    show b silent
    MC "(!!)"
    MC "I’m not doing anything!"
    show b normal
    B "[mc], get down from there. What if you fall?"
    MC "Sorry?"
    B "For goodness sake, this is the second floor. What were you even doing?"
    show b silent
    MC "Sorry, I just wanted to decorate my window."
    MC "Look at what I found! Isn’t it pretty?"
    show b normal
    B "{b}Where did you get that?{/b}"
    show b silent
    MC "(Uh oh.)"
    "Her mood shifted from concern to anger in a second as she took a step closer to me, slowly closing the distance between us."
    show b normal
    B "Throw it away, [mc]."
    MC "I don’t want to. I like it!"
    B "Well, I {b}don’t{/b}."
    MC "It’s not your room, it’s mine. I can decorate it as I like."
    show b normal with vpunch
    B "Why won’t you listen?!"
    MC "Why should I?"
    show b normal with vpunch
    B "Just listen to me!"
    show b silent
    B "..."
    show b normal
    B "No. You know what. Keep it. But don’t ask for more and don’t hang it on the window."
    MC "Why?"
    B "You lost your memory so you probably don’t remember but that thing attracts monsters."
    menu:
            "That sounds really fake":
                show b normal with vpunch
                B "It’s real!"
                B "If you hang that thing, it will make you a target."
                MC "Target for what?"
                B "Who knows, one of these days you could be stolen away into the woods."
                B "You may feel safe now while it’s day time but just wait till the night comes."
                MC "Okay?"
            "Monsters???":
                B "Scared? I am too."
                B "It will approach you if it sees you with its feather."
                MC "What if I want it to approach me? The monster sounds pretty-"
                show b normal with vpunch
                B "NO DON’T"
                B "Just..listen to me. Alright? I want you safe."

    B "You should rest."
    MC "I’m not tired."
    B "{b}Rest.{/b}"
    "Swiftly, she tucks me into bed, closes the window and places her hand onto my forehead."
    B "You don’t have a fever, do you?"
    MC "Not that I know of?"
    B "Sleep."
    MC "Don’t want to."
    B "Are you sure about that?"
    B "As your eldest sister, I know best. Now close your eyes."
    MC "(Are you really?)"
    MC "(I’m not sure who to trust here.)"

    scene black with fade
    B "That’s right, rest your eyes. Take a nap."
    MC "(Don’t..wanna...)"
    B "Rest well, [mc].."
    MC "(Rest...?)"
    "..."
    "..."
    #wind blows
    MC "(It’s quiet all of of a sudden.)"
    #creak
    MC "(What was that?)"
    scene bedroomnight3 with fade
    MC "Hello? Who’s there?"
    scene bedroomnight3:
        parallel:
            ease .5 zoom 2.0
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.1
    pause 1.5
    scene bedroomnight3 with fade:
        parallel:
            ease .5 zoom 2.0
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.8
    pause 1.5
    scene bedroomnight3 with fade

    #bg moves left to right before back to normal
    #swoosh
    MC "(Where is that noise coming from?)"
    #swooshcreak
    MC "(There!)"
    #tackle
    scene surprisedtacklecg with vpunch
    #bgm: https://dova-s.jp/EN/bgm/play19295.html

    NO "Ack! Mercy! Mercy!"
    scene tacklecg
    "Taking a few moments to calm myself, I finally took a good look at the person I tackled to the floor."
    "His mask may hide his expression but it can’t hide his rapid breathing or the way his body shakes under me."
    "For someone I assume to be a burglar, he doesn’t seem any good at it. "
    MC "Who are you? What do you want?!"
    NO "I’m not a strange person I swear!"
    MC "What are you doing in my room? How did you get in?"
    scene surprisedtacklecg
    NO "Ow! C-can you remove your hands first..?"
    scene tacklecg
    MC "{b}No{/b}"
    NO "A-alright! I understand. I’ll explain myself.."
    MC "So, who are you?"
    BM "Oh! Um…You can call me Howard. If you don’t mind?"
    BM "N-not that you would mind over something as trivial as this but..uh.."
    BM "Nevermind.."
    MC "Alright, {i}Howard.{/i}"
    extend "What are you doing in {b}my{/b} room?"
    scene surprisedtacklecg
    BM "I’m not doing anything nefarious here, I swear!"
    scene tacklecg
    BM "I saw the decorations on your window and I wanted to take a closer look."
    MC "Why?"
    BM "I’m not telling!"
    MC "Is that so?"
    show mc knife
    #Sfx, knife asset
    MC "How about now?"
    scene surprisedtacklecg with vpunch
    BM "Eek!! Alright, alright I’ll talk!!"
    hide mc knife
    #put away
    BM "Can I..ask you something first..?"
    menu:
            "Sure. Ask away.":
                BM "Thank you."
            "No. I’m doing all the asking here.":
                BM "Please? My answer will depend on this."
                MC "Hmm.."
                BM "Please..? I swear I won’t ask about anything else after this.."
                MC "Somehow I doubt that."
                BM "No I’m serious! Really!"
                MC "Hmm..Fine. Just one."
                BM "Thank you!"

    BM "So umm..why did you hang those feathers on your window?"
    BM "Don’t get me wrong, I think you did a wonderful job decorating!"
    #extend I-i just…wanted to know why you used those feathers specifically.
    BM "I’m sure there are plenty of other things you could’ve used..?"
    MC "Man, you’re a weirdo."
    MC "You broke into my room for those?"
    BM "I wasn’t gonna do anything! I just wanted to see!"
    MC "Well, I kinda get it. Those feathers are really pretty aren’t they?"
    scene btacklecg
    BM "You think they’re pretty?"
    MC "Well obviously, I have eyes and good taste."
    BM "So you really think they’re pretty?"
    MC "Yes I do. Do I need to repeat myself again?"
    BM "Umm..Maybe?"
    #knife asset, sfx
    scene surprisedtacklecg with vpunch
    show mc knife
    BM "Ack! I’m sorry! I won’t do that again!"
    scene tacklecg
    BM "But also.."
    BM "What if I tell you that those feathers come from a monster? Would you still think they're pretty?"
    menu:
            "I thought I made it clear that you only get one question.":
                BM "Sorry! I phrased it wrong! I just.. wanted to tell you that they do in fact, come from a monster."
                MC "Uh huh, sure thing."
                BM "I’m serious!"
                MC "Go on then."
                extend "What does it look like?"
                BM "Well..."

            "Do they? Tell me more.":
                BM "It’s been a local legend for.."
                extend "umm.."
                BM "I’m not actually sure, but it sure has been a while."
                BM "But haven’t you heard about it?"

    BM "It looks like a bird but with hands..? Kinda like a bat if it has feathers?"
    MC "Interesting, I’ve never heard of it."
    BM "It has claws and stuff..? Really sharp ones."
    MC "And..where is this monster? I want to meet it."
    BM "{size=-10} You’re on top of it..{/size}"
    MC "What was that? Speak up."
    BM "Nothing!"
    BM "It..umm..lives at the edge of the world… in a cage."
    MC "Cool, I’ve decided that you’re a total weirdo."
    BM "I’m not! I swear!"
    MC "You admitted to me that you broke into my room just to see the window decorations."
    MC "You’re insane. I live on the second floor."
    BM "Well it wasn’t that hard to-"
    #knife
    scene surprisedtacklecg with vpunch
    show mc knife
    BM "Alright, alright! I’m sorry for breaking in!" 
    scene tacklecg
    show mc knife
    BM "I-it wasn’t {i}just{/i} for the decorations."
    MC "If you’re looking for money you came to the wrong house."
    BM "It’s not the money!"
    BM "I..I..also wanted to meet the person behind the decorations."

    hide mc
    MC "Me?"
    BM "Y..yea.."
    #knock
    B "[mc]?"
    MC "My sister’s here. You have to hide!"
    BM "Huh?"
    MC "Now! Hurry!"

    scene bedroomnight3 with fade
    #feather, window sfx
    MC "Yes? What’s wrong?"
    B "I heard a noise coming from your room. Is everything alright?"
    MC "I’m fine?"
    B "Are you sure? I’m fairly certain I heard something."
    MC "Oh, I just fell off the bed earlier."
    B "Did you scrape your knee? Any bruises?"
    MC "Stop worrying, I’m fine."
    B "If you say so. Goodnight, [mc]."
    MC "Yea good night."
    #door close
    "..."
    MC "She’s gone, you can come out now."
    "..."
    MC "(He’s gone.)"
    "..."
    MC "(Oh?)"
    show mc fehand
    MC "(I guess one of those feathers fell off the window.)"
    hide mc fehand
    MC "(I’m missing the one over...)"
    MC "(Wait, they’re all intact.)"
    scene black with fade
    centered "Where did this come from?"
    "Was that a dream? Or was it a forgotten memory?"
    "Howard, who was he?"

    #zooming back to reality, door slam
    scene bedroomday with vpunch
    show y happy
    Y "[mc]! We’re back!"
    MC "(???)"
    Y "Really, you gotta stop sleeping the day away. You’re not an owl."
    Y "You used to sleep normally like the rest of us!"
    show y smile
    MC "Well it’s not my fault. I was told-"
    show y happy
    Y "Ah, got it. Say no more! "
    Y "I bet she told you to take a nap, didn’t she?"
    MC "Yea."
    Y "Anyway, it’s time for dinner!"
    MC "Dinner?"
    show y happy
    Y "Yea, look outside."
    show y smile
    MC "(It really is night.)"
    MC "How did I miss the entire day?"
    show y happy
    Y "Don’t worry about it too much. Happens to the best of us."
    Y "Come on, let’s head down. We’re eating stew tonight!"
    MC "Okay?
    "
    scene kitchen with fade
    show y happy
    Y "Time for dinner everyone! [mc]’s up!"
    #plate sfx.
    show d happy at right
    show y smile at left
    D "Are you feeling alright [mc]? I was told you slept the whole day."
    show d normal at right
    MC "I’m fine. Although, a certain{i}someone{/i} insisted that I rest."
    show b silent 
    "She returns my glare and pointed tone, unimpressed that I singled her out during dinner."
    show b normal
    B "It’s for your own good, [mc]."
    menu:
            "I appreciate it.":
                show y happy
                Y "You should tell her if you’re upset, [mc]. I’d be mad if I was stuck in bed the whole day."
            "(Oh is it? Or is it for some other mysterious reason I’m not told about?)":
                show y happy
                Y "Woa, that’s an intense glare [mc]. Are you that hungry?"

    MC "We should eat."
    Y "No kidding, I’m starving!"
    B "Please chew your food properly."
    show b silent
    show y grumpy
    Y "Whatever."
    Y "I gotta be ready to head back out later."
    show y smile
    MC "Why? It’s dark out."
    show d happy
    D "Oh [mc], it’s like you’ve forgotten about the night patrol."
    MC "Night patrol?"
    D "Your sisters and I will be out tonight to patrol the village for the next 3 nights or so."
    D "As we have been doing for the past few months."
    show d normal
    MC "Why can’t I go?"
    show b normal
    B "It’s dangerous, you can’t go."
    show b silent
    show y grumpy
    Y "Stop lying, [player_gender] can’t go because [player_possessive] boots are all torn and [player_possessive] coat isn’t thick enough."
    #stomp
    show y grumpy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Ow! Come on, what did I say?"
    show b normal
    B "{size=-10} Keep your mouth shut.{/size}"
    show b silent
    MC "(As much as I think they’re keeping secrets from me, they’re not very good at hiding them are they?)"
    MC "(Now I just need to figure out what those secrets are)"
    show y grumpy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "I’m not wrong!"
    MC "Why am I the only one without proper clothes?"
    show d happy
    D "[mc]... I tried telling you this during the fair, remember?"
    D "I asked if you wanted a coat or new boots and you said that you wanted a feather instead."
    show d normal
    MC "(Curse you past me!)"
    MC "(But also..it was really pretty. Maybe it was worth it?)"
    Y "I tried telling you that it wasn’t gonna be useful."
    #stompsfx
    show y grumpy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Ow! What did I say this time?"
    show b normal
    B "In any case, it’d be best if [mc] guarded the house while we’re away."
    show b silent
    show d happy
    D "I agree, I believe the intruder would be far more scared of [mc] than the other way around."
    show d normal
    show y happy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "That’s right! Nothing can beat my little [player_fm]!"
    show y smile
    B "Still, you need to be careful [mc]. Don’t let anyone inside the house."
    MC "I won’t."
    show b happy
    B "We’ll be on our way now. Take care."
    show y happy
    show b silent
    Y "Sorry you have to clean after us [mc]. I’ll be on duty in a few days so don’t worry!"
    MC "It’s fine, I haven’t done any chores today."
    Y "You’re kidding. "
    show y grumpy
    Y "Hey, you can’t make [player_object] rest all day. Physical movement is necessary to help [player_object] remember things."
    #stomp
    show y grumpy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Watch it! Are we gonna have a prob-"
    show b normal
    B "{b}We will talk outside.{/b}"
    show b silent
    show d happy
    D "Sorry for leaving you, [mc]. Stay safe."
    show d normal
    MC "I will."
    scene kitchen with fade
    #doorclose
    MC "(Time to clean up.)"
    #platesfx
    scene kitchen with fade
    MC "(I’m home alone.)"
    "..."
    MC "(I’m home alone!!)"
    MC "(Time to sneak around the house to find things that will jog my memory!)"

    scene bedroomnight with fade
    MC "(And we’ll start here!)"
    MC "(My bedroom seems to be the entry point for that masked man to enter the house)"
    MC "(Maybe if I find more feathers I’d remember more..?)"
    MC "(Where do I start?)"
    jump bedroomsearch

label bedroomsearch:
    scene bedroomnight with fade
    #pokoknya ini nge-loop kyk pas milih sayur di rute tsm atau kita tes yg bg bisa diklik
    # kalau bisa yg diklik yg diklik aja

    menu: 
            #menu 1
            "The bed, it’s gotta be there. It’s closest to the window.":
                scene bedroomnight:
                    parallel:
                        ease .5 zoom 2.0
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.5 xalign 0.5
                #zoom
                MC "(I checked under the covers earlier, what about under the pillow though?)"
                #sfx
                MC "(Ah! There is one!)"
                MC "(Why would it be here though?)"

                scene black with fade
                "..."
                #window sfx, knock
                BM "Hello? "
                BM "It’s me... Howard? If you even remember me..?"
                BM "Psst, can you open the window? "
                #knock
                scene night with fade
                show bm surprised:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                show window
                MC "You!"
                show bm idia
                MC "The one from yesterday!"
                BM "Umm...I’m sorry about that?"
                BM "But also.. You shouldn’t be too loud. I thought you didn't want that woman from yesterday to find out, right [mc]?"
                MC "I didn’t tell you my name."
                show bm explanation
                BM "D-did I get it right? That’s what that woman from yesterday called you."
                MC "Right, my sister."
                MC "How did you disappear so quickly yesterday?"
                show bm finger
                BM "Can you please let me in now?"
                MC "No."
                show bm idia
                show fx sweat
                BM "Please? Talking to you would be much nicer if I’m not perching on the side of a roof?"
                hide fx
                MC "You’re a suspicious stranger. How do I know you won’t do anything?"
                show bm idia:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                BM "I won’t touch you by a hair, I swear!"
                MC "I can’t be sure of that."
                show bm explanation
                BM "What do I need to do to convince you I won’t do anything?"
                MC "I’ve got an idea."
                show bm surprised:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                BM "Eek! Can you drop the knife? "
                MC "No."
                show bm idia
                BM "W-what are you gonna do?"
                MC "Why do you seem even more scared than I am? {i}You’re{/i} the intruder here."
                show bm finger
                BM "Your knife looks very sharp."
                MC "Your gloves look really sharp and you’re not putting them away. Are you in any position to complain about this little thing?"
                show bm swpose
                BM "Very well, do as you please."
                BM "J-just..don’t hurt me, please?"
                MC "Depends, will you attack me?"
                show bm idia
                BM "I won’t!"
                MC "Alright, don’t make me regret this."
                #window open, thump
                scene bedroomnight3 with fade
                show bm swpose
                BM "Thank you for letting me in."
                MC "Now, lie down on the bed."
                BM "Pardon?"
                MC "Stick your hands up, I’m gonna tie them to the bed post with my scarf."
                show fx sweat2
                BM "I-is this really necessary..?"
                hide fx
                MC "If you don’t want to, you can always get out of my room? The window’s still open."
                BM "I’ll do it."

                scene tiedupcg
                MC "And done!"
                BM "I fail to see how this would make you safe. This scarf is already torn and you didn’t tie it very tightly."
                BM "I can break out of this fairly easily."
                MC "That’s the point."
                MC "If you try to break out of it, I’ll take it as a sign of attack."
                MC "You’ll have to {i}try{/i} to stay restrained."
                BM "May I ask why I must be on the bed?"
                MC "If you’re lying down it takes you longer to get up and lunge at me."
                BM "I won’t do that.."
                MC "Well I can’t be sure of that yet."
                MC "Anyway, state your business! Why are you here again?"
                BM "I-I uh.."
                MC "Speak."
                BM "I-I wanted to see you."
                MC "Why? Did you like being held at knife point?"
                BM "Y-ye..
                scene tiedupcg with vpunch
                extend I mean NO! NO I don’t!"
                BM "I-I wanted to ask for your opinions on the monster?"
                MC "Again, why?"
                BM "Please? Just tell me?"
                MC "I’m taking off your mask. I need to see who I’m dealing with."
                BM "N-no please? Please let me keep it on..!"
                #rip
                BM "Wai-"
                BM "Oh.."
                MC "Exactly, try to stay restrained."
                BM "Promise you won’t be mean?"
                menu:
                        "Fine, I promise I won’t be mean.":
                            BM "Thank you."
                            MC "You really shouldn’t thank me for the bare minimum."
                            BM "But still, you’re much nicer than everyone else I’ve met."
                            MC "I’m sorry to hear that."
                        " A bit too late for that.":
                            BM "[mc].."
                            MC "Relax, I’m not gonna heckle you or anything."
                            MC "I’m not much of a looker myself."
                            BM T"hat’s not true.."
                        #maskoffcg
                scene tiedupscaredcg with fade
                MC "..."
                BM "[mc], w-why are you quiet? Please don’t stare at me too much."
                MC "Honestly, I don’t see the issue."
                scene sdtiedupcg 
                BM "Y-you’re lying!"
                MC "I’m not! "
                MC "You look like fairy tale royalty! I was expecting an actual monster face!"
                scene tiedupworrycg
                BM "But, I am a monster?"
                MC "(Uhhh, is he seeing something that I’m not seeing?)"
                MC "(If this guy is a monster then what am I? I’m starting to feel really bad about tying him to my bedpost.)"
                MC "A monster? Are you... cursed or something?"
                scene tiedupworrycg with vpunch
                BM "How did you know?!"
                MC "I was joking. You really think you’re cursed?"
                scene tiedupinquirecg
                BM "Y-yes?"
                MC "Okay, so what’s the curse about?"
                scene sdtiedupcg
                BM "I don’t want to say.."
                MC "Don’t? Or can’t say?"
                scene tiedupinquirecg
                BM "Both?"
                MC "Can I assume that you’re cursed to become a monster of some kind?"
                scene sdtiedupcg
                BM "{size=-10}Already am one{/size}"
                MC "Hey, don’t hide your face! If you keep moving you might tear my scarf and I’ll have to fix it."
                scene tiedupscaredcg
                BM "Sorry!"
                BM "I-I just feel antsy without that mask.."
                scene tiedupinquirecg
                BM "But I’m safe here right? I don’t see any other houses nearby and no one else can see me?"
                MC "Yea? If you don’t count my sisters and my dad."
                BM "Y-you’ll hide me from them, right? Like you did yesterday?"
                MC "I guess? I wouldn’t want them to see me with a stranger in my room either."
                BM "Anyway, I came to ask for your opinion on the monster? Please?"
                MC "Well, I’ve never heard of it. But I do remember getting that first feather from a bird while I was out for a stroll."
                MC "If that bird was a monster, I remember it being beautiful?"
                MC "It didn’t attack me when I saw either so I don’t think it’s very aggressive?"
                MC "It’s not much of a monster is it?"
                scene tiedupworrycg
                BM "But it can transform!"
                MC "Into what?"
                BM "A scarier version!"
                MC "Howard, you’re not making it sound very scary."
                MC "I get that birds can be terrifying but you don’t have to call it a monster."
                scene tiedupinquirecg
                BM "But it can shapeshift?"
                MC "Into a “scarier version”? Isn’t that called “turning into an adult”?"
                scene tiedupworrycg
                BM "No no no, it can turn into a human!"
                menu:
                        "Well if it turns out as pretty as you are then I have no issues with it.":
                            scene tiedupsurprisedcg with vpunch
                            BM "(!!)"
                            scene tiedupscaredcg
                            BM "H-hey..You can’t just say things like that.."
                            MC "Why not?"
                            BM "W-what if it does anything to you?"
                            MC "Like?"
                            scene sdtiedupcg
                            BM "Uh..Scratch you? I-i don’t know but it could be dangerous."
                        "Does it kill people?":
                            scene tiedupworrycg with vpunch
                            BM "NO! I would never!"
                            MC "{i}I?{/i}"
                            scene sdtiedupcg
                            BM "Nothing!"
                            BM "I’m just saying it would never kill anyone, or not on purpose at least.."
                MC "You sure know a lot about this monster. Is it your friend or something?"
                #footsteps
                MC "Someone’s coming, I’ll let you go now!"
                scene tiedupscaredcg
                BM "W-who?"
                MC "Under the covers, now!"
                BM "W-wait! I have a better way."
                MC "What?"
                BM "Close your eyes"
                scene black with fade
                #sfx
                scene bedroomnight with fade
                MC "Howard?"
                show bm bird
                BM "Yea?"
                scene bedroomnight with vpunch
                MC "(!!!)"
                MC "(The bird can talk!!!)"
                show fx sweat2
                BM "NO no no, don’t be scared please? I-it’s just me..? Howard?"
                BM "P-please don’t hurt me!"
                hide fx
                MC "You’re a bird?!"
                BM "Monster but-"
                #footsteps
                MC "Woops, no time for that! Hurry!"
                #sfx
                BM "Can I visit you tomorrow night?"
                MC "Whatever, just hurry!"
                MC "Oh, and be careful!"
                show bm bird:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                BM "I will!"
                scene black with fade
                "And with that, he flew into the darkness of the night."

            #menu 2
            "My wardrobe has to have something, right?":
                scene bedroomnight:
                            parallel:
                                ease .5 zoom 1.3
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.0 xalign 0.3
                #sfx
                MC "(I don’t have a lot of clothes in here do I?)"
                #fabric
                MC "(I’ve got one set for daily wear and another for night)"
                MC "(I can’t say I’m well equipped to go out. I don’t even have a cloak.)"
                #fabric
                MC "(Do I even have a hat?)"
                MC "(?)"
                MC "(A feather..)"

                scene kitchennight with fade
                show b normal
                B "Are you sure you’re alright?"
                MC "Positive."
                show b happy
                B "Very well, we’ll be off now."
                show b silent at right
                show y happy at left
                Y "Bye, [mc]!"
                hide b
                hide y
                MC "Bye!"
                MC "(They’re gone.)"
                #stepssfx
                scene bedroomnight3 with fade
                MC "You can come out now."
                MC "Howard?"
                #wardrobeopensfx
                show bm explanation
                BM "Here!"
                BM "You don’t have a lot of clothes in there do you?"
                BM "I can’t even find a coat."
                MC "That’s half your fault y’know."
                show bm surprised
                BM "Me?! What did I do?"
                MC "If I wasn’t so entranced by those feathers of yours I would’ve asked my dad for clothes instead."
                show bm swpose
                BM "How is that my fault?"
                menu: 
                        "You’re too beautiful. You’ve led my decision making astray.":
                            show fx blush
                            MC "What are you gonna do about it?"
                            BM "I-I don’t know… What do you want me to do..? Buy you a coat?"
                            
                            BM "I-I can’t really do much.."
                            MC "I was thinking you could take responsibility and marry me but that works too."
                            hide fx
                            show bm surprised:
                                        linear 0.050 yoffset +10
                                        linear 0.050 yoffset -10
                            BM "M-m-marry you??"
                            show fx blush
                            show bm swpose
                            BM "I-uh..I.."
                            MC "Don’t want to?" 
                            show bm idia
                            BM "No that’s not it..! But I..uh.."
                            MC "Relax, I’m kidding. It’s all because of my poor decision making anyway."
                        "It isn’t, I’m just joking.":
                            BM "Thanks goodness."
                            BM "Still.."
                            show fx blush
                            extend "It’s nice to know that you view my appearance favorably."
                            MC "Who wouldn’t?"
                            BM "Lot’s of people. Me included."
                            MC "Well they have horrific taste,"
                            extend "you included."
                            BM "[mc]..."
                            MC "I think you’re lovely."

                hide fx
                MC "But really, you have to stop coming here. They’re gonna find out eventually."
                show bm finger
                show fx huffy
                BM "But [mc]..."
                MC "Really Howard?"
                MC "If you’re making a pitiful expression, just know that I can’t see it under the mask."
                show bm explanation
                BM "Curses."
                MC "If you want to pout at me all you like, you’ll have to take off your mask so I can actually see it."
                BM "Hmph."
                hide fx
                show bm swpose
                BM "I don’t want to leave."
                MC "Why? Did you fall in love with me?"
                show bm idia:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                BM "N-no..! I didn’t!"
                show fx blush
                extend "{size=-10}Or.. Maybe I did..?{/size}"
                MC "Well?"
                show bm swpose
                BM "Please don’t come closer..!! Seriously, you’ll give me a heart attack..."
                MC "Sorry."
            
            #menu 3
            "That chest over there, what did I store in it?":
                scene bedroomnight:
                        parallel:
                            ease .5 zoom 1.75
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.8 xalign 0.2
            #zoom, chestsfx
                MC "(I have a lot crafting supplies, I guess that’s to be expected.)"
                MC "(I wasn’t expecting this many sharp objects though. Scissors, dagger, needles, you name it.)"
                MC "(I suppose I needed the supplies to make those decorations somehow.)"
                MC "(But, where are those decorations? It’s not at the window.)"

            #menu 4
            "There’s usually something under the carpet, I gotta look.":
                scene bedroomnight:
                    parallel:
                        ease .5 zoom 1.75
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.8 xalign 0.5
                #carpet sfx
                MC "(Here we go! There’s...)"
                extend "nothing?"
                MC "(Wait no, there’s a heart etched onto the floor.)"
                scene black with fade
                MC "(Why would it be under the carpet though?)"
                scene night with fade
                show bm swpose
                show window
                "..."
                #knock
                show bm swpose
                BM "Hello? Are you here?"
                "..."
                BM "Did [player_gender] leave?"
                MC "Boo!"
                #stumblesfx
                show bm surprised with vpunch
                BM "Ack!"
                MC "Sorry! I’ll open the window for you."
                scene bedroomnight3 with fade
                #sfx
                show bm finger
                BM "[mc].. Don’t scare me like that, what if I fell off?"
                BM "Your whole family would hear me.."
                MC "I thought you were gonna say that you’d be seriously injured."
                show bm explanation
                BM "Oh that too, but I’ll be fine."
                MC "That’s worrying, you need to care for yourself more."
                BM "It’s alright, you won’t be able to see any cuts or bruises anyway."
                MC "Please don’t tell me you’re hiding cuts and bruises underneath your clothes."
                show bm idia
                BM "I-I’m not!"
                MC "Are you sure? I can’t see your face but you don’t sound very convincing."
                show bm swpose
                BM "R-really, don’t worry about me."
                MC "If you say so."
                MC "Anyway, we can’t talk for long today."
                BM "W-why not? Did I do something?"
                MC "Oh it’s not your fault, don’t worry."
                MC "Or maybe it is in a way..?"
                show bm idia
                BM "I-I’m not sure what I did but I’m sorry..? Please don’t leave me.."
                MC "I’m not leaving you. It’s just that my family has caught on to the fact that I’ve been super tired in the daytime now."
                MC "Since I’ve been spending my nights talking to you, I haven’t been getting much sleep."
                show bm swpose
                BM "Sorry.."
                MC "It’s fine. I just really like talking to you."
                show bm finger
                BM "You do..?!"
                MC "Well yea? Otherwise I would just ignore you."
                MC "Anyway, while I did say that we can’t talk for long, that doesn’t mean I want you to leave."
                BM "Really? You want me to stick around..?"
                MC "Definitely."
                MC "Anyway, wanna sleep with me tonight?"
                #cough
                show bm idia:
                            linear 0.050 xoffset +10
                            linear 0.050 xoffset -10

                BM "WHAT."
                BM "Y-y-you want m-me to.."
                extend "to WHAT???"
                MC "Sleep."
                extend "We’re sleeping. "
                extend "Do you not like to sleep??"
                show fx sweat2
                BM "B-but..the bed?? It’s...there’s ..There’s only one??"
                hide fx
                MC "Yea? It fits up to three people last I checked, my older sisters used to sleep over when I have nightmares."
                show bm explanation
                BM "This thing fits three people??"
                MC "Then again, that was a few years ago..."
                MC "Is the bed too small for you?"
                show bm swpose
                BM "W-well no.. but that would mean y-you and me, we’d be..uhh"
                MC "Use your words, I don’t understand you."
                show bm idia
                BM "We’d be too close!"
                menu:
                        "Why would that be an issue?":
                            show bm swpose
                            BM "Because.."
                            BM "W-what if I hurt you..? I have sharp claws and if I transform in the middle of night-"
                            MC "Then I get to hangout with a super cool monster."
                            MC "What’s the issue?"
                            BM "I just..don’t want to accidentally hurt you.."
                            BM "You’re human and as strong as you are, you get injured easily and you don’t heal as quickly.."
                        "Oh I get it, I like my personal space too.":
                            MC "As long as we have space to be further apart, would that be an issue?"
                            show bm swpose
                            BM "N-no that’d be fine."

                MC "So you’ll agree if one of us sleeps on  the bed and the other sleeps on the carpet?"
                show bm explanation
                BM "That sounds fine, your carpet doesn’t look too bad to sleep on."
                MC "Did I say {i}you{/i} were the one who’s sleeping on the floor?"
                BM "Why wouldn’t it be me? This is your room."
                MC "I don’t know, your clothing makes me think you’re used to finer things."
                MC "And people like that don’t usually sleep on hard surfaces."
                MC "What if your bones broke because you slept on the floor?"
                show bm idia
                BM "That won’t happen! I’m not that fragile!"
                MC "Are you sure? "
                show fx huffy
                show bm idia:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10

                BM "Yes! Gosh, you can be stupid sometimes.."
                show bm swpose
                show fx blush
                BM "B-but I guess it’s nice to know that you care.."
                show bm explanation
                BM "What if I sleep on the floor with you?"
                BM "On the carpet, if you don't mind?"
                hide fx
                extend "Or I can stay in the area without the carpet if you don’t want me there"
                MC "Howard, that would place you right in front of the door, I can’t do that."
                MC "The carpet covers half the room anyway."
                show bm swpose
                BM "Alright, if you say so."
                MC "Here’s my blanket, if we turn it horizontally it’ll be enough to cover both of us."
                BM "Thank you."
                scene bedroomnight3 with fade
                #thump,fabric
                MC "So, any thoughts so far?"
                show bm swpose:
                    parallel:
                        ease .5 zoom 1.5
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.0 xalign 0.5

                BM "It’s.. strange. But I like it."
                MC "You think you can go to sleep like this?"
                BM "Well...if you’re with me then perhaps I can."
                BM "Goodnight, [mc]."
                scene black with fade
                MC "Goodnight Howard."
                
                #menu 5
            "It feels weird to see the walls being barren, it’s like there should be something there.":
                    scene bedroomnight:
                            parallel:
                                ease .5 zoom 1.5
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.5 xalign 0.9

                #zoom
                    "Looking closer at the walls I notice the residue of something sticky, perhaps adhesives."
                    MC "(So there should be something hanging on my walls, but they’re not here.)"
                    MC "(Did I tear them off?)"

                #menu 6
            "The window! Will he show up tonight?":
                    show tsm nsdnormal:
                        parallel:
                            ease .5 zoom 1.5
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.35 xalign 0.5

                    MC "(I hope he does, maybe he can fill in a few gaps for me)"
                    MC "(Speaking of gaps...)"
                    MC "(What are these vertical slits in the window sill? They don’t seem like they came from any animal.)"
                    MC "(Honestly, it’s more like if I placed knives on my window to deter intruders.)"
                    MC "(Wait, did I?)"
                    scene cg2 with fade
                    #sfx
                    NO "Let me in."
                    #sfx
                    NO "LET ME IN"
                    scene bedroomnight with vpunch
                    #stumblesfx
                    MC "(!!!)"
                    MC "(Ow, my head really hurts)"
                    MC "(I wouldn’t do that, would I?)"
                    MC "(Maybe I would..)"
                #gw ga ngerti teknis, tp pilihan kelar abis milih semua choice
                #menu 7
            "I think that’s it.":
                    MC "(I can’t think of anything else to search in this room and it’s nearing day time.)"
                    #distantdoorsfx
                    Y "{size=-10} [mc]! We’re back!{/size}"
                    MC "(I should sleep before anyone gets too suspicious.)"
                    jump afternight1

label afternight1:
    scene black with fade
    pause 1
    # knock
    B "[mc]? Are you in here?"
    B "Oh, it seems that you are."
    Y "Fast asleep?"
    B "Seems so."
    Y "Great, it’s been a while since [player_gender] had a good night's sleep."
    Y "Usually, our little [player_fm] here would stay up all night."
    B "All because of that monster.."
    B "{size=-10}Anyway, don’t be too loud. We don’t want to wake [player_object] up. {/size}"
    Y "Whatever."
    #door
    MC "(THEY KNOW ABOUT HOWARD.) "
    MC "(And more importantly, they don’t like him very much.)"
    MC "(I wonder why..)"
    #pause,changebgm
    "..."
    #doorslam
    Y "Wakey wakey [mc]! You feeling good today?"
    scene bedroomday with fade
    show y smile
    MC "Good morning?"
    MC "Have you always slammed the door when you’re waking me up?"
    show y happy:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10

    Y "Of course! It’s effective, yea?"
    show y smile
    MC "I guess? It makes my head ring though."
    show y happy
    Y "Sorry..It’s the whole ‘losing your memories’ thing isn’t it?"
    Y "I’ll try to stop."
    Y "Are you feeling okay?"
    show y smile
    MC "Better? I guess"
    show y happy
    Y "Good to hear, but also it’s time for lunch."
    MC "Lunch?? I missed breakfast?"
    Y "Yea, we all did. Those night patrols really sap the energy out of you, huh?"
    Y "Let’s head down, I caught us some fish!"

    scene kitchen with fade
    show y happy:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10
    Y "Guess who’s back!"
    MC "Morning! Or I guess, afternoon?"
    show y smile at left
    show d happy at center
    D "Good afternoon [mc], sit down."
    show d normal
    #sfx
    MC "How was the night patrol?"
    show b normal at right
    B "Oh you wouldn’t want to know, it might frighten you."
    show d happy
    D "Now, now, we all know that’s not true. [mc]’s the one most interested in them afterall."
    show d normal
    MC "Yea! You heard what dad said."
    show b normal:
            linear 0.050 yoffset +5
            linear 0.050 yoffset -5
    B "Father, we should-"
    show d happy
    show b silent
    D "Let [player_object] listen."
    MC "(Woo! Dad’s on my side here!)"
    MC "So, what’s the night patrol for anyway?"
    D "Haven’t we had this discussion before?"
    show d normal
    MC "Well I forgot and I’d like to ask again."
    show b normal
    B "It’s to keep everyone safe."
    show b silent
    MC "From..?"
    show y happy
    Y "The monster, obviously."
    show y smile
    MC "(Please tell me the monster isn’t Howard.)"
    MC "Well, what does it look like?"
    show d happy
    D "You should know best [mc], you asked for its feathers afterall."
    show d normal
    MC "(Darn it, it is him.)"
    MC "But that just means it wasn’t dangerous! Why do we need the night patrol?"
    show b normal
    B "[mc], just because something is pleasing to the eye, does not mean that it isn’t dangerous."
    MC "But that thing wouldn't hurt-"
    show b normal:
            linear 0.050 yoffset +5
            linear 0.050 yoffset -5
    B "Yes it would, [mc]! Why do you think the disappearance cases have gone up alongside the monster sightings?"
    MC "What?"
    B "That thing is clearly kidnapping members of our community."
    show b silent
    MC "Is that true dad?"
    show d happy
    D "Unfortunately so."
    MC "(Would he do something like that..?)"
    MC "(The man in my memories…how much of it was true..?)"
    D "In any case, if we ever manage to hunt him down, I'll make sure to take some of its feathers for you."

    show d normal with vpunch
    MC "NO DON’T"
    MC "(PLEASE DON’T KILL HIM.)"
    show d happy
    D "[mc]?!"
    MC "I mean..I don’t need them anymore."
    D "Really? Why the sudden change of mind?"
    D "Then again, I noticed that your window decorations disappeared. Did something happen?"
    show d silent
    MC "(Yea, I lost my memory. But also.."
    extend "Good question, where did they go??)"
    MC "Nothing dad, to be honest, I don’t know where they went either."
    show y smile:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10
    show b silent:
            linear 0.050 yoffset +5
            linear 0.050 yoffset -5
    #Y&B sprite jump
    MC "(It’s their doing isn’t it?)"
    show d happy
    D "That’s odd. Have you two seen where it went?"
    show d normal
    MC "Yea, {i}Have you?{/i}"
    show y happy
    Y "Ha ha, Nope! Not at all! Gee, I wonder where it went."
    show y grumpy:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10
    #stomp
    Y "Ow!"
    show b normal:
                        parallel:
                            ease .5 zoom 1.1
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.2

    B "No, we haven’t seen it."
    MC "That’s odd, you seem like you know something."
    show b normal:
                        parallel:
                            ease .5 zoom 1.2
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.2

    B "{b}We don’t.{/b}"
    MC "{b}Do you?{/b}"
    D "Now, now, let’s finish our lunch in peace."
    show b silent:
             parallel:
                ease .5 zoom 1.0
    
    show y happy:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10
    Y "Sounds great!"
    MC "Yea.. sounds {i}great{/i}"

    scene kitchen with fade
    show d happy
    D "Alright, I’ll be off with your eldest sister today. Stay safe and guard the house, alright?"
    show d normal
    show y happy at right:
            linear 0.050 yoffset +10
            linear 0.050 yoffset -10
    Y "Leave it to us!"
    show b silent at left
    B "..."
    MC "Good bye."
    show d happy
    D "See you at dinner."
    #footsteps, doorclose
    scene kitchen with fade
    show y happy
    Y "So [mc], you feeling better after lunch?"
    show y smile
    MC "I’m fine."
    show y happy
    Y "Don’t think too hard about the monster alright? You’ll be safer without it in your life."
    show y smile

    MC "(My other sister..)"
    MC "(She seems worse at hiding things than the eldest, maybe I can actually get something out of her.)"
    MC "(But then again, if she’s bad at hiding it, other people would know about me asking immediately.)"
    MC "(Do I take the risk?)"
    menu:
            "Can I talk to you?":
                show y happy
                Y "Uhh, sure?? About what?"
                show y smeile
                MC "The monster. The missing window decorations, my sudden memory loss. There’s a lot."
                show y happy
                Y "Sorry! Can’t tell you! I promised her I wou-"
                show y grumpy:
                        linear 0.050 yoffset +10
                        linear 0.050 yoffset -10
                Y "YOU DIDNT HEAR THAT! I’M BUSY!"
                Y "BYE"
                show y at offscreenright with easeoutright
                #zoomoffscreen, runsfx
                MC "(That settles it, those two are hiding something.)"
                hide y
                MC "(And my memory loss is possibly related to them, but why?)"
            "(No, I need to shut up.)":
                show y happy
                Y "Uhh [mc]? Why are you glaring at me like that?"
                show y smile
                MC "I’m not, that’s just my face."
                show y happy
                Y "Well I know that but you look extra scary today."
                MC "What about you? You look shifty today, like you’re hiding something."
                show y grumpy:
                    linear 0.050 yoffset +10
                    linear 0.050 yoffset -10
                Y "Uh..I. I’M DOING MY CHORES BYE."
                show y at offscreenright with easeoutright
                #sfx
                hide y
                MC "(Those two are definitely keeping secrets from me, secrets that are potentially related to my sudden lack of memories.)"

    MC "(In any case, she’s unlikely to hang around me for now. Seems like a good time to re-familiarize myself with the layout of my own house.)"
    MC "(Starting..here.)"
    scene hallwayday
    "Given that I haven’t spent much time outside my room and the kitchen, I figured that going through each room one by one would be a great idea."
    "But reality seems to disagree."
    #sfx
    MC "(None of these doors open.)"
    MC "(Why is my room the only one without a lock? This isn’t fair..)"
    #sfx
    MC "(This one doesn’t open either.)"
    MC "(I think I’ll go back to the kitchen.)"
    scene kitchen with fade
    #kyk td
    menu: 
            #menu1
            "Maybe our shelf has something useful?":
                #zoom
                MC "(Then again, we don’t have a lot of things here.)"
                MC "(Maybe the few books we do have can help..?)"
                MC "(“Edible Plants”, “Children’s Fairytales”, “Grandma’s Recipe”, “Local Animals” and “Basic Emergency Care”..?)"
                MC "(Wait, this last one seems familiar.)"

                scene bedroomnight2 with fade
                "..."
                MC "(It’s getting late. Is he not showing up tonight?)"
                MC "(I guess he can’t show up {i}every{/i} night, I should try and sleep for once.)"
                scene bedroomnight3
                MC "(I’ll open the windows, just in case.)"
                scene black with fade
                #feathers,cough
                BM "[mc]...I’m here"
                BM "Curses, am I too late?"
                BM "H-hey, [mc]?"
                scene bedroomnight3 with fade
                MC "?"
                show bm swpose
                MC "Hey, you came. I thought you wouldn’t be here tonight."
                BM "I try my best."
                MC "Wait, what happened to your arm?"
                BM "D-don’t worry about me. An arrow just grazed my wing."
                MC "So your arms are what turns into wings, huh?"
                show bm explanation
                BM "Well, yes."
                MC "Interesting, I thought they’d grow out of your back like on portraits of angels."
                show bm swpose
                BM "But I’m not an angel. "
                MC "You sure? You seem like one to me."
                show bm idia
                show fx blush
                BM "[mc]... Stop saying things that would make me go red.."
                MC "But I can’t see your expressions..?"
                show bm finger
                BM "Still...Hearing you say things like that is embarrassing.."
                MC "Well, too bad." 
                MC "Anyway, we should hurry and clean up that wound."
                show bm explanation
                hide fx
                BM "You don’t need to care about me that much, I’ll heal. Besides, your family will hear us."
                MC "They’re out for the night patrol."
                BM "What if they come back?"
                MC "They won’t, not at this hour. Now don’t be stubborn, we should wash and bandage it."
                show bm idia
                BM "B-but then you’ll see my bare arm!"
                menu: 
                    "No complaints, I’ll carry you downstairs.":
                        show bm surprised:
                            parallel:
                                ease .5 zoom 2.0
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.0 xalign 0.5
                        show bm idia
                        BM "Eek! [mc]! P-please put me down!"
                        MC "I wouldn’t have to do this if you agreed to let me take care of you."
                        show bm finger
                        show fx blush:
                            parallel:
                                zoom 2.0
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.0 xalign 0.5
                        BM "T-that’s not fair..."
                        MC "What is?"
                        show fx huffy
                        BM "Hmph.. I don’t wanna say it.."
                        show fx blush
                        MC "Just let me clean the wound, it won’t take more than five minutes."
                        show bm swpose
                        BM "Fine.. but be nice to me, alright?"
                        MC "As you wish."

                    "Really? How {i}scandalous{/i}.":
                        MC "Do I have to take responsibility for your shattered pride if I see your bare arm?"
                        show bm swpose
                        BM "W-well no..."
                        MC "Must I swear to stay with you in sickness and health just so I can clean your wound?"
                        show fx blush
                        show bm idia
                        BM "[mc].. Please stop teasing me."
                        MC "Sorry, I bet you’re all red underneath that mask huh?"
                        BM "I-if you knew that then why did you keep going?"
                        MC "Because I like seeing your reactions?"
                        show bm swpose
                        show fx huffy
                        BM "Hmph.."
                        hide fx
                        MC "Come on, let me take care of you."
                        BM "P-please be gentle, alright?"
                        MC "I will."

                        scene kitchennight with fade
                        MC "There we go, all done! Does it hurt?"
                        show bm swpose:
                                    parallel:
                                        ease .5 zoom 1.5
                                    parallel:
                                        yalign 0.0
                                        linear 0.0 yalign 0.0 xalign 0.5

                        BM "No.. I guess not."
                        show bm explanation
                        BM "Honestly, I was expecting you to knock me out first."
                        MC "Why would I do that?"
                        BM "Is that not how typical medical procedures go?"
                        MC "Uhh no? I’m not a healer but I don’t think that’s how it works. Is that how it works where you came from?"
                        show fx sweat
                        BM "Umm..In a way, yes?"
                        hide fx
                        MC "Whatever healer you’ve been visiting, you need to stop seeing them immediately."
                        BM "I’ll keep that in mind."
                        show bm swpose
                        BM "Thank you. You’re.. really nice to me"
                        MC "I wouldn’t say that I’m nice, in fact I’m sure I may have pushed you out of your comfort zone a few times."
                        BM "W-well...I..I don’t hate it.."
                        BM "The fact that I can’t ever win against you..."
                        MC "Really? Well.. I like that but I’m also curious, why not? You’re strong enough to do it."
                        BM "But what if you get hurt..? I really don’t want that.."
                        MC "You’re not gonna hurt me, especially when you’re too scared to even touch me."
                        MC "By this point, I don’t mind if you touch me y’know?"
                        BM "I-i’m still scared.. What if I hurt you..?"
                        show bm explanation
                        BM "It almost feels easier for me if you just tie me up with that scarf again."
                        MC "Like I did the first few nights you broke into my room?"
                        BM "Y-yea.."
                        BM "But if you put it that way I guess I did come off as someone up to no good."
                        show bm swpose
                        BM "I’m sorry, I was just.."
                        extend "really desperate for any sort of positive interaction."
                        BM "And I thought that someone who likes my feathers might also take an interest in me..?"
                        MC "Sweetie, by this point I’m more than just interested in you." 
                        MC "I like getting to know you and I definitely enjoy having you around."
                        show fx blush:
                                    parallel:
                                        zoom 1.5
                                    parallel:
                                        yalign 0.0
                                        linear 0.0 yalign 0.0 xalign 0.5
                        BM "Promise you’re not lying to me?"
                        MC "I promise. "
                        show bm explanation
                        BM "Are you sure?  I don’t think I’ve ever met someone who liked having me around before."
                        show bm sw pose
                        BM "I..I..uh..nevermind."
                        MC "Whoa, don’t stop there! Now I’m curious."
                        BM "N-no need."
                        MC "C’mon, use your words."
                        BM "W-well, I was about to ask if I could hug you but... I got scared. W-what if I scratch you?"
                        MC "Well in that case, {i}I{/i} can hug you instead?"
                        show bm idia
                        show fx blush
                        BM "You would do that..?!"
                        MC "Of course."
                        #zoom sprite
                        show bm swpose:
                                    parallel:
                                        zoom 1.9
                                    parallel:
                                        yalign 0.0
                                        linear 0.0 yalign 0.0 xalign 0.5
                        "As I wrap my arms around him, his posture straightens at the sudden contact. Despite his initial reaction, he soon lets himself relax as he melts into my embrace, carefully placing the weight of his head onto my shoulder."
                        scene black with fade
                        BM "Thank you..really, I can’t thank you enough.."

                    "I might as well check the table.":
                            scene kitchen:
                                    parallel:
                                        zoom 1.5
                                    parallel:
                                        yalign 0.0
                                        linear 0.0 yalign 0.8 xalign 0.5
                            #zoom
                            MC "(I’ve eaten on this table multiple times but I haven’t really inspected it before.)"
                            MC "(Too bad it just seems like a normal table.)"
                            MC "(Is there anything underneath it though?)"
                            #papersfx
                            MC "(Oh, there’s something taped to the underside.)"
                            show mc paper
                            MC "(It’s paper?)"
                            "“Witch Hut, head north into the forest until you see a house, it might move so call out to it”"
                            MC "(Witch hut? The house might move?)"
                            MC "(Who wrote this?)"
                            "“Once inside, speak politely to the witch, do her chores when asked, she’ll return the favor in the morning”"
                            "“Warning : Quite far, be patient, give proper excuse to father”"
                            MC "(“Father” huh? Sounds like my ‘eldest sister’ has been here.)"
                            hide mc
                            MC "(I’ll keep this for now.)"

                    "The cupboards seem like they’re hiding something.":
                            MC "(Let’s see what’s in here..)"
                            MC "(Plates, cutlery and..knives??)"
                            MC "(Maybe not {i}knives{/i}, more like a huge assortment of blades with sporadic sizing?)"
                            MC "(What could these be for?)"
                            scene cg2 with fade
                            NO "LET ME IN"
                
                            scene kitchen with vpunch
                            MC "(!!!)"
                            MC "(No, no, no, nonono)"
                            scene hallway with fade
                            pause 1
                            #run,doorslam
                            scene bedroomday with fade
                            MC "(Is this really what these blades are for..?)"
                            #minicg, bladenoise
                            show w blades
                            MC "(Oh no..)"
                            MC "(They fit perfectly into the window sills. It’s like I was trying to deter someone from entering.)"
                            MC "(Did I do this to Howard..?)"
                            MC "(But why..?)"
                            hide w
                            "..."
                            MC "(It’s no use, I can’t remember anything.)"
                            MC "(I’ll have to search for more pieces of my memory.)"
                            scene hallway with fade
                            pause 1
                            scene kitchen with fade

                    "What’s in this little basket?":
                            MC "(How cute, it’s as if we’ll be going to a picnic.)"
                            MC "(But is anything actually inside?)"
                            MC "(Nope not much, just a blanket.)"
                            #cling
                            MC "(Wait, there’s something else.)"
                            #mini cg
                            MC "(A key!)"
                            MC "(Although to where? I don’t know yet.)"
                            MC "(I’ll be storing this for future use)"


    #Muncul pas pilihan lain udah
                    "I can’t think of anything else to check here.":
                            show y happy
                            Y "[mc]! You’re still in the kitchen? I thought you’d be in your room."
                            show y smile
                            MC "Yea, just looking for a new view."
                            show y happy
                            Y "Yea I get that, being stuck in bed like yesterday must suck huh?"
                            show y smile
                            MC "It sure does."
                            MC "Do you need any help with anything?"
                            show y happy
                            Y "Nah, you should rest. I handled all your chores."
                            show y smile
                            MC "(I’ll guess I’ll continue tonight.)"
                            jump afterchoice2

label afterchoice2:
    #door
    scene kitchen with day
    show d happy
    D "We’re back."
    show d normal
    show y happy at left:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Hi dad! What did you bring today?"
    show y smile
    show b normal at right
    B "Not much. We merely foraged for some mushrooms."
    show b silent
    D "Sorry, no more meat tonight."
    show y happy
    Y "It’s alright, we’ll reheat yesterday’s stew."
    Y "Are you hungry, [mc]?"
    show y smile
    MC "I guess I am."
    show y happy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Sweet! It’s dinner time!"

    scene kitchennight with fade
    #platesfx
    "..."
    MC "(Today’s dinner is eerily quiet..)"
    MC "(It doesn’t help that my 'sisters' are stealing glances at me every few minutes..)"
    MC "(Are they even really my sisters?)"
    MC "(Well, I live with them so maybe they are?)"
    show y happy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "I’m done eating!"
    show y smile
    show b normal at left
    B "The rest of us aren’t finished."
    show b silent
    show y grumpy
    Y "Whatever, I’ll get ready for tonight's patrol."
    show y at offscreenright with easeoutright
    MC "Speaking of the night patrol, any updates on the monster?"
    hide y
    show b normal
    B "Don’t concern yourself with it."
    show b silent
    MC "I have a right to know."
    show d happy at right
    D "You do, [mc]."
    show b normal
    B "But fathe-"
    show b silent
    D "We have plans to finish off the monster by the end of the week."
    D "We have received a report of its last sighting where it was severely injured, which was 2 days ago."
    D "The community has decided that we should try and end it while it’s injured."
    show d normal
    MC "(2 days ago? That was around when I lost my memory.)"
    MC "But it wasn’t seen yesterday, was it?"
    show d happy
    D "That’s right, we haven’t seen it since. A few members are planning on exploring nearby caves to see if it has taken refuge there."
    MC "(I sure hope Howard’s not hiding in one of those caves then.)"
    show b normal
    B "Can I clear the table now? It seems that we’ve all finished eating."
    show b silent
    D "Oh yes, thank you."
    show b normal
    B "Now let us hurry, we mustn't be late."
    show b silent
    show y happy:
        linear 0.050 yoffset +10
        linear 0.050 yoffset -10
    Y "Alright! I’ve been waiting for this!"
    Y "Take care of the house and be safe, okay [mc]?"
    show y smile
    MC "Sure thing."
    hide y
    show d happy
    D "See you in the morning, [mc]."
    hide d
    show b normal at center
    B "Don’t let anyone in, understood?"
    show b silent
    MC "Sure sure."
    show b normal
    B "I’m serious."
    show b silent
    MC "I got it, you don’t have to say it again."
    show b happy
    B "I sure hope you got it. Farewell, [mc]."
    show b silent
    MC "Byee."
    #doorsfx

    MC "(Time to explore the rest of the house.)"
    scene hallwaynight with fade
    MC "(I couldn’t go into any of the rooms earlier but I have this key now!)"
    MC "(Time to figure out where this key leads.)"
    #sfx
    MC "(Nope.)"
    #sfx
    MC "(Not this one too.)"
    #sfx
    MC "(And...no. Honestly, it’d be useful if this key could open up my sisters rooms.)"
    MC "(What’s this door? Looks pretty dilapidated compared to the other ones.)"
    MC "(It’s not a haunted room is it?)"

    show attic with fade
    show keyhole
    show attic with fade:
        parallel:
                ease .5 zoom 1.0
        parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.3
    pause 2
    show attic with fade:
        parallel:
                ease .5 zoom 1.0
        parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.85
    pause 2
    show attic with fade:
        parallel:
                ease .5 zoom 1.0
        parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.5
    pause 2
    #zoom,movebg left&right
    scene hallway with fade
    MC "(Seems normal enough, I’ll give it a try.)"

    #sfx
    MC "(AH! It opened!)"

    scene attic with fade
    MC "(So this is the attic..)"
    MC "(Feels like I’ve been here a bunch of times.)"
    MC "(Now, where do I start?)"
    #ini ky tadi jg
    menu: 
            "The old wardrobe shows some promise.":
                MC "(Let’s see what we have in here..)"
                MC "(Wait, there’s a whole bunch of stuff in here! There’s coats, cloaks, extra boots?)"
                MC "(If we had these all along, why couldn’t I have joined the night patrols?)"
                MC "(Unless these don’t fit me?)"
                #fabricsfx
                MC "(Nope, they do fit.)"
                MC "(So I do have proper clothing! They were just making excuses so I couldn’t tag along.)"
                "..."
                MC "(How do I even have these?)"
            
                scene bedroomnight3 with fade
                MC "(And in 3..2..1)"
                #feathersfx
                show bm swpose at center:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                BM "[mc], I’m here!"
                MC" Nice to see that you got here safely."
                MC "You seem happier than normal, did something happen?"
                show bm swpose at center:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                BM "W-well, yes! How did you know? My mask is still on, right?"
                MC "Of course it is. "
                show bm idia at center:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                BM "Great!"
                show bm finger
                BM "Anyway, I..have something to give you..?"
                MC "Really?"
                show bm explanation
                BM "So, you know how I’ve been molting for a few weeks and I have a lot of feathers in my room?"
                BM "Well, I remembered that you told me about how you asked for a feather of mine instead of new clothes when your father was going to the fair."
                BM "And, since I had the opportunity to learn recently, I made a few things for you made out of my feathers..! "
                BM "Here’s the coat I made you along with some boots and a scarf."
                show bm swpose
                show fx sweat
                BM "Y-you don’t find that weird..do you? The fact that I made them with my feathers..?"
                BM "{size=-10}Maybe I should’ve thought this through..{/size}"
                hide fx
                MC "You made me all this..?"
                show bm swpose at center:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                BM "Y..yes! If..you don’t mind that they’re made of my feathers..?"
                MC "No, I don’t mind at all! But they didn’t hurt you, did they?"
                show bm swpose at center:
                            linear 0.050 yoffset +10
                            linear 0.050 yoffset -10
                BM "Oh not at all! I assure you that I wasn’t hurt in the slightest! I used the feathers that fell out!"
                menu:
                        "Thank you! I appreciate you doing all this.":
                            show bm explanation
                            BM "Well, I’ve been a guest in your home every night so I thought I’d have to bring a gift to my host eventually?"
                            MC "You really didn’t need to. Especially when I can’t give you anything back that’s this nice."
                            MC "Unless you’re willing to wait a few years..?"
                            show fx blush
                            BM "Well, I certainly don’t mind a gift from you. But you really shouldn’t have to give me something back."
                            hide fx
                    
                        "Tackle him into a hug.":
                            #zoom
                            show bm surprised at center:
                                parallel:
                                    ease .5 zoom 2.0
                                parallel:
                                    yalign 0.0
                                    linear 0.0 yalign 0.0 xalign 0.5

                                linear 0.050 yoffset +10
                                linear 0.050 yoffset -10
                                linear 0.050 xoffset +10
                                linear 0.050 xoffset -10

                            BM "(!!!)"
                            show fx blush:
                                parallel:
                                    zoom 2.0
                                parallel:
                                    yalign 0.0
                                    linear 0.0 yalign 0.0 xalign 0.5

                            BM "[mc]..Y-you can’t just do things like this without warning..!"
                            BM "I thought my heart was going to leap through my chest for a moment.."
                            MC "Do you hate it though?"
                            show bm swpose
                            BM "W-well.."
                            extend "Nevermind.."
                            BM "I-I don’t hate it."
                            MC "I know."
                            BM "Don’t let me go. You started this."
                            MC "Sure sure. I’ll keep on going until you pull away."
                            BM "You better.."
                            "..."
                            BM "What if I don't want to pull away?"
                            MC "Fine by me."
                            BM "I feel like I forgot something.."
                            extend "Can you pull away for a moment?"
                            MC "Sure"
                            show bm sw pose:
                                parallel:
                                    ease .5 zoom 1.0
                                parallel:
                                    yalign 0.0
                                    linear 0.0 yalign 0.0 xalign 0.5

                BM "Anyway,.."
                MC "Yea?"
                BM "Can you try it on now?"
                MC "Sure thing."
                #fabricsfx
                scene bedroomnight with fade
                show bm swpose
                BM "So.."
                show bm explanation
                extend "How is it?"
                BM "I’m..well..not exactly human so these should be sturdier than average."
                MC "They feel great! I feel like royalty in these!"
                BM "So you like them?"
                MC "I love them! "
                menu: 
                        "Like I love you!":
                            show bm surprised:
                                linear 0.050 yoffset +10
                                linear 0.050 yoffset -10
                                linear 0.050 xoffset +10
                                linear 0.050 xoffset -10
                            BM "L-love..?!! M-me..?!!"
                            show bm explanation
                            BM "W-well, surely you jest..?"
                            MC "Not at all, I’m completely serious."
                            show bm swpose
                            BM "A-are you?"
                            MC "I am. And I’ll say it as many times as I need to get it through your head."
                            MC "Or is your mask in the way?"
                            show bm idia:
                                linear 0.050 yoffset +10
                                linear 0.050 yoffset -10
                            BM "NO..! The mask is not in the way!"
                            show fx blush
                            BM "I-i don’t need you to see how red I am..!"
                            MC "Sure sure."

                        "It’s the best gift I’ve ever received.":
                            show bm swpose
                            show fx blush
                            BM "I’m glad you think that way."
                            MC "It kinda feels like a representation of you in a way. Like you’re right by my side even when you’re not."
                            BM "T-that would be nice.."
                            BM "I want to make you more things now..."
                            MC "Well aren’t you just the sweetest?"
                
                            scene attic with fade
                            MC "(Right, that’s how I got these.)"
                            MC "(They were from him..)"

                        "Time to open up some chests!":
                            MC "(Great, this one isn’t locked.)"
                            MC "(There’s a lot of paper and there’s something drawn on them.)"
                            MC "(Did I draw all these?)"
                            MC "(They have residue on the back, I’m guessing these were what previously decorated my walls?)"
                            MC "(Oh? This is Howard as a bird. Shame I didn’t draw any portraits of his human form though.)"
                            MC "(Then again, I wouldn’t want my family to catch on.)"

                        "The window! It’s always worth checking.":
                            MC "(Why did we barricade it?)"
                            MC "(I don’t remember those wooden planks being there..)"
                            #woodnoise
                            MC "(There! Now I can see the sky again.)"
                    
                            scene hallwaynight with fade
                            MC "(Man, these night patrols sure are convenient. Without my family around I don’t have to worry about them finding Howard.)"
                            MC "(I should get back to my room before he gets here.)"
                            #steps, crash, feather
                            BM "Ow.. That arrow almost hit me.."
                            MC "(Is that him? He’s already here?)"
                            BM "[mc]! I’m here! "
                            BM "Oh! I forgot I have to be quieter.."
                            BM "[mc]?"
                            extend "I guess [player_gender] [player_sbn] here yet.."
                            MC "(I kinda wanna know what he’ll do when I’m not around.)"
                            show bedroomnight with fade
                            show bm swpose
                            show mc keyhole
                            BM "..."
                            MC "(He’s just waiting on my bed.)"
                            #humming soundbite
                            "He sits on the edge as politely as I thought anyone ever could, his back seemingly straight as a ruler and his feet flat on the floor."
                            "After a few brief glances at my pillow he forgoes his perfect posture and lies down, snuggling into the warmth of my blanket."
                            MC "(He’s getting really comfortable there..It’s almost like it’s his room now.)"
                            MC "(Then again, it might as well be with the way he’s visiting every night.)"
                        
                            #creak
                            MC "(Woops)"
                            scene hallwaynight with fade
                            show bm swpose
                            BM "[mc]? "
                            MC "(No use in hiding anymore.)"
                            scene bedroomnight with fade
                            MC "Getting comfy on my bed?"
                            show fx sweat2
                            BM "N-no! I wasn’t..uhh.."
                            show fx sweat
                            extend "Sorry, I was getting too comfortable."
                            hide fx
                            "Giving him a small smile, I placed myself near him on my bed."
                            show bm swpose:
                                        parallel:
                                            ease .5 zoom 1.5
                                        parallel:
                                            yalign 0.0
                                            linear 0.0 yalign 0.0 xalign 0.5

                            MC "No worries, I don’t mind anymore."
                            show bm explanation
                            BM "A-are you sure?"
                            MC "Yea? You basically live with me by this point."
                            BM "Live with you..? W-well that sounds nice.."
                            show bm swpose
                            BM "..."
                            BM "Can I..get closer to you..?"
                            MC "Sure, scoot over."
                            BM "Thank you."
                            show bm swpose:
                                            parallel:
                                                ease .5 zoom 1.8
                                            parallel:
                                                yalign 0.0
                                                linear 0.0 yalign 0.0 xalign 0.5
                            #spritezoom
                            BM "Can you hold me..?"
                            MC "Someone’s making a lot of requests today."
                            MC "But of course I can."
                            show bm finger
                            BM "Thank you, I really needed this tonight."
                            MC "What’s up? You seem more on edge than usual."
                            show bm explanation
                            BM "W-well, is it just me or has there been more hunters at night recently?"
                            BM "Even your family has gone on these ‘night patrols’ right?"
                            BM "The night used to be pretty safe for me, maybe one or two people wandering about."
                            show bm swpose
                            BM "Like when I met you."
                            show bm explanation
                            BM "But now.. There’s mobs going around looking for...something?"
                            BM "Is it me? The thing they were looking for?"
                            MC "Well, I’m not sure either. My family said they’re looking for a monster but it might not be you?"
                            MC "But to be honest, the amount of missing people has increased recently."
                            show bm idia
                            BM "Really..?!"
                            MC "That’s what I read in the newspapers."
                            MC "If you’re curious, you can read it?"
                            show bm swpose
                            #paper
                            BM "List of missing people..."
                            MC "A few of them have portraits, maybe you’ll recognize some of them?"
                            BM "Hmm.."
                            show bm idia:
                                    linear 0.050 yoffset +10
                                    linear 0.050 yoffset -10
                            BM "(!!)"
                            MC "What’s wrong?"
                            show bm swpose
                            BM "I feel like I recognize them.."
                            MC "You probably would if you lived in the village down the hill, is that where you’re from?"
                            BM "No, I live much further than that."
                            #papersfx
                            BM "Hmm.."
                            BM "You’re saying that they went missing..?"
                            MC "That’s what I’ve been told."
                            BM "They weren’t just looking for a new job?"
                            MC "No."
                            show bm explanation
                            BM "This might sound a little strange to say but I think I have a theory..?"
                            MC "Go ahead."
                            BM "Do you think that they just moved to find jobs?"
                            BM "After looking at the list, I noticed that everyone was pretty quiet? Or maybe they didn’t like talking to people much?"
                            MC "Quiet?"
                            show bm swpose
                            BM "As in, when I tried talking to them they ignored me..although I suppose they were busy?"
                            MC "Busy?"
                            MC "I feel like you have the wrong people, these are the friendliest folks I know."
                            MC "Like Mr Hansen here, he’d always smile and wave whenever me and my family passed by."
                            BM "But I know this face..and he never had anything other than a blank stare.."
                            MC "Well I’ve known him since I was a kid and he’d never do that!"
                            BM "What about her? As far as I know she always has this tired look to her, I’ve never seen her so..lively?"
                            MC "Well that’s what she’s like? Mrs Jones is always full of energy."
                            BM "..."
                            BM "[mc], how long ago did they disappear?"
                            MC "Uhh, A month ago?"
                            "His movements froze for a moment, he stares at me dead in the eye as if he’s trying to say something but none of the words are coming out."
                            
                            show bm swpose:
                                            parallel:
                                                ease .5 zoom 1.3
                                            parallel:
                                                yalign 0.0
                                                linear 0.0 yalign 0.0 xalign 0.5

                            BM "I..I think I know where they are..."
                            MC "Really?! Where? Maybe we-"
                            show bm swpose:
                                            parallel:
                                                ease .5 zoom 1.0
                                            parallel:
                                                yalign 0.0
                                                linear 0.0 yalign 0.0 xalign 0.5

                            BM "Thecastletheyarestuckinthecastle."
                            MC "What?"
                            show bm explanation
                            BM "I can’t stay here any longer."
                            MC "Wait, why not?"
                            BM "I have to go."
                            MC "I said wait!"
                            #tackle (reuse first cg?)

                            scene tacklecg with vpunch
                            BM "[mc], let me go!"
                            MC "Not before you tell me what’s going on!"
                            scene tacklecg with vpunch
                            BM "I can’t!"
                            MC "Why not?"
                            BM "Because it’s all my fault!"
                            MC "Whatever it is no it’s not. You haven’t done anything wrong and I know it."
                            BM "But they wouldn’t have gone missing if it weren’t for me..!!"
                            MC "Take a deep breath, and explain to me slowly. I’m right here for you."
                            MC "What makes you think it’s your fault?"
                            BM "I-I’ve seen them. Recently."
                            BM "They’re the new servants back where I came from."
                            BM "I didn’t know.. That they were..."
                            BM "T-they were.."
                            MC "Servants? Why would th-"
                            BM "[mc], please let me go!"
                            BM "I really need to go back now..!"
                            menu:
                                    "Do you really have to leave?":
                                        BM "I do."
                                        MC "Will you come back tomorrow?"
                                        BM "I-I want to."
                                        extend "I really do."
                                        BM "I-I want to see you everyday if fate allows it."
                                        MC "Then come back tomorrow, I want to see you too."
                                        BM "N-no, you won’t want to see me again after this."
                                        MC "Why not?"
                                        BM "I can’t tell you yet."
                                        MC "Will you explain it to me someday?"
                                        BM "I.. I will try."
                                        MC "Good enough for me."

                                        scene bedroomnight3 with fade
                                        show bm swpose
                                        MC "I guess this is good bye for now?"
                                        BM "Y..yea."
                                        MC "Before you leave, can I ask for one thing?"
                                        show bm explanation
                                        BM "S-sure, what is it?"
                                        MC "Close your eyes."
                                        BM "A-alright."
                                        MC "Now, hands behind your back."
                                        show bm swpose
                                        BM "[mc], w-what are you doing..?"
                                        MC "Sorry, I just wanted to make sure you wouldn’t interrupt me."
                                        show bm explanation
                                        BM "W-what..? Before you continue, will this thing you’re asking for stop me from leaving?"
                                        MC "It’d be nice if it does but I doubt it."
                                        show bm swpose
                                        BM "W-will it hurt?"
                                        MC "It won’t and it’ll only take a second."
                                        MC "Do you trust me?"
                                        BM "I..I."
                                        extend "I do."
                                        #take off mask
                                        show bm close
                                        BM "[mc]..? What are you doing..?"
                                        MC "Shh."
                                        scene black with fade
                                        "And with that, I pull him closer to give him a peck on his cheek."
                                        scene bedroomnight3 with fade
                                        MC "There, all done."
                                        show bm basking:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                                linear 0.050 xoffset +10
                                                linear 0.050 xoffset -10
                                        BM "D-did you just..?!"
                                        MC "Sorry, did you hate it?"
                                        show bm brhappy:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                        BM "NO! "
                                        show bm happy
                                        extend "I mean..no I didn’t hate it."
                                        BM "I really liked it..!"
                                        show bm questioning
                                        BM "Curses, you’re making it really hard for me to leave..."
                                        show bm swpose
                                        #put mask on
                                        MC "But you still have to leave, yea?"
                                        BM "Y-yes."
                                        MC "I understand, I’ll keep the window open for you.  "
                                        BM "Promise?"
                                        MC "Promise"
                                        BM "I'll be back when I can, I swear."
                                        MC "Goodbye Howard."
                                        BM "Goodbye, [mc]."
                                        scene black with fade
                                        #feathersfx

                                    "No, not until you explain it to me.":
                                        BM "[mc]..! PLEASE!"
                                        MC "No!"
                                        #fabricrip
                                        MC "Howard..?"
                                        BM "I..hurt you.. You’ll hate me.."
                                        MC "It’s just a tear on my sleeve, I’m fine."
                                        BM "No, no, no, nonono.."
                                        MC "Shh, Howard I’m fine."
                                        scene tacklecg with vpunch
                                        BM "DON’T COME NEAR ME..!"
                                        MC "..."
                                        BM "I..I.. I’m sorry!! I’ll leave!!"
                                        scene bedroomnight3 with fade
                                        MC "Wait! I’m not hurt!"
                                        show bm swpose:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                                linear 0.050 xoffset +10
                                                linear 0.050 xoffset -10
                                                repeat 2
                                        BM "I can’t be here anymore, I’ve done something to you...!"
                                        MC "It’s just my shirt, I’m fine!"
                                        show bm swpose:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                        BM "No, I-"
                                        MC "Shut up."
                                        show bm idia:
                                                parallel:
                                                    ease .5 zoom 2.0
                                                parallel:
                                                    yalign 0.0
                                                    linear 0.0 yalign 0.0 xalign 0.5

                                        #zoom
                                        "In a spur of the moment decision,  I grab him by the collar and place a brief kiss on where his mouth should be."
                                        BM "(!!!)"
                                        #zoom out a little
                                        show bm swpose:
                                                parallel:
                                                    ease .5 zoom 1.7
                                                parallel:
                                                    yalign 0.0
                                                    linear 0.0 yalign 0.0 xalign 0.5

                                        BM "Y..you..kissed me..?"
                                        MC "Well the mask but yes, that was the idea."
                                        MC "Howard, I’m not hurt and I don’t hate you."
                                        MC "Get that into your head before you leave me for the night."
                                        BM "I’m never washing this mask ever again.."
                                        MC "That’s a bit extreme."
                                        BM "But really, [mc]..I..I.. "
                                        extend "nevermind."
                                        MC "Hey, you can’t do that! I want to know what you have to say."
                                        show bm idia
                                        BM "[mc]..I really can’t.. I’ll die of embarrassment here.."
                                        MC "Can I hear it tomorrow then? If you ever come back?"
                                        BM "I..I’ll try. I really want to."
                                        BM "I..need to see you every day to make my life mean something.."
                                        MC "I’ll keep the window open for you."
                                        BM "Really? You'd still do that for me?"
                                        MC "Of course."
                                        show bm explanation
                                        BM "Thank you..and.. goodbye [mc]."
                                        MC "Goodbye Howard."
                                        scene black with fade
                                        #sfx


                        "Do we have a hidden trap door somewhere?":
                                scene attic:
                                                parallel:
                                                    ease .5 zoom 1.3
                                                parallel:
                                                    yalign 0.0
                                                    linear 0.0 yalign 0.85 xalign 0.5

                                #zoom left to right
                                MC "(Yea, I didn’t think so.)"
                                scene attic with fade
                                MC "(Maybe I should clean a little so I can actually find something?)"
                                MC "(I can just use this rag.)"
                                MC "(Wait, this isn’t a rag.)"
                                extend "(It’s my scarf!)"

                                scene bedroomnight with fade
                                pause 1
                                scene black with fade
                                "..."
                                MC "(I can’t sleep.)"
                                MC "(It’s been 2 days since that bird man, Howard, has broken into my room.)"
                                MC "(And also 2 days since he’s ruined my sleeping schedule, now I feel tired during the day but can’t sleep at night.)"
                                MC "(This sucks.)"
                                #knock
                                MC "(?)"
                                BM "H-hello? It’s me? Howard..? If you even remember me..?"
                                MC "(Well I’ve got nothing better tonight.)"
                                scene night with fade
                                show bw bird
                                show window
                                MC "Give me a minute, I need to grab a few things."
                                BM "Oh! You do remember me..!"
                                BM "Take your time, I can wait."
                                #openchest, knife
                                MC "Hm."
                                #close
                                MC "Alright, you can go in now."

                                scene bedroomnight3 with fade
                                show bm bird:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                BM "Thank you for letting me in!"
                                MC "So you really are a bird."
                                BM "Yea! Unless..you find that displeasing?"
                                MC "I don’t mind, talking to a bird is pretty cool."
                                BM "Don’t you find it scary..?"
                                MC "What’s the scary part?"
                                BM "I..I don’t quite understand the details but most people seem to either despise my existence or fear me..?"
                                MC "What did you do?"
                                show bm bird:
                                        linear 0.050 yoffset +10
                                        linear 0.050 yoffset -10
                                        linear 0.050 xoffset +10
                                        linear 0.050 xoffset -10
                                BM "I don’t know!"
                                MC "Maybe I should tie you up again, just in case."
                                MC "But I can’t really tie up a bird huh?"
                                show bm bird:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                BM "No problem! I can change into my human form."
                                BM "C-can you close your eyes first?"
                                MC "Don’t want to. What if you do something?"
                                show bm bird:
                                        linear 0.050 yoffset +10
                                        linear 0.050 yoffset -10
                                BM "I won’t!"
                                #knife
                                show mc knife
                                MC "Fine, but don’t make me regret it."
                                scene black with fade
                                BM "Eek! That knife of yours always scares me..."
                                MC "Well? Get on with your transformation, my eyes are closed."
                                BM "Right, sorry!"
                                #sfx
                                BM "I’m done. You can open your eyes again?"

                                scene bedroomnight3 with fade
                                MC "Are you ever gonna let me see you transform? It seems pretty cool."
                                show bm explanation
                                BM "Uhh n-no. It’s sort of grotesque actually."
                                menu:
                                        "Even better.":
                                            show bm idia:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                            BM "B-better?!"
                                            MC "Now I’m really curious."
                                            show bm swpose:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                            BM "Y-you can’t! P-please..?"
                                            BM "I don’t think my heart is ready for that..!"
                                            MC "{i}Really?{/i}"
                                            show bm idia:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10        
                                            BM Y"es really! Now can you please tie me up already?"
                                            MC "You like being tied up that much?"
                                            show bm idia:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                                linear 0.050 xoffset +10
                                                linear 0.050 xoffset -10
                                                repeat 2
                                            BM "Wh-what..?! No! Uhh..That’s not what I was trying to say.."
                                            MC "So? What were you trying to say?"
                                            show bm finger
                                            BM "Uh..I..uh.."
                                            BM "Nevermind..just do it already..."
                                            MC "Sure sure."
                                    
                                        "Oh, got it. I won’t pry.":
                                            show bm explanation
                                            BM "Really? You understand?"
                                            MC "Yea. If you don’t want me to see then I won’t."
                                            show bm explanation:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                            BM "Why thank you! Y-you’re really sweet.."
                                            MC "Sweet? I’m about to tie you up here."
                                            show bm swpose:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                            BM "G-go ahead! I know you won’t hurt me."
                                            MC "Are you sure about that?"
                                            show bm swpose
                                            BM "Y-you won’t right?"
                                            MC "Who knows?"
                                            show bm explanation
                                            BM "W-well I guess you can hurt me a little..?"
                                            MC "I’m just teasing. I won’t hurt you , or at least I’ll try?"
                            
                                scene tiedupcg with fade
                                MC "There, all done!"
                                MC "Is it too tight? I can loosen it a little if it is."
                                BM "N-not at all! You’re very gentle with me."
                                MC "If this is gentle, I don’t want to know what your daily life is like."
                                BM "It’s not that bad..! I..think?"
                                MC "That’s a little concerning."
                                BM "I-it’s not, really! You don’t need to be concerned about me."
                                MC "Okay then, I'm taking off your mask now."
                                BM "M-must you do it again? You already saw my face yesterday.."
                                MC "Our time was cut short, I want to see it again."
                                BM "Can I keep it on, please..?"
                                MC "How about this, I take off your mask tonight and I don't it for the rest of your visits?"
                                MC "Last time I'll see your face, I swear."
                                BM "I..suppose that would be fine..?"
                                MC "Alright, I'm taking it off"
                                BM "Do as you please"
                                scene tiedupinquirecg with fade
                                BM "So..?"
                                MC "Well you're definitely was less scary without the mask" 
                                BM "Anyway, I suppose you have questions for me..?"
                                MC "I do."
                                BM "W-well, what is it?"
                                MC "Would you say you’re more bird or human?"
                                scene sdtiedupcg
                                BM "Umm..I’m not sure."
                                MC "What’s the default?"
                                scene tiedupworrycg
                                BM "W-well you haven’t seen it yet but during the day I tend to exist in another form."
                                BM "A more monstrous, frightening form as one might say."
                                menu:
                                        "Cool, can you visit me during the day?":
                                            scene tiedupscaredcg
                                            BM "P-pardon? You want to see that form..?"
                                            MC "Definitely."
                                            scene sdtiedupcg
                                            BM "But aren’t humans normally frightened by monsters like me..?"
                                            MC "I don’t know, I haven’t seen how scary you could be."
                                            MC "Especially when I can tie you up so easily."
                                            BM "Uhh..That might be a hard request.."
                                            scene tiedupworrycg
                                            BM "Travelling here is much easier to do when the world is shrouded by darkness."
                                            MC "Right, I guess hunters might try and shoot you down if they ever saw you."

                                        "Are your transformations affected by daylight?":
                                            scene tiedupinquirecg
                                            BM "I’m not quite sure myself, but I do find that my human form is much easier to maintain once the sun goes down."
                                            BM "The same goes for that smaller bird-like form."
                                            MC "Interesting."
                                            MC "So, how do you search for food?"
                                            BM "I don’t. I’m kept in a cage most of the time."
                                            MC "Whoa what?"
                                            scene tiedupsurprisedcg with vpunch
                                            BM "(!)"
                                            scene tiedupscaredcg
                                            BM "Nevermind, forget I said anything..!"

                                scene tiedupinquirecg
                                BM "In any case, your place is actually much safer than any other place I’ve been to."
                                MC "In what way?"
                                BM "Well, there’s not a lot of people here. So I can still stay hidden and no one will attack me, right?"
                                MC "I guess?"
                                show mc knife
                                MC "Just don’t forget that I still have this knife."
                                hide mc
                                BM "But you won’t hurt me for no reason right? You’ll only use it if I attack you first?"
                                MC "That’s right."
                                BM "And even if I am tied up, I should be able to break free fairly easily."
                                BM "So it’s not too presumptuous of me to think that I’m safe, r-right?"
                                MC "Well if you put it that way, I guess you’re right?"
                                scene black with fade
                                MC "(I don’t how he normally goes through his life and honestly I’m too scared to ask at this point.)"

                        "What’s underneath those curtains?":
                                #fabric
                                MC "(Oh it’s like a secret hide out!)"
                                MC "(If I took him here then I guess that explains why this area has less dust.)"
                                MC "(And one of his feathers.)"
                                scene black with fade
                                pause 1
                                scene bedroomnight3 with fade
                                show bm swpose
                                BM "Hello, [mc]?"
                                show bm surprised:
                                        linear 0.050 yoffset +10
                                        linear 0.050 yoffset -10
                                        linear 0.050 xoffset +10
                                        linear 0.050 xoffset -10
                                        repeat 3
                                MC "BOO!"
                                show bm idia
                                BM "(!!)"
                                #sfx
                                BM "[mc]..? Is that you?"
                                MC "Woops sorry, are you hurt?"
                                show bm swpose
                                BM "N-no, just a little spooked. What’s with the sheet over you?"
                                MC "I thought it’d fit today’s theme but I guess it was too much? Or was it too little? MC I’ve never been good at imitating ghosts."
                                show bm explanation
                                BM "No, it wasn’t too much. But what’s this about a theme?"
                                MC "It’s All Hallow’s Eve. Haven’t you heard of it?"
                                BM "IO’m afraid not, is it famous around here?"
                                MC "It is! There’s normally a festival of sorts in the village but this year it was cancelled."
                                MC "So, I figured I’d celebrate with you to make up for it. Unless you don’t want to?"
                                show bm swpose:
                                        linear 0.050 yoffset +10
                                        linear 0.050 yoffset -10
                                BM "Not at all..! It sounds fun. I’m happy you’ve decided to involve me in this."
                                MC "Great, we’re going somewhere today."
                                show bm idia:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                BM "W-what?!"
                                BM "I don’t want to go outside, what if someone sees me?"
                                MC "That’s why we’re not going outside. "
                                show bm explanation
                                BM "So, where are we going?"
                                MC "Just across the hall, in the attic."
                                BM "Oh.! That’s exciting, I’ve never been there."
                                MC "It’s not much but I did clean up a bit before you got here. Let’s go."
                                #sfx
                                scene hallwaynight with fade
                                pause 1.5
                                #sfx
                                scene attic with fade
                                MC "Welcome to the attic."
                                show bm swpose
                                BM "..."
                                MC "Uhh, Howard? You okay?"
                                BM "I-I’m fine, it’s just.."
                                show bm explanation
                                extend "I’ve never been in a room like this before."
                                BM "Or at least, I haven't see one in a long time."
                                MC "You don’t have an attic?"
                                show bm swpose
                                BM "If I did, I wouldn’t know. I don’t explore the place much."
                                MC T"hat’s a shame. Anyway, let’s go over there."
                                show bm explanation
                                BM "Under those curtains..?"
                                MC "Yep. I promise I washed them a few days ago."
                                BM "I see."
                            
                                scene curtains with fade
                                show bm swpose:
                                        parallel:
                                            ease .5 zoom 1.5
                                        parallel:
                                            yalign 0.0
                                            linear 0.0 yalign 0.0 xalign 0.5

                                MC "I hope you’re not too scared of the dark? I only have this candle for lighting."
                                BM "I’m used to it."
                                show bm explanation
                                BM "So, enlighten me. What does one do on All Hallow’s Eve?"
                                MC "Well normally I’d visit the festival with my family and we’ll dress up as ghosts like I’m doing right now."
                                MC "But since this year that was cancelled, I figured we can swap scary stories?"
                                show bm swpose
                                BM "Scary stories..?"
                                MC Y"ea, do you have any?"
                                show bm explanation
                                BM "I suppose I can share a few details about my life..?"
                                menu:
                                        "Is your life that scary?":
                                            show bm swpose
                                            BM "Well.."
                                            BM "..."
                                            show bmexplanation
                                            BM "I suppose I can tell a made-up story?"
                                            MC Y"ea, that works!"
                                            scene curtain with fade
                                            show bm explanation:
                                                    parallel:
                                                        zoom 1.5
                                                    parallel:
                                                        yalign 0.0
                                                        linear 0.0 yalign 0.0 xalign 0.5

                                            BM "Ever since then, the villagers say that they were never seen again..."
                                            MC "Spooky. Ready for my turn?"
                                            BM "Go ahead."
                                        "I was expecting local legends and myths." :
                                            show bm swpose
                                            BM "I..I don’t know any."
                                            MC "Want me to go first?"
                                            show bm swpose:
                                                    linear 0.050 yoffset +10
                                                    linear 0.050 yoffset -10
                                            BM "Yes, please!"
                                            scene curtain with fade
                                            MC "And so, they would be cursed to spend their lives wandering aimlessly through the woods.."
                                            show bm finger
                                            BM "It’s not a real story, is it, [mc]?"
                                            MC "Well I sure hope not. I made it up just now."
                                            show bm explanation
                                            BM "Can I tell mine now ?"
                                            MC "Go ahead!"
                            
                                scene black with fade
                                pause 1 
                                scene curtains with fade
                                show bm swpose:
                                        parallel:
                                            ease .5 zoom 1.5
                                        parallel:
                                            yalign 0.0
                                            linear 0.0 yalign 0.0 xalign 0.5
                                MC "I think I’m out of stories now."
                                show bm explanation
                                BM "I may have one final tale, may I?"
                                MC "Sure."
                                BM "It’s not really a tale, more like an anecdote?"
                                MC "Okay?"
                                BM "Whenever I fly to your place, I would always pass the woods. They stretch for quite a bit so it’s inevitable that I’d occasionally need to catch my breath."
                                BM "Once in a while, I’d land near a house in the woods. Its gates were made of bones which were lit on fire, and the house itself will move whenever you approach."
                                MC "How?"
                                BM "I wish I knew."
                                BM "But luckily, there lives a sweet old lady in the house! Her appearance does seem to shift ever so slightly from visit to visit but she’s not fond of talking about herself so I can’t confirm."
                                MC "A sweet old lady who lives in a house with flaming bones around it?"
                                MC "Are you sure she’s sweet?"
                                show bm swpose
                                BM "Well she hasn’t hurt me and she hasn’t ignored me either, so she seems... nice?"
                                MC "I see. What else?"
                                BM "That’s it really, I simply wanted to tell you but haven’t had the chance."
                                MC "In that case, thanks for telling me."
                                BM "The pleasure is all mine."
                                show bm finger
                                BM "May I move closer to you..?"
                                MC "Of course."
                                show bm swpose:
                                        parallel:
                                            ease .5 zoom 1.5
                                        parallel:
                                            yalign 0.0
                                            linear 0.0 yalign 0.0 xalign 0.5
                                #sfx, zoomsprite
                                MC "So what’s up?"
                                BM "Nothing much, but I do have a few things to tell you..and also a question.."
                                BM "Hopefully, I get more than one this time..?"
                                MC "Sure, ask away."
                                BM "So..umm..when I said I came here because I was desperate for any kind of positive interaction.."
                                BM "There were..other reasons I didn’t tell you."
                                MC "Like what? You ran from home or something?"
                                show bm idia:
                                                linear 0.050 yoffset +10
                                                linear 0.050 yoffset -10
                                                linear 0.050 xoffset +10
                                                linear 0.050 xoffset -10
                                BM "You knew?!"
                                MC "I was joking! I didn’t think you were actually on the run!"
                                show bm swpose
                                BM "Well..I am or at least I try to, but..it finds me everytime.."
                                MC "Who is ‘it’?"
                                BM "I-I..I’m not at liberty to say.."
                                BM "But I wanted to tell you that my freedom ends in a few months month and I won’t be able to visit anymore."
                                MC "Why?"
                                BM "I can’t tell you.."
                                MC "Would telling me put your life at risk?"
                                BM "Maybe..? But honestly, it’s more likely to put {i}you{/i} at risk.."
                                extend "and I really don’t want that."
                                MC "How would it put me at risk?"
                                BM "As I said, I can’t tell you."
                                show bm explanation
                                BM "And..I know it’s unreasonable of me to ask this, but if I am in trouble.."
                                BM "Would you mind visiting my home?"
                                menu:
                                        "Of course I’d visit.":
                                            show bm finger
                                            BM "R..really? Even if it’s quite far..?"
                                            MC "I’d go to the edge of the world to see you."
                                            show bm idia:
                                                    linear 0.050 yoffset +10
                                                    linear 0.050 yoffset -10
                                                    linear 0.050 xoffset +10
                                                    linear 0.050 xoffset -10
                                            BM "(!!!)"
                                            BM "[mc], are you sure about this?"
                                            MC "Of course I am."
                                        "How far is your house?":
                                            MC "I mean, you visit me every night so it can’t be that bad but how far is it?"
                                            show bm explanation
                                            BM "I..it’s much further away than here."
                                            MC "Oh."
                                            MC "Then again, you did say that this is in case you were in trouble."
                                            MC "I guess I’ll try."
                                            show bm swpose:
                                                    linear 0.050 yoffset +10
                                                    linear 0.050 yoffset -10
                                            BM "Y-you will..?!"
                                            MC "I’ll try, even if you live at the edge of the world."
                                            show bm idia:
                                                    linear 0.050 yoffset +10
                                                    linear 0.050 yoffset -10
                                                    linear 0.050 yoffset +10
                                                    linear 0.050 yoffset -10
                                            BM "(!!!)"
                            
                                scene black with fade
                                #add voice line
                                centered "[mc], I-I love you..!"
                                scene attic with vpunch
                                MC "(!!)"
                                MC "(That was unexpected..)"
                                MC "(But also, what happened next?)"
                                MC "(Curse my lack of memories and whoever caused it!)"

                        "I’m done with the attic.":
                            jump afterattic
label afterattic:
    MC "(I should go to sleep before my family returns.)"
    #sfx(door/steps)
    scene hallwaynight with fade
    #sfx
    scene bedroomnight with fade
    #sfx(fabric/pillow)
    scene black with fade
    "..."
    #birdsfx, door
    MC "(Someone’s in the room.)"
    Y "Is [mc] asleep?"
    B "I believe so."
    B "If you have something to say, we should talk outside. I don’t want [mc] to hear."
    Y "I’m not gonna let you brush me off anymore. I need to say it."
    Y "You think [mc]’s caught on to the truth of that night?"
    B "If you stay silent, [player_gender] won’t."
    Y "We spiked [player_possessive] drink so [player_gender] wouldn’t wake up that night."
    Y  "We stuck blades to [player_possessive] window, there’s little slits in the window sill! [player_gender] WILL catch on."
    MC "(So it wasn’t me!)"
    B "We already cleaned the blood off the windows, replaced the broken parts and tore every reminder of him down,  [player_gender] won’t if you can {b}shut up{/b}."
    Y "We can’t hide this for long. If we can’t kill that thing by..I don’t know, tonight?? [mc] will soon recover all [player_possessive] memories and {b}leave{/b} us."
    B "We can’t be sure about that."
    Y "That witch we visited said that those memories will return when they see something that triggers a memory."
    Y "[mc] spent so much time in this room with that monster, that I’m sure  [player_gender]’ll recover [player_possessive] memories the moment they saw {i}anything{/i}."
    MC "(Oh, SHE KNOWS.)"
    B "No, [player_gender] won’t."
    Y "Don’t delude yourself, [mc]’s a lot smarter than I am. If the truth is ever revealed, [player_gender]’ll go out and chase after that monster all on [player_possessive] own."
    B "That won’t happen, we shoved most of [player_possessive] clothes into the attic and we hid the key. [mc] won’t have anything useful."
    Y "Any idiot can find that key, even I can find it."
    B "That’s because {i}you{/i} hid it."
    Y "It doesn’t matter, I {b}know{/b} that [mc] will find out soon enough."
    B "THAT WON”T HAPPEN!"
    "..."
    Y "Look who’s raising her voice now."
    B "{b} I will do anything to protect our little [player_fm]. Don’t get in my way{/b}"
    Y "I’m not, I’ve been helping so far."
    Y "But you need to consider the possibility tha-"
    B "I’m leaving."
    #doorsfx
    "..."
    MC "(Did they leave?)"
    scene bedroomday with fade
    B "{size=-10}tired…later..{/size}"
    #doorclosesfx
    MC "(I think they went into their room.)"
    MC "(I can’t be too sure though.)"
    #camera to window
    MC "(So it really wasn’t me.)"
    MC "(It was my sisters who tried to keep him away from me.)"
    MC "(But now I know it wasn’t out of malice, it’s because they were worried about me.)"
    MC "(I don’t know why I doubted that they were my sisters.)"
    MC "(Although..)"
    MC "(Whether Howard really is a monster or not is still unknown to me though.)"
    scene cg2 with fade
    #corespondingvoicelinehere
    BM "Let me in."
    BM "LET ME IN"
    #editedvoiceline
    MC "(What was he saying here..?)"
    MC "(If only I can remember.)"

    scene bedroomday with fade
    MC "(What do I do now?)"
    MC "(I can try and visit the witch and hope I’ll find a way to retrieve the rest of my memories.)"
    MC "(Or I can stay home with my sisters like I always have..?)"
    MC "(I’d like to think Howard is as sweet as I remember him but without all my memories I can’t be sure.)"
    menu:
            "I’ll stay home until I recover the rest of my memories, I can’t put all my faith in him.":
                jump ed1
            "I can’t stay here any longer, I {b}need{/b} to see Howard again.":
                jump othereds

label ed1:
    MC "(Even I know that falling in love with a shape shifting bird man isn’t the most rational decision.)"
    MC "(If he really loved me he’ll come back and I’ll leave the window open for him.)"
    MC "(Like I’ve always done.)"
    MC "(But..)"
    extend "I need to talk to my sisters first."
    scene hallwayday with fade
    MC "(Which one’s their room again?)"
    #steps
    MC "(I think..It’s this one.)"
    #knock
    B "I said we’ll talk later."
    MC "Sorry?"
    B "(!)"
    #door
    show c sorry
    B "[mc]? You’re awake?"
    MC "Yea. I know that you’re tired but I have something to say, can you please listen to me?"
    MC "I can come back later?"
    show c happy
    B "No, I can talk now. I’ll always make time for you."
    MC "(!)"
    MC "(She smiled.)"
    MC "(How could I ever forget about my caring eldest sister, Cathy?)"
    MC "(It’s as if all the fog surrounding them disappeared, leaving me with the bare truth.)"
    MC "(The person in front of me is my sister who’s trying to keep me out of danger in her own way, not a stranger keeping secrets.)"
    MC "(She’s gotten more ragged recently, probably from all the worrying she’s done about me.)"
    show c normal
    C "Would you like to call Elizabeth as well?"
    MC "Absolutely."
    scene hallwayday with fade
    #knock
    MC "Lizzie! It’s me [mc]!"
    #doorslam
    scene hallwayday with vpunch
    show e happy
    E "Really?! You’re awake!"
    E "Now that I think about it, it's been a while since you've called me by name!"
    show e smile
    MC "Yea It has, I’d like to talk to you and Cathy. Is now a good time?"
    show e happy
    E "When is it {i}not{/i} a good time?"
    show e smile
    MC "(Oh Lizzie, as energetic as ever.)"
    MC "(It’s been a while since I was able to look her in the eye like this.)"
    show e smile at left
    show c normal at right
    C "So, what would you like to say?"
    E "Yea, It’s been a while since we’ve spent time like this."
    MC "I..."
    extend "know what you’ve done."
    show c sorry
    C "It’s not-"
    MC "I know, you’re worried about me. But it’s okay, because I still love you guys and I’m not leaving."
    C "R-really?"
    show c silent
    MC "I know you stuck blades on the window to keep Howard away and I’m mad about it."
    MC "But I’d like you to trust me a little on this, I’d like you to meet him someday."
    MC "If he ever comes back that is."
    show e happy
    E "So the monster has a name?"
    show e sorry
    MC "He’s not a monster!"
    MC "Or..maybe he is but I swear he’s really sweet!"
    MC "And I’d like you to meet him one day, if the opportunity ever came."
    show c sorry
    C "I see what you’re going for, [mc]. But honestly, I’m not quite sure he’ll ever come by again after what we’ve done to him."
    show e sorry
    E "I hate to say it but there sure was a lot of blood on the window."
    MC "I’m not sure if he’ll visit either, but he used to visit every night."
    MC "So I’m holding out on the chance that he’ll come by again some day."
    MC "I’m sorry I’ve been keeping secrets for so long but I didn’t think you’d be fine with me chatting the night away with a guy you don’t know."
    MC "And I guess that decision brought us to this moment."
    C "[mc]..I’m really sorry too. I’ve done things that might be unforgivable, I visited a witch to make you lose your memories, I’ve lied about a lot of things, and I never quite considered your feelings throughout all of it."
    E "Don’t fully place the blame on yourself! I was in it too.."
    E "I’m sorry too [mc]. It can’t bring him back but I hope you can forgive us..?"
    MC "Of course I do."
    MC "I don’t know about Howard though."
    show e happy
    E "Tell you what [mc], if he doesn’t turn out to be evil. We’ll apologize a hundred times to him."
    show c happy
    C "We’ll welcome him with open arms."
    MC "That’s the best outcome I can ask for at this moment."
    MC "(I don’t know how things will go in the future.)"
    MC "(I don’t if Howard will ever visit me ever again.)"
    MC "(In fact, I’m not sure if he’s still alive.)"
    MC "(But I won’t lose hope because I still have my family with me and I know they’ll love me no matter what.)"
    "ENDING 1 : Maybe Someday He’ll Return"

label othereds:
    MC "(I’ll definitely see him again, I’ll go to him no matter where he is.)"
    scene hallway with fade
    "..."
    MC "(It’s quiet.)"
    MC "(I hope my sister’s are asleep by now.)"
    scene attic with fade
    #wardrobesfx
    MC "(Glad I searched the attic, I wouldn’t have known that I have these otherwise.)"
    #fabricsfx
    MC "(There we go, all warm.)"
    #doorsfx
    scene hallwayday with fade
    pause 1
    scene kitchen with fade
    MC "(I should bring some food with me.)"
    NO "[mc]? What are you doing?"
    scene kitchen with vpunch
    MC "(!!!)"
    MC "(Crap, someone’s still awake!)"
    show d happy
    D "[mc], are you leaving somewhere?"
    MC "No, I’m just going for a walk."
    show d happy
    D "[mc], I think we all know that you’re carrying too many things for it to just be a walk."
    D "Are you perhaps thinking about seeking out the monster yourself?"
    show d normal
    MC "Well.."
    MC "Yes I am. Is it that obvious?"
    show d happy
    D "Indeed."
    show d normal
    MC "Are you going to stop me from leaving? I figured my sisters wouldn’t be very happy if they found out."
    show d happy
    D "Not at all. In fact, you should bring this loaf of bread for your journey."
    show d normal
    MC "You’re not mad?"
    show d happy
    D "Of course not, I know you have good instincts. If you think that the monster wasn’t all that bad then you might be right."
    show da smile
    "At that moment, it was as if time had stopped and the fog that had covered my head slowly lifted itself. Not enough for it to fully clear, but enough for me to finally recognize the person in front of me."
    MC "(That’s not just a bearded man who lives in the same house as me. He really is my dad.)"
    show da open
    DA "Besides, it’s not like your sisters haven’t secretly snuck out before."
    show da smile
    MC "They have?"
    show da open
    DA "Of course, something about visiting a witch? I’m not too sure about the specifics but I’ve chosen to trust all of you."
    show da smile
    show da open
    MC "(So he knew about that too.)"
    DA "You’re now an adult who’s ready to spread [player_possessive] wings."
    show da smile
    MC "Thanks Dad."
    show da open
    DA "Here, bring some food with you."
    DA W"ill your journey be long?"
    show da smile
    MC "I don’t know."
    show da open
    DA "Stay safe [mc], we’ll still be here waiting for you."
    show da smile:
                parallel:
                    ease .5 zoom 1.8
                parallel:
                    yalign 0.0
                    linear 0.0 yalign 0.0 xalign 0.5
    #zoom
    show da open
    DA "Oh? You haven’t hugged me since you were a kid."
    show da smile
    MC "Thanks dad, I wouldn’t be able to do this without you."
    show da open
    D "Of course, [mc]."
    #zoomout
    show da smile:
        parallel:
            ease .5 zoom 1.0  
        parallel:
            yalign 0.0
            linear 0.0 xalign 0.5 yalign 0.5

    MC "See you again someday."
    D "Good bye, [mc]."

    scene kitchen with fade
    MC "(I haven’t been outside for a while.)"
    #paper
    MC "(“Witch Hut, head north into the forest until you see a house, it might move so call out to it”)"
    MC "(It sounds unreal but if both Howard and my sisters have visited this place before then it can’t possibly be fake)"
    #
    MC "(Now, time to head north.)"
    #give black fadeout to bg for seamless movement
    scene forest with fade
    #sfx,steps,bushes,wind
    show forest:
        parallel:
            ease .5 zoom 1.2
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.5
        linear 0.050 xoffset -0
        linear 0.050 xoffset +0
        linear 0.050 yoffset -5
        linear 0.050 yoffset +5
        repeat 2
    MC "(The woods sure look scarier once you’ve actually entered them.)"
    #repeatcode&sfx
    show forest:
        parallel:
            ease .5 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.5
        linear 0.050 xoffset -0
        linear 0.050 xoffset +0
        linear 0.050 yoffset -5
        linear 0.050 yoffset +5
        repeat 2
    "..."
    #rp
    show forest:
        parallel:
            ease .5 zoom 1.4
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.5
        linear 0.050 xoffset -0
        linear 0.050 xoffset +0
        linear 0.050 yoffset -5
        linear 0.050 yoffset +5
        repeat 2
    "..."
    scene forest with fade
    MC "(It’s gotten darker.)"
    show rain1
    show rain2
    MC "(And now it's raining, {i}great{/i})"
    scene forest with fade
    MC "(I really hope I’m heading in the right direction)"

    scene hutoutside with fade
    show rain1
    show rain2
    #if we can figure out particles make it rain here
    MC "(Is that..?)"
    MC "(I think that’s the witch hut. If nothing else, it really does have the fence made of flaming bones.)"
    #rpcode,zoom1.4, sfx
    show hutouside:
        parallel:
            ease .5 zoom 1.4
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.5
        linear 0.050 xoffset -0
        linear 0.050 xoffset +0
        linear 0.050 yoffset -5
        linear 0.050 yoffset +5
        repeat 2
    show rain1
    show rain2
    pause 0.5
    scene hutoutside with vpunch
    show rain1
    show rain2
    MC "(!!!)"
    MC "(The hut, it moved further away.)"
    #paper
    MC "(“it might move so call out to it”)"
    MC "(Worth a shot.)"
    MC "Excuse me! Witch hut? May you allow me to enter?"
    #wind
    "..."
    MC "(I guess the witch hut can’t talk.)"
    MC "Excuse me? If anyone resides in that house, may I enter?"
    #door
    scene witchhutoutside2
    MC "(There’s someone inside!)"
    WI "What is someone like you doing at this time of night?"
    MC "I come to ask for help, if I may. I’m looking for someone and it seems that my sisters have wiped my memories of him."
    MC "If it isn’t too much, I’d like it if you could help me recover what I’ve lost so I can reunite with him."
    WI "And who is this person that you seek out?"
    MC "He’s someone dear to me. If what remains of my memory of him are correct, he may have visited you? His name’s Howard."
    WI "Howard..?"
    MC "Yes."
    MC "I’m not sure how secret this information is but he can transform into a bird?"
    WI "I see, you must be [mc] then."
    MC "You know me?"
    WI "Indeed, he has spoken favourably about you."
    MC "I’m glad to hear that but I doubt he’ll ever say nice things about me again."
    WI "And why not?"
    MC "The last time he visited he was wounded by knives on my window."
    WI "Did you not help him?"
    MC "I was asleep and I couldn’t wake up."
    WI "Do you perhaps have two sisters?"
    MC "Yes I do."
    WI "I see your predicament, you may enter. The morning is wiser than the evening."

    scene hutinside with fade
    MC "Thankyou for letting me in. Are you sure I can be here? I'm pretty dirty from the trip.."
    show wi normal
    WI "Don’t worry about such things. You may rest here for the night."
    MC "What shall I address you as?"
    WI "Call me grandmother."
    MC "As you wish, grandmother."
    MC "How will I ever pay you back?"
    WI "Save Howard. That’s the only thing you can do."
    MC "Save him? From what..?"
    show wi hand
    WI "Given that I aided your sisters in sealing your memory, I shall now undo the effects."
    WI "Now sleep, I can’t work my magic while you’re awake."
    MC "Of course. Goodnight grandmother."
    WI "Sleep well."

    scene black with fade
    #bgm: https://dova-s.jp/EN/bgm/play22027.html

    pause 0.5
    show b happy
    B "[mc], before you head to sleep, would you like to drink with us?"
    show y happy at right
    show b silent at left
    Y "It’s just milk, it shouldn’t keep you awake at night."
    show y smile
    MC "I’m feeling really sleepy now, I don’t th-"
    show y happy
    Y "Pleasee? We haven’t spent much time together recently."
    show b happy
    B "I’m inclined to agree. Can we have just ten minutes of your time to chat?"
    Y "We can add honey into the milk if you’d like?"
    show y smile
    show b silent
    MC "Fine, I guess you’re right."
    MC "I do miss you guys.."
    MC "And you two haven’t been around the house much either."
    show b happy
    B "Exactly, we’ll be making up for lost time."
    #clink
    MC "Well, cheers."

    scene kitchen with fade
    show y happy
    Y "How’s the milk? Not enough honey?"
    MC "(My head feels kinda heavy..)"
    MC "It’s good. But I guess warm milk does make you kind of sleepy?"
    show y smile at right
    show b happy at left
    B "I understand the feeling, I think I’ll head to bed early."
    show y happy
    Y "Me too."
    MC "I guess that makes all of us."
    MC "Goodnight everyone. Sweet dreams."

    scene black with fade
    #wind
    MC "(I can’t open my eyes.)"
    #witch hut dream scene
    scene cg2 with fade
    BM "Let me in."
    MC "(Howard!)"
    #brutal stabbing, layer w/ wood noise?
    BM "LET ME IN!"
    #rattling, window breaking, stabbing noise

    BM "T-that’s a lot of blood.."
    BM "H-hey, did you get sick of me already..?"
    MC "(No, I haven’t!)"
    BM "I..I thought y-you wouldn’t do that to me.."
    BM "D..do you really not care anymore? P-please..tell me.."
    BM "Why won’t you wake up..?! Pl–please help me.."
    BM "[mc]..P-please..I thought you loved me.. Have I been fooled this whole time..?"
    BM "Even when I’m bleeding like this my voice still can’t seem to reach you. Is this the end of us..?"
    BM "So be it then, I’ll leave."
    BM "If you ever wish to find me you’ll have to head north, search through three times nine countries at the edge of the world."
    BM "A-are you still not listening to me..?"
    BM "I’m really leaving."
    "..."
    BM "Fine, I understand."
    #feathersfx

    scene insidehut with vpunch
    MC "(!!!)"
    show wi normal
    WI "You’re awake, how are you feeling?"
    MC "Like I’ve been kicked by a horse."
    WI "Now that’s a new one, everyone seems to say different things when they wake up."
    WI "I suppose you have many questions surrounding him?"
    MC "I do. May I?"
    show wi hand
    WI "Go ahead dear." 
    MC "So, what is Howard really?"
    show wi normal
    WI "Who knows, at best I can only say that he is a magical creature."
    show wi hand
    WI "He may have been human at some point but those days are long gone."
    MC "Just to make sure, he really is at the edge of the world right now?"
    MC "He told me to go to the edge of the world if I wanted to find him."
    show wi hand
    WI "Indeed, he currently resides with his betrothed in a castle at the edge of the world."
    MC "{b}His betrothed?{/b}"
    show wi normal
    WI "Yes."
    show wi hand
    WI "The creature he’s marrying, is cruel and has no care for the beings around it. It wants to steal his power and it has kept him locked in a cage for many decades."
    WI "The moment he is wed to the creature, he will be bound to the castle for eternity."
    #ngeloop ampe kelar semua
    menu:
            "Wait, if he’s locked in a cage, why could he visit me at night?":
                WI "He snuck out. The creature sleeps at night so it’s an ideal time."
                show wi normal
                WI "But no matter how careful he is, it’ll find out eventually."
                MC "Is that why the number of missing villagers started rising? Because it was trying to find Howard?"
                MC "I believe Howard has mentioned that they now work in the castle?"
                WI "Indeed they do. The creature has sucked the life out of them to make itself stronger, they currently live as empty shells of their former lives."
            "Why hasn’t the creature done anything to him? Why wait decades?":
                show wi normal
                WI "It’s waiting for the right conditions. Soon enough, the moon will shine a brilliant blue."
                WI "Under that moon, the creature will finally be able to absorb Howard’s power."
            "And what is this creature?":
                show wi normal
                WI "I can’t speak its name, as it will hear me the moment I do."
                MC "(I guess that explains why Howard never went into details.)"

    WI "In any case, I’d like it if you could rescue him from his fate. Marry him, only then will he be free from its grasp."
    MC "I will."
    show wi hand
    WI "You better, I’d rather have him marry someone who has traveled months to see him."
    show wi normal
    MC "True that."
    MC "(WAIT.)"
    scene inside hut with vpunch
    MC "(MONTHS???)"
    show wi hand
    WI "What’s the matter, [mc]?"
    MC "I’ve been travelling for months??"
    show wi normal
    WI "Of course you have. Given how confused you are I can tell you didn’t realize it had been that long."
    MC "How much further is the edge of the world?"
    show wi hand
    WI "You’re almost there. Just beyond these woods is the castle you seek."
    WI "Now take this and heed my words. Once you enter the castle pretend to be a fellow servant, copy the blank stares and monotone movements."
    show wi normal
    WI "When the sun sets, approach the creature in the throne room and present these items as a trade."
    WI "The moment it lays interest in the golden saucer and its diamond ball, demand one night with your beloved in exchange."
    show wi hand
    WI "Proceed with caution, as it will use magical items to give you a disadvantage."
    show wi normal
    WI "Do you understand [mc]?"
    MC "Yes, grandmother."
    WI "Good, now hurry before they are actually wed."

    scene forest with vpunch
    MC "Wait grandmother!"
    "..."
    MC "(The hut, it’s gone.)"
    MC "(I don’t have any more time to waste, I should hurry to the castle.)"
    #running sfx
    show forest:
        parallel:
            ease .5 zoom 1.4
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.5 xalign 0.5
        linear 0.050 xoffset -0
        linear 0.050 xoffset +0
        linear 0.050 yoffset -5
        linear 0.050 yoffset +5
        repeat 6
    #insert effect from earlier, repeat 6?
    MC "(I’ll be there soon Howard, I swear.)"
    scene castlefront with fade
    MC "(Is that..the castle?)"
    MC "(I guess grandmother did say it was just beyond these woods.)"

    scene castleinside with fade
    #gatesfx
    MC "(This is it, I’m finally here.)"
    "..."
    MC "(I know that there’s a lot people here but the silence prevails.)"
    MC "(Copy their movements, [mc])"
    scene castleinside with vpunch
    #bump
    MC "I’m sorry..!"
    MC "Wait, Mrs Jones?"
    "Her hair has lost all its luster, her eyes are blank and her complexion has developed an unnatural shade of purple."
    "Despite me bumping into her, she ignores it with ease, walking into the kitchen as if I wasn’t there at all."
    MC "(It’s like she doesn’t recognize me anymore.)"
    MC "(Is this what happens to all the missing people..?)"
    #onscreeen, crowd silhouette, hide bm behind
    show bm swpose
    show crowd
    MC "(Is that..?)"
    show crowd at offscreenright with easeoutright
    #crowd move, show bm
    hide crowd
    MC "(Howard..?)"
    #zoom, steps sfx
    MC "Howard! I’m-"
    #stomp echoing
    scene castleinside with vpunch
    MC "(!!!)"
    MC "(Nevermind, I need to hide.)"
    scene castleinside with fade
    show cr hand at left:
                        parallel:
                            zoom 0.8
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.0
    show castle wall
    #blurry asset infront, bm behind
    #kalau bisa dia beda font
    NO "You look displeased."
    BM "..."
    NO "Eat."
    BM "N-no."
    NO "I don’t think I made myself clear, {b}eat.{/b}"
    #platesfx
    BM "..."
    NO "The date is nearing, be on your best behaviour."
    BM "..."
    BM "I’m done."
    NO "Did I not make myself clear?"
    BM "I did eat. You know where I’ll be."
    NO "That’s too many words from someone like you. You will soon regret your insolence."
    NO "Now, remember to wear this."
    BM "Hm."
    MC "(Wait, what did it give him? What did it make him wear?)"
    MC "(Damn it, I can’t see.)"
    #squeak.
    MC "(CRAP.)"
    show cr hand at left:
                        parallel:
                            zoom 1.0
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.0
    #creature sprite zoom closer
    MC "(I need to get out of here.)"
    show cr hand at left:
                        parallel:
                            zoom 1.3
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.0
    #zoom closer
    MC "(NEVERMIND.)"
    NO "..."
    MC "(Stay calm.)"
    NO "..."
    #leave screen
    MC "(I think I’m safe, for now.)"
    MC "(Now I know why Howard couldn’t escape so easily.)"
    MC "(But you can do this, [mc].)"
    MC "(Probably.)"

    scene throne1 with fade
    #sfx
    "Upon entering the lavish room, I noticed that it wasn’t the creature I previously saw that was sitting on the throne. Instead, there's a human-like figure in a gown sitting cross legged."
    "It raises an eyebrow in my direction, whether it was because it thought I was rude or because I’m dirty, I’m not sure."
    MC "Excuse me? I’m looking for someone."
    NO "Yes?"
    NO "You.."
    extend "I’ve never seen you before. You’re not one of my servants." 
    NO "State your purpose."
    MC "I came from far away to propose a trade with you."
    NO "HA"
    Extend "HAHAHA"
    NO "You?"
    extend "Trade with me?"
    NO "How foolish. Do you not know who I am?"
    show throne1 with fade
    pause 1
    show throne2 with fade
    pause 1
    show throne3 with fade
    pause 1
    show throne4 with fade
    pause 1

    MC "You wouldn’t call it foolish once I show you what I have."
    NO "Oh really?"
    MC "Really."
    #sfx
    MC "In my possession lies this golden plate with a diamond ball."
    NO "..."
    NO "It moves by itself..? How curious."
    NO "I want it."
    MC "I have a price for it."
    NO "Well obviously. State your price, there’s nothing I can’t pay."
    MC "(Here goes nothing..)"
    MC "I’d like a night with your betrothed."
    NO "What?"
    extend "That’s it?"
    extend "You’d like a night with {i}that{/i}?"
    MC "Indeed, I’d like to see him."
    NO "I can offer countless other treasures, money, status, perhaps you’d even like power?"
    MC "I want a night with your betrothed, Howard."
    NO "So that’s what you're after?"
    MC "Yes."
    NO "I now see that {i}you{/i} are the one that fool has been sneaking out to see."
    NO "No wonder you smell like him, I almost mistook you for that fool."
    NO "Well, a single night with him means nothing to me. He’s still mine after this is done."
    NO "I accept your trade."
    MC "So we have a deal?"
    NO "Indeed, don’t regret it."
    MC "I won’t"

    scene cagecg1 with fade
    #stop bgm
    MC "Howard?"
    "An uncomfortable silence fills the room, broken only by the sounds of my steps towards the cage."
    "If there was another light source besides that puny torch in the corner, I can’t see it."
    MC "(Is that him? I’ve never seen him like this before.)"
    #wind
    "Now in front of me lies the man I’ve travelled all the way to the edge of the world for, sleeping silently inside a cage larger than my house with the appearance that he never allowed me to see."
    "All the greetings he used to give me are gone, replaced with an uneasy nothingness that almost makes my skin crawl."
    MC "Howard, I’m here."
    "..."
    MC "Howard, please say something."
    "..."
    MC "(He’s not responding to me. Just like I did the last time he tried to visit.)"
    #start bgm here
    #https://dova-s.jp/EN/bgm/play22027.html
    MC "(What did that thing feed him? He’s so..unresponsive)"
    MC "(In any case, I could hear what he said despite my state so I can only hope that he can hear me too.)"
    MC "Howard.."
    MC "I know that you’re not responding to me."
    extend "But please hear me out."
    MC "I’m really sorry that you had to suffer like that the last time you visited me. I swear I wasn’t the one who stuck the blades on the window, I was under a sleeping potion and I couldn’t wake up no matter how badly I wanted to."
    MC "My sisters, they placed them there because they thought you were a monster. And I know in my heart that they were wrong."
    MC "No matter how many forms you have, no matter how sharp your claws are, no matter what you think about yourself. I don’t think you’re a monster and I never will."
    MC "It doesn’t make up for what happened to you, but I’m here. I traveled three times nine countries to see you, just like you told me."
    MC "I followed you to the edge of the world and I won’t leave you ever again."
    MC "(I said a fraction of what I wanted to say but it might be meaningless if he doesn’t acknowledge me.)"
    MC "(What do I do now?)"
    #loop ky milih sayur di tsm
    menu:
            "Inspect the room for anything that can help.":
                "Looking around the room, there’s not much to be found. The creature really did give him the bare minimum to survive."
                "He lives in a cage where he sleeps on the floor with a bucket to drink from."
                "There’s a clock in this room but honestly you can’t really see it in darkness like this."
                "It’s easy to see why he thought of himself as a monster if this is how he lived for decades."
            "Enter the cage with him.":
                jump aftercage
            "Consider murdering the creature I made a deal with.":
                "I rummage through whatever pockets I have for anything that can give me a leg up in battle."
                MC "(I have this dagger but is it enough? I doubt it.)"


label aftercage:
    scene cage2cg with fade
    "Given how large the gaps in his cage are, I easily slip inside."
    "The gaps were definitely made while considering his ‘monster form’ as the only way he could leave was if he transformed into either a human or a small bird."
    MC "Howard, wake up."
    "Despite my shaking, he continues to slumber as deeply as the dead."
    MC "(I sure hope he’s not actually dead.)"
    MC "Howard?"
    MC "(He’s still breathing..That’s good.)"
    MC "(But how do I get him to wake up? I don’t have magical powers like grandmother does.)"

    scene witchhut with fade:
            matrixcolor TintMatrix(color="#d9b6ec" )
    #use tint matrix??
    show wi hand:
            matrixcolor TintMatrix(color="#d9b6ec" )
    WI "“Proceed with caution, as it will use magical items to give you a disadvantage.”"
    scene insidecastle with fade
    show bm swpose
    show cr hand at left
    show castlewall

    NO "That’s too many words from someone like you. You will soon regret your insolence."
    NO "Now, remember to wear this."
    BM "Hm."
    MC "(Wait, what did it give him? What did it make him wear?)"
    MC "(Damn it, I can’t see.)"

    scene cage2cg with vpunch
    MC "(That’s it!)"
    MC "(I need to find this thing that the creature made him wear.)"
    MC "(What is it though..?)"
    MC "(What do I check?)"

    #ky td lg
    menu:
            "The mask.":
                MC "(He wears this every time he visits so I doubt this was the magical item that the creature gave him but it doesn’t hurt to check.)"
                MC "(I mean, I’m glad I can see his bare face but it’s a shame that it has to happen in a circumstance like this.)"
                "I pick up the mask from the floor and run my fingers through every bump and crevice in an attempt to find anything that seems magical."
                MC "(It’s just a mask.)"
                MC "I never got to tell you this before, but I think your mask looks pretty cool. Did you make it yourself?"
                MC "I know you’re pretty crafty, so it’s not too far fetched right?"
                "..."
                MC "(I’ve heard of doctors who shove herbs in the beak portion of the mask but his is empty.)"
                MC "(Maybe it’s to accommodate for his actual beak?)"
                MC "(Although, if I put it up to his face it doesn’t quite fit anymore)"
                MC "(Maybe the mask isn’t the magical item?)"
            "The Veil.":
                MC "(It didn’t occur to me before but the veil does make him look like a bride.)"
                MC "(Was he forced to wear the veil? Or did he choose this on his own?)"
                MC "(He looks beautiful but if it makes him unhappy I’d want him to remove it.)"
                MC "(Wait, did it always have this hairpin?)"
                MC "(It’s gorgeous, I’ll give it that)"
                "It seemed to glimmer even within the darkness of the room, without any light for it to reflect."
                MC "(Still, who sleeps with a hairpin on?)"
                MC "Did you always sleep with a hairpin on? I’m sorry I never noticed but it looks good on you."
                MC "I am worried that it’ll stab you in your sleep though, does it hurt you?"
                BM "..."
                MC "I’ll put it next to your mask, okay?"
                "Carefully, I took out the hairpin from the veil adorning his face and placed it next to his mask."
                jump labelhairpinremove
            "The gloves.":
                "Given that he currently has wings {i}and{/i} massive claws, his gloves are placed neatly next to his mask."
                MC "(I used to wonder why his gloves look pointy and sharp but looking at it now they just seems like normal gloves.)"
                MC "(I guess even in his human form he had claws..?)"
                MC "If you ever wake up and forgive me, can I hold your hand? Now that things are like this I kinda regret never doing it."
                BM "..."
                MC "I guess I can’t expect you to just wake up from my words alone, huh?"
                MC "(Still, I don’t see anything on here that wasn’t normally there.)"
            "The cape.":
                "Even with his current form, the cape remains on him, albeit with a different purpose."
                "It now drapes over him, acting as a blanket of sorts."
                MC "(I gotta be honest though, that cape doesn’t seem like it would do much to shield him from the cold.)"
                "Any pins or brooches that previously adorned it had been removed, leaving only the fabric and threads that form it."
                MC "(I don’t think anything was added to the cape, maybe it’s not here?)"

label hairpinremove:
    scene cage2cg with fade
    "..."
    MC "(Well at least he could sleep more comfortably?)"
    MC "(I still need to find the magical item though.)"
    scene black with fade
    MC "(Where else am I supposed to look?)"
    BM "[mc]? Is..is that you?"
    scene cage3cg with vpunch
    #bgm : https://dova-s.jp/EN/bgm/play22621.html
    MC "(!!!)"
    MC "Howard..? You’re awake."
    scene cage3cg
    BM "Yes? I..uh. Heard everything you said earlier."
    BM "Y..you don’t mind that I look like this, do you?"
    scene cage4cg
    MC "Not at all. I’m glad I can finally see you like this."
    scene cage3cg
    BM "Really..? You don’t regret travelling all the way here for.."
    extend "this, right?"
    scene cage4cg
    MC "Howard, look at me. I haven't taken a bath in months."
    MC "The real question is {i}you{/i} mind if I look like this."
    scene cage3cg
    BM "I don't mind at all! You went all they way here for me.."
    BM "You really don't mind me, right..?"
    scene cage4cg
    MC "Howard. Stay still. Lower your head if possible."
    scene cage3cg
    BM "Y..yes?"
    scene cage4cg
    #If possible, i need you to make a noise that sounds like you were about to say something but got interrupted by a kiss.

    scene black with fade
    "Without waiting for another second, my hands reached to pull us together as I connected my lips to his beak."
    "In that little moment it almost seemed like all his worries were behind him as I could feel him placing his wing on my back to bring us closer than ever before."
    "For once, there was no hesitation in him. It felt {i}right{/i}."
    scene cage3cg with fade
    BM "Well, I guess it would be foolish of me to doubt you any longer."
    scene cage4cg
    MC "It would."
    scene cage3cg
    BM "Thank you for coming all the way here for me."
    BM "But..What now? I don’t know how we can escape that {i}thing{/i}."
    scene cage4cg
    MC "I’ve got an idea."

    MC "We need to get married. Right now."
    scene cage3cg
    BM "What?"
    scene cage4cg
    MC "Unless you don’t want to? "
    scene cage3cg with vpunch
    BM "NO I DO! Please..! You’ll really marry me..?!"
    scene cage4cg
    MC "Obviously, that’s why I asked."
    MC "Howard, will you marry me?"
    scene cage3cg with vpunch
    BM 'YES.'
    BM "B-but not here, we should get to the altar. There’s one nearby."
    scene cage4cg
    MC "Let’s go then."
    scene cg1a with fade
    "And so, we took off into the brilliant night sky, away from the castle, away from the creature, away from anything that could stop us at that moment."
    "With me on his back, he flew us straight into a chapel, grander than any I’ve ever seen in my life."

    scene chapel with fade
    MC "The moon..it’s blue."
    show bm happy
    BM "This is it.."
    BM "We’re really doing this.."
    show bm smile
    menu:
            "You’re not in your other form anymore?":
                show bm happy
                BM "I don’t want to be, I can’t kiss you if I don’t have lips."
                show bm smile
                MC "How exciting, I can finally taste your lips on mine."
                show bm brhappy
                BM "[mc]..Don’t get me too excited here.."
            "Don’t back down on me, okay?":
                show bm happy
                BM "I definitely won’t. I can’t live my life without you anymore."
                show bm smile
                MC "So do I."
    MC "Now, shall we?"
    show bm happy
    BM "Please, lead the way."
    show bm smile
    "Without a proper guide, we make up our own procedures as we go. I offered him my hand and we walked down the aisle together."
    "Once we reached the edge, we stood there towards each other, hands not letting go even for a minute."
    show bm smile:
                parallel:
                    ease .5 zoom 1.7
                parallel:
                    yalign 0.0
                    linear 0.0 yalign 0.0 xalign 0.5
    MC "I have to be honest, I don’t know how weddings are supposed to work."
    show bm happy
    BM "S-so do I. I haven’t had the opportunity to see one in decades."
    MC "Shall we just say our vows and then kiss?"
    show bm happy
    BM "That works for me."
    show bm smile
    MC "May..I?"
    show bm happy
    BM "Go ahead."
    show bm smile
    MC "Howard, I don’t know how long it’s been since we’ve met but it sure felt like every second of my day has been consumed by you."
    MC "You’ve intrigued me from the very moment we met and I can’t seem to get you out of my mind, no matter what form you may take."
    MC "Even when I lost my memories, a mere glimpse from a remnant of you was enough for me to remember. No matter what happens in the future, I’ll keep a window open for you and if you don’t visit, I’ll seek you out myself." 
    MC "Even if it takes me days, weeks, months, I’ll still be moving towards you."
    MC "I love you Howard and I’m honored that you gave me this opportunity."
    show bm chappy
    BM "[mc]..give me a moment. I can’t stop crying.."
    MC "Take your time."
    BM "Thank you.."
    show bm bhappy
    BM "Well.."
    BM "I..don’t think I deserve you but I’m glad you looked past all the things that I hated about myself and found beauty in them."
    BM "You’ve shown interest in me, listened to me and most importantly, you actually care about me."
    BM "I know it’s weird to say but I kind of liked it when you tied me up, especially since I knew you wouldn’t cause me any harm and you’d always give me a way out."
    BM "I liked that you treated me gently and I hope you’ll continue to stay with me until the end of time."
    BM "I promise that I will always return to your side each night, no matter how far apart we were during the day."
    BM "If you ever need me for anything at all, wave a feather of mine at your window and I’ll be at your side as soon as I can."
    BM "I love you.. And I’ll never stop, now and forever."
    show bm smile
    "No more words were said between us but one look into his eyes gave me the final confirmation I needed before officially sealing the deal."
    scene black with fade
    "When our lips finally collided, I felt his hands cupping my face as I wrapped mine around his shoulders, not wanting him to move away for even a second."
    "As I hug him tighter, his hands move from my face to embrace me even further, holding me like I’ll leave if he doesn’t."
    scene chapel with fade
    show bm chappy
    BM "It’s official."
    MC "Indeed it is."
    show bm happy
    BM "What now? Is there anything else that you wanted to do?"
    
    menu:
        "I want you to meet my family for real.":
            show bm basking
            BM "R-really? Don’t they hate me..?"
            show bm questioning
            BM "I mean, your sisters did place knives on your window to deter me..."
            MC "They won’t do anything like ever again. I’ll make sure they accept you with open arms."
            BM "What if they don’t?"
            MC "Stop thinking negatively here, they won’t. Once they get to know you, I’m sure they’ll love you."
            show bm happy
            BM "W-well, it’d be nice if they do."
            BM "Can I really have hope like this..?"
            MC "Of course. You always deserve hope."
            scene black with fade
            pause 1
        
            scene ed2cg with fade
            E "Catherine, c’monnnn. Are you not gonna wear the flower crowns with us?"
            E "Even Howard and dad are joining in!"
            C "Lizzie, I’m not a child."
            C "Howard, take that off. I can’t have her use you as an excuse against me."
            BM "I’m sorry?"
            MC "Hey, don’t make him apologize when he did nothing wrong."
            MC "Lizzie’s right y’know? You’re the only one not wearing them."
            DA "Catherine, why don’t you join us?"
            MC "Please?"
            BM "Um, please? Sister in law?"
            C "I guess I can’t refuse when both my little [player_fm] and brother in law are asking so nicely, can I?"
            E "Woo! I am so glad [mc] has good taste. Welcome to the family Howard."
            C "I know we’ve said this before, but let us say it again."
            C "We’re deeply sorry for what we’ve done to you." 
            BM "Oh it’s okay now! We’re.. family right?"
            BM "{size=-5}Family..That’s an unfamiliar word{/size}"
            MC "We’ll get you used to it."
            BM "Promise?"
            MC "Promise."
            BM "In that case, I’m glad to be here."
            "Nothing warms my heart quite like seeing him happy. After decades of isolation, he’s finally found people who will welcome him with open arms."
            "It was hard at first, but as the missing villagers slowly returned, everyone soon realised that it wasn’t Howard who they should hate."
            "With the two of us together, surrounded by other people who love us to our core, I think we’ve finally reached our happily ever after."
            "Ending 2 : Reunited at last"

        "Definitely, we need to kill that thing.":
            show bm questioning
            BM "A-are you sure about this?"
            MC "When am I not sure?"
            show bm happy
            BM "Alright then."
            scene black with fade
            centered "As you wish."
            pause 1
            scene runcg with fade
            #think lightly jogging to freedom
            VA "RUN..!"
            VB "WE’RE FREE!!"
            VA "Wait, [mc]’s in there!!"
            VA "..."
            VA "Actually, [mc] looks pretty happy in there."
            VB "Just run!"
            VA "Well, as long as those two are happy I guess."

            scene ed3cg with fade
            #sfx
            BM "Was this..enough [mc]?"
            BM "I don’t think even this {i}thing{/i} can recover when we’ve sliced it into this many pieces."
            MC "You did great." 
            MC "This was a lot more blood than I was expecting though, clean up’s gonna take a while."
            BM "Where do you want to dispose of the body?"
            MC "Let’s use it to light up the fireplace."
            MC "After we clean up all this, it’ll just be the two of us here."
            BM "Ahaha, I can’t think of anything better." 
            BM "Just you and me. Together for eternity."
            "Under the moonlight, there’s nothing more captivating than the sight of him smiling at me while stained with blood."
            "With the creature gone, he can finally be free, completely unchained. He’s left his cage for good and I couldn’t be happier."
            "As far as I’m concerned, the two of us have reached our very own happy ever after."
            "Ending 3: Stained with blood"









## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade
    
    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:
 
        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results
    
    centered "Fin"

    hide screen results

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            achieve completionist

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return
