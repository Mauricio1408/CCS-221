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

  st.header("Task 1")
  st.subheader("Midpoint line")
  st.pyplot(task_one.MIDPOINT(x1,y1,x2,y2))
  
  st.subheader("Bresenham line")
  st.pyplot(task_one.BRESENHAMS_LINE(x1,y1,x2,y2, 'ro'))
  
  st.subheader("DDA line")
  st.pyplot(task_one.DDALine(x1,y1,x2,y2, 'r'))
            
  if st.button("Exit"):
            st.stop()
           
if  __name__ == "__main__":
    main()
