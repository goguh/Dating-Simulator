#Add this to the origin storyboard

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#-----------------------------Love Meter Define--------------------------------
init -5 python:
    #custom bar -----------------------
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 315 # bar width
    style.my_bar.ymaximum = 30 # bar height
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5
    
    # I have all my User Interface graphics stored in one file called ui. 
    # To access them in my code, I put ui/ in front of all images in that file. 
    
    style.my_bar.left_bar = Frame("bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("bar_empty.png", 0, 0)
    style.my_bar.hover_left_bar = Frame("bar_hover.png", 0, 0)
    
    style.my_bar.thumb = "thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5
    
init -2 python:
    ## Character Jessica --------------
   
    Jessica_love = 10 #The number of points she Starts with. 
    max_love = 150  #The maximum points she can get. 

init python: 
    ## ------------ Love Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_Jessica=False

    ## ------------ Love Points Floating Meter --------------------
    def stats_overlay():               
        
        # --- Jessica's Love Bar -------
        if show_Jessica:
            ui.frame(
                xalign = 0.5, #centered
                ypos = 400,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Jessica's Love Points: %d" %Jessica_love, 
                xalign = 0.5)
            ui.bar(max_love, Jessica_love, 
                style="my_bar")
            
            ui.close()
    config.overlay_functions.append(stats_overlay)

#-----------------------------Love Meter Define-----------------------------------------

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

#images for Characters

#ED
image Ed = im.Scale("Ed.png",700,900)

#Jessica
image Jessica angry1 = "Character1/angry.png"
image Jessica angry2 = "Character1/angry2.png"
image Jessica blush = "Character1/blush.png"
image Jessica confuse1 = "Character1/confuse.png"
image Jessica confuse2 = "Character1/confuse2.png"
image Jessica glad = "Character1/glad.png"
image Jessica neutral = "Character1/neutral.png"
image Jessica sad = "Character1/sad.png"
image Jessica smile = "Character1/smile.png"

#Nickolas
image Nickolas neutral = im.Scale("Character2/neutral.png",700,950)

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
    show Ed
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
    hide Ed
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
    show Jessica neutral
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

#------------------------------Love Meter Update-----------------------------------
    $ show_Jessica=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Jessica_love+=50
    #This adds points to the meter. 
    
    show expression Text("{color=ffffff}{font=Raleway-Light.ttf}+50 Love Points{/font}{color=ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Jessica=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Jessica=False
    # This hides the Meter. 
#-------------------------------------Love Meter Update------------------------------- 

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
#------------------------------Love Meter Update-----------------------------------
    $ show_Jessica=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Jessica_love+=50
    #This adds points to the meter. 
    
    show expression Text("{color=ffffff}{font=Raleway-Light.ttf}+50 Love Points{/font}{color=ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Jessica=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Jessica=False
    # This hides the Meter. 
#-------------------------------------Love Meter Update-------------------------------

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

#------------------------------Love Meter Update-----------------------------------
    $ show_Jessica=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Jessica_love+=50
    #This adds points to the meter. 
    
    show expression Text("{color=ffffff}{font=Raleway-Light.ttf}+50 Love Points{/font}{color=ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Jessica=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Jessica=False
    # This hides the Meter. 
#-------------------------------------Love Meter Update------------------------------- 

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
    hide Jessica neutral
    P "Shes overdratic lol"
    #show nickolas
    show Nickolas neutral
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
