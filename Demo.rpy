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
    P "My name is [povname]."

    #if pov is blank
    if not povname:
        $ povname = "Mao"

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
    E "Morning!, i hope youre having a great first day"
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
                    N "By the way my name is Nick"
                    P "Hey, am [povname]"
                    N "Its crazy how females are now a days"
                    "Youre telling me lol"
                    N "You seem like a cool dude, honestly"
                    N "Hey this is crazy that i just meet you"
                    N "But can i walk you to your class"
                    return

                #Library chapter 3.2 (maybe)
                label choice_9:
                    N "Dont let it go to your head."
                    N "You know what, i was going to get a snack"
                    N "Do you want something?"
                    "Whos going to turn down free food"
                    "Ended up just going with Nick"
                    P "thanks man, youre good people."
                    return

                #Library chapter 3.3 (No)
                label choice_10:
                    P "Im good man, thank you"
                    N "If you need a shoulder to cry on ill be in the corner"
                    N "Watching you jk"
                    N "ill catch you xoxo"
                    return
