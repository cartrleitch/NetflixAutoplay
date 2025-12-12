import pyautogui
import time

p = pyautogui

p.FAILSAFE = True

p.pause = 1

screen_size = p.size()
screen_center_x = screen_size[0]
screen_center_y = screen_size[1]

print(f"Screen size: {screen_size}")
print("Automatically skipping intro and selecting next episode on Netflix!")

def move_center():
    p.moveTo(int(screen_center_x/2), int(screen_center_y/2), 0)

while True:
    try:
        next_episode_button_location = p.locateCenterOnScreen(r'next_episode.png', confidence=0.5)
        print("Locating next episode: " + str(next_episode_button_location))
        p.leftClick(next_episode_button_location)
        move_center()

    except p.ImageNotFoundException:
        #print("Next episode button not on screen.")
        pass

    try:
        skip_intro_button_location = p.locateCenterOnScreen(r'skip_intro.png', confidence=0.8)
        print("Locating skip intro: "+ str(skip_intro_button_location))
        p.leftClick(skip_intro_button_location)
        move_center()

    except p.ImageNotFoundException:
        #print("Skip intro button not on screen.")
        pass
    
    time.sleep(0.5)
