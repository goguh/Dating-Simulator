# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#POV character
define P = Character("[povname]")

#Story characters
define E = Character("Ed") #School help 
define M = Character("") #professor

#1st main characters
define J = Character("Jessica") 
define N = Character("Nickola") 

#background images
image picture_1 = "1.jpg" #black bg
image picture_2 = "2.jpg" #school
image picture_3 = "3.jpg" #library
image picture_4 = "4.jpg" #hall
image picture_5 = "5.jpg" #sushi date


#images for Characters




# The game starts here.
label start:
    
    #player insert name
    $ povname = renpy.input("What is your name?", length=32)
    $ povname =povname.strip()
    #if pov is blank
    if not povname:
        $ povname = "Mao"
    
    P "Youre name is [povname]."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene picture_1
    "Its the first day of school and youre already running late."
    "You decide to get ready in a rush."
    #add some type of sound of getting ready to go to school
    scene picture_2
    "Once at school youre confused on where to go."
    "As soon you decide to walk around and find help."
    "Well walking to the quad, you end up bumpimg in Ed."

    #show a Ed
    E "Morning! I hope youre having a great first day"
    #respone
    P "Good morning i was just wonder how do I get the library from here"
    P "Also to Jacaranda hall?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        #show Ed happy to help
        E "No problem which buliding do you want to go first?"
        #this first to choices are going to be yes and no, just so you can meet the characters
        "Library":
            jump choice_1
        "Jacaranda hall":
            jump choice_2
    # This ends the game.
    return

#First Location

#Library chapter 1
label choice_1:
    #show Ed joyful
    E "Well at the moment we are ..."
    #show library
    scene picture_4
    P "Well it took a while but Im finally here."
    #audio of people
    P "Once inside you noticed its packed."
    #audio of walking
    P "Your walking around to find a open table."
    #show a table
    P "Once sat, a girl approaches you."
    #introduce jessica
    J "Hi, Im jessica."
    menu:
        #Show jessica
        J "i was wondering if i could seat here?"
        "yes":
            jump choice_3 #chapter2
        "No":
            jump choice_4 #chapter3
    return

#Library chapter 2 (yes)
label choice_3:
    P "Of course! You can!"
    P "My name is [povname] by the way"
    J "Its nice to meet you"
    P "Same, so how's your first day going?"
    J "honestly, kinda of boring"
    menu:
        J "Hey, do you want to get out of here"
        "Yes":
            jump choice_5
        "Maybe":
            jump choice_6
        "No":
            jump choice_7
    return

#Library chapter 2.1 (Yes)
label choice_5:
    P "Yeah sure!"
    J "I know this awesome place to eat"
    P "What kind?"
    menu:
        #would need a sushi resturant for next scene
        J "you like sushi right?"
        "Yes":
            jump choice_11
        "Maybe":
            jump choice_6
        "No":
            jump choice_7
    return

#Library chapter 2.2 (Maybe)
label choice_6:
    P "Well i could be convinced"
    P "What did you have in mind"
    J "Actually nvm lets stay here and what for class lol"
    "All you were thinking is that"
    "I just got friend zoned"
    return

#Library chapter 2.3 (No)
label choice_7:
    J "well looks up my time is up"
    J "got class in a few mintues"
    P "That girl was weird."
    return

#Library chapter 2.11
label choice_11: 
    J "Awesome! Whats your normal dish?"
    P "Oh, its totally basic."
    P "Whats your number btw? so in case i get lost getting there."
    J "Dont be silly will go in the same care. <3"
    "All your thinking is that you might a future gf."
    return

#Library chapter 3 meeting Nick (No)
label choice_4:
    #show jessica mad
    J "well i didnt want to seat here anyways. rude ass!"
    P "Shes overdratic lol"
    #show nickolas
    N "Hey man, just saw what happened with that girl"
    menu:
        N "are you okay?"
        "Yeah":
            jump choice_8
        "Maybe":
            jump choice_9
        "Nah":
            jump choice_10
    return

#Library chapter 3.1 (yes) still need to be worked on
label choice_8:
    #show nick
    N "By the way my name is Nick"
    P "Hey, am [povname]"
    #still in the library
    N "Its crazy how females are now a days"
    "Youre telling me lol"
    N "You seem like a cool dude, honestly"
    N "Hey this is crazy that i just meet you"
    N "But can i walk you to your class"
    return

#Library chapter 3.2 (maybe)
label choice_9:
    #show nick annoyed
    N "Dont let it go to your head."
    N "You know what, i was going to get a snack"
    N "Do you want something?"
    "Whos going to turn down free food"
    "Ended up just going with Nick"
    P "thanks man, youre good people."
    return

#Library chapter 3.3 (No)
label choice_10:
    #show nick mad
    P "Im good man, thank you"
    N "If you need a shoulder to cry on ill be in the corner"
    N "Watching you jk"
    N "ill catch you xoxo"
    return

#Second location

label choice_2:
    #show Ed confused
    E "Well at the moment we are ..."
    scene picture_3 #classroom
    P "That took a while but Im finally here."
    "Once entering the class, you noticed that youre early lol."
    #sound of crickets
    "You decide to seat in the back."
    #end sound
    "which normally seems right and put your head down."
    "A few mintues pass by and head foot steps walking towards you."
    #introduce nickola
    N "Hey man, i know this is awkard but is this the senior design class??"
    N "I kinda got lost and the numbers are confusing"
    menu:
        "Yes":
            jump choice_12
        "No":
            jump choice_13
    return

#Hall chapter 2 (Yes)
label choice_12:
    #show nick happy
    P "Yeah it is"
    P "I'm [povname]"
    N "Nickolas but everyone calls me Nick for short."
    menu:
        N "Is this your last year?"
        "Yeah":
            jump choice_14 # Yes
        "Nah":
            jump choice_18 #No
    return

label choice_18:
    N "Damn how many more semsters do you have"
    P "I think i have one more year"
    N "Thats not bad!"
    N "Hopefully works out for you!"
    menu:
        N "Do you want to get coffee?"
        "yeah":
            jump choice_15
        "Nah":
            jump choice_17
        "Maybe":
            jump choice_16
    return

#Hall chapter 2.1 (Yes)
label choice_14:
    N "Nice!"
    P "What about you?"
    N "If everything go right then yeah"
    menu:
        N "Hey, do you want get coffee? since we are early"
        "Absolutely!":
            jump choice_15 
        "Maybe":
            jump choice_16
        "Nah":
            jump choice_17
    return

label choice_15: #(Yes)
    #show nick happy
    P "You had me at coffee"
    N "Great! I wonder how many times I can make you happy"
    "Nervous laugh"
    N "Im kidding <3"
    return

label choice_16: #(Maybe)
    #show nick annoyed
    N "Do you like the coffee here"
    P "Nah, they dont know how to make coffee"
    N "True! maybe after class then"
    #introduce the profressor
    return

label choice_17: #(No)
    #show nick mad
    N "Are you sure i can always bring it back for you?"
    P "Im good, i dont really like coffee"
    N "Alright :/"
    return

#Hall chapter 3 (No)
label choice_13:
    N "Are you sure?"
    P "Well yeah. I know where im at"
    #show nick mad
    N "Well ass, i was making sure."
    #sound of people walking in
    "As soon as nick let you coming on napping"
    "You hear someone else walking up"
    #show jessica
    J "Hey, is anyone sitting here?"
    P "Nah, your good."
    J "Im Jessica btw, whats your name?"
    P "Im [povname]"
    menu:
        J "Has the professor shown up"
        "Yeah":
            jump choice_19
        "maybe":
            jump choice_20
        "nah":
            jump choice_21
    return

label choice_19: #(yes)
    J "He did? where is he then."
    P "I think he just because they arent enough"
    P "people for the class."
    menu:
        J "If thats the case, do you want to get out of here. Lets get sushi?"
        "Yes":
            jump choice_11
        "Maybe":
            jump choice_6
        "No":
            jump choice_7
    return

label choice_20: #(maybe)
    #show jessica annoyed
    J "How dont you know?"
    P "well i wasnt here the whole time"
    "But you were lol"
    J "sorry, i just assumed."
    P "All good"
    return

label choice_21: #(No)
    J "Are you sure?"
    #show Jessica annoyed
    P "well ive been here for an hour. im sure"
    return
