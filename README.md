# ascii-webcam
It is very basic way to get ASCII live video captured from a webcam. In the project I used OpenCV library that allows capturing image from a webcam.

## How does it work?
The best explanation how to convert image on ASCII can be found [here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/).

In the nutshell:

Image or video frame are just matrices of RGB values. So we change these values on a gray scale and get level of brightness for every pixel. Next we change brightness value on our own ASCII-scale value. For example white pixel has equivalent as " " and the black is "@". Of course if our background is black we have to reverse the scale.

Lags are caused the gif format

![ascii-webcam](./gif/camera.gif)

### Libraries
* `OpenCV` - to capture the webcam video
* `subprocess` - only to clear console after every frame

### Important
To work properly on Windows I had to enable `Use legacy console` option in CMD properties. For me the best bufor size and window size is `400x120`. Font size 7.

#### Might be helpful

```
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```
`0` means that captured image will come from webcam. `cv2.CAP_DSHOW` will show image with default proportion without black borders.

I used this [documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html) to get info about capturing images with OpenCV.

##### Inspirations
[eebmagic project](https://github.com/eebmagic/video_text_filter)

License
--------
MIT
