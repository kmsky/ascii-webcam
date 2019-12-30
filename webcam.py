import cv2
import os

width = 100
height = 75
ascii_scale = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def ascii_convert(frame):
    asciiTab = []
    for i in range(width):
        index = (int(frame[i]/25.5))-1
        asciiTab.append(ascii_scale[index])
    return asciiTab


def cmd_print(gray):
    # clear console every frame
    os.system("cls")

    for h in range(height):
        print("\n")
        row = ascii_convert(gray[h])
        for w in range(width):
            print(row[w]*3, sep="", end="")

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (width, height))
    cmd_print(resized)

    # webcam capture
    cv2.imshow('ascii-webcam', gray)

    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()