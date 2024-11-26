import streamlit as st
from streamlit_option_menu import option_menu
import Home, Filtering, Analysis, Prediction
from PIL import Image

img = Image.open("D:\Cardekho ML\img\myimg.jpg")
st.set_page_config(page_title = 'Cardekho Used cars Price Prediction', page_icon = img,layout = 'wide')

class multiapp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({'title':title,'function':function})
    def run(self):
        with st.sidebar:
            app = option_menu('Car Used Cars Price Prediction', ["Data Filtering","Data Analysis","Data Prediction"], 
                icons=['search',"reception-4","dice-5-fill"], 
                menu_icon='cash-coin', default_index=0, orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#A95C68"}, # #008080
                    "icon": {"color": "violet", "font-size": "20px"}, 
                    "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#C4A484"},
                    "nav-link-selected": {"background-color": "#C04000"}, 
                }
            )
        if app == 'Data Filtering':
            Filtering.app()
        elif app == 'Data Analysis':
            Analysis.app()
        elif app == 'Data Prediction':
            Prediction.app()
        
app = multiapp()

# Add your apps to the multiapp instance
app.add_app("Data Filtering", Filtering.app)
app.add_app("Data Analysis", Analysis.app)
app.add_app("Data Prediction", Prediction.app)

# Run the multiapp
app.run()