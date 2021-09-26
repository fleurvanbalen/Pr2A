# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage.interpolation import shift
import RUStack5

def animate(i):
    ''' This event handler is called by animation events. The array of y-values of the existing line object is shifted one
     position to the  left and the new datapoint read from the M5Stack is added on the right, resulting in a scrolling
      graph.'''
    old_y_values=lines[0].get_ydata() # retrieve the y values from the current line object in the graph
    value_to_plot = acc.accX # take a measurement from the M5Stack
    new_y_values = shift(old_y_values,-1,cval=value_to_plot) # shift the existing y-value-array one position to the left, add                             the new datapoint on the right
    lines[0].set_ydata(new_y_values) # put the updated values back into the y-values array of the first line object
    return lines # return the new line collection so the animate function can redraw them


def closeall():
    ''' This function takes care of ending the script safely.'''
    ani.event_source.stop() # stop generation of animation events
    plt.close() # close the matplotlib plot
    display.turn_on() # turn the display of the M5Stack back on
    mystack.disconnect() # disconnect from the M5Stack and free up the serial port

def on_keypress(event):
    ''' This event handler handles keypress events '''
    closeall() # perform a safe shutdown

def on_close(event):
    ''' This event handler is called when the matplotlib figure is closed '''
    closeall() # perform a safe shutdown

def init():
    '''The first time an animation event is generated this function is called instead of animate(). It fills the graph
    with a line of 100 zeroes'''
    lines[0].set_data(np.linspace(0, 100, num=100), np.linspace(0, 0, num=100)) # fill the graph with 100 equally spaced points with a y-value of 0
    return lines # return the collection of line objects

# --- Entry point of the main program ---

# Make the intial plot:
plt.plot([],[]) # create an empty plot
plt.show() # show it
fig = plt.gcf() # extract several objects from this plot
ax = plt.gca()
lines = ax.get_lines()
ax.set_xlim(left=0, right=100) # set the x-axis limits
ax.set_ylim(bottom=-2, top=2) # set the y-axis limits

# Set up the M5Stack:
mystack=RUStack5.Devices.M5Stack() # create an M5Stack object "mystack"
acc=RUStack5.Internals.IMU(mystack) # create the object representing the IMU with "mystack" as the host device
display=RUStack5.Internals.Display(mystack) # create the object representing the display
mystack.autoconnect() # establish connection with the M5Stack
display.turn_off() # turn off the display of the M5Stack to prevent sampling jitter due to display update events

# Bind events:
fig.canvas.mpl_connect('key_press_event', on_keypress) # link both shutdown handlers
fig.canvas.mpl_connect('close_event', on_close)

# Start animation:
ani = animation.FuncAnimation(fig, animate, interval=20, init_func=init, blit=True) # start generating animation events
