# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#POV character
define P = Character("[povname]")

#Story characters
define E = Character("Ed") #School help 

#Potential date characters
define J = Character("Jessica") 
define N = Character("Nickola") 
define H = Character("Hugo")
define S = Character("Sasha")

#background images
image black_background = "1.jpg" #black bg
image school = "2.jpg" #school
image library = "3.jpg" #library
image hall = "4.jpg" #hall


#images for Characters

# The game starts here.
label start:

    #player insert name
    $ povname = renpy.input("What is your name?", length=32)
    $ povname =povname.strip()
    #if pov is blank
    if not povname:
        $ povname = "Tony"
    
    P "Your name is [povname]."

    scene school
    # jump jacaranda_hall

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.jpg" or "bg room.jpg") to the
    # images directory to show it.

    scene black_background
    "Its the first day of school and you're already running late."
    "You decide to get ready in a rush."
    #add some type of sound of getting ready to go to school
    scene school
    "Once at school you're confused on where to go."
    "As you decide to walk around and find help."
    "You end up bumping into Ed."

    #show a Ed
    show ed happy
    E "Morning! I hope you're having a great first day"
    #response
    P "Good morning I was just wondering how do I get the library from here"
    P "Also, how do I get to to Jacaranda hall?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.jpg" to the images
    # directory.
    E "I'll be glad to help!"
    E "Which building do you want to go first?"
    menu:
        #this first to choices are going to be yes and no, just so you can meet the characters
        "Library":
            jump library
        "Jacaranda hall":
            jump jacaranda_hall
    # This ends the game.
    return

#First Location

#Library stage 1
label library:
    #show Ed thinking
    show ed thinking
    E "The library isn't too far from here"
    E "Simply go straight for about a minute and you're going to see a small small staircase"
    E "Go up the staircase and you'll be there"

    #show library
    scene library
    P "Well it took a while but I'm finally here."
    #audio of people
    P "Once inside you notice it's pretty empty."
    #audio of walking
    P "You find an open table."

    #making a choice
    P "You look around and see two people. Who do you find more interesting?"
    show jessica happy at left
    show hugo neutral at right
    menu:
        "Jessica":
            jump stage_1_j #stage 2, option 1
        "Hugo":
            jump stage_1_h #stage 2, option 1
    return

label jacaranda_hall:
    #show Ed thinking
    show ed thinking
    E "Jacaranda Hall is where we have our class!"
    E "Simply take a left here and you'll see it on your right hand side"

    #show library
    scene hall
    P "I can't believe I forgot where Jacaranda Hall is haha."
    #audio of people
    P "Once inside you notice it's pretty empty."
    #audio of walking
    P "As you're walking to find a class you see two people"

    #making a choice
    P "Who do you find more interesting?"
    show nick posing at left
    show sasha happy at right
    menu:
        "Nick":
            jump stage_1_n #stage 2, option 1
        "Sasha":
            jump stage_1_s #stage 2, option 1
    return


#JESSICA******************************************************************


#Library stage 1
label stage_1_j:
    hide hugo neutral
    hide jessica happy
    #show a table
    P "Once seated, a girl approaches you."
    #introduce jessica
    show jessica happy
    J "Hi, I'm jessica."
    menu:
        #Show jessica
        J "i was wondering if i could sit here?"

        "Of course, have a seat. I'm [povname], by the way.":
            jump stage_2_1_j #stage 2, option 1
        "Sorry, I'm waiting for someone.":
            jump stage_2_2_j #stage 2, option 1
    return


label stage_2_1_j:

    show jessica happy
    
    P "Of course, have a seat. I'm [povname], by the way."
    show jessica listening
    J "Nice to meet you, [povname]. So, what brings you here?"
    menu:
        "I just needed a change of scenery. How about you?":
            jump stage_3_1_j
        "I come here to enjoy the ambiance and maybe meet new people.":
            jump stage_3_2_j

label stage_2_2_j:

    show jessica mad
    
    P "Sorry, I'm waiting for someone."
    show jessica mad
    J "Oh, I see. No worries, have a nice day."
    menu:
        "Oh wait... they just texted me that they aren't going to make it.":
            jump stage_3_3_j
        "Actually, I think I might have been mistaken. Please have a seat.":
            jump stage_3_4_j

label stage_3_1_j:

    show jessica happy
    
    P "I just needed a change of scenery. How about you?"
    J "Same here. I like coming to new places to clear my mind."
    menu:
        "Do you have any hobbies you like to do in your free time?":
            jump stage_4_1_j
        "What's something you've always wanted to try but never had the chance?":
            jump stage_4_2_j

label stage_3_2_j:

    show jessica listening
    
    P "I come here to enjoy the ambiance and maybe meet new people."
    show jessica happy
    J "That's a great idea. I should do that more often."
    menu:
        "What's something you've always wanted to try but never had the chance?":
            jump stage_4_2_j
        "Do you have any hobbies you like to do in your free time?":
            jump stage_4_1_j


label stage_3_3_j:

    show jessica listening
    
    P "Oh wait... they just texted me that they aren't going to make it. You seem interesting. What do you do for fun?"
    J "I enjoy hiking and trying out new restaurants. You?"
    menu:
        "I love hiking too! Have you been to any great trails lately?":
            jump stage_4_3_j
        "I'm more of a homebody. I like watching movies and playing games.":
            jump stage_4_4_j

label stage_3_4_j:

    show jessica happy
    
    P "Tell me something unique about yourself."
    show jessica listening
    J "I can play three musical instruments: piano, guitar, and violin."
    menu:
        "That's amazing! What's your favorite piece to play?":
            jump stage_4_7_j
        "Do you have any favorite bands or artists?":
            jump stage_4_8_j

label stage_4_1_j:

    show jessica listening
    
    P "Do you have any hobbies you like to do in your free time?"
    J "I love painting and exploring new places. You?"
    menu:
        "I'm really into photography, capturing moments is fascinating.":
            jump stage_5_1_j
        "I like playing video games and watching movies.":
            jump stage_5_2_j

label stage_4_2_j:

    show jessica listening
    
    P "What's something you've always wanted to try but never had the chance?"
    J "I've always wanted to try skydiving. What about you?"
    menu:
        "I'd love to learn how to dance the tango.":
            jump stage_5_3_j
        "I think I'd like to try bungee jumping.":
            jump stage_5_4_j

label stage_4_3_j:

    show jessica happy
    
    P "I love hiking too! Have you been to any great trails lately?"
    J "Yes, I recently went to this amazing trail with a waterfall."
    menu:
        "That sounds beautiful. I'd love to join you on a hike sometime.":
            jump stage_5_5_j
        "Sounds great, I'll have to check that out sometime.":
            jump stage_5_6_j

label stage_4_4_j:

    show jessica happy
    
    P "I'm more of a homebody. I like watching movies and playing games."
    J "That's cool. We all have our preferences, right?"
    menu:
        "That's cool. We all have our preferences, right?":
            jump stage_5_7_j
        "Well, maybe we could have a game night or a movie marathon sometime.":
            jump stage_5_8_j

label stage_4_5_j:

    show jessica happy
    
    P "That's awesome! Do you have a favorite cuisine?"
    show jessica happy
    J "I love Italian food. How about you?"
    menu:
        "I also love Italian food!.":
            jump stage_5_9_j
        "I'm not the biggest fan of Italian food but I really like Mexican food!":
            jump stage_5_10_j

label stage_4_6_j:

    show jessica listening
    
    P "I prefer staying in and cooking. I enjoy trying out new recipes."
    J "That's impressive! What's your favorite dish to cook?"
    menu:
        "I love making homemade pasta and experimenting with sauces.":
            jump stage_5_11_j
        "I make a mean lasagna, if I do say so myself.":
            jump stage_5_12_j

label stage_4_7_j:

    show jessica happy
    
    P "That's amazing! What's your favorite piece to play?"
    J "I love playing Beethoven's 'Moonlight Sonata' on the piano."
    menu:
        "That's one of my favorites! I'd love to hear you play it sometime.":
            jump stage_5_13_j
        "That's cool! I've always admired musicians.":
            jump stage_5_14_j

label stage_4_8_j:

    show jessica listening
    
    P "Do you have any favorite bands or artists?"
    J "I love a wide range of music, but lately, I've been into indie rock bands."
    menu:
        "I love indie rock too! We should go to a concert together sometime.":
            jump stage_5_15_j
        "That's cool, I've never really been into indie rock unfortunately":
            jump stage_5_16_j

label stage_5_1_j:

    show jessica listening
    
    P "I'm really into photography, capturing moments is fascinating."
    J "That's so cool! We should go on a photo adventure together!"
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_2_j:

    show jessica listening
    
    P "I like playing video games and watching movies."
    J "Nice! It's great to have some downtime activities."
    "Conclusion: You two remain friends."
    return


label stage_5_3_j:

    show jessica happy

    P "I'd love to learn how to dance the tango."
    J "That sounds like fun! Maybe we could take a class together?"
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_4_j:

    show jessica happy
    
    P "I think I'd like to try bungee jumping."
    J "Wow, you're quite the thrill-seeker!"
    "Conclusion: You two remain friends."
    return

label stage_5_5_j:

    show jessica listening
    
    P "That sounds beautiful. I'd love to join you on a hike sometime."
    J "I'd like that! Let's plan a hike together."
    "CONCLUSION: They agree to go on a date."
    return

label stage_5_6_j:

    show jessica happy
    
    P "Sounds great, I'll have to check that out sometime."
    J "Definitely! Let me know if you need any recommendations."
    "CONCLUSION: You two remain friends."
    return

label stage_5_7_j:

    show jessica happy
    
    P "That's cool. We all have our preferences, right?"
    J "Definitely! It's nice to find people who share your interests."
    "CONCLUSION: You two remain friends."

label stage_5_8_j:

    show jessica listening
    
    P "Well, maybe we could have a game night or a movie marathon sometime."
    J "That sounds like a lot of fun! Count me in."
    "CONCLUSION: They agree to go on a date."


label stage_5_9_j:
    
    show jessica listening
    
    P "I also love Italian food!."
    J "That sounds delicious! I'd love to try it sometime."
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_10_j:

    show jessica sad
    
    P "I'm not the biggest fan of Italian food but I really like Mexican food!"
    J "Oh dang that's unfortunate, well anyways I'm late for class, see ya"
    "Conclusion: You two walk away from each other"
    return

label stage_5_11_j:

    show jessica listening
    
    P "I love making homemade pasta and experimenting with sauces."
    J "That sounds delicious! I'd love to try it sometime."
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_12_j:

    show jessica listening
    
    P "I make a mean lasagna, if I do say so myself."
    J "I bet it's great! Homemade lasagna is always a treat."
    "Conclusion: You two remain friends."
    return


label stage_5_13_j:

    show jessica happy
    
    P "That's one of my favorites! I'd love to hear you play it sometime."
    J "I'd be happy to play it for you!"
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_14_j:

    show jessica happy
    
    P "That's cool! I've always admired musicians."
    J "Thank you! Music is a huge part of my life."
    "Conclusion: You two remain friends."
    return

label stage_5_15_j:

    show jessica happy
    
    P "I love indie rock too! We should go to a concert together sometime."
    J "That would be amazing! Let's do it."
    "Conclusion: You two agree to switch numbers and go on a date!."
    return

label stage_5_16_j:

    show jessica mad
    
    P "That's cool, I've never really been into indie rock unfortunately"
    J "You should give it another listen , maybe you'll change your mind"
    "Conclusion: You walk away from each other"
    return

#HUGO******************************************************************


label stage_1_h:

    scene library

    hide jessica happy
    hide hugo neutral

    show hugo neutral

    P "Hey Hugo, I noticed we're in the same class. How are you finding it so far?"
    H "Oh, hey! Yeah, it's been interesting. Some of the topics are a bit challenging, but I'm enjoying it overall. How about you?"
    menu:
        "I agree, some parts are tough, but it's fun to learn new things. By the way, I love your sense of style!":
            jump stage_2_1_h
        "Yeah, the class is a bit challenging, but I think it's worth it. So, what do you like to do outside of school?":
            jump stage_2_2_h


label stage_2_1_h:

    show hugo shy

    P "I agree, some parts are tough, but it's fun to learn new things. By the way, I love your sense of style!"
    H "Thanks! I appreciate that. I like to express myself through my clothes."
    menu:
        "You definitely have a unique look. Do you have any favorite designers or brands?":
            jump stage_3_1_h
        "I've always wanted to try thrift shopping. Do you have any tips for a beginner?":
            jump stage_3_2_h


label stage_2_2_h:

    show hugo neutral

    P "Yeah, the class is a bit challenging, but I think it's worth it. So, what do you like to do outside of school?"
    H "I'm into photography and exploring the city. It's always fun to find new spots to capture."
    menu:
        "That's awesome! I love photography too. We should go on a photo walk sometime.":
            jump stage_3_3_h
        "Photography is such a great way to capture memories. What's your favorite thing to photograph?":
            jump stage_3_4_h
        

label stage_3_1_h:

    show hugo neutral

    P "You definitely have a unique look. Do you have any favorite designers or brands?"
    H "Not really, I just pick up whatever catches my eye. I like shopping in thrift stores and finding unique pieces."
    menu:
        "That's cool! I love thrift shopping too. Maybe we could go together sometime?":
            jump stage_4_1_h
        "I've never been thrift shopping, but I'd love to try it out with you.":
            jump stage_4_2_h_1

label stage_3_2_h:

    show hugo neutral

    P "I've always wanted to try thrift shopping. Do you have any tips for a beginner?"
    H "Sure, just be patient and have an open mind. You never know what you'll find."
    menu:
        "Thanks for the advice. Maybe you could show me the ropes sometime?":
            jump stage_4_2_h
        "I'll definitely keep those tips in mind. Thanks, Hugo!":
            jump stage_4_3_h

label stage_3_3_h:

    show hugo laughing

    P "That's awesome! I love photography too. We should go on a photo walk sometime."
    H "I'd love that! It's always more fun to explore with someone else."
    menu:
        "How about next weekend? We could make a day of it.":
            jump stage_4_4_h
        "Do you have any favorite spots for photography around the city?":
            jump stage_4_5_h

label stage_3_4_h:

    show hugo neutral

    P "Photography is such a great way to capture memories. What's your favorite thing to photograph?"
    H "I love taking pictures of urban landscapes and candid moments with people."
    menu:
        "Those are great subjects. I'd love to see some of your work sometime.":
            jump stage_4_6_h
        "That's really cool. I've always admired people who can capture the essence of a moment.":
            jump stage_4_7_h
            
label stage_4_1_h:

    show hugo laughing

    P "That's cool! I love thrift shopping too. Maybe we could go together sometime?"
    H "Sounds like a plan! I'm always up for some treasure hunting."
    menu:
        "Great, let's exchange numbers and plan a day for our thrifting adventure.":
            jump stage_5_1_h
        "Awesome, I'll keep an eye out for any cool thrift shops around and let you know.":
            jump stage_5_2_h


label stage_4_2_h_1:

    show hugo laughing

    P "I've never been thrift shopping, but I'd love to try it out with you."
    H "Sure, it's always fun to introduce someone new to thrifting. Let's do it!"
    menu:
        "Sounds like a plan! When's the best time for you?":
            jump stage_5_3_h
        "Great, I'm excited to see what kind of unique pieces we can find.":
            jump stage_5_4_h



label stage_4_2_h:

    show hugo laughing

    P "Thanks for the advice. Maybe you could show me the ropes sometime?"
    H "I'd be happy to! Let's plan a day to go thrifting together."
    menu:
        "That sounds great! How about next weekend?":
            "CONCLUSION: They plan a thrifting date for the following weekend, excited to explore together."
            return
        "Awesome! Let's exchange numbers so we can plan our thrifting adventure.":
            "CONCLUSION: They exchange numbers and plan to go thrifting together, looking forward to getting to know each other better."
            return

label stage_4_3_h:

    show hugo neutral

    P "I'll definitely keep those tips in mind. Thanks, Hugo!"
    H "No problem! If you ever want to go thrifting, just let me know."
    menu:
        "I'll take you up on that offer. Let's plan something soon.":
            "CONCLUSION: They agree to plan a thrifting outing together, opening the door for a potential date."
            return
        "I appreciate that. I'll definitely reach out if I decide to give it a try.":
            "CONCLUSION: They remain friendly acquaintances, with the potential to explore thrifting together in the future."
            return

label stage_4_4_h:

    show hugo laughing

    P "How about next weekend? We could make a day of it."
    H "I'm not available next weekend unfortunately"
    menu:
        "That's ok how about the week after!?":
            "CONCLUSION: Hugo thinks its a great idea and you two exchange numbers to go on a date"
            return
        "*You think he's lying and give him a weird look* Well that's ok I'll catch you around":
            show hugo angry
            "CONCLUSION: He was off put by the way you came off and you two part ways"
            return

label stage_4_5_h:

    show hugo neutral

    P "Do you have any favorite spots for photography around the city?"
    H "I do, but I like to keep them a secret. Maybe I'll show you sometime."
    menu:
        "I'd love that! It would be fun to discover new places together.":
            "CONCLUSION: They agree to plan a photography outing together, which could potentially lead to a date."
            return
        "I'll hold you to that! It's always nice to have a photography buddy.":
            "CONCLUSION: They express interest in exploring photography spots together, leaving the door open for a future date."
            return

label stage_4_6_h:

    show hugo neutral

    P "Those are great subjects. I'd love to see some of your work sometime."
    H "Sure, I'd be happy to show you my portfolio. Maybe we can grab coffee and go through it together."
    menu:
        "That sounds like a lovely idea. How about next weekend?":
            "CONCLUSION: They agree to meet for coffee next weekend and go through Hugo's photography portfolio, turning it into a casual date."
            return
        "Great, I'm looking forward to it! Let's exchange numbers so we can coordinate.":
            "CONCLUSION: They exchange numbers and plan to meet for coffee, opening the door for a potential date while discussing their shared interest in photography."
            return

label stage_4_7_h:

    show hugo laughing

    P "That's really cool. I've always admired people who can capture the essence of a moment."
    H "Thanks! It's something I'm passionate about. Maybe we could go out and take pictures together sometime."
    menu:
        "I'd love that! Let's plan a day to go on a photography adventure.":
            "CONCLUSION: They agree to plan a day for a photography outing together, which could potentially lead to a date."
            return
       
        "Photography is such a great way to connect with people. I'll definitely take you up on that offer.":
            "CONCLUSION: They express interest in going on a photography outing together, leaving the door open for a future date."
            return

label stage_5_1_h:

    show hugo neutral

    P "Great, let's exchange numbers and plan a day for our thrifting adventure."
    H "Sure, here's my number. Looking forward to it!"
    "CONCLUSION: They exchange numbers and agree to go thrifting together as a fun first date"
    return

label stage_5_2_h:

    show hugo laughing

    P "Awesome, I'll keep an eye out for any cool thrift shops around and let you know."
    H "Sounds good! I can't wait to see what we find."
    "CONCLUSION: They agree to go thrifting together and look forward to sharing their finds with each other."
    return

label stage_5_3_h:

    show hugo neutral

    P "Sounds like a plan! When's the best time for you?"
    H "How about next Saturday? We could make a day of it."
    menu:
        "Perfect! Let's exchange numbers and plan our thrifting adventure.":
            "CONCLUSION: They exchange numbers and look forward to their thrifting date on the following Saturday, excited to get to know each other better."
            return
        "Next Saturday works for me. Looking forward to it!":
            "CONCLUSION: They agree to go thrifting together on the following Saturday and look forward to spending time together and getting to know each other better."
            return

label stage_5_4_h:

    show hugo laughing

    P "Great, I'm excited to see what kind of unique pieces we can find."
    H "Me too! Thrifting can be full of surprises."
    menu:
        "Let's exchange numbers so we can stay in touch and plan our thrifting day.":
            "CONCLUSION: They exchange numbers and plan to go thrifting together, looking forward to getting to know each other better."
            return
        "Can't wait to go thrifting with you. See you then!":
            "CONCLUSION: They plan a thrifting date and are excited to see what treasures they can uncover together."
            return


#NICK******************************************************************


label stage_1_n:

    hide sasha
    hide nick

    show nick posing

    P "Hi, are you planning on using this charging port? I saw that it was being used earlier."
    N "No, it's not, go right ahead and use it if you need to."
    menu:
        "Thanks! By the way, I go by [povname]. What's your name?":
            jump stage_2_1_n
        "Thanks for letting me use the charging port. By the way, do you come here often?":
            jump stage_2_2_n

label stage_2_1_n:

    show nick loving

    P "Thanks! By the way, I go by [povname]. What's your name?"
    N "Nice to meet you, [povname]. I'm Nick."
    menu:
        "So, Nick, what brings you here?":
            jump stage_3_1_n
        "What do you do for fun, Nick?":
            jump stage_3_2_n


label stage_2_2_n:

    show nick posing

    P "Thanks for letting me use the charging port. By the way, do you come here often?"
    N "Yeah, I usually come here to work on my laptop or meet friends. How about you?"
    menu:
        "It's my first time here, actually. What's your favorite thing to order?":
            jump stage_3_3_n
        "I've been here a few times. It's a nice place to relax and catch up on some reading.":
            jump stage_3_4_n

label stage_3_1_n:

    show nick posing

    P "So, Nick, what brings you here?"
    N "Just waiting for a friend. How about you?"
    menu:
        "I'm actually waiting for my ride.":
            jump stage_4_1_n
        "I'm here for a meeting actually.":
            jump stage_4_2_n

label stage_3_2_n:

    show nick posing

    P "What do you do for fun, Nick?"
    N "I love exploring new places and trying out new food. How about you?"
    menu:
        "I'm into photography, so I love exploring too!":
            jump stage_4_3_n
        "I enjoy playing video games and watching movies.":
            jump stage_4_4_n

label stage_3_3_n:

    show nick laughing

    P "It's my first time here, actually. What's your favorite thing to order?"
    N "I love their iced lattes. You should give it a try!"
    menu:
        "I'll definitely try that. Do you mind if I join you until my friend arrives?":
            jump stage_4_5_n
        "I'm more of a tea person, but I'll give it a shot. What do you like to do when you're not here?":
            jump stage_4_6_n

label stage_3_4_n:

    show nick posing

    P "I've been here a few times. It's a nice place to relax and catch up on some reading."
    N "I agree. What kind of books do you like to read?"
    menu:
        "I enjoy reading science fiction and fantasy. How about you?":
            jump stage_4_7_n
        "I mostly read non-fiction, especially about history and science. What about you?":
            jump stage_4_8_n

label stage_4_1_n:

    show nick posing

    P "I'm actually waiting for my ride."
    N "Oh, cool. Do you live around here?"
    menu:
        "Yeah, I live pretty close by.":
            jump stage_5_1_n
        "No, I'm just visiting from out of town.":
            jump stage_5_2_n

label stage_4_2_n:

    show nick posing

    P "I'm here for a meeting actually."
    N "Oh, are you a student or working?"
    menu:
        "I'm a student. Studying computer science.":
            jump stage_5_3_n
        "I work as a graphic designer.":
            jump stage_5_4_n

label stage_4_3_n:

    show nick laughing

    P "I'm into photography, so I love exploring too!"
    N "That's great! We should go on a photo walk together sometime."
    menu:
        "I'd love that! Let's exchange numbers and plan it.":
            jump stage_5_5_n
        "Maybe some other time. I'm pretty busy these days.":
            jump stage_5_6_n

label stage_4_4_n:

    show nick loving

    P "I enjoy playing video games and watching movies."
    N "Nice! What's your favorite movie?"
    menu:
        "It's hard to pick just one, but I love The Matrix.":
            jump stage_5_7_n
        "I can't decide on a favorite, but I enjoy sci-fi films.":
            jump stage_5_8_n

label stage_4_5_n:

    show nick laughing

    P "I'll definitely try that. Do you mind if I join you until my friend arrives?"
    N "Not at all! I enjoy the company."
    menu:
        "Great, thanks! So, what do you do for a living?":
            jump stage_5_9_n
        "Thanks! What are you working on right now?":
            jump stage_5_10_n

label stage_4_6_n:

    show nick posing

    P "I'm more of a tea person, but I'll give it a shot. What do you like to do when you're not here?"
    N "I'm a big fan of hiking and exploring nature. What about you?"
    menu:
        "I love hiking too! Maybe we can go together sometime?":
            jump stage_5_11_n
        "That's nice. I'm more into art and museums, but I can appreciate nature too.":
            jump stage_5_12_n

label stage_4_7_n:

    show nick laughing

    P "I enjoy reading science fiction and fantasy. How about you?"
    N "I'm a fan of mystery and thriller novels."
    menu:
        "That's cool! Do you have any recommendations for a good mystery novel?":
            jump stage_5_13_n
        "Interesting. Maybe we can start a book club together?":
            jump stage_5_14_n

label stage_4_8_n:

    show nick posing

    P "I mostly read non-fiction, especially about history and science. What about you?"
    N "I like biographies and memoirs. It's fascinating to learn about other people's lives."
    menu:
        "Any favorite biographies or memoirs you'd recommend?":
            jump stage_5_15_n
        "That's a great genre. Maybe we can attend a book reading or signing together sometime?":
            jump stage_5_16_n

label stage_5_1_n:

    show nick posing

    P "Yeah, I live pretty close by."
    N "That's convenient. Maybe we can hang out sometime?"
    "CONCLUSION: You two agree to hang out later."
    return

label stage_5_2_n:

    P "No, I'm just visiting from out of town."
    "Nick is a little discouraged because you're not from around here"
    N "Ah, I see. Well, I hope you enjoy your time here. Any plans while you're in town?"
    menu:
        "I'll be attending a conference, but I hope to explore the city a bit too.":
            "CONCLUSION: You two exchange recommendations for places to visit in the city."
            return
        "Sorry it looks like I have to get going my ride should be here soon":
            show nick angry
            "CONCLUSION: You two chat about your friends and family, and eventually part ways."
            return

label stage_5_3_n:

    show nick loving

    P "I'm a student. Studying computer science."
    N "That's awesome! What's your favorite programming language?"
    menu:
        "I love Python. It's so versatile and easy to learn.":
            "CONCLUSION: You two chat about programming languages and computer science."
            return
        "I'm a big fan of JavaScript, since it's essential for web development.":
            "CONCLUSION: You two chat about web development and programming languages."
            return

label stage_5_4_n:

    show nick posing

    P "I work as a graphic designer."
    N "That's cool! What kind of projects do you usually work on?"
    menu:
        "I mostly design logos and branding for companies.":
            "CONCLUSION: You two chat about design and the creative process."
            return
        "I work on various projects like websites, posters, and packaging designs.":
            "CONCLUSION: You two chat about the different types of design projects you work on."
            return

label stage_5_5_n:

    show nick posing

    P "I'd love that! Let's exchange numbers and plan it."
    N "Sounds great! I'm looking forward to it."
    "CONCLUSION: You two exchange numbers and plan to meet for a photo walk."
    return

label stage_5_6_n:

    show nick loving

    P "Maybe some other time. I'm pretty busy these days."
    N "No worries! Maybe we'll run into each other again."
    "CONCLUSION: You two part ways, hoping to meet again in the future."
    return

label stage_5_7_n:

    show nick laughing

    P "It's hard to pick just one, but I love The Matrix."
    N "That's a classic! Have you seen any good movies lately?"
    menu:
        "I recently watched 'Inception,' and I really enjoyed it.":
            "CONCLUSION: You two chat about movies and share recommendations."
            return
        "I haven't seen anything great recently, but I'm always looking for suggestions.":
            "CONCLUSION: You two chat about movies and Nick offers some recommendations."
            return

label stage_5_8_n:

    show nick laughing

    P "I can't decide on a favorite, but I enjoy sci-fi films."
    N "I like sci-fi too! What are some of your favorite sci-fi movies or series?"
    menu:
        "I love 'Blade Runner' and the 'Star Wars' series.":
            "CONCLUSION: You two chat about your favorite sci-fi films and series."
            return
        "Some of my favorites are 'Interstellar' and 'The Expanse' series.":
            "CONCLUSION: You two chat about your favorite sci-fi films and series."
            return

label stage_5_9_n:

    show nick posing

    P "Great, thanks! So, what do you do for a living?"
    N "I'm a software engineer. What about you?"
    menu:
        "I'm a freelance writer. I write articles and blog posts for various clients.":
            "CONCLUSION: You two chat about your careers and share experiences."
            return
        "I work in marketing, helping businesses grow their online presence.":
            "CONCLUSION: You two chat about your careers and share experiences."
            return

label stage_5_10_n:

    show nick loving

    P "Thanks! What are you working on right now?"
    N "I'm just finishing up some work for a project. Do you have any exciting projects going on?"
    menu:
        "I'm currently working on a new website design for a client.":
            "CONCLUSION: You two chat about your projects and share design ideas."
            return
        "I'm in the middle of writing a series of articles for an online publication.":
            "CONCLUSION: You two chat about your projects and the writing process."
            return

label stage_5_11_n:

    show nick loving

    P "I love hiking too! Maybe we can go together sometime?"
    N "That sounds like a great idea! Let's exchange numbers and plan a hike."
    "CONCLUSION: You two exchange numbers and plan to go hiking together."
    return

label stage_5_12_n:

    show nick loving

    P "That's nice. I'm more into art and museums, but I can appreciate nature too."
    N "It's always good to have a variety of interests. Maybe we can check out a museum together sometime."
    "CONCLUSION: You two discuss your interests and plan to visit a museum together."
    return

label stage_5_13_n:

    show nick posing

    P "That's cool! Do you have any recommendations for a good mystery novel?"
    N "I recently read 'Gone Girl' by Gillian Flynn and really enjoyed it. You should give it a try."
    "CONCLUSION: You two chat about books and share recommendations."
    return

label stage_5_14_n:

    show nick loving

    P "Interesting. Maybe we can start a book club together?"
    N "That's a great idea! Let's exchange numbers and plan our first book club meeting."
    "CONCLUSION: You two exchange numbers and plan to start a book club."
    return

label stage_5_15_n:

    show nick laughing

    P "Any favorite biographies or memoirs you'd recommend?"
    N "I recently read 'Educated' by Tara Westover, and it was a powerful memoir. I highly recommend it."
    "CONCLUSION: You two chat about books and share recommendations."
    return

label stage_5_16_n:

    show nick loving

    P "That's a great genre. Maybe we can attend a book reading or signing together sometime?"
    N "I'd love that! Let's keep an eye out for any interesting events happening in the area."
    "CONCLUSION: You two plan to attend a book-related event together in the future."
    return


#SASHA******************************************************************


label stage_1_s:

    hide sasha
    hide nick

    show sasha happy

    P "You walk down the hall and make eye contact with Sasha."
    S "Hey, I noticed you aced that pop quiz today! What's your secret, some kind of mind control?"
    menu:
        "No mind control, just a lot of hard work and studying!":
            jump stage_2_1_s
        "Haha, well, I guess I just got lucky this time.":
            jump stage_2_2_s

label stage_2_1_s:

    show sasha happy

    P "No mind control, just a lot of hard work and studying!"
    S "Wow, I'm impressed! We should study together sometime."
    menu:
        "That sounds like a great idea! When are you free?":
            jump stage_3_1_s
        "I appreciate the offer, but I prefer to study alone.":
            jump stage_3_2_s

label stage_2_2_s:

    show sasha happy

    P "Haha, well, I guess I just got lucky this time."
    S "Luck or not, that was quite impressive. Maybe you can share some of that luck with me next time?"
    menu:
        "I'd be happy to! Maybe we can form a study group?":
            jump stage_3_3_s
        "I can't make any promises, but I'll try my best!":
            jump stage_3_4_s

label stage_3_1_s:

    show sasha happy

    P "That sounds like a great idea! When are you free?"
    S "How about after school on Thursday?"
    menu:
        "Thursday works for me. See you then!":
            jump stage_4_1_s
        "Actually, I'm not sure if I can make it. Can we find another time?":
            jump stage_4_2_s

label stage_3_2_s:

    show sasha sad

    P "I appreciate the offer, but I prefer to study alone."
    S "No worries, to each their own!"
    menu:
        "Maybe we can hang out some other time?":
            jump stage_4_3_s
        "I hope I didn't come off as rude. I just have my own study habits.":
            jump stage_4_4_s

label stage_3_3_s:

    show sasha shy

    P "I'd be happy to! Maybe we can form a study group?"
    S "That sounds like a great idea. Let's do it!"
    menu:
        "Awesome! How about we meet in the library after school tomorrow?":
            jump stage_4_5_s
        "I'll check with some classmates if they want to join as well.":
            jump stage_4_6_s

label stage_3_4_s:

    show sasha shy

    P "I can't make any promises, but I'll try my best!"
    S "That's all anyone can ask for. Keep up the good work!"
    menu:
        "Thanks, Sasha. Maybe we can hang out sometime outside of school?":
            jump stage_4_7_s
        "Well, good luck with your future quizzes!":
            jump stage_4_8_s

label stage_4_1_s:

    show sasha shy

    P "Thursday works for me. See you then!"
    S "Great! I'm looking forward to it."
    menu:
        "Me too. Maybe we can grab some coffee afterward?":
            jump stage_5_1_s
        "Alright, see you on Thursday!":
            jump stage_5_2_s

label stage_4_2_s:

    show sasha sad

    P "Actually, I'm not sure if I can make it. Can we find another time?"
    S "No problem, just let me know when you're free."
    menu:
        "Thanks, I'll check my schedule and get back to you.":
            jump stage_5_3_s
        "You know what, I think I'll just study on my own. Thanks anyway.":
            jump stage_5_4_s

label stage_4_3_s:

    show sasha sad

    P "Maybe we can hang out some other time?"
    S "Sure, that sounds fun. Let's do it!"
    menu:
        "How about going to see a movie this weekend?":
            jump stage_5_5_s
        "Great, I'll see you around then!":
            jump stage_5_6_s

label stage_4_4_s:

    show sasha sad

    P "I hope I didn't come off as rude. I just have my own study habits."

    S "No worries, I understand. Everyone has their own way of doing things."
    menu:
        "Thanks for understanding. Let's catch up some other time.":
            jump stage_5_7_s
        "Maybe it's best if we just keep things as they are.":
            jump stage_5_8_s

label stage_4_5_s:

    show sasha shy

    P "Awesome! How about we meet in the library after school tomorrow?"
    S "Perfect, I'll see you there."
    menu:
        "Maybe we can grab a bite to eat after we study?":
            jump stage_5_9_s
        "Great, looking forward to it!":
            jump stage_5_10_s

label stage_4_6_s:

    show sasha shy

    P "I'll check with some classmates if they want to join as well."
    S "Sounds good, the more the merrier!"
    menu:
        "I'll let you know who's in. Catch you later!":
            jump stage_5_11_s
        "Actually, never mind. I think I'll just focus on my own studies.":
            jump stage_5_12_s

label stage_4_7_s:

    show sasha shy

    P "Thanks, Sasha. Maybe we can hang out sometime outside of school?"
    S "I'd like that. Let's plan something soon."
    menu:
        "How about going to a concert this weekend?":
            jump stage_5_13_s
        "Great, let's talk more about it later.":
            jump stage_5_14_s

label stage_4_8_s:

    show sasha shy

    P "Well, good luck with your future quizzes!"
    S "Thanks, you too!"
    menu:
        "Maybe we'll cross paths again soon. Take care!":
            jump stage_5_15_s
        "I think we should focus on our own studies for now. Good luck!":
            jump stage_5_16_s

label stage_5_1_s:

    show sasha shy

    P "Me too. Maybe we can grab some coffee afterward?"
    S "Sounds perfect. It's a date!"
    "CONCLUSION: They agree to go on a date."
    return

label stage_5_2_s:

    show sasha happy

    P "Alright, see you on Thursday!"
    S "Can't wait! Catch you later."
    "CONCLUSION: You two remain friends."
    return

label stage_5_3_s:

    show sasha happy

    P "Thanks, I'll check my schedule and get back to you."
    S "Sounds good. Talk to you later!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_4_s:

    show sasha sad

    P "You know what, I think I'll just study on my own. Thanks anyway."
    S "Oh, alright. Good luck with your studies!"
    "CONCLUSION: You two realize you are not a good fit for each other."
    return

label stage_5_5_s:

    show sasha shy

    P "How about going to see a movie this weekend?"
    S "I'd love to! It's a date."
    "CONCLUSION: They agree to go on a date."
    return

label stage_5_6_s:

    show sasha happy

    P "Great, I'll see you around then!"
    S "Definitely. Have a great day!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_7_s:

    show sasha happy

    P "Thanks for understanding. Let's catch up some other time."
    S "Of course! Have a great day."
    "CONCLUSION: You two remain friends."
    return

label stage_5_8_s:

    show sasha mad

    P "Maybe it's best if we just keep things as they are."
    S "That's totally fine. Have a good day!"
    "CONCLUSION: You two realize you are not a good fit for each other."
    return

label stage_5_9_s:

    show sasha shy

    P "Maybe we can grab a bite to eat after we study?"
    S "I'd love that! It's a date."
    "CONCLUSION: They agree to go on a date."
    return

label stage_5_10_s:

    show sasha happy

    P "Great, looking forward to it!"
    S "Awesome, see you there!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_11_s:

    show sasha happy

    P "I'll let you know who's in. Catch you later!"
    S "Great, I'm looking forward to it. See you later!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_12_s:

    show sasha sad

    P "Actually, never mind. I think I'll just focus on my own studies."
    S "No problem, good luck with your studies!"
    "CONCLUSION: You two realize you are not a good fit for each other."
    return

label stage_5_13_s:

    show sasha shy

    P "How about going to a concert this weekend?"
    S "That sounds amazing! It's a date."
    "CONCLUSION: They agree to go on a date."
    return

label stage_5_14_s:

    show sasha happy

    P "Great, let's talk more about it later."
    S "Sure, let's discuss it later. Have a great day!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_15_s:

    show sasha happy

    P "Maybe we'll cross paths again soon. Take care!"
    S "Definitely, take care!"
    "CONCLUSION: You two remain friends."
    return

label stage_5_16_s:

    show sasha sad

    P "I think we should focus on our own studies for now. Good luck!"
    S "You too, good luck with everything!"
    "CONCLUSION: You two realize you are not a good fit for each other."
    return
