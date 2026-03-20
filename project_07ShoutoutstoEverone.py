
#%%
#given name ko prounce karna hai
#using win32 API.
#awaz like - shoutout to Parth , shoutout to harry ..

# %pip install pyttsx3

import pyttsx3
engine=pyttsx3.init()

t=["parth","harry","abhay"]

for name in t:
    engine.say(f"shoutout to {name}")
    engine.runAndWait()



