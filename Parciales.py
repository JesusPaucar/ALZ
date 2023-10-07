# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:56:51 2023

@author: @Jesus
"""

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("Mensaje de Ánimo para tus Exámenes")

imagen_fondo = Image.open("fondo.jpg")

#st.image(imagen_fondo, use_column_width=True)


mensaje = """
¡Muchos éxitos en tus exámenes!

Eres increíble. 💪😊
"""

imagen_superpuesta = imagen_fondo.copy()
dibujo = ImageDraw.Draw(imagen_superpuesta)
font = ImageFont.load_default() 
posicion_texto = (100, 500)  
tamaño_fuente = 200 
font = ImageFont.truetype("Popping-Cute.ttf", tamaño_fuente) 
color_texto = "white"
color_sombra = "black" 
tamaño_sombra = 2 
dibujo.text(posicion_texto, mensaje.upper(), fill=color_sombra, font=font, stroke_width=tamaño_sombra)
dibujo.text(posicion_texto, mensaje.upper(), fill=color_texto, font=font)

st.image(imagen_superpuesta, use_column_width=False, width=800, caption="Mensaje")

col1, col2 = st.columns(2)

imagen_charmander = Image.open("charmander.png")  
col1.image(imagen_charmander, use_column_width=True)

col2.write("""

Estoy seguro de que vas a hacer un excelente trabajo en tus exámenes. 
Recuerda que tienes la capacidad y la determinación para superar cualquier desafío que se te presente en la vida.

La preparación que has realizado te llevará lejos, y estoy aquí para apoyarte en todo momento. 
Tú eres increíble y tienes un futuro brillante por delante.

Confía en ti misma, mantén la calma y da lo mejor de ti en cada examen. 
Estoy ansioso por verte triunfar y celebrar contigo tus logros. ¡Vamos, tú puedes hacerlo!
""")
