# Poetry Phone Project

# Poem ideas
- A couple of small poems that are structured like voicemails

# Form ideas

- Phone booth: Full sized phone booth where the user can enter the booth and record poems on the phone, and either listen to poems on the reciever or on a loudspeaker outside of the booth or both
- There could be a little 'log book' that contain self contained poems in the form of voice mails
- A retro style phone for recording and listening or broadcast on a loudspeaker
- Little handsets for recording and listening
- Maybe there could be an associated video of a face that mouths the words or two faces having a conversation from the words of many people. Representing common experiences
- Need to figure out the best way 


# Extra ideas

- Maybe I could keep all the lines that don't totally fit 
- Reading someone elses poem is like stepping into their shoes


# Input Phase:
 - Take audio from the user
 - Clean and compress audio
 - Maybe I could find the root note of their voice and play a note underneath it

# Analysis Phase:
 - Take in n lines audio
 -     - Length could be an issue, but maybe we could find the longest pause between 30-50 seconds in and cut the audio down
 - Find which lines the audio corresponds to
 - Cut the audio into lines
 - Store the audio segments linked to the line it contains
 -     - Keep database of lines to audio files?

# Broadcast Phase:
 - Take a poem
 - For each line of the poem take a random corresponding audio file
 -     - Ideally store the recorder ID so that multiples from the same recorder aren't in the same playback
 - Combine those 
