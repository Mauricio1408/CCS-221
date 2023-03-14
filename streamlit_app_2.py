import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import cv2

import pages.tasks as task_one
import pages.tasks2 as task_two

def main():
  
  st.title('Midterms in CC201')
  st.sidebar.subheader("Activity 1")
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
  
  #activity 2
  st.header("Task 2")
  st.sidebar.subheader("Activity 2")
  
  st.subheader("Boundary Fill")
  st.pyplot(task_two.boundary_fill(task_2_x,tas_2_y,color_,boundary_color))
  
  st.subheader("Flood Fill")
  st.pyplot(task_two.flood_fill(task_2_x,tas_2_y,color_,boundary_color))
            
  if st.button("Exit"):
            st.stop()
           
if  __name__ == "__main__":
    main()
    
