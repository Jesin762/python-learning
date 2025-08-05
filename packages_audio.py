from gtts import gTTS
import os
store=input("enter your text :")
c=gTTS(store)
c.save("test_audio.mp3")
os.system("start test audio.mp3")