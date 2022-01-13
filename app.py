import streamlit as st
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

OCR_model = load_model('model/model.h5')

st.set_page_config(layout="wide")

page_style = """
    <style>
        .block-container{
            padding-top: 10px;
            padding-bottom: 10px;
            width: 80vw !important;
        }
    </style>
"""

st.markdown(page_style, unsafe_allow_html=True)

labels_dict = {0:"A", 1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",
               11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S", 19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

st.title('Character Recognition')

col1, col2 = st.columns(2)

with col1.container():
    inst_text = f'<p style="font-size: 15px;">Draw a character from A-Z in the box below</p>'
    st.markdown(inst_text, unsafe_allow_html=True)
    data = st_canvas(
        height=300,
        width=300
    )

    button = st.button('Run')

if data.image_data is not None:
    image_data = data.image_data[:,:,3]

    img = Image.fromarray(image_data)
    img = img.resize(size=(28, 28))
    img_arr = np.array(img)
    img_arr = img_arr/255

if button:
    img_arr_reshaped = np.reshape(img_arr, (1,28,28))
    predictions = OCR_model.predict(img_arr_reshaped)
    pred_sorted = np.argsort(predictions[0])[::-1]
    letter = labels_dict[pred_sorted[0]]

    with col2.container():
        pred_text = f'<p style="font-size: 150px; text-align:center;">{letter}</p>'
        subtext = f'<p style="font-size: 25px;">Your letter is:</p>'
        pred2 = labels_dict[pred_sorted[1]]
        pred3 = labels_dict[pred_sorted[2]]
        pred4 = labels_dict[pred_sorted[3]]
        other_text = f'<p style="font-size: 20px;">Or perhaps {pred2}, {pred3} or {pred4}</p>'
        st.markdown(subtext, unsafe_allow_html=True)
        st.markdown(pred_text, unsafe_allow_html=True)
        st.markdown(other_text, unsafe_allow_html=True)
