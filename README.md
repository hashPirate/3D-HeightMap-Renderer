# 3D-HeightMap-Renderer
Given a grayscale heightmap image rendering it in 3D with a keyboard controllable camera

# Overview
The 3D Heightmap Renderer is a Python-based application that visualizes grayscale heightmap images as interactive 3D terrains using OpenGL. Users can navigate the terrain with a keyboard-controllable camera, switch between rendering modes, and customize various aspects of the view to explore landscapes from all angles.

# Features
- Heightmap Visualization: Converts NxN grayscale images into detailed 3D terrains, where pixel intensity determines elevation.
- Interactive Camera: Smooth and customizable camera controls allow users to move, rotate, and explore the terrain seamlessly.
- Rendering Modes: Toggle between wireframe and point-based rendering to view the terrain structure or individual vertices.
- Performance Optimizations: Utilizes Vertex Buffer Objects (VBOs) and Vertex Array Objects (VAOs) for efficient rendering leveraging GPU capabilities.

# Installation
- Install the required Python packages using pip: pip install glfw PyOpenGL numpy Pillow PyGLM
- Clone the Repository
- git clone https://github.com/yourusername/3d-heightmap-renderer.git
- cd 3d-heightmap-renderer
# Usage
- Run the renderer by providing the path to a grayscale heightmap image as a command-line argument:

- python heightmaprenderer.py imagepath
- testImage is provided for testing.
- Ensure that the heightmap image is a square (NxN) grayscale image. Darker pixels represent valleys, while lighter pixels represent mountains.

# Controls

Movement:
- W: Pitch camera upwards.
- S: Pitch camera downwards.
- A: Yaw camera to the left.
- D: Yaw camera to the right.
- Up Arrow: Move camera forward.
- Down Arrow: Move camera backward.
- Space: Move camera upwards.
- Left Shift: Move camera downwards.
Camera Speed:
- O: Decrease camera movement speed.
- P: Increase camera movement speed.
Rendering Mode:
- X: Toggle between wireframe and point rendering modes.

# Example

Sample visualization of a 3D terrain generated from a grayscale heightmap.
