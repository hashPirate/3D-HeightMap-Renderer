# Rohan Shanbhag 3D heightmap renderer
# Just some comments up here outlining my initial thought process throwing out all ideas I had in the beginning.
# Terrain renderer with a keyboard controllable camera(I think openGL is going to be the best for this and I have previous experience using it in Java)
# Heightmap image is an NxN grayscale image so we're going to consider darker areas "valleys" and lighter areas "mountains". Calculating pixel intensity (similar to energy from seam carving) would be appropriate to determine heights for each point on map. 
# We want to define SkyColors and make sure our image is well rendered either using dots initially then we can work on creating a wireframe (also previous experience from creating ESP, shaders and chams in video games)
# We want the rendering of the keyboard camera to be smooth so im unsure how to render frames yet. Goal is to get a working prototype first and then work on optimization.
# Every aspect of the camera should be customizeable down to rotation speed and should be able to view the map from all sides
# Should the map be solid?? Unsure yet but if you want to go around and view the objects perhaps some collision logic should exist (unless going under the map is an extra angle to view the 3D render from)
# Unsure of what colors to render the map in. Perhaps black and white or some gradient as the end goal.
# Thinking of using some vbos to improve performance initially (GPU superiority)
# I want the image to be passed in as a command line argument.
# Did some reasearch and found out that glfw can be used for making a window.
# image objects can be used and we can convert the pixels to a numpy array for vertice calculation
import sys
import glfw
import Image
import numpy as np
from PIL import Image


def initializeWindow():
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE,glfw.OPENGL_CORE_PROFILE)
    window = glfw.create_window(800,600,"Terrain Renderer",None,None)
    glfw.make_context_current(window)
    return window

def loadMap(path):
  # Simple function to load the map into a numpy array and hopefully add color
    img=Image.open(path).convert('L')  #Convert to grayscale using ~pillow~
    width,height=img.size
    pixelData = np.array(img)/255.0 # This should give us values between 0 and 1
    print(pixelData)
    vertices,texcoords = [],[] #texture coordinates are just going to be the vertices divided by their position.
    for y in range(height):
        for x in range(width):
            z=pixelData[y,x]
            vertices.extend([x,z,y])
            texcoords.extend([x/width,y/height])
    print(texcoords)
    print(vertices)


 


def processKeyInput():
    print('hi')
    #define functions for processing keyboard input





def main():
    print("Entered main")
    if(len(sys.argv)<2): 
        print("Please enter the image as a command line argument!")
        exit()
    window=initializeWindow()


    
    




if(__name__=='__main__'):
    main()
