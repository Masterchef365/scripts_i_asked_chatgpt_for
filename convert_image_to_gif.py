#!/usr/bin/env python3
"""
convert_image_to_gif.py
Author: OpenAI's ChatGPT
Editor and error detective: Duncan F.

Converts an image consisting of 64x64 frames side by side into the equivalent animation as a gif.

Usage:
    python convert_image_to_gif.py <input_image_path> <output_gif_path>
"""

import sys
from PIL import Image
import imageio

def convert_to_gif(input_image_path, output_gif_path):
    try:
        # Open the input image
        img = Image.open(input_image_path)

        # Get the size of the input image
        img_width, img_height = img.size

        # Set frame size to equal height (assumes frames are going left to right)
        frame_size = img_height

        # Calculate the number of frames in the image
        num_frames = img_width // frame_size

        # Create a list to store individual frames
        frames = []

        # Extract frames from the input image
        for i in range(num_frames):
            left = i * frame_size
            right = (i + 1) * frame_size
            frame = img.crop((left, 0, right, img_height))
            frames.append(frame)

        # Create a GIF using imageio
        imageio.mimsave(output_gif_path, frames, duration=0.1, loop=True)

        print(f"GIF created successfully: {output_gif_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(__doc__)
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_gif_path = sys.argv[2]

    convert_to_gif(input_image_path, output_gif_path)

