# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:56:51 2023

@author: @Zafiro
"""

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
#import streamlit_ace as st_ace

# Título de la aplicación
st.title("Mensaje de Ánimo para tus Exámenes")

# Cargar la imagen de fondo
imagen_fondo = Image.open("fondo.jpg")

# Mostrar la imagen de fondo
#st.image(imagen_fondo, use_column_width=True)


# Mensaje extenso
mensaje = """
¡Muchos éxitos en tus exámenes!

Eres increíble. 💪😊
"""

# Mostrar el mensaje animado
#st_ace(mensaje_largo, language="markdown", height=300, theme="dracula", key="mensaje_animado")
#st.markdown(mensaje_largo)
# Superponer el mensaje en la imagen de fondo
imagen_superpuesta = imagen_fondo.copy()
dibujo = ImageDraw.Draw(imagen_superpuesta)
font = ImageFont.load_default()  # Puedes personalizar la fuente y el tamaño aquí
posicion_texto = (100, 500)  # Ajusta la posición del texto según tus preferencias
#color_texto = "blue"  # Cambia el color del texto a negro
tamaño_fuente = 200  # Cambia el tamaño de la fuente a 20
font = ImageFont.truetype("Popping-Cute.ttf", tamaño_fuente)  # Cambia la fuente y el tamaño
#dibujo.text(posicion_texto, mensaje, fill=color_texto, font=font)
color_texto = "white"
color_sombra = "black"  # Cambia el color de la sombra a blanco o cualquier otro color que desees
tamaño_sombra = 2  # Ajusta el tamaño de la sombra según tus preferencias
dibujo.text(posicion_texto, mensaje.upper(), fill=color_sombra, font=font, stroke_width=tamaño_sombra)
dibujo.text(posicion_texto, mensaje.upper(), fill=color_texto, font=font)
# Mostrar la imagen superpuesta
st.image(imagen_superpuesta, use_column_width=False, width=800, caption="Mensaje")

# Crear dos columnas: una para la imagen de Charmander y otra para el mensaje completo
col1, col2 = st.columns(2)

# Agregar imagen de Charmander en la columna 1
imagen_charmander = Image.open("charmander.png")  # Reemplaza con la ruta de tu imagen de Charmander
col1.image(imagen_charmander, use_column_width=True)

# Mensaje completo en la columna 2
col2.write("""
# Mensaje Completo:

Estoy seguro de que vas a hacer un excelente trabajo en tus exámenes. 
Recuerda que tienes la capacidad y la determinación para superar cualquier desafío que se te presente en la vida.

La preparación que has realizado te llevará lejos, y estoy aquí para apoyarte en todo momento. 
Tú eres increíble y tienes un futuro brillante por delante.

Confía en ti misma, mantén la calma y da lo mejor de ti en cada examen. 
Estoy ansioso por verte triunfar y celebrar contigo tus logros. ¡Vamos, tú puedes hacerlo!
""")