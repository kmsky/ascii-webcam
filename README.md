# ascii-webcam 📸

## Overview 📝

`ascii-webcam` is a Python script designed to capture live video from a webcam and convert each video frame into ASCII art in real-time.

## How it works 🤔

The core concept behind converting an image or video frame to ASCII art involves several steps:

1. **Capture the Frame**: Use OpenCV to capture a frame from the webcam.
2. **Grayscale Conversion**: Convert the captured frame from RGB to grayscale to simplify brightness calculations.
3. **Brightness Calculation**: Determine the brightness level of each pixel.
4. **ASCII Mapping**: Map each pixel’s brightness level to a corresponding ASCII character. 
5. **Display**: Render the ASCII representation of the frame in the console.