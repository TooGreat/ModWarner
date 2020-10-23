import discord 
import asyncio
import os
import pyttsx3

# Use a class to make the variable static #
class UserChannel:
    id = 0

# Define things im gonna use #
clientToken = 'PLACE_TOKEN_HERE' #the login token
client =  discord.Client() #the discord client object
userChannel = UserChannel() #the class that contains the variable for the channel the user is in
voiceEngine = pyttsx3.init() #used for text to speech

# Voice state event #
@client.event
async def on_voice_state_update(member, before, after):

   if member.voice == None: #make sure that voice is not null
       return #return out of the function

   eventChannel = member.voice.channel #get the current channel

   if member == client.user: #check if the member that changed voice state is the user
       userChannel.id = eventChannel.id #set the user channel id to the event one
       return

    
   if eventChannel.id == userChannel.id: #check if the eventChannel id is the userChannel id
        if member.permissions_in(eventChannel).mute_members or member.permissions_in(eventChannel).priority_speaker: #check if the freshly changed voice state has mute permissions
            voiceEngine.say("Moderator " + member.display_name + " has joined") #TTS that a moderator has joined
            voiceEngine.runAndWait() #run the routines that have been stated

    
client.run(clientToken, bot=False, reconnect=True) #execute the client
