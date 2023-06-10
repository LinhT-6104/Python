x,y,z = [float(input()) for x in ['x','y','z']]

# Tinh f(X,y)
f = x**2 + x*y + y**2 - 2*x -y
print("{:.2f}".format(round(f,2)))

# Tinh f(x,y,z)
try:
    f = x*y*z + x / (y**z)
    print("{:.2f}".format(round(f,2)))
except ZeroDivisionError:
    print("N/A")