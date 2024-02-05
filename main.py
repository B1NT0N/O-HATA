import flet as ft
import math

import flet as ft


def main(page):
    page.window_min_height = 650        # window's width is 200 px
    page.window_min_width = 600       # window's height is 200 px
    # page.window_resizable = True  # window is not resizable

    t = ft.Text(theme_style=ft.TextThemeStyle.DISPLAY_SMALL, weight=ft.FontWeight.BOLD,color=ft.colors.GREEN_200,)
    frequency = ft.Ref[ft.TextField]()
    distance = ft.Ref[ft.TextField]()
    mobile_height = ft.Ref[ft.TextField]()
    base_height= ft.Ref[ft.TextField]()
    
    k_ac = ft.Ref[ft.Checkbox]()
    k_al = ft.Ref[ft.Checkbox]()
    k_th = ft.Ref[ft.Checkbox]()
    k_hp = ft.Ref[ft.Checkbox]()
    k_ih = ft.Ref[ft.Checkbox]()
    
    area_type = ft.Ref[ft.Dropdown]()
    city_type = ft.Ref[ft.Dropdown]()
    

    def calculate_correction_factors():
        d = float(distance.current.value)
        f = float(frequency.current.value)
        m_h = float(mobile_height.current.value)
        b_h = float(base_height.current.value)
        d_h = b_h-m_h
        
        value_k_ac = -2.1*math.log(d) -6.3 if k_ac.current.value == True else 0
        
        if k_al.current.value != True:
            value_k_al = -2.7*math.log(d)+8.6 if d <= 40 else -2.7*math.log(d)+10.7
        else:
            value_k_al = 0
            
        value_k_th = -3*(math.log(d_h))**2-0.5*math.log(d_h)+4.5 if k_th.current.value == True else 0
        
        value_k_hp =  -2*(math.log(d_h))**2+16*math.log(d_h)-12 if k_hp.current.value == True else 0
        
        value_k_su = 2*(math.log(f/28))**2 + 5.40 if area_type.current.value == "Suburbs" else 0
        
        value_k_oa = 4.78*(math.log(f))**2 -8.33*math.log(f) + 40.9 if area_type.current.value == "Open Area" else 0
        
        value_k_qo = (4.78*(math.log(f))**2 -8.33*math.log(f) + 40.9) - 5 if area_type.current.value == "Semi-Open Area" else 0
        
        if city_type.current.value == "Medium City":
            c=0
        elif city_type.current.value == "City Center":
            c = 3
        else:
            c=0
            
        if city_type.current.value == "Medium City":
            H_mu = (1.10*math.log(f)-0.7)*m_h -(1.56*math.log(f)-0.8)
        elif city_type.current.value == "City Center" and f>=400:
            H_mu = 3.2*(math.log(11.75*m_h))**2-4.97
        elif f<200:
            H_mu = 8.29*(math.log(1.54*m_h))**2-1.10
        else:
            H_mu = 0
        
        
        
        k_sum = value_k_ac + value_k_al + value_k_th + value_k_hp + value_k_su + value_k_oa + value_k_qo + c - H_mu
        
        return k_sum

    def calculate(e):
        
        K_factors = 0
        
        if frequency.current.value != "" and distance.current.value != "" and base_height.current.value != "" and mobile_height.current.value != "" :
            
            objects = [frequency.current, distance.current, base_height.current, mobile_height.current]

            for obj in objects:
                obj.error_text = ""
                
            if (float(frequency.current.value) >= 150 and float(frequency.current.value) <= 2000) != True:
                frequency.current.error_text = "Not in Range"
            else:
                if (float(distance.current.value) >= 1 and float(distance.current.value) <= 20) != True:
                    distance.current.error_text = "Not in Range"
                else:
                    if (float(base_height.current.value) >= 30 and float(base_height.current.value) <= 1000) != True:
                        base_height.current.error_text = "Not in Range"
                    else:
                        if (float(mobile_height.current.value) >= 1 and float(mobile_height.current.value) <= 10) != True:
                            mobile_height.current.error_text = "Not in Range"
                        else:
                            K_factors = calculate_correction_factors()
                            loss = 46.30+33.90*math.log(f)-13.82*math.log(b_h) + \
                                (44.90-6.55*math.log(b_h))*math.log(d) + K_factors
                            t.value = f"Total Loss = {loss:.3f} dB"
                            
                            
                            for obj in objects:
                                obj.error_text = ""
                            
            d = float(distance.current.value)
            f = float(frequency.current.value)
            m_h = float(mobile_height.current.value)
            b_h = float(base_height.current.value)
            

            t.value = ""
            page.update()
        
        else:
            objects = [frequency.current, distance.current, base_height.current, mobile_height.current]

            for obj in objects:
                if obj.value == "":
                   obj.error_text = f"{obj.label} is not set"
                else:
                    obj.error_text = ""



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
                                                    error_text=""
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
                                                    error_text=""
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
                                                    error_text=""
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
                                                    error_text=""
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
                                                
                                                label="K_al - Radial Streets", value=False,ref=k_al,),
                                            ft.Checkbox(
                                                label="K_ac - Circumferential Streets", value=False,ref=k_ac,),
                                            # ft.Checkbox(
                                            #     label="K_sp - Medium Incline", value=False,ref=k_sp,),
                                            ft.Checkbox(
                                                label="K_th - Terrain Slope", value=False,ref=k_th,),
                                            ft.Checkbox(
                                                label="K_hp - Position on the Ondulation of the Terrain", value=False,ref=k_hp,),
                                            ft.Checkbox(
                                                label="K_ih - Isolated Hill", value=False,ref=k_ih,),
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
                                                ref = area_type,
                                                        options=[
                                                            ft.dropdown.Option(
                                                                "Open Area"),
                                                            ft.dropdown.Option(
                                                                "Semi-Open Area"),
                                                            ft.dropdown.Option(
                                                                "Suburbs"),
                                                            
                                                        ],
                                                    ),
                                            
                                            ft.Dropdown(
                                                label="City Type",
                                                        ref =city_type,
                                                        options=[
                                                            ft.dropdown.Option(
                                                                "Medium City"),
                                                            ft.dropdown.Option(
                                                                "City Center"),
                                                            
                                                        
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
                    ),
                    
                ]
            )

        ),
        t

    )


ft.app(target=main, 
    #    view=ft.AppView.WEB_BROWSER
       )
