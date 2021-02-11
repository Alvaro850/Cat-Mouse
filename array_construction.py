import numpy as np
def coord_array(n,PI_x,PI_y,PF_x,PF_y):
    dx = (PF_x-PI_x)/(n-1)   
    dy = (PF_y-PI_y)/(n-1)
    coord = np.ndarray((n,n),dtype=tuple)
    x = 0

    while x < n:
        y = 0
        while y < n:
            coord[y,x] = (PI_x+(dx*x),PI_y+(dy*y))  
            y += 1
        x += 1  
    return coord
    
 