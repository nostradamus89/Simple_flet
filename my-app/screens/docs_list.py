import flet as ft
from flet import *
from controls import BaseScreen

class DocumentFilterHeader(Container):
    def __init__(self):
        super().__init__()

        btn_doc_filter = PopupMenuButton(
            content=Text("Сборка", color=colors.BLACK87, weight=FontWeight.BOLD, size=18, expand=1),
            items=[
                PopupMenuItem(text="Все"),
                PopupMenuItem(text="Реализация товаров и услуг"),
                PopupMenuItem(text="Инвентаризация"),
                PopupMenuItem(text="Заказ клиенту"),
                PopupMenuItem(text="Сбор ШК"),
            ],
            tooltip='показать меню'
        )

        btn_status_filter = PopupMenuButton(
            content=Text("Все", color=colors.BLACK87, weight=FontWeight.BOLD, size=18, expand=1),
            items=[
                PopupMenuItem(text="Все"),
                PopupMenuItem(text="К выполнению"),
                PopupMenuItem(text="Выгружен"),
                PopupMenuItem(text="К выгрузке"),
            ],
            tooltip='показать меню'
        )

        filter_row = Row([
            Column([btn_doc_filter], expand=1),
            Column([btn_status_filter], horizontal_alignment=CrossAxisAlignment.START, expand=1)
        ])

        # Configure the properties of this container
        self.content = filter_row
        self.padding = Padding(5, 0, 0, 3)

class FirstLineCard(Container):
    def __init__(self, status_text='', doc_type_text=''):
        super().__init__()
        
        # Popup Menu Button
        popup_menu_button = PopupMenuButton(
            Icon(icons.MORE_VERT, color=colors.BLACK87),
            items=[
                PopupMenuItem(text="Удалить"),
                PopupMenuItem(text="Очистить данные пересчета"),
                PopupMenuItem(text="Отправить повторно"),
            ],
            tooltip='показать меню'
        )

        # Columns for the Row
        left_column = Column(controls=[Text(status_text, color=colors.BLACK87, size=12)], expand=1)
        
        right_column_content = Row([
            Text(doc_type_text, color=colors.BLACK87, size=14),
            popup_menu_button
        ], alignment=MainAxisAlignment.END)
        
        right_column = Column(controls=[right_column_content], expand=1, horizontal_alignment=CrossAxisAlignment.END)

        # Setting content for the Container
        self.content = Row([left_column, right_column])
        
        self.padding = Padding(3, 0, 0, 3)

class DocumentCard(Container):
    def __init__(self, status_text, doc_type_text, doc_num, company_name, location):
        super().__init__()
        
        self.first_line = FirstLineCard(status_text, doc_type_text)
        
        self.doc_num = Text(doc_num, color=colors.BLACK54, size=21, weight=FontWeight.W_700)
        self.company_name = Text(company_name, color=colors.BLACK54)
        self.location = Text(location, color=colors.BLACK54)
        
        self.content = Column(
            controls=[
                self.first_line,
                self.doc_num,
                self.company_name,
                self.location
            ],
            spacing=0,
        )
        
        self.bgcolor = ft.colors.WHITE
        self.border_radius = ft.border_radius.all(5)
        self.padding = 10
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=2,
            color=ft.colors.BLACK12
        )

        self.on_click=lambda _: self.page.go('/documents/docs_details')

class DocumentsListScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self._initialize_screen()

    def _initialize_screen(self):
        super()._initialize_screen()
        docs_data = (
            ("К выполнению", "Сборка", "ТД00-000013", "ООО Бытовая техника", "Центральный склад"),
            ("К выполнению", "Сборка", "ТД00-000014", "ООО Рога и копыта", "Центральный склад"),
            ("К выполнению", "Сборка", "ТД00-000015", "ООО Торговый Дом", "Центральный склад"),
            ("К выполнению", "Сборка", "ТД00-000016", "ООО Ромашка", "Центральный склад"),
            ("К выполнению", "Сборка", "ТД00-000017", "ООО Бытовая техника", "Центральный склад")
        )
        header = DocumentFilterHeader()
        list_view = ListView(expand=1, spacing=10, padding=3)
        
        for elem in docs_data:
            list_view.controls.append(DocumentCard(*elem))
        
        self.controls=[header, list_view]
        
