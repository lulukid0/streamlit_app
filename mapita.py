import folium
import folium
from folium.plugins import MiniMap

popuptext='<b>Óvalo de Miraflores</b>'


ovalo_miraflores = folium.Map(location=[-12.110372628922658, -77.03693043439692],zoom_start=16)
folium.Marker(location=[-12.110372628922658, -77.03693043439692],popup=popuptext).add_to(ovalo_miraflores)
folium.Circle(location=[-12.110372628922658, -77.03693043439692],color='purple',fill_color='red',radius=40,weight=-4,fill_opacity=0.5,tooltip='Punto de recolección de datos').add_to(ovalo_miraflores)
folium.TileLayer('stamenterrain').add_to(ovalo_miraflores)

minimap=MiniMap(tile_layer='stamenterrain')
ovalo_miraflores.add_child(minimap)
ovalo_miraflores
