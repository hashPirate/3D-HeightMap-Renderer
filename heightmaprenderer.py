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
import numpy as np
from PIL import Image
import glm
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.arrays import vbo
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texCoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 TexCoords;

void main()
{
    gl_Position = projection * view * model * vec4(position, 1.0);
    TexCoords = texCoords;
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec2 TexCoords;
out vec4 color;

void main()
{
    color = vec4(TexCoords, 0.5, 1.0);  // Simple coloring based on texture coordinates
}
"""



def initializeWindow():
    if(glfw.init()==False): return None # forgot to add this in the first github commit
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
    vertices = np.array(vertices,dtype=np.float32)
    texcoords = np.array(texcoords,dtype=np.float32)
    combined = np.empty((width*height,5),dtype=np.float32) # setting up empty numpy array with 5 cols to combine the data into 1 array!!
    combined[:,0:3] = vertices.reshape(-1,3) # adds the vertices to the first 3 columns of the matrice
    combined[:,3:5] = texcoords.reshape(-1,2) # adds texture data to the next 2 cols of the matrix.
    print(combined)
    return combined,width,height


 

def vaoSetup(vertices):
     # This took a LONG time to implement and understand what arguments were needed
     # These comments are all explanations of the functions copied from documentation/gpt so that I could understand what arguments were required
     # the goal was to implement vbos and vaos in order to configure the scene
    vao=glGenVertexArrays(1) 
    vbo=glGenBuffers(1)      
    glBindVertexArray(vao)  
    glBindBuffer(GL_ARRAY_BUFFER, vbo) # Bind the VBO to the GL_ARRAY_BUFFER target (for vertex attributes)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)  # this one line took forever
    # - GL_ARRAY_BUFFER specifies this buffer will store vertex attributes.
    # - vertices.nbytes is the size of the data in bytes.(I did not realize that this was required.)
    # - vertices contains the actual vertex data.
    # - GL_STATIC_DRAW hints that the data will not change frequently.
    glEnableVertexAttribArray(0)  # Enable the position attribute at location 0
    glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,5*vertices.itemsize,ctypes.c_void_p(3*vertices.itemsize))
    # - ctypes.c_void_p(3 * vertices.itemsize) specifies the offset within each vertex where the texture data starts (after 3 floats for x, y, z).
    glEnableVertexAttribArray(1)  
    glBindBuffer(GL_ARRAY_BUFFER, 0)  
    glBindVertexArray(0)              
    return vao    

def setupShaders(): # GRADIENT WISE SHADERS!
    shader = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    return shader

def processKeyInput(window, cameraPos, cameraFront, cameraUp):
    print('hi')
    #define functions for processing keyboard input
    cameraSpeed = 0.1
    if glfw.get_key(window, glfw.KEY_W)==glfw.PRESS:
        cameraPos+=cameraSpeed*cameraFront
    if glfw.get_key(window, glfw.KEY_S)==glfw.PRESS:
        cameraPos-=cameraSpeed*cameraFront
    if glfw.get_key(window,glfw.KEY_A)==glfw.PRESS:
        cameraPos-= glm.normalize(glm.cross(cameraFront,cameraUp))*cameraSpeed # Normalize gets the unit vector, cross gets the perpendiculr to the up and front regions enabling us to go down and right 
    if glfw.get_key(window,glfw.KEY_D)==glfw.PRESS:
        cameraPos+=glm.normalize(glm.cross(cameraFront,cameraUp))*cameraSpeed





def main():
    print("Entered main")
    if(len(sys.argv)<2): 
        print("Please enter the image as a command line argument!")
        exit()
    window=initializeWindow()
    heightmapImage = sys.argv[1]
    vertices, width, height = loadMap(heightmapImage)
    cameraPosition  = glm.vec3(width/2,40,height+20) # glm can be used for 3d vectors in python and is very fast. We set the initial camera position to half the width and on top of the base of the image. This is a placeholder for later.
    cameraPosition = glm.vec3(0.0, 1.0, 3.0)
    cameraFront = glm.vec3(0.0, 0.0, -1.0)
    cameraUp = glm.vec3(0.0, 1.0, 0.0)
    shader = setupShaders() # WE ADDED SHADERS
    vao = vaoSetup(vertices)
    glEnable(GL_DEPTH_TEST) # Close to LOD
    # Infinite main rendering loop down below ->>

    while(glfw.window_should_close(window)==False): 
        glfw.poll_events() # We can get keyboard input this way
        processKeyInput(window,cameraPosition,cameraFront,cameraUp)
        glViewport(0, 0, 800, 600) # size of the window
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear area and set colors as well for the 3dwindow
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glDrawArrays(GL_POINTS,0,len(vertices)//3)
        # not working yet still have to implement vbos
        view=glm.lookAt(cameraPosition,cameraPosition+cameraFront,   cameraUp) # lookat and perspective should move the camera but theres still nothing rendering
        projection=glm.perspective(glm.radians(45.0),800/600,0.1,100) # will have to implement some shaders to actually use the view and projection. Perspective from a 45 degree angle for a 800*600 image.
        glGetUniformLocation(shader, "model")
        viewLocation=glGetUniformLocation(shader,"view")
        projectionLocation=glGetUniformLocation(shader,"projection")

        glUniformMatrix4fv(viewLocation,1,GL_FALSE,glm.value_ptr(view))
        glUniformMatrix4fv(projectionLocation,1,GL_FALSE,glm.value_ptr(projection)) # USING LOCATIONS FOR PROJECTION TO ACTUALLY RENDER
        print(view)
        print(projection)
        glfw.swap_buffers(window)
    glfw.terminate() #removing 
    

    # needs work... isnt showing anything and i cant figure out why



if(__name__=='__main__'):
    main()
