import gradio as gr
import cv2
import os


def fadeIn(img1, img2, duration=60):
    for i in range(duration):
        alpha = i / duration
        blended = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        yield blended


def convert_images_to_video(image_directory, video_name):
    images = [img for img in os.listdir(image_directory) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_directory, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video_name = video_name + ".mp4"  # Add ".mp4" extension to filename
    video = cv2.VideoWriter(output_video_name, fourcc, 60, (width, height))

    for i in range(len(images) - 1):
        img1 = cv2.imread(os.path.join(image_directory, images[i]))
        img2 = cv2.imread(os.path.join(image_directory, images[i + 1]))
        for blended in fadeIn(img1, img2, duration=60):
            video.write(blended)
        for j in range(120):  # Display each image for 5 seconds (60 * 3 = 180 frames, minus 60 for the fade transition)
            video.write(img2)

    # Write last frame for 5 seconds
    for j in range(180):
        video.write(cv2.imread(os.path.join(image_directory, images[-1])))

    cv2.destroyAllWindows()
    video.release()
    return f"Video {output_video_name} has been saved!"


def image_to_video(image_directory, video_name):
    return convert_images_to_video(image_directory, video_name)


input_image = gr.inputs.Textbox(label="Enter full path to image directory")
input_video_name = gr.inputs.Textbox(label="Enter video name")
output_video = gr.outputs.Textbox()

interface = gr.Interface(
    fn=image_to_video,
    inputs=[input_image, input_video_name],
    outputs=output_video,
    title="Image to Video",
    description="Convert a folder of images to an MP4 video file with fade transition using OpenCV",
)

interface.launch()
