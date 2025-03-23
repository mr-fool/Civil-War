# The script of the game goes in this file.

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

#Imagine resource for the seventh part
image scene38 = "bg/seventh/scene1.png"
image scene39 = "bg/seventh/scene2.png"
image scene40 = "bg/seventh/scene3.png"
image scene41 = "bg/seventh/scene4.png"
image scene42 = "bg/seventh/scene5.png"

#Imagine resource for the eighth part
image scene43 = "bg/eighth/scene1.png"
image scene44 = "bg/eighth/scene2.png"
image scene45 = "bg/eighth/scene3.png"
image scene46 = "bg/eighth/scene4.png"
image scene47 = "bg/eighth/scene5.png"
image scene48 = "bg/eighth/scene6.png"
image scene49 = "bg/eighth/scene7.png"
image scene50 = "bg/eighth/scene8.png"
image scene51 = "bg/eighth/scene9.png"
image scene52 = "bg/eighth/scene10.png"
image scene53 = "bg/eighth/scene11.png"

#Imagine resource for the ninth part
image scene54 = "bg/ninth/scene1.png"
image scene55 = "bg/ninth/scene2.png"
image scene56 = "bg/ninth/scene3.png"
image scene57 = "bg/ninth/scene4.png"
image scene58 = "bg/ninth/scene5.png"
image scene59 = "bg/ninth/scene6.png"
image scene60 = "bg/ninth/scene7.png"
image scene61 = "bg/ninth/scene8.png"

label splashscreen:
    stop music
    scene disclaimer
    with Pause(5)
    hide disclaimer

    play movie "images/gunFightwithSound.webm"  
    $ renpy.pause(2.0, hard=True) 
    stop movie

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
    
    play movie "images/pound.webm"  # Use the path from your screenshot
    $ renpy.pause(7.0, hard=True)  # 7 seconds duration as you specified
    stop movie
    
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


    play movie "images/bodies.webm"  # Use the path from your screenshot
    $ renpy.pause(6.0, hard=True)  # 6 seconds duration as you specified
    stop movie

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
    
    play movie "images/rocket.webm"  # Use the path from your screenshot
    $ renpy.pause(4.0, hard=True)  # 4 seconds duration as you specified
    stop movie

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

label seventh:
    stop music
    play music "audio/Gloria.mp3"    

    scene scene38
    e "The young male demographic was excited at the beginning of the war. They were all thinking that the war would be their moment to shine."

    scene scene39
    e "The rose blossom smile on their face when they first wore their battle uniforms. Girls on both sides of the main street cheered them on and drums beat as they marched to war. "

    scene scene40
    e "They thought it would be a short and glorious war. They could not have been more wrong. "

    scene scene41
    e "Having served in the Great Meme War (four tours in the USA, Germany, France and UK)  prior, the bloodiest war ever recorded in the history of the internet, I know war is never short and glorious."

    scene scene42
    e "I am not some POG, fobbit, non combat type who completed the basic training but never deployed. I have seen my comrades getting blown away right next to me and tortured by enemies. "

label eighth:
    stop music
    play music "audio/Mars na Drinu.mp3"

    scene scene43
    e "Television networks were reporting victories after victories."

    scene scene44
    e "One memorable interview was done by a government network, CAC, where the network interviewed a young soldier holding up a capture flag from the enemy’s military headquarter." 

    scene scene45
    e "At that point, I thought I was missing out by staying at home. This was exacerbated by the guilt-shame stare people shot at me everywhere I went. It was driving me nuts." 

    scene scene46

    play movie "images/shortage.webm"  # Use the path from your screenshot
    $ renpy.pause(15.0, hard=True)  # 15 seconds duration as you specified
    stop movie
    
    scene scene46
    e "Soon it was announced that citizens must do their parts by conserving food so they could send it to the front line. As expected, this caused mass panic."

    scene scene47
    e "The media was heavily censored and reporting alternative truth so people thought everything was under control. There were however small citizen journalist groups that were reporting the truth over the internet."

    scene scene48
    e "They reported the actual material shortage in the front line. For example, soldiers had to improvise and duct tape magazines together as the shortage of vests persisted.  The authorities dealt with them quickly, labeled them conspiracy theorists, and executed them." 

    scene scene49

    play movie "images/shelling.webm"  # Use the path from your screenshot
    $ renpy.pause(24.0, hard=True)  # 24 seconds duration as you specified
    stop movie
    
    scene scene49
    e "It did not take long before my town was under siege and shelled. The establishment could no longer hide the truth. People were forced to wake up to the reality."

    scene scene50
    e "The alternative truth media is no longer useful to the elites so they have become the pleb class. At first, people would fork over top dollars to fuck former news anchors as it was the new and hip thing."
    
    scene scene51
    e "Soon the cool factor died off. Most of them become addicted to drugs. Drugs have taken a toll on their once beautiful bodies.  Like most wars, it eventually reached a stalemate."

    scene scene52
    e "Despite that most people are unable to accept that and believe in a final victory. People lost hope. People looked right through me as they realized that I was right about the war from the beginning. It will be a prolonged war."

    scene scene53
    e "People turn to drugs to cope as resources become scarce.  This leads to the rise of mafia power. The government turned a blind eye to it as they also want a pacified public too. In addition, the government encouraged the consumption of soy based products in an attempt to pacify the public."

label ninth:
    stop music
    play music "audio/sokoly.mp3"
    
    
    scene scene54
    pause #

    scene scene55
    e "It is hard to recollect how it all started but I will try my best. Every morning when I wake up, I feel like the war started yesterday. Everything happens too quickly. It is just surreal."

    scene scene56
    
    play movie "images/collapse.webm"  # Use the path from your screenshot
    $ renpy.pause(3.0, hard=True)  # 3 seconds duration as you specified
    stop movie

    scene scene56
    e "It is hard to nail what single factor started the war. It just falls like a house of cards. Before the start of the civil war, Canada underwent 3 years of economic hardship." 
    
    scene scene57
    e "Mainstream centrist parties were uninspiring and corrupt. The leaders went on fancy vacations while the public were left to die." 
    
    scene scene58
    e "To the average public, there seemed to be no end to the abyss. Centrist parties were gradually replaced by radicals. Under the radicals’ vision, Canada was being reimagined."
    
    scene scene59
    e "Different identity groups who previously lived in harmony now blamed each other for their problems."
    
    scene scene60
    e "There were constant small clashes in the street. I classified those as riots but not a civil war."

    scene scene61
    e "It all changed on June 27 a speech given in Truro Public Square. A bald middle aged man with a mustache wearing a black mariner hat gave a speech on the oppressed young male."

label tenth:
    stop music

    #scene 1  The Spark of Rebellion
    e "His name is Slobo. Despite mainstream media blackout, it was broadcasted on all the major alt-tech and alt-media. I did not watch it live. "
    e "I came across it through the dissenter network. The footage was reposted, shared, and upvoted. Phrases like 'reimagineCanada' and 'Do you want to be part of the new future' were trending."
    
    #scene 2 Slobo’s Electric Speech

    e "I watched the playback of the speech. It was different from your average boring centrist’s speech. I could feel the electric atmosphere and the sturdy hand gesture as he spoke."
    e "Not only did the speech resonate in my head, the speech sparked new imagination in the minds of young males like me."
    e "The surge of new-found realization was infectious; the air was filled with a spirit of togetherness which was hard to ignore. The sudden realization made everything seem possible. "
    e "It all made sense why young males were not well-off in modern society. I no longer feel alone. "

    play movie "images/speech.webm"
    $ renpy.pause(10.0, hard=True)
    stop movie

    e "This particular part of the speech stuck in my mind: 'Many powers are against us but this time God is with us and we will win."


    #Scene 3: Clash of Ideologies

    e "For every action, there is an equal and opposite reaction. The elites and authorities further responded by portraying feminized males as the 'real male.' "
    e"Centralists desperately tried to rally and mobilize femboys, soyboys, and feminists to defend the power structure. All was lost when the authorities’ femboy thugs clashed with the radicals. "
    e "The femboys were no match to the radicals despite being armed with batons. The first encounter emboldened the radical and it all escalated."

    #Scene 4: Propaganda Spreads

    e "Propaganda from the radicals started to circulate portraying a muscular young male hero called Knock Out Man capable of knocking out the authorities’ femboy thug with a single punch."

    #Scene 5: Night of Terror
    e "Towns were divided between revolutionaries and counter-revolutionaries. The authorities began terrorizing the public, dragging potential revolutionaries to secret prisons. "
    e "Black four-door sedans would show up in the middle of the night grabbing people. Those people were never seen again."

    #Scene 6: Hope in the Streets

    e "The terror period resulted in radical parties forming their own paramilitary groups patrolling the streets. People cheered on as the young guards patrolled the street. "
    e"The ranks were tightly closed with strong marching beats. People saw hope in this reimagined Canada. "
    e"The street was cleaned. Radical groups handed out food to the homeless, elders, and the disenfranchised people. Parties’ banners fly all over the street. "
    e "Previously closed shops were making guns. Even the moderate felt the pressure and replaced the national Canadian flag. Moderates were the new minority. Unity amongst provinces was gone. "
    e "People questioned what they have in common with people in other provinces."

    #Scene 7: Descent into War
    e "The good days rarely last. Soon, we were at an economic crisis again and full-scale war broke out. The purpose of the war became less and less clear as the war went on."



    return
