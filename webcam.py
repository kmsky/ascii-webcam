import cv2
import os

width = 80
height = 60
ascii_scale = ['@', '%', '#', '*', '+', '=', '-', ':', ' ', ' ']

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def pixel_to_ascii(pixel_color):
    index = (int(pixel_color / 25.5)) - 1
    return ascii_scale[index]


def cmd_print(image):
    os.system("cls")

    for h in range(height):
        for w in range(width):
            sign = pixel_to_ascii(image[h][w])
            print(sign * 3, sep="", end="")

        print("\n")


while True:
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
