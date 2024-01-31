import flet as ft
import time

import flet as ft

def main(page):
    page.window_min_height = 650        # window's width is 200 px
    page.window_min_width = 600       # window's height is 200 px
    # page.window_resizable = True  # window is not resizable

    page.title = "O-HAMA"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=10,
                        padding=10,
                        content=ft.Text(
                            "O-HAMA",
                            theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
                            weight=ft.FontWeight.BOLD,

                            )
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.symmetric(horizontal=15),
                        
                        content=ft.Card(

                            content=ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[
                                    
                                    ft.Container(
                                        content=ft.Text(
                                            "Freq.",
                                            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE_200,
                                            ),
                                        margin=10,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        ),
                                        
                                    ft.Container(
                                        content= ft.TextField(
                                        label = "Frequency",
                                        hint_text="150 - 2000 ",
                                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
                                        keyboard_type="NUMBER",
                                        suffix_text = " MHz",
                                        text_align = "RIGHT",
                                        # border=ft.InputBorder.UNDERLINE,
                                        # filled=False,
                                        ),

                                        margin=5,
                                        padding=10,
                                        # alignment=ft.alignment.center_right,
                                    ) 
                                ]
                                
                            ),
                            
                        ),

                        # content = ft.ListTile(
                        #     leading=ft.Icon(ft.icons.ALBUM),
                        #     title=ft.Text("The Enchanted Nightingale"),
                        #     subtitle=ft.Text(
                        #         "Music by Julie Gable. Lyrics by Sidney Stein."
                        #     ),
                        # ),
                        
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.symmetric(horizontal=15),
                        
                        content=ft.Card(

                            content=ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[
                                    
                                    ft.Container(
                                        content=ft.Text(
                                            "Dist.",
                                            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE_200,
                                            ),
                                        margin=10,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        ),
                                        
                                    ft.Container(
                                        content= ft.TextField(
                                        label = "Distance",
                                        hint_text="1 - 20 ",
                                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
                                        keyboard_type="NUMBER",
                                        suffix_text = " Km",
                                        text_align = "RIGHT",
                                        # border=ft.InputBorder.UNDERLINE,
                                        # filled=False,
                                        ),

                                        margin=5,
                                        padding=10,
                                        # alignment=ft.alignment.center_right,
                                    ) 
                                ]
                                
                            ),
                            
                        ),

                        # content = ft.ListTile(
                        #     leading=ft.Icon(ft.icons.ALBUM),
                        #     title=ft.Text("The Enchanted Nightingale"),
                        #     subtitle=ft.Text(
                        #         "Music by Julie Gable. Lyrics by Sidney Stein."
                        #     ),
                        # ),
                        
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.symmetric(horizontal=15),
                        
                        content=ft.Card(

                            content=ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[
                                    
                                    ft.Container(
                                        content=ft.Text(
                                            "Hgt.",
                                            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE_200,
                                            ),
                                        margin=10,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        ),
                                        
                                    ft.Container(
                                        content= ft.TextField(
                                        label = "Height",
                                        hint_text="1 - 10 ",
                                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
                                        keyboard_type="NUMBER",
                                        suffix_text = " m",
                                        text_align = "RIGHT",
                                        # border=ft.InputBorder.UNDERLINE,
                                        # filled=False,
                                        ),

                                        margin=5,
                                        padding=10,
                                        # alignment=ft.alignment.center_right,
                                    ) 
                                ]
                                
                            ),
                            
                        ),

                        # content = ft.ListTile(
                        #     leading=ft.Icon(ft.icons.ALBUM),
                        #     title=ft.Text("The Enchanted Nightingale"),
                        #     subtitle=ft.Text(
                        #         "Music by Julie Gable. Lyrics by Sidney Stein."
                        #     ),
                        # ),
                        
                    ),

                    ft.Container(
                        margin = ft.margin.symmetric(horizontal=100),
                        alignment=ft.alignment.center,
                        content=ft.ElevatedButton(
                            
                            "Calculate",
                            bgcolor=ft.colors.BLUE_800,
                            color=ft.colors.WHITE,
                            style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            width=2050,
                            height=50,
                            )
                    )
                ]
            )
        )
        
    )

ft.app(target=main, )