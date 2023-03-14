#4 pixel implementation
#bounary fill
def change_boundary_fill(x_val, y_val, c, boarder, two_d_arr):
  fig = plt.figure()

  if two_d_arr[x_val][y_val] != boarder and two_d_arr[x_val][y_val] != c:
       
    two_d_arr[x_val][y_val] = c
        
    change_boundary_fill(x_val + 1, y_val, c, boarder, two_d_arr)
    change_boundary_fill(x_val - 1, y_val, c, boarder, two_d_arr)
    change_boundary_fill(x_val, y_val + 1, c, boarder, two_d_arr)
    change_boundary_fill(x_val, y_val - 1, c, boarder, two_d_arr)
   
  return fig
    
    
def boundary_fill(x_val, y_val, c, boarder):
  fig = plt.figure()
  
  two_d_arr = np.array([[1,1,1,1,1], 
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,1,1,1,1]])
 
  change_boundary_fill(x_val, y_val, c, boarder, two_d_arr)

  fig = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'BrBG')
  fig.set_clim([0,50])    
  plt.colorbar()
  return fig


#flood_fill_algorithm
def change_flood_fill(x_val, y_val, c, old_color, two_d_arr):
        fig = plt.figure()
        x = len(two_d_arr)
        y = len(two_d_arr[0])

        if x_val < 0 or x_val >= x or y_val < 0 or y_val >= y or two_d_arr[x_val][y_val] != old_color:
                return fig
        
        else:
                two_d_arr[x_val][y_val] = c
                change_flood_fill(x_val + 1, y_val, c, old_color, two_d_arr)
                change_flood_fill(x_val - 1, y_val, c, old_color, two_d_arr)
                change_flood_fill(x_val, y_val - 1, c, old_color, two_d_arr)
                change_flood_fill(x_val, y_val + 1, c, old_color, two_d_arr)
                
        return fig
      
      
def flood_fill(x_val, y_val, c, old_c):
    fig = plt.figure()
    two_d_arr = np.array([[1,0,1], 
                      [1,1,1],
                      [1,0,1]]) 
    
    if old_c == c:
        return fig
    change_flood_fill (x_val, y_val, c, old_c, two_d_arr)
    fig = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'BrBG')
    fig.set_clim([0,50])    
    plt.colorbar()
    
    return fig

        
