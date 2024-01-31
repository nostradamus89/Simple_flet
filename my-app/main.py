from typing import Any, Optional, Union
import flet as ft
from flet import Page, Column, Row, Container, padding, alignment, LinearGradient, animation, Text
from flet_core.buttons import ButtonStyle
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
from views import views_handler
    

def main(page: Page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            secondary_container=ft.colors.WHITE10,
            primary="#c55b36",
        ),
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
        views_handler(page)[page.route]
        )

    
    page.on_route_change = route_change
    page.go('/')


if __name__=="__main__":
    ft.app(target=main, assets_dir="assets")
