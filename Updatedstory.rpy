#Add this to the origin storyboard

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#------------------------------MiniGame Definition-----------------------------------

#-----------------------MiniGame Defnition--------------------------------------


 




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
    Jessica_love = 0 #The number of points she Starts with. 
    
    ## Character Nickola --------------
    Nickola_love = 0
    
    max_love = 150  #The maximum points she can get. 

init python: 
    ## ------------ Love Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_Jessica=False
    show_Nickola=False

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
            
        # --- Nickola's Love Bar -------
        if show_Nickola:
            ui.frame(
                    xalign = 0.5, #centered
                    ypos = 400,) #400 px Down from the Top
                
                ui.vbox(xalign = 0.5)
                ui.text ("Nickola's Love Points: %d" %Nickola_love, 
                    xalign = 0.5)
                ui.bar(max_love, Nickola_love, 
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
define X = Character("X")

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
    $ povname = povname.strip()
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
            jump choice_201
        "Jacaranda hall":
            jump choice_1

    # This ends the game.

    return


#---------------------------Library chapter 1------------------------------------
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
    #------------------------------Love Meter Update-----------------------------------
    $ show_Jessica=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Jessica_love+=0
    #This adds points to the meter. 
    
    show expression Text("{color=ffff00}{font=Raleway-Light.ttf}+0 Love Points{/font}{color=ffffff}", 
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
    P "Well i could be convinced"
    P "What did you have in mind"
    J "Actually nvm lets stay here and what for class lol"
    "All you were thinking is that"
    "I just got friend zoned"
    return


#Library chapter 2.3 (No)
label choice_7:
#------------------------------Love Meter Update-----------------------------------
    $ show_Jessica=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Jessica_love-=50
    #This adds points to the meter. 
    
    show expression Text("{color=ff0000}{font=Raleway-Light.ttf}-50 Love Points{/font}{color=ffffff}", 
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
#------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love+=50
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
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 

    N "By the way my name is Nick"
    P "Hey, am [povname]"
    N "Its crazy how females are now a days"
    "Youre telling me lol"
    N "You seem like a cool dude, honestly"
    N "Hey this is crazy that i just meet you"
    N "But can i walk you to your class"
    P "Sure"
    jump choice_12

#Library chapter 3.2 (maybe)
label choice_9:
#------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love+=20
    #This adds points to the meter. 
    
    show expression Text("{color=ffffff}{font=Raleway-Light.ttf}+20 Love Points{/font}{color=ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 

    N "Dont let it go to your head."
    N "You know what, i was going to get a snack"
    N "Do you want something?"
    "Whos going to turn down free food"
    "Ended up just going with Nick"
    P "thanks man, youre good people."
    jump choice_13

#Library chapter 3.3 (No)
label choice_10:
    P "Im good man, thank you"
    N "If you need a shoulder to cry on ill be in the corner"
    N "Watching you jk"
    N "ill catch you xoxo"
    "..."
#------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love-=100
    #This adds points to the meter. 
    
    show expression Text("{color=#ff0000}{font=Raleway-Light.ttf}-100 Love Points{/font}{color=#ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 
    "This man..."
    return
    
#Library chapter 3.4
label choice_12:
    N "Hey, have you ever played Memoria Sushi before?"
    P "No, I haven't. What is it?"
    N "It's a memory game where you have to match different types of sushi to win points"
    N "Let's play the game!!"
    menu:
        N "That sounds interesting"
        "Let's play":
            window hide
            jump memoria_game
        "But but I'm not really in the mood to play a game right now...":
            jump choice_14
    
#Library chapter 3.5
label choice_13:
    N "Hey, have you ever played Memoria Sushi before?"
    P "No, I haven't. What is it?"
    N "It's a memory game where you have to match different types of sushi to win points"
    N "Let's play the game!!"
    menu:
        N "That sounds interesting"
        "Let's play":
            window hide
            jump memoria_game
        "But but I'm not really in the mood to play a game right now...":
            jump choice_15
    
    
#chapter 3.5
label choice_14:
#------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love+=0
    #This adds points to the meter. 
    
    show expression Text("{color=#ffffff}{font=Raleway-Light.ttf}0 Love Points{/font}{color=#ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 

    N "Oh, no problem. I understand"
    N "Just let me know if you ever want to play"
    N "Bye"
    "Will do next time. Thanks again."
    return
    
#chapter 3.5
label choice_15:
#------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love-=20
    #This adds points to the meter. 
    
    show expression Text("{color=#ff0000}{font=Raleway-Light.ttf}-20 Love Points{/font}{color=#ffffff}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text with dissolve

    # This is the Announcement Text for the Love Meter, including a specific font, and font color.
    # This states how many points Jessica is being awarded.  
    # Note the FONT! If you use this code without replacing the font Name with one In Your Game,
    # you will get an error message. 
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 

    N "Oh, okay. I was really looking forward to playing with someone."
    P "I'm sorry, maybe we can play another time?"
    N "Yeah, sure. I just don't understand why you can't play now. It's not like you have anything else going on"
    P "I just don't feel like playing right now. Can't you respect that?"
    N "I'm sorry, I didn't mean to come across as pushy. It's just that I was excited to play the game and I guess I got a little carried away"
    P "..."
    "...grumpy person..."
    return

#chapter 3.5
label choice_17:
    P "..."
    return
    
#chapter 3.5
label choice_18:
    P "..."
    return
    
#chapter 3.5
label choice_19:
    P "..."
    return
    
## ---------------------- Memoria Mini Game ------------------------------------    
init python:

        # DEFAULT GAME SETTINGS:

        # default card type set
        all_cards = ['A', 'B', 'C', 'D']
        # width and height of the field
        ww = 4
        hh = 3
        # how many cards can be opened for 1 turn
        max_c = 2
        # text size in the card for text mode
        card_size = 30
        # time allocated for the passage
        max_time = 25
        # pause before the cards disappear
        wait = 0.5
        # mode of cards with images, not with the text
        img_mode = True

        values_list = []
        temp = []
        # we announce picture cards
        # must be in the format "images/Memoria_image/card_*.png"
        # required "card_back.png" and "card_empty.png"
        for fn in renpy.list_files():
            if fn.startswith("images/Memoria_image/card_") and fn.endswith(".png"):
                name = fn[12:-4]
                renpy.image("card" + name, fn)
                if name != "empty" and name != "back":
                    temp.append(str(name))
        # if the picture found> 1,
        # then change the set of card types, but the file names
        if len(temp) > 1:
            all_cards = temp
        else:
            # otherwise turn on the text mode,
            # because the pictures are very small
            img_mode = False

        # the function of initializing the playing field
        def cards_init():
            global values_list
            values_list = []
            while len(values_list) + max_c <= ww * hh:
                current_card = renpy.random.choice(all_cards)
                for i in range(0, max_c):
                    values_list.append(current_card)
            renpy.random.shuffle(values_list)
            while len(values_list) < ww * hh:
                values_list.append('empty')



screen memo_scr:
        # timer
        timer 1.0 action If(memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose")) repeat True
        # field
        grid ww hh:
            align(.5, .5)  # in the center
            for card in cards_list:
                button:
                    left_padding 0
                    right_padding 0
                    top_padding 0
                    bottom_padding 0
                    background None
                    if card["c_value"] == 'empty':
                        if img_mode:
                            add "card-empty"
                            top_padding .05
                        else:
                            text "" size card_size
                    else:
                        if card["c_chosen"]:
                            if img_mode:
                                add "card" + card["c_value"]
                                top_padding .05
                            else:
                                text card["c_value"] size card_size
                        else:
                            if img_mode:
                                add "card_back"
                            else:
                                text "#" size card_size
                    # pressing the button-card
                    action If((card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"])])
        text str(memo_timer) xalign .5 yalign 0.0 size card_size
        
# the game itself
label memoria_game:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range(0, len(values_list)):
            if values_list[i] == 'empty':
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": True})
            else:
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": False})
    $ memo_timer = max_time
    # show the game screen
    show screen memo_scr
    # main game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append(cards_list[result]["c_number"])
                $ turned_cards_values.append(cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # prevent opening of extra cards
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump("memo_game_loop")
                renpy.jump("memo_game_win")
        jump memo_game_loop
        
## ---------------------- Memoria Mini Game ------------------------------------
# loss
label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    centered "{size=36}Vdul! Re-Try.{/size}"
    
    P "Aw, man. I can't believe I lost. I thought I had it for a second there."
    N "It was a close game. You almost had me a few times."
    P "Yeah, but almost doesn't count. I really wanted to win."
    N "Don't worry about it too much. We can play again and you can try to get revenge."
    menu:
        "Yeah, Next time I'll have to step up my game.":
            jump memoria_game
        "No, Today.":
            jump choice_16

# winnings
label memo_game_win:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    
    #------------------------------Nickola's Love Meter Update-----------------------------------
    $ show_Nickola=True 
    # This makes the Meter appear.

    pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    $ Nickola_love+=50
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
    
    $ show_Nickola=True
    # This is a Refresh that shows the increase in points ON the meter.

    $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    hide text with dissolve
    # This hides the Text. 

    $ show_Nickola=False
    # This hides the Meter. 
#-------------------------------------Nikcola's Love Meter Update------------------------------- 

    
    #centered "[size=36][b]Winning![/b][/size]"
    # centered "{size=36}{b}Winning!{/b}{/size}"
    jump winwin
        
label winwin:
    P "Yes, I won! That was a close game, but I managed to get a few lucky matches."
    N "Yeah, you did well. I'll have to practice more for next time."
    P "Thanks for playing with me. It was a lot of fun."
    N "Yeah, it was a good time. We should definitely play again sometime."
    P "Absolutely. Maybe we can try a different game next time."
    N "Sure, that sounds like a plan."
    return
    
#chapter 3.5
label choice_16:
    N "I'll be ready for you. Thanks for playing with me."
    P "No problem. It was still fun, even if I did lose."
    N "Yeah, it was a good time. We should definitely play again sometime."
    return
    
#----------------------------Jacaranda Hall------------------------

label choice_201:
    hide Ed
    P "Hi, excuse me, is this seat taken?"
    X "Oh no, it's all yours."
    menu:
        P "Thanks. So,"
        "Do you come here often?":
            jump choice_203
        "Do you happen to know where the computer section is?":
            jump choice_204
    return

label choice_203:
    X "Actually, yes. I love reading, and the library is the perfect place for that."
    P "That's great!"
    menu:
        "What are you reading now?":
            jump choice_205
        "I see. Do you have any other hobbies besides reading?":
            jump choice_206
    return
        
label choice_205:
    X "I'm reading the Alchemist."
    menu:
        X "Have you read it?"
        "Yes, it's one of my favorites.":
            jump choice_207
        "No, I haven't read it.":
            jump choice_208
    return
        
label choice_207:
    X "Oh, we have something in common!"
    "CONCLUSION:Let's exchange numbers and go out sometime!"
    return
    
label choice_208:
    X "You should definitely read it."
    X "It's an amazing book!"
    "CONCLUSION: I think we can be good friends."
    return
    
label choice_206:
    X "Well, I love to dance."
    menu:
        X "What about you?"
        "I love dancing too!":
            jump choice_209
        "I'm not much of a dancer, to be honest.":
            jump choice_210
    return
  
label choice_209:
    "CONCLUSION: Let's go out dancing together sometime!"
    return
    
label choice_210:
    X "That's too bad."
    X " Dancing is so much fun!"
    "CONCLUSION: I don't think we're a good match."
    
label choice_204:
    X "Yes, it's on the second floor."
    menu:
        X "Do you need help finding it?"
        "Yes, please.":
            jump choice_211
        "No, I think I can find it on my own.":
            jump choice_212
    return
        
label choice_211:
    P "I'm not very good with directions."
    X "No problem."
    X "I can show you the way."
    "show the way..."

    P "Thanks for showing me around."
    P "You're really nice."
    X "You're welcome."
    X "I try my best."
    "CONCLUSION: Let's exchange numbers and go out sometime!"
    return
    
label choice_212:
    P "But thanks for offering."
    X "Alright then."
    X "Let me know if you need anything else."
    menu:
        P "Actually, can I buy you a coffee as a thank you for your help?" :
            jump choice_213
        P "No problem, thanks anyway.":
            jump choice_214
    return
    
label choice_213:
    X "That's very sweet of you, but I'm not really a coffee drinker."
    "CONCLUSION: I don't think we're a good match."
    return
    
label choice_214:
    X "You're welcome."
    X "Have a good day!"
    "CONCLUSION: I don't think we're a good match."
    return
