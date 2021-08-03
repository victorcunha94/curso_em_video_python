from pygame import mixer, load, play, wait, event, music
pygame.init()
mixer.music.load('paul.mp3')
mixer.music.play()
mixer.event.wait()

