import matplotlib.pyplot as plt
from playsound import playsound as pl
import RIGHT_ARM as ra
import LEFT_ARM as la
import BICEP_CURL as b_c
import LATER_RAISE as l_r
import CHEST_ROW as c_r
import SHOULDER_PRESS as sho
import OVER_HEAD as over
import BARBELL as bar
import PICS_0RDER as sp

import numpy as np

set1 = 1
x11 = 0
x22 = 0
x33 = 0
x44 = 0
x55 = 0
x66 = 0
x77 = 0
x88 = 0

a = input("start the exercise ---y/n   ->")
try:
    while (a!= "n"):

        print("START THE EXERCISE\nDON'T DO TOO FAST\nTAKE 30 SECONDS BREAK FOR ONE  EXERCISE DONE ")

        for b in range(1, 10):
            if b == 1:
                sp.one_pic()

                print("1--RIGHT ARM")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = ra.right_arm()
                x1 = v()[-1]

            elif b == 2:
                sp.one_pic()

                print("2--LEFT ARM")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = la.left_arm()
                x2 = v()[-1]
            if b == 3:
                sp.one_pic()

                print("3--BICEP CURLS")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = b_c.bicepcurl()
                x3 = v()[-1]
            elif b == 4:
                sp.two_pic()

                print("4--LATERAL RAISES")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = l_r.later_raise()
                x4 = v()[-1]
            elif b == 5:
                sp.three_pic()
                print("5--CHEST ROWS")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = c_r.chest_row()

                x5 = v()[-1]
            elif b == 6:
                sp.foruth_pic()
                print("6--SHOULDER PRESS")
                #pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = sho.shoulder_press()
                x6 = v()[-1]

            elif b == 7:
                sp.fith_pic()

                #print("7--OVER HEAD ")
                pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = over.over_head()
                x7 = v()[-1]

            elif b == 8:
                sp.sixth_pic()
                print("8--BARBELL CURLS")
                pl(r"c:\Users\koran\Downloads\ttsMP3.com_VoiceText_2024-5-4_22-56-24.mp3")
                v = bar.barbell_curl()
                x8 = v()[-1]
            elif b == 9:
                pass

        a = input("DO YOU WANT TO CONTINUE \" N FOR EXIT\"")
        x11 += int(x1)
        x22 += int(x2)
        x33 += int(x3)
        x44 += int(x4)
        x55 += int(x5)
        x66 += int(x6)
        x77 += int(x7)
        x88 += int(x8)



except ValueError:
    print("enter only letters yes/no  [ y or n]")

x = (
"RIGHT ARM ", "LEFT ARM", "BICEP CURLS", "LATER RASE", "CHEST ROW ", "SHOULDER PRESS", "OVER HEAD", "BARBELL CURLS")
y = np.array([x11, x22, x33, x44, x55, x66, x77, x88])
plt.pie(y, labels=x)
plt.legend(title="EXERCISE LIST")
plt.show()
