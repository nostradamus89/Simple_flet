import flet as ft
from flet import *
from controls import BaseScreen

class DocumentsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self._initialize_screen()
    

    def _initialize_screen(self):
        super()._initialize_screen()
        self.appbar.leading = None
        self.appbar.title = Text('Документы', size=18)
        self.appbar.actions=[]
        # buttons on the screen
        gv = ft.GridView(expand=True, max_extent=250, child_aspect_ratio=1.4)
        docs_data = (
            ("ЗаказКлиенту", "1/0", "Строк: 2/0", "Товаров: 20/0"),
            ("ЗаказПоставщику", "1/0", "Строк:22/0", "Товаров: 8/0"),
            ("Инвентаризация", "3/0", "Строк: 126/0", "Товаров: 2299/0"),
            ("Приобретение товаров и услуг", "1/0", "Строк: 2/0", "Товаров: 9/0"),
            ("Реализация товаров и услуг", "1/0", "Строк: 2/0", "Товаров: 30/0"),
        )
        for elem in docs_data:
            gv.controls.append(
                Container(
                    Column(
                        controls=[
                            Row(controls=[
                                Text(elem[0], 
                                    color="black", 
                                    text_align=TextAlign.CENTER, 
                                    weight= FontWeight.BOLD, 
                                    size=16, 
                                    expand=1)
                                ], 
                                alignment='center'),
                            Row(controls=[Text(elem[1], color="black"),]),
                            Row(controls=[Text(elem[2], color="black"),]),
                            Row(controls=[Text(elem[3], color="black"),])
                        ],
                        spacing=3
                        ),
                bgcolor=ft.colors.WHITE,
                border=ft.border.all(1, ft.colors.ORANGE_100),
                border_radius=ft.border_radius.all(5),
                padding=4,
                on_click=lambda _: self.page.go('/documents/docs_list')
                )
            )

        self.controls=[gv]
        
