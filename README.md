# Image to Video Converter
This is a Python script that converts a folder of images into an MP4 video file using the OpenCV library. 
The script takes the full path to the image directory and the desired video name as inputs, and outputs the saved video file location.

## Installation
Before running the script, you need to have OpenCV and gradio libraries installed. You can install them using the following commands:

```
pip install opencv-python
pip install gradio
```

## Dependencies
This script requires the following dependencies to be installed:

1.`Python 3`
2.`OpenCV`
3.`Gradio`


## Usage

1. Clone the repository: `git clone https://github.com/your_username/image-to-video-converter.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Place the images you want to convert into a folder named `images`.
4. Run the script: `python image_to_video.py`
5. Enter the full path to the `images` directory and the desired name for the output video when prompted.

## Options

You can customize the frame rate and video resolution by modifying the values of the `FPS` and `RESOLUTION` constants at the beginning of the script.


