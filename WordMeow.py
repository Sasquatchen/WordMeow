
from playsound import playsound
import urllib.request, urllib.parse, urllib.error
import json




def start():
    
    x = ('bottle', 'pebble', 'single', 'jumble', 'tickle', 'rattle', 'middle', 'bubble', 
         'sample', 'cattle', 'snuggle', 'kettle', 'jungle', 'ankle', 'giggle', 'simple', 
         'settle', 'temple', 'battle', 'mumble')

    y = ('bottle.mp3', 'pebble.mp3', 'single.mp3', 'jumble.mp3', 'tickle.mp3', 'rattle.mp3', 'middle.mp3', 'bubble.mp3', 
         'sample.mp3', 'cattle.mp3', 'snuggle.mp3', 'kettle.mp3', 'jungle.mp3', 'ankle.mp3', 'giggle.mp3', 'simple.mp3', 
         'settle.mp3', 'temple.mp3', 'battle.mp3', 'mumble.mp3')

    i = 0
    print("WordMeow")
    print("See if you can spell all the words correctly")
    print('Type r to repeat word')

    while (i < len(x)):

        playsound(y[i])

        playsound(y[i])

        word = input("Spell the word:")

        if (word == x[i]):
            playsound('clap.mp3')
        elif(word == 'r'):
            i -= 1
        elif (word != x[i]):
            playsound('cat.mp3')
            i -= 1

        i += 1

if __name__ == "__main__":
    start()
    
