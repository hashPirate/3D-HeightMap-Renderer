# 3D-HeightMap-Renderer
Given a grayscale heightmap image rendering it in 3D with a keyboard controllable camera and toggleable wireframe.

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
- git clone https://github.com/hashPirate/3d-heightmap-renderer.git

# Usage
- cd 3d-heightmap-renderer
- Run the renderer by providing the path to a grayscale heightmap image as a command-line argument:
- python heightmaprenderer.py <imagepath>
- 3 test images are provided for testing named testimage.png,test_crater_image.png(a depth map), and highrestest.jpg which is a higher resolution image.
- Ensure that the heightmap image is a square (NxN) grayscale image for the best results! Darker pixels represent valleys, while lighter pixels represent mountains.

# Controls


- W: Pitch camera upwards.
- S: Pitch camera downwards.
- A: Yaw camera to the left.
- D: Yaw camera to the right.
- Up Arrow: Move camera forward.
- Down Arrow: Move camera backward.
- Space: Move camera upwards.
- Left Shift: Move camera downwards.
- O: Decrease camera movement speed.
- P: Increase camera movement speed.
- X: Toggle between wireframe and point rendering modes.

# Example of mountains and valleys

- Sample visualization of a 3D terrain generated from a grayscale heightmap with the example input.
![testimage](https://github.com/user-attachments/assets/e2c719f3-7dbd-4d14-bd2f-2008b3c2a410)

- Below is the mesh generation of this input image.
<img width="880" alt="Screenshot 2024-10-27 215215" src="https://github.com/user-attachments/assets/4f9bc86d-9349-4da2-819e-dd4f41850f2a">

# Example of a crater
- Another visualization of 3D generated terrain from a grayscale depthmap
![test_crater_image](https://github.com/user-attachments/assets/b94d08cc-c483-4449-adf4-01828121d97f)

- Mesh generation of the image above with depth
<img width="928" alt="Screenshot 2024-10-27 222230" src="https://github.com/user-attachments/assets/4897c7d2-6077-44bc-8c18-e4cb98424e05">

# Performance report with scale

- On my laptop running an NVIDIA 3070 Laptop GPU and an AMD Ryzen 5950x the performance report for tested image resolutions is below
<img width="476" alt="log" src="https://github.com/user-attachments/assets/23850508-08ed-4c33-bd05-424875ad5315">

- All 4 images are the same with just the resolutions changed and an automated camera script and logging was used to simulate the same movement every time.
- As observed the setup time increases by a factor of 4 every time which aligns with the actual change in pixels introduced between the tests.
- The average FPS for the wireframe tests remained the same until the 1024x1024 image, where the render distance of 1000 was fully used and had an 8% imapact on the fps.
- The average FPS for the dot tests consistently reduced by around 90 every time we increased the image size by a factor of 4.

# GPU observations

- The GPU memory consumption is manageable for the lower resolutions but once we cross 1024x1024 we have to store over a million vertices
- Implementing frustum culling and LOD management should have a significant change on the FPS received.
- Despite the increased image size, the rendering remains efficient because of the VBO's and EBO's.
- As the heightmap size increases for larger images such as 2048x2048 memory consumption can approach the limits of lower end GPUs and cause slowdowns.







