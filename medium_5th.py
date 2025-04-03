import math
def euler_to_quaternion(roll_deg, pitch_deg, yaw_deg):
    # Convert degrees to radians
    roll = math.radians(roll_deg)
    pitch = math.radians(pitch_deg)
    yaw = math.radians(yaw_deg)
    # TO COMPUTE HALF ANGLE TRIG TERMS
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    # FORMULA TO CALCULATE QUATERNION COMPONENTS
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    w = cr * cp * cy + sr * sp * sy
    return (x, y, z, w)
# FOR NOW GETTING INPUT FROM USER
print("Enter Euler angles in degrees:")
roll_deg = float(input("Roll (X-axis rotation): "))
pitch_deg = float(input("Pitch (Y-axis rotation): "))
yaw_deg = float(input("Yaw (Z-axis rotation): "))
#PASSING INTO FUNCTION TO CONVERT TO QUATERNION
quaternion = euler_to_quaternion(roll_deg, pitch_deg, yaw_deg)
print(f"Martian Quaternion (x, y, z, w): {quaternion}")
