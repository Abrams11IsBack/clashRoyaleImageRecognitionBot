import random
import time

import cv2
import numpy as np
import pyautogui
import os
from gtts import gTTS
import pygame

def find_image_on_screen(image_folder, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screen_img = np.array(screenshot)
    screen_img = cv2.cvtColor(screen_img, cv2.COLOR_RGB2BGR)

    screen_gray = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)

    for image_name in os.listdir(image_folder):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            template_path = os.path.join(image_folder, image_name)
            template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

            if template is None:
                print(f"Failed to load image: {image_name}")
                continue

            result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val >= threshold:
                x, y = max_loc
                return (x, y, image_name)

    return None


if __name__ == "__main__":
    language = 'pl'
    time.sleep(5)
    #pygame.mixer.init()

    print("Gram na decku kartosza")
    #myobj = gTTS(text="Zaczynam.", lang=language, slow=False)
    #myobj.save("mowa.mp3")
    #pygame.mixer.music.load("mowa.mp3")
    #pygame.mixer.music.play()
    while True:
        try:
            image_folder = "guwno"
            threshold = 0.7 # TRESHOLD
            result = find_image_on_screen(image_folder, threshold)

            if result:

                x, y, image_name = result
                print(f"Found image '{image_name}' at coordinates: ({x}, {y})")
                print()

                #myobj = gTTS(text="Wykryłem obrazek.", lang=language, slow=False)
                #myobj.save("mowa.mp3")

                #pygame.mixer.music.load("mowa.mp3")
                #pygame.mixer.music.play()

                if image_name == "egiant.png":
                    print("Widzę elektro chuja. To czas na push.")
                    pyautogui.moveTo(x, y)
                    pyautogui.dragTo(x, (y - 400), button='left', duration=0.3)
                elif image_name == "fireball.png":
                    pyautogui.moveTo(x, y)
                    print("Ok musze przycelować.")
                    result = find_image_on_screen("przeciwnik", threshold) # CUSTOM
                    if result:
                        x, y, image_name = result
                        print(f"Widze chuja. '{image_name}' Tutaj szczelam! ({x}, {y+150})")
                        pyautogui.dragTo(x, y+150, button='left', duration=0.5)
                    else:
                        print("Chyba mnie popierdoliło.")
                elif image_name == "log.png":
                    pyautogui.moveTo(x, y)
                    nigaY = y
                    print("JEZU JAK JA KOCHAM KŁODE!!! ")
                    print("Musze pomyśleć. Gdzie mam ją wytoczyć.")
                    result = find_image_on_screen("log", 0.9) # CUSTOMOWY TRESHOLD DO GOBLINOW
                    if result:
                        x, y, image_name = result
                        print(f"Wykryto Izraelskie Świnie (Żydzi). '{image_name}' Uwalniam palestyne. ({x}, {y})")
                        pyautogui.dragTo(x, (nigaY-400), button='left', duration=0.3)
                    else:
                        result = find_image_on_screen("przeciwnik", threshold)
                        if result:
                            x, y, image_name = result
                            print(f"Widze tam kogoś. Moje drewno aż stoi. ({x}, {y})")
                            pyautogui.dragTo(x, (y+200), button='left', duration=0.3)
                        else:
                            result = find_image_on_screen("danger_tower", 0.9)
                            if result:
                                x, y, image_name = result
                                print(f"Moja wieża jest zagrożona. Nie chcemy 9/11. ({x}, {y})")
                                pyautogui.dragTo(x, (y-100), button='left', duration=0.3)
                            else:
                                print("Dobra w dupie to mam.")
                elif image_name == "bats.png":
                    pyautogui.moveTo(x, y)
                    oldX = x
                    oldY = y
                    print("Muszę przyjąć strategię defensywną, zlokalizować przeciwnika i postawić tam batsy.")
                    result = find_image_on_screen("przeciwnik", threshold)
                    if result:
                        x, y, image_name = result
                        print(f"Przeciwnik zlokalizowany. Wypuszczam szarańcze. ({x}, {y})")
                        pyautogui.dragTo(x, y, button='left', duration=0.3)
                    else:
                        print("Szczerze to troche tweakuje. Rzucam monetą jak bede mial reszke to wale byle gdzie.")
                        if random.randint(0, 1) == 0:
                            print("reszka. no dobra")
                            pyautogui.dragTo(oldX, oldY, button='left', duration=0.3)
                        else:
                            print("orzeł. wywalone jajca w takim razie.")
                elif image_name == "goldenknight.png":
                    pyautogui.moveTo(x, y)
                    print("Golden Knight. Przyznam, przystojny gość. Ważne żeby abilitka była w dobrym momencie.")
                    pyautogui.dragTo(x, (y - 400), button='left', duration=0.3)

                    time.sleep(2)
                    result = find_image_on_screen("golden", threshold)
                    if result:
                        x, y, image_name = result
                        print(f"Przeciwnik zlokalizowany. Wypuszczam szarańcze. ({x}, {y})")
                        pyautogui.click(x, y)
                    else:
                        print("Chyba jestem ślepy bo nie widze przycisku abilitki golden jajca.")
                elif image_name == "tesla.png" or image_name == "evo_tesla.png":
                    print("Elektromachina.")
                    pyautogui.moveTo(x, y)
                    pyautogui.dragTo(x, (y - 600), button='left', duration=0.3)
                else:
                    print("Dobra wale to na pałe.")
                    pyautogui.moveTo(x, y)
                    pyautogui.dragTo(x, (y - 400), button='left', duration=0.3)
                time.sleep(2)
            else:
                print("Gówno widze za przeproszeniem.")
                time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")