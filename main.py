import flet as ft
import math

import flet as ft


def main(page):
    page.window_min_height = 650        # window's width is 200 px
    page.window_min_width = 600       # window's height is 200 px
    # page.window_resizable = True  # window is not resizable

    t = ft.Text()
    frequency = ft.Ref[ft.TextField]()
    distance = ft.Ref[ft.TextField]()
    mobile_height = ft.Ref[ft.TextField]()
    base_height= ft.Ref[ft.TextField]()

    def calculate(e):
        print(frequency.current.value)
        # freq = float(frequency.current.value)
        # dist = float(distance.current.value)
        # hgt = float(height.current.value)
        
        c = 0
        h = 0
        ksum = 0
        # loss = 46.30+33.90*math.log(freq)-13.82*math.log(hgt) + \
        #     (44.90-6.55*math.log(hgt))*math.log(dist)-h+c+ksum
        loss = 0

        t.value = f"{loss}"
        page.update()

    page.title = "OKUMURATA-HATA"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            margin=10,
            padding=10,
            content=ft.Text(
                "OKUMURATA-HATA",
                theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
                weight=ft.FontWeight.BOLD,

            )
        ),
        ft.Container(
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        
                        [

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
                                                ft.Text(
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

                                                ft.TextField(
                                                    label="Frequency",
                                                    ref=frequency,
                                                    hint_text="150 - 2000 ",
                                                    input_filter=ft.InputFilter(
                                                        allow=True, regex_string=r"[0-9.]", replacement_string=""),
                                                    keyboard_type="NUMBER",
                                                    suffix_text=" MHz",
                                                    text_align="RIGHT",
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
                                                content=ft.TextField(
                                                    ref=distance,
                                                    label="Distance",
                                                    hint_text="1 - 20 ",
                                                    input_filter=ft.InputFilter(
                                                        allow=True, regex_string=r"[0-9.]", replacement_string=""),
                                                    keyboard_type="NUMBER",
                                                    suffix_text=" Km",
                                                    text_align="RIGHT",
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
                                                content=ft.TextField(
                                                    ref=base_height,
                                                    label="Base Station Height",
                                                    hint_text="30 - 1000",
                                                    input_filter=ft.InputFilter(
                                                        allow=True, regex_string=r"[0-9.]", replacement_string=""),
                                                    keyboard_type="NUMBER",
                                                    suffix_text=" m",
                                                    text_align="RIGHT",
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
                                                content=ft.TextField(
                                                    ref=mobile_height,
                                                    label="Mobile Station Height",
                                                    hint_text="1 - 10 ",
                                                    input_filter=ft.InputFilter(
                                                        allow=True, regex_string=r"[0-9.]", replacement_string=""),
                                                    keyboard_type="NUMBER",
                                                    suffix_text=" m",
                                                    text_align="RIGHT",
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

                            ),

                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.symmetric(horizontal=20, ),
                                # margin=ft.margin.only(top=20, left=20, right=20),
                                # padding=ft.padding.symmetric(horizontal=20),
                                padding=ft.padding.only(top=0, left=20, right=20),
                                content=ft.ElevatedButton(
                                    "Calculate",
                                    bgcolor=ft.colors.BLUE_800,
                                    color=ft.colors.WHITE,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(
                                            radius=10),
                                    ),
                                    width=420,
                                    height=60,
                                    on_click=calculate
                                )
                            ),

                            t
                        ]
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                margin=ft.margin.only(right=50,top=0),
                                content=ft.Card(
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                padding=ft.padding.symmetric(horizontal=15, vertical=15),
                                                # margin=10,
                                                content=ft.Text(
                                                "Correction Factors",
                                                theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.colors.BLUE_200,
                                                ),
                                            ),
                                            
                                            ft.Container(
                                                padding=ft.padding.symmetric(horizontal=15),
                                                content=ft.Column(
                                                    [
                                                        ft.Checkbox(
                                                label="K_al - Radial Streets", value=False),
                                            ft.Checkbox(
                                                label="K_ac - Circumferential Streets", value=False),
                                            ft.Checkbox(
                                                label="K_sp - Medium Incline", value=False),
                                            ft.Checkbox(
                                                label="K_th - Terrain Slope", value=False),
                                            ft.Checkbox(
                                                label="K_hp - Position on the Ondulation of the Terrain", value=False),
                                            ft.Checkbox(
                                                label="K_ih - Isolated Hill", value=False),
                                                    ]
                                                )
                                            ),
                                            
                                            ft.Container(
                                                padding=ft.padding.only(left=15, right=15, bottom=15),
                                                # padding=ft.padding.symmetric(horizontal=15, vertical=15),
                                                content=ft.Row(
                                                    [
                                                        ft.Dropdown(
                                                label="Area Type",
                                                
                                                        options=[
                                                            ft.dropdown.Option(
                                                                "Open Area"),
                                                            ft.dropdown.Option(
                                                                "Semi-Open Area"),
                                                            ft.dropdown.Option(
                                                                "Suburbs"),
                                                            ft.dropdown.Option(
                                                                "Unknown"),
                                                        ],
                                                    ),
                                            
                                            ft.Dropdown(
                                                label="City Type",
                                                
                                                        options=[
                                                            ft.dropdown.Option(
                                                                "Medium City"),
                                                            ft.dropdown.Option(
                                                                "City Centers"),
                                                            ft.dropdown.Option(
                                                                "Unknown"),
                                                        
                                                        ],
                                                    ),
                                                    ]
                                                )
                                            ),
                                            
                                            
                                        ]
                                    )
                                )
                            )
                        ]
                    )
                ]
            )

        )

    )


ft.app(target=main, 
    #    view=ft.AppView.WEB_BROWSER
       )
