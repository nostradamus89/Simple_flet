from flet import *
from controls import BaseScreen, ProcessButton


class HomeScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self._initialize_screen()
    
    def _initialize_screen(self):
        super()._initialize_screen()
        # buttons on the screen
        list_view = ListView(expand=1, spacing=20, padding=3)
        list_view.controls.extend([
            ProcessButton("Документы", icon=icons.EDIT_DOCUMENT, on_click=lambda _: self.page.go('/documents')),
            ProcessButton("Групповая обработка", icon=icons.SPEAKER_GROUP_OUTLINED),
            ProcessButton("Адресное хранение", icon=icons.ALL_INBOX_OUTLINED),
            ProcessButton("Сбор ШК", icon=icons.BARCODE_READER),
            ProcessButton("Товары",  icon=icons.SHOPPING_CART_ROUNDED),
            ProcessButton("Параметры", icon=icons.SETTINGS_OUTLINED),
            ProcessButton("Отладка", icon=icons.BUG_REPORT_OUTLINED),
            ProcessButton("Проводник", icon=icons.FOLDER_OUTLINED)
            ])
        
        self.controls = [list_view]
        
          
                
  
  
  
  