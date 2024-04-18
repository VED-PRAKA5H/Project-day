# The Hirst Painting Project

A Python project that generates art inspired by Damien Hirst's iconic spot paintings using the turtle graphics library. This project extracts vibrant colors from an image and uses them to draw colorful spots in a grid pattern.

***

## Features
- Extracts intense colors from an image using the `colorgram.py` library.  
- Draws 100 colored dots in a grid layout mimicking Damien Hirst’s spot paintings.  
- Uses Python’s `turtle` module for graphical rendering.  
- Easy to customize with different source images and color counts.  

***

## Installation & Setup

1. Clone the repository

2. Install the required Python package:  
   ```bash
   pip install colorgram.py
   ```

3. Place your source image (e.g., `image.jpg`) in the project directory.

4. Run the main script to generate the painting:  
   ```bash
   python main.py
   ```

***

## How It Works

- The project uses `colorgram.extract()` to pull 30 prominent colors from the specified image.  
- The turtle starts at a predefined position on the screen and draws dots of size 20 using the extracted colors’ RGB values.  
- It moves horizontally across the screen and shifts rows down in a zigzag pattern to fill the grid with dots.  
- The `turtle.colormode(255)` sets the color system to RGB mode for accurate coloring.  

***


## Resources and References

- Python Turtle Graphics Documentation  
- [Colorgram.py Library](https://github.com/obskyr/colorgram.py)  
- Colors RGB and RGBA reference from [W3Schools](https://www.w3schools.com/colors/colors_rgb.asp)  
- Inspirations from Damien Hirst’s [Spot Paintings](https://en.wikipedia.org/wiki/Damien_Hirst#Spot_paintings)  
