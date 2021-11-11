"""
The following program creates an empty context by using the GLFW library.

A context is like a canvas. OpenGL can be understood as an artist
toolbox containing a variety of pencils, brushes and colors. However, those are
useless unless you provide them a canvas or context to be used in.

Notice that OpenGL has no idea about creating windows or managing users inputs
such us mouse, keyboard or joystick. Hence, an external library is used being in
this case Graphics Library FrameWork (GLFW). Other available libraries are GLUT
(better use FreeGLUT nowadays).

The GLFW library is well maintained and offers a fresh modern approach.

"""

import glfw

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

    # Once the context has been created, it is time to start the main loop of
    # the application. We want our context to be displayed until the user closes
    # it
    while not glfw.window_should_close(main_window):
        # The following function allows to collect all the events that were
        # generated while the application was running. If the "CLOSE" event is
        # read, the application will stop as the main condition of the loop is
        # no longer valid
        glfw.poll_events()

    # Once the application has finished, we destroy the window and terminate the
    # execution of GLFW
    glfw.destroy_window(main_window)
    glfw.terminate()


if __name__ == "__main__":
    main()
