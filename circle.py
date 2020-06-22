#program that reads the radius value of a circle and informs:
# 1 - The value of your diameter
# 2 - The value of your perimeter
# 3 - The value of your area
radius = input("Enter circle radius value: ")
radius = float (radius)
pi = 3.14
diameter = 2*radius
perimeter = 2*pi*radius
area = pi*(radius**2)

print ("Diameter value: ", diameter)
print ("Perimeter value: ", perimeter)
print ("Area value: ", area)

print ("Have a nice day!")