"""
This program adds a background color over the previously created empty context.

Notice that in the last tutorial, we did not make use of OpenGL. Hence, our
context (supported by a window) was empty and black.

Let us add some color and introduce the concept of SWAP BUFFERS!
"""

import glfw
import OpenGL.GL as gl

def main():

    # Start by initializing GLFW
    glfw.init()

    # Before creating the context, we need to configure it. That means decalring
    # which OpenGL version are we using, if we want the classic or the modern
    # pipeline.

    # We will be using OpenGL 3.3 version
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)

    # Do not allow the deprecated model (i.e. classic OpenGL). If you want to 
    # enable the classic interface use the "glfw.OPENGL_COMPAT_PROFILE" variable
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # For the moment let us block user for having a full screen context. I
    # decided to use the "False" boolean variable here but you can also use the
    # boolean "glfw.FALSE" one
    glfw.window_hint(glfw.RESIZABLE, False)

    # Now, let us create the window which will be used as the basis for the
    # context.  The resolution is VGA (i.e. 640x480). The last parameters are
    # used for specifying in which monitor is expected to be displayed the
    # window and if it a shared one. For the moment, let us do not specify
    # those. Your main monitor will be used as the default one.
    main_window = glfw.create_window(640, 480, "The title of the window", None, None)

    # We impose previous window to be the one for the context
    glfw.make_context_current(main_window)

    # Before starting the main loop of the application, we need to specify the
    # background color. Since we are adding color to the context, we have to use
    # OpenGL. Colors are specified using the RGBA, where A means "alpha" (i.e.
    # the transparency of the color being 1 solid and 0 fully transparent). A
    # dark gray color is applied in this case.
    gl.glClearColor(0.3, 0.3, 0.3, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Let us introduce now the concept of SWAP BUFFERS. Because data coming from
    # the CPU/GPU is faster than the one being displayed by the screen, a buffer
    # is required. Buffers are memory assets holding data which needs to be
    # processed. Its main purpose is to ensure a constant stream of data so the
    # drawing program does not hang. OpenGL creates two buffers, the front and
    # the back one. While one of these buffers is being displayed, the other one
    # is being painted. Once it is done, they swap and the process starts again.
    # But we need to specify this behavior to the context manager.
    glfw.swap_buffers(main_window)

    # Once the context has been created, it is time to start the main loop of
    # the application. We want our context to be displayed until the user closes
    # it.
    while not glfw.window_should_close(main_window):
        # The following function allows to collect all the events that were
        # generated while the application was running. If the "CLOSE" event is
        # read, the application will stop as the main condition of the loop is
        # no longer valid.
        glfw.poll_events()

    # Once the application has finished, we destroy the window and terminate the
    # execution of GLFW
    glfw.destroy_window(main_window)
    glfw.terminate()


if __name__ == "__main__":
    main()
