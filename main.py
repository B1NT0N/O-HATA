import flet as ft
import time

def main(page):

    page.theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.colors.GREEN,
        primary_container=ft.colors.GREEN_200
        # ...
    ),
)

    def add_clicked():
        ft.Text(value="12", color="green"),

    parameter = ft.TextField(hint_text="Number", width=200)

    unity_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Watts"),
            ft.dropdown.Option("Log"),
        ],
    )

    page.add(
        

        ft.Text(value="Frequency", color="green"),
        ft.Row([
            ft.TextField(hint_text="150 - 2000 MHz", width=200),
                ]),

        ft.Text(value="Distance", color=""),
        ft.Row([
            ft.TextField(hint_text="1 - 20 Km", width=200),
            unity_dropdown
                ]),

        ft.Text(value="Mobile Station Heigh", color=""),
        ft.Row([
            ft.TextField(hint_text="1 - 10 m", width=200),
            unity_dropdown
            ]),
 
        )

ft.app(target=main)   