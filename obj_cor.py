import math

def deg_to_rad(angle):
	return angle * math.pi / 180
	
def rotate_point(x, y, z, x_angle, y_angle, z_angle):

	#converting the angle units
	x_rad = deg_to_rad(x_angle)
	y_rad = deg_to_rad(y_angle)
	z_rad = deg_to_rad(z_angle)
	
	# Rotation about X-axis
	y1 = y * math.cos(x_rad) - z * math.sin(x_rad)
	z1 = y * math.sin(x_rad) + z * math.cos(x_rad)
	x1 = x

	# Rotation about Y-axis
	x2 = x1 * math.cos(y_rad) + z1 * math.sin(y_rad)
	z2 = -x1 * math.sin(y_rad) + z1 * math.cos(y_rad)
	y2 = y1

	# Rotation about Z-axis
	x3 = x2 * math.cos(z_rad) - y2 * math.sin(z_rad)
	y3 = x2 * math.sin(z_rad) + y2 * math.cos(z_rad)
	z3 = z2
    	
	return x3, y3, z3
    	
def obj_cor(obj_camfr, rover_pos, angles):
	x_cam, y_cam, z_cam = obj_camfr
	x_rover, y_rover, z_rover = rover_pos
	x_angle, y_angle, z_angle = angles

	# Rotating point
	x_rot, y_rot, z_rot = rotate_point(x_cam, y_cam, z_cam, x_angle, y_angle, z_angle)

	# Translating (add rover position)
	x_world = x_rot + x_rover
	y_world = y_rot + y_rover
	z_world = z_rot + z_rover

	return x_world, y_world, z_world

# Given Input
obj_cam = (2, 1, 3)
rover_pos = (10, 5, 0)
angles = (0, 0, 45)

result = obj_cor(obj_cam, rover_pos, angles)

print("Object position in world frame:", result)
    	
