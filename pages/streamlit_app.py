import streamlit as st
import matplotlib.pyplot as plt
import sys
import pages.tasks as task_one

st.title('Midterms in CC201')

x1 = st.sidebar.slider('x1')
y1 = st.sidebar.slider('y1')
x2 = st.sidebar.slider('x2')
y2 = st.sidebar.slider('y2')

st.header("Task 1")
st.subheader("Midpoint line")
st.pyplot(task_one.MIDPOINT(x1,y1,x2,y2)








