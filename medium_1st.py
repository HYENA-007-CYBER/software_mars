import math # importing math library to use squareroot from it

def new_reference_frame(x, y, z, c=55): #as per the question we need to change the frame of reference
    x_final = x
    y_final = y
    z_final = z + c  #as the rover stops we need to change z co-ordinate by +55 
    return x_final,y_final,z_final

def distance_calculate(x1, y1, z1, x2=0, y2=0, z2=0):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
def adjust_rover_navigation(x, y, z):
    # To adjust the rover's movement based on a new reference frame."""
    print(f"Original Marker Position: ({x}, {y}, {z})")
    x_new, y_new, z_new = new_reference_frame(x, y, z)
    print(f"New Reference Frame Position: ({x_new}, {y_new}, {z_new})")
    
    distance_before = distance_calculate(x, y, z)
    distance_after = distance_calculate(x_new, y_new, z_new)
    
    print(f"Distance from origin (before adjustment): {distance_before:.2f} cm")
    print(f"Distance from origin (after adjustment): {distance_after:.2f} cm")
    
    return x_new, y_new, z_new

# getting original marker's position input from camera feed
# here for now getting manual input from user 
x=int(input("ENTER THE X MARKER CO-ORDINATE))
y=int(input("ENTER THE Y MARKER CO-ORDINATE))
z=int(input("ENTER THE Z MARKER CO-ORDINATE))


adjust_rover_navigation(x, y, z)

