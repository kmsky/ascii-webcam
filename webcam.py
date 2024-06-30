import cv2

# need to be adjusted to your screen and terminal size
WIDTH = 80
HEIGHT = 60
ASCII_SCALE = ['@', '%', '#', '*', '+', '=', '-', ':', ' ', ' ']


def pixel_to_ascii(pixel_color):
    """
    Converts pixel color to ascii character.
    Index is calculated depending on the pixel color. Darker colors -> denser characters.
    We multiply by 2 because the aspect ratio of characters is not 1:1.
    """
    index = (int(pixel_color / 25.5)) - 1
    return ASCII_SCALE[index] * 2


def cmd_print(image):
    """
    Prints the image to the command line.
    Written as list comprehension for performance.
    """

    single_frame = "\n".join(["".join([pixel_to_ascii(image[h][w]) for w in range(WIDTH)]) for h in range(HEIGHT)])
    print(single_frame)


def webcam_capture():
    capture = cv2.VideoCapture(0)

    while True:
        returned, frame = capture.read()

        if not returned:
            raise ValueError("Can't read frame from webcam")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (WIDTH, HEIGHT))
        cmd_print(resized)

        # webcam capture
        cv2.imshow('ascii-webcam', gray)

        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    webcam_capture()
