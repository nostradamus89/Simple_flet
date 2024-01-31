from flet import *
from controls import BaseScreen


class DocumentDetailsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self._initialize_screen()

    def _initialize_screen(self):
        super()._initialize_screen()
        
        # Document Number Display
        doc_num_display = Container(
            Column(
                controls=[
                    Text(
                        'ТД00-00013', 
                        color="#750273", 
                        size=21, 
                        weight=FontWeight.W_700, 
                        text_align=TextAlign.CENTER
                    ),
                    Text(
                        '05-22-2023 12:53:10', 
                        color=colors.BLACK54, 
                        size=12, 
                        text_align=TextAlign.CENTER
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            height=70,
            
        )
        
        # DataTable
        order_table = DataTable(
            border=border.all(1, "black"),
            heading_row_height=30,
            # data_row_color={"hovered": "#750273"},
            divider_thickness=0,
            column_spacing=20,
            columns=[
                DataColumn(Text("Название", color=colors.BLACK,)),
                DataColumn(Text("План", color=colors.BLACK), numeric=True),
                DataColumn(Text("Факт", color=colors.BLACK), numeric=True)
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(name, color=colors.BLACK),on_tap=lambda _: self.page.go('/documents/item_details')),
                        DataCell(Text(str(plan), color=colors.BLACK)),
                        DataCell(Text(str(fact), color=colors.BLACK))
                    ],
                    color=colors.RED_50 if idx % 2 == 0 else None
                ) for idx, (name, plan, fact) in enumerate(self._get_table_data())
            ]
        )
        
        btn_upload = ElevatedButton(
            'ВЫГРУЗИТЬ ДОКУМЕНТ',
            bgcolor = '#dbd9db',
            color = colors.BLACK,
            width = 400,
            height = 35,
            style = ButtonStyle(
               shape=RoundedRectangleBorder(radius=5),
            ),
            elevation = 3   
        )
       
        content = Column(
            controls=[doc_num_display, order_table, btn_upload],
            expand=2,
            spacing=10,
            alignment= MainAxisAlignment.START,
            horizontal_alignment= CrossAxisAlignment.CENTER
        )
        
        self.controls = [content]

    def _get_table_data(self):
        return (
            ("Комбайн кухонный BINATONE FP 67", 20, 1),
            ("Комбайн кухонный BINATONE FP 67", 0, 0),
            ("Комбайн кухонный BINATONE FP 67", 20, 0),
            ("Вентилятор JIPONIC (Тайв.) напольный", 2, 1),
            ("Вентилятор JIPONIC (Тайв.) напольный", 2, 0)
        )

# Later when you create the screen, pass the document number to it
# screen = CustomerOrderScreen("ТД00-000013")
