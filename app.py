"""
import streamlit as st
from datetime import date
from plotly import graph_objs as go
import requests
import json
import itertools

if 'ls' not in st.session_state:
	st.session_state.ls = {}

	
@st.cache
def load_data(city):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f4f19cae7d4100d1cceb1599f25c750e&units=imperial").json()

data = [x for y in list(json.load(open('cities.json')).values()) for x in y]

selected_city = st.selectbox("Select a city", data)
loaded = load_data(selected_city)['main']
st.write(loaded)
st.session_state.ls[selected_city] = loaded
st.table(st.session_state.ls)"""
import streamlit as st
import requests
import json

sts = st.session_state

if 'ls' not in sts:
	sts.craftRecipies = {'thing1': ['thing1', 'thing2', 'thing3']}
	sts.refineRecipies = {}
	sts.cityCaftBonus = {}
	sts.cityRefineBonus = {}
	sts.cities = ['Bridgewatch', 'Caerleon', 'Fort Sterling', 'Lymhurst', 'Thetford']
	sts.saveCraft = {}
	sts.saveRefine = {}
	sts.craftItems = list(sts.craftRecipies.keys())
	sts.refineItems = list(sts.refineRecipies.keys())

selected_city = st.selectbox("Select A City", sts.cities)
selected_item = st.selectbox('Select An Item To Craft', sts.craftItems)
with st.form(key='columns_in_form'):
    cols = st.beta_columns(len(sts.craftRecipies[selected_item]))
    for i, col in enumerate(cols):
        col.number_input(f"Enter price of {sts.craftRecipies[selected_item][i]}", key=i)
    submitted = st.form_submit_button('Submit')


selected_item = st.selectbox('Select An Item To Refine', sts.refineItems)
