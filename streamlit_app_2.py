import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.tasks as task_one

def main():
  st.title('Midterms in CC201')

  x1, y1, x2, y2 = st.sidebar.slider('x1', 1, 10), \
                st.sidebar.slider('y1', 1, 10), \
                st.sidebar.slider('x2', 1, 10), \
                st.sidebar.slider('y2', 1, 10)

  
  task_2_x, tas_2_y, color_, boundary_color = st.sidebar.slider('X: (0-4)', 0, 4), \
                 st.sidebar.slider('Y: (0-8)', 0, 8),\
                 st.sidebar.slider('Color value: (1-50)', 1, 50),\
                 st.sidebar.slider('Boundary Color: ', 1, 50)
  
  st.header("Task 1")
  
  st.subheader("DDAline")
  st.pyplot(task_one.DDALine(x1,y1,x2,y2,'ro'))
  
  st.subheader("Midpoint line")
  st.pyplot(task_one.MIDPOINT(x1,y1,x2,y2))
  
  st.subheader("Bresenham line")
  st.pyplot(task_one.BRESENHAMS_LINE(x1,y1,x2,y2, 'ro'))
  
  st.subheader("Boundary Fill")
  st.pyplot(BOUNDARY_FILL(task_2_x,tas_2_y,color_,boundary_color))
            
  if st.button("Exit"):
            st.stop()
           
if  __name__ == "__main__":
    main()
    
    
    
    
    
  #4 pixel implementation
def change_boarder_fill(x_val, y_val, c, boarder, two_d_arr):
    
    fig = plt.figure()

    if two_d_arr[x_val][y_val] != boarder and two_d_arr[x_val][y_val] != c:
        
        two_d_arr[x_val][y_val] = c
        
        change_boarder_fill(x_val + 1, y_val, c, boarder, two_d_arr)
        change_boarder_fill(x_val - 1, y_val, c, boarder, two_d_arr)
        change_boarder_fill(x_val, y_val + 1, c, boarder, two_d_arr)
        change_boarder_fill(x_val, y_val - 1, c, boarder, two_d_arr)
    
    return fig

def BOUNDARY_FILL(x_val, y_val, c, boarder):
    two_d_arr = np.array([[1,1,1,1,1], 
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,4,0,3,1],
                      [1,7,5,9,1],
                      [1,1,1,1,1]])
    
    change_boarder_fill(x_val, y_val, c, boarder, two_d_arr)

    img = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'BrBG')
    img.set_clim([0,50])    
    plt.colorbar()
    
    return img
