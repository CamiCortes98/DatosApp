"""Welcome to Reflex!."""

from DatosApp import styles

# Import all the pages.
from DatosApp.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    objetoVacio = {}

# Create the app.
app = rx.App(style=styles.base_style)
