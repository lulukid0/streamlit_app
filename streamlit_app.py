import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MiniMap

popuptext='<b>Óvalo de Miraflores</b>'
popuptext1='<b>Complejo Deportivo "Manuel Bonilla"</b>'

ovalo_miraflores = folium.Map(location=[-12.110372628922658, -77.03693043439692],zoom_start=15)
folium.Marker(location=[-12.110372628922658, -77.03693043439692],popup=popuptext).add_to(ovalo_miraflores)
folium.Circle(location=[-12.110372628922658, -77.03693043439692],color='purple',fill_color='red',radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recolección de datos').add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(ovalo_miraflores)

folium.Marker(location=[-12.109942556243945, -77.05185625658847], popup=popuptext1).add_to(ovalo_miraflores)
folium.Circle(location=[-12.109942556243945, -77.05185625658847],color='purple',fill_color='red', radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recoleccion de datos'). add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(ovalo_miraflores)

minimap=MiniMap(tile_layer='stamenterrain')

minimap=MiniMap(tile_layer='stamenterrain')
ovalo_miraflores.add_child(minimap)
ovalo_miraflores
from folium.plugins import MiniMap

popuptext='<b>Óvalo de Miraflores</b>'
popuptext1='<b>Complejo Deportivo "Manuel Bonilla"</b>'

ovalo_miraflores = folium.Map(location=[-12.110372628922658, -77.03693043439692],zoom_start=15)
folium.Marker(location=[-12.110372628922658, -77.03693043439692],popup=popuptext).add_to(ovalo_miraflores)
folium.Circle(location=[-12.110372628922658, -77.03693043439692],color='purple',fill_color='red',radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recolección de datos').add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(ovalo_miraflores)

folium.Marker(location=[-12.109942556243945, -77.05185625658847], popup=popuptext1).add_to(ovalo_miraflores)
folium.Circle(location=[-12.109942556243945, -77.05185625658847],color='purple',fill_color='red', radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recoleccion de datos'). add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(ovalo_miraflores)

minimap=MiniMap(tile_layer='stamenterrain')

minimap=MiniMap(tile_layer='stamenterrain')
ovalo_miraflores.add_child(minimap)
ovalo_miraflores
st_data= st_folium(ovalo_miraflores,width=725)

