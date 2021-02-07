init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("audio/Funeral.mp3", always_unlocked=True)
    mr.add("audio/moonlight.mp3", always_unlocked=True)
    mr.add("audio/train.mp3", always_unlocked=True)
    mr.add("audio/csardas.mp3", always_unlocked=True)
    mr.add("audio/Lights.mp3", always_unlocked=True)
    mr.add("audio/Life.mp3", always_unlocked=True)
    mr.add("audio/Gloria.mp3", always_unlocked=True)
    mr.add("audio/Mars na Drinu.mp3", always_unlocked=True)

# Step 3. Create the music room screen.
screen music_room:

    tag menu
    use game_menu("Music Room"):

        has vbox

        # The buttons that play each track.
        textbutton "Tamo daleko" action mr.Play("audio/Funeral.mp3")
        textbutton "Moonlight Sonata" action mr.Play("audio/moonlight.mp3")
        textbutton "Young Train Driver" action mr.Play("audio/train.mp3")
        textbutton "Csárdás" action mr.Play("audio/csardas.mp3")
        textbutton "Lights from the Party Central" action mr.Play("audio/Lights.mp3")
        textbutton "Where my life came into bloom" action mr.Play("audio/Life.mp3")
        textbutton "Gloria" action mr.Play("audio/Gloria.mp3")
        textbutton "Mars na Drinu" action mr.Play("audio/Mars na Drinu.mp3")
        
        null height 20


        # Buttons that let us advance tracks.
        textbutton "Next" action mr.Next()
        textbutton "Previous" action mr.Previous()

        null height 20

        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "audio/game_menu_mortar_fire.mp3")