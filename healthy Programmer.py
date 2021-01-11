import pygame
from pygame import mixer
from datetime import datetime
from time import time
def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user=input()
        if input_of_user==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")


if __name__=='main':
    #musi("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=40*60
    exsecs=30*60
    eyessecs=45*60

    while True:
        if time()-init_water>watersecs:
            print("Water drinking time.Enter Drank to stop the music")
            music("water.mp3",'drank')
            init_water=time()
            log_now("Drank water at")
        if time()-init_eyes>eyessecs:
            print("Eyes exercise time.Enter Done to stop the music")
            music("Exercise.mp3",'Done')
            init_eyes=time()
            log_now("Eyes Relaxed at")
        if time()-init_exercise>exsecs:
            print("Exercise time.Enter DoneEx to stop the music")
            music("Ex.mp3",'Exercise Done')
            init_exercise=time()
            log_now("Physical activity done at")


