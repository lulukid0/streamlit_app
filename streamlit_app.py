import streamlit as st
from streamlit_folium import st_folium
import folium
m = folium.Map(location=[-12.110372628922658, -77.03693043439692],zoom_start=15)
folium.Marker(location=[-12.110372628922658, -77.03693043439692],popup=popuptext).add_to(m)
folium.Circle(location=[-12.110372628922658, -77.03693043439692],color='purple',fill_color='red',radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recolección de datos').add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(m)

st_data=st_folium(m,width=725)

