﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mauzer")

#Image resource for the first part
image scene1 = "bg/first/scene1.png"
image scene2 = "bg/first/scene2.png"
image scene3 = "bg/first/scene3.png"
image scene4 = "bg/first/scene4.jpg"
image scene5 = "bg/first/scene5.png"
image scene6 = "bg/first/scene6.png"
#bonus
image scene7 = "bg/first/sniper.png"
#Splashscreen

#Imagine resource for the second part
image scene8 = "bg/second/scene1.png"
image scene9 = "bg/second/scene2.png"
image scene10 = "bg/second/scene3.png"
image scene11 = "bg/second/scene4.png"
image scene12 = "bg/second/scene5.png"

#Imagine resource for the third part
image scene13 = "bg/third/scene1.png"
image scene14 = "bg/third/scene2.png"
image scene15 = "bg/third/scene3.png"
image scene16 = "bg/third/scene4.png"
image scene17 = "bg/third/scene5.png"
image bonus2 = "bg/third/bonus.png"

#Imagine resource for the fourth part
image scene18 = "bg/fourth/scene1.png"
image scene19 = "bg/fourth/scene2.png"
image scene20 = "bg/fourth/scene3.png"
image scene21 = "bg/fourth/scene4.png"
image scene22 = "bg/fourth/scene5.png"
image scene23 = "bg/fourth/scene6.png"
image scene24 = "bg/fourth/scene7.png"

#Imagine resource for the fifth part
image scene25 = "bg/fifth/scene1.png"
image scene26 = "bg/fifth/scene2.png"
image scene27 = "bg/fifth/scene3.png"
image scene28 = "bg/fifth/scene4.png"
image scene29 = "bg/fifth/scene5.png"
image scene30 = "bg/fifth/scene6.png"

#Imagine resource for the sixth part
image scene31 = "bg/sixth/scene1.png"
image scene32 = "bg/sixth/scene2.png"
image scene33 = "bg/sixth/scene3.png"
image scene34 = "bg/sixth/scene4.png"
image scene35 = "bg/sixth/scene5.png"
image scene36 = "bg/sixth/scene6.png"
image scene37 = "bg/sixth/scene7.png"

label splashscreen:
    stop music
    scene disclaimer
    with Pause(5)
    hide disclaimer

    $ renpy.movie_cutscene("gunFightwithSound.webm")

    return

# The game starts here.


label start:
    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/Funeral.mp3"
    scene scene1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show me

    # These display lines of dialogue.

    #First Part

    e 'Laying there in the comfort of rubble, I ponder “How long have I been here? How long will I remain?" “Time waits for no one”, they say."'
    
    scene scene2

    e "The glassy office buildings that were once symbols of prosperity have been reduced to charcoaled towers. The street is filled with shattered glasses, concrete rubble and artillery fragments.  "

    
    scene scene3

    e "Empty charcoaled cars are left on the streets. "

    scene scene4
    e "Barricades in and around the town were set up by different paramilitary groups."

    scene scene5
    e "Food rations are being hijacked by the local mafia. And only a narrow supply route is keeping the city alive."

    stop music
    show scene6
    $ renpy.movie_cutscene("pound.webm")
    
    play  sound "audio/artillery.mp3"
    scene scene6
    e "The city is surrounded by eerie gloomy hills. Within the gloomy hills lay the artilleries staring down at us waiting to pound us."
    
    #bonus scene
    stop sound
    scene scene7
    play sound "audio/m76.mp3"
    e "Inside the building ruins lie the silent wolves"

    #Second Part
label second:
    stop sound
    stop music
    scene scene8
    show me
    play sound "audio/re.mp3"
    e "Who am I? My name is Mauzer. I was a NEET, Not in Education, Employment, or Training, before the start of the civil war so I guess you can say the war really did not have much effect on me. "

    stop sound
    play music "audio/moonlight.mp3"

    scene scene9
    e "I am used to social isolation. In fact, I am asocial. I have nothing in common with the rest of the world. I hate sports and rap music."

    scene scene10
    show me2
    e "Thankfully, I still have my accordion so I can make turbofolk music to cope with the current situation. I am a wannabe musician that wants to write diss songs like Oj Alija, alio by Koridor and war songs like Maj 92 by Pirgo.  "

    scene scene11
    e "I don’t keep track of time as there is nothing to look forward to. I don’t even want to wake up, but each morning I wake up to the sound of shelling.  The only thing I really miss is tendies. Before the Canadian civil war, I was able to grab tendies from the McDick close to my home. "

    stop music
    show scene12
    $ renpy.movie_cutscene("bodies.webm")
    scene scene12
    e "Now my food source is just new dead bodies that I can find on the street. It is not as bad as you think."

    #third part
label third:
    stop music
    play music "audio/train.mp3"
    scene scene13
    e "My initial thought when the civil war began was that it’s a dream come true. I finally got a chance to become a superhero like in anime and have a purpose in life. Not surprisingly, I did not become a hero. "

    scene scene14
    e "I was a young male NEET who was being blamed for everything wrong with Canadian society despite working hard for my entire life and becoming a computer science graduate."

    scene bonus2
    e "My existence is a void. A blackhole, dragging everyone down with its bleak gravity. Time stretches out before me, endless, and everyday, I must face this truth: my existance is a burden on myself and everyone around me."
    scene scene15
    e "I did not gain anything from the civil war either. Let’s be real, misery loves company. I am delighted to see all those successful arrogant chads and karens are struggling to cope and survive."

    scene scene16
    e "You know the stereotypical asses who think they are better than you because they worked at big corporations, especially the affirmative action types. The affirmative type who think they know what they are talking about."

    scene scene17
    e "The entitled type that always be like “Get a job, Anon” or “Is McDick too good for you” or the “Get educated so you don’t have to work at McDick”. Many of them are in the upper middle class due to their compliance to the government’s narrative."
    

label fourth:
    stop music
    play music "audio/csardas.mp3"

    scene scene18
    e "Privileged attractive girls are able to become the mafia’s sex toys. It is kind of like that time when Princess Leia becomes Jabba’s sex toy in Star Wars."

    scene scene19
    e "They are constantly begging for dicks so they will have excess rice to send to their families. Some less fortunate ones are now having to whore themselves out to the mafia for a mere 30g of rice. "
    
    scene scene20
    e "Grannies in retirement demoralized. Their faces timeworn and wrinkled. Their voices are weak and fragile."
    
    scene scene21
    e "They have to do B.D.S.M and anal sex in order to stay competitive in the “food market.”"
    
    scene scene22
    e "Many of them even attempt to deepthroat to stay further ahead of the fierce competition. They are lucky if they only have a gag reflex."

    scene scene23
    e "Sadly age catches up with everyone. They ended up either with a broken jaw or just downright death from choking on a dick."

    scene scene24
    e "The constant stretching of the anus resulted in anal leakage and rose bud. Getting nutrients is so hard that jizz is considered a protein shake."
    

label fifth:
    stop music
    play music "audio/Lights.mp3"

    scene scene25
    e "What is my daily routine? Since it is a civil war, there is no internet or electricity. I have to admit initially I was not used to it since I am a tech guy. "

    scene scene26
    e "Eventually, I got used to it. I am a chill person and have learned to cope since my early age. I always think on the bright side. I no longer have to deal with annoying neighbors who lectured about where I can park on the street and church blasting annoying music. "

    #bonus
    show scene27
    $ renpy.movie_cutscene("rocket.webm")

    scene scene27
    e "My daily routine is really not that different from the pre-war period. After I wake up, I wait until the artillery fire stops, then different paramilitary forces start shooting at each other."
    
    scene scene28
    e "By midnight, I look for any dead bodies. I scavenge anything I can find on the bodies from clothing to the body itself aka my food."

    scene scene29
    e "The transition to cannibalism was not that hard. I took a hunting and food preparation course before the war. I am used to seeing gore. "

    scene scene30
    e "You are probably wondering how I pass time from the morning to midnight, right? I make turbofolk music to cope. Other musicians make propaganda music to please the elites."

label sixth:
    stop music
    play music "audio/Life.mp3"

    scene scene31
    e "There are only two groups of people in this era: the paramilitary and the war-profit mafia. I want nothing to do with the society so I am neither. I am just a scavenger."

    #changed
    scene scene32
    e "The void has consumed me and all that's left is pain. My invisible agony has reached an unendurable level and killing myself is preferable to the never ending flames of life."

    scene scene33
    e "Rich and powerful grandmas have boy toys to sexually entertain them. The boy toys will lick old wrinkled granny pussies for food."

    scene scene34
    e "Guys become ladyboys like a circus freak in hopes the powerful will tip them rice. In order to draw more attention, some of them even try to suck a big horse dong."

    scene scene35
    e "In a sense I am lucky because I don’t have to become a ladyboy. Oh yeah, I forgot to mention why everything is measured in 30g of rice. 30g of rice is not because of rice shortage but rather rice monopolization. "

    scene scene36
    e "The rich and the powerful want to give enough food to the plebs so they can survive and work yet not enough to give them the energy to rebel."
    
    scene scene37
    e "Foot soldier is the only group other than the elites that are receiving a decent amount of food. The foot soldier usually gets around 50-60g of rice per day."

    return