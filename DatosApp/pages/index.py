"""The home page of the app."""

from DatosApp import styles
from DatosApp.templates import template
import re
import reflex as rx
import pandas as pd

@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)


#Funcion para registro de usuario

def usuario(email, contraseña):
    usuarios : {}
    for i in range(len(usuarios)):
        if re.match(r'^\S+@', email) and ' ' not in email and re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', contraseña):
            email = input("Ingrese el correo a registrar")
            contraseña = input("Ingresar la contraseña")
            usuarios[email] = contraseña
            print("Usuario registrado exitosamente")
        else:
            print("El usuario no pudo ser creado")




#Funciones para transformar un archivo excel a csv
        
def excel_a_csv():
    df = pd.read_excel()


#Funciones para transformar un archivo de pdf a csv
        