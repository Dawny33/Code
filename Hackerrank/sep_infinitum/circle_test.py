def dis(x,y,x_center,y_center,radius):
    return (((x - x_center)^2 + (y - y_center)^2) <= radius)

print dis(10,0,0,0,10)
