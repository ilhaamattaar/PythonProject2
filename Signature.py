import cv2
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas


image= cv2.imread("../signature.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)

_,thresh_signature= cv2.threshold(image,127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresh_signature", thresh_signature)
cv2.imwrite("../signature_output.png", thresh_signature)
colorImg= cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
bgra= cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
bgra[:, :,3]= thresh_signature
cv2.imshow("bgra", bgra)
cv2.imwrite("../bgra_output.png", bgra)


st.title("Change Color")
pen_color = st.color_picker("Pen color", "#000000")
canvas_result = st_canvas(
    fill_color="rgba(0, 0, 0, 0)",
    stroke_width=3,
    stroke_color=pen_color,
    background_color="#FFFFFF",
    height=300,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)
cv2.waitKey(0)
cv2.destroyAllWindows()

