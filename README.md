# ascii-webcam
Created in Python 3.7. It is very basic way to get ASCII live video captured from webcam. In the project I used OpenCV library allowing to capture webcam image.

## How does it work?
The best explanation how to convert image on ASCII can be found [here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/).

In the nutshell:

Image or video frame are just matrices of RGB values. So we change these values on a gray scale and get level of brightness for every pixel. Next we change brightness value on our own ASCII-scale value. For example white pixel has equivalent as " " and the black is "@". Of course if our background is black we have to reverse the scale.

![](https://p40.f3.n0.cdn.getcloudapp.com/items/5zuJBvy4/Screen+Recording+2019-12-30+at+04.37.37.78+PM.gif?v=d8694659ac6ca55b074319d1aa0d546b)

### Libraries
* `OpenCV` - to capture the webcam video
* `subprocess` - only to clear console after every frame

#### Might be helpful

To work properly on Windows I had to enable `Use legacy console` option in CMD properties.

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