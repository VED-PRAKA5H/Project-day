# NumPy Fundamentals & Image Manipulation

This project is a hands-on exploration of **NumPy**, the fundamental package for scientific computing with Python. It covers essential concepts such as array creation, slicing, broadcasting, linear algebra, and image processing by representing images as NumPy arrays.

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Learning Outcomes](#learning-outcomes)  
- [Project Structure](#project-structure)  
- [Acknowledgements](#acknowledgements)  
- [License](#license)

***

## Overview

This project provides a step-by-step introduction to working with **ndarrays**, applying NumPy's capabilities to generate arrays, manipulate multidimensional data, perform mathematical computations including matrix multiplication, and manipulate image data at the pixel level.

It also demonstrates how to convert images to grayscale, flip and rotate images, and invert colors — key image processing techniques using NumPy and Matplotlib.

***

## Features

- Creating arrays manually and programmatically using `np.array()`, `.arange()`, `.random()`, and `.linspace()`.
- Inspecting array shapes and dimensions.
- Array slicing and subsetting using Python indexing.
- Element-wise operations and broadcasting for scalars and arrays.
- Matrix multiplication following linear algebra rules.
- Loading and visualizing images as NumPy arrays.
- Converting RGB images to grayscale using luminance-preserving formulas.
- Visual image manipulations like flipping, rotating, and color inversion.
- Plotting arrays and image data with Matplotlib.

***

## Installation

To run this project locally, ensure you have the following Python packages installed:

```bash
pip install numpy matplotlib scipy pillow
```

***

## Usage

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Open the Jupyter notebook `eda.ipynb` (or equivalent filename) in Jupyter or Google Colab.

3. Follow through each notebook cell, executing code and reading explanations.

4. Experiment by loading your own images (JPEG/PNG with RGB channels) and applying the array manipulations demonstrated.

***

## Learning Outcomes

By working through this project, you will gain practical experience with:

- Core NumPy ndarray manipulation and matrix operations.
- Python indexing and slicing for data subsetting.
- Understanding and leveraging broadcasting rules in NumPy.
- Applying linear algebra in code with NumPy functions.
- Image processing basics using NumPy arrays for pixel-level transformations.
- Visualizing numeric and image data using Matplotlib.

***

## Project Structure

```plaintext
.
├── eda.ipynb                        # Jupyter notebook with all lessons and exercises
├── images/                          # Folder for custom images used in the notebook
│   └── example.jpg
├── README.md                       # This README file
└── requirements.txt                # Optional: project dependencies
```

***

## Acknowledgements

- NumPy and SciPy documentation for foundational scientific computing tools.
- Matplotlib for powerful and flexible visualization capabilities.
- Python image libraries Pillow and SciPy for image handling.
- Inspired by practical projects and tutorials focusing on scientific Python ecosystems.

***

## License

This project is open source and available under the MIT License.
