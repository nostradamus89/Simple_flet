from flet import *
from controls import BaseScreen


class ItemDetailsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        
        self._initialize_screen()
    
    def _initialize_screen(self):
        super()._initialize_screen()
        self.item_data = {
            'order_info': {
                'number': 'TD00-5',
                'date_time': '05-22-2023 12:53:10',
                'article_number': 'KV-900',
                'characteristic': '2/5',
                'price': '0.0',
                'packing': 'шт (1 шт)'
            },
            'product_name': 'Комбайн кухонный BINATONE FP 67',
            'plan': 2,
            'fact': 0,
            'to_be': 0,
        }
        # Top Section: Order Details
        order_details = Column(
            controls=[
                Text(f"Заказ клиента № {self.item_data['order_info']['number']} {self.item_data['order_info']['date_time']}", color=colors.BLACK),
                Text(f"Артикул: {self.item_data['order_info']['article_number']}", color=colors.BLACK),
                Text(f"Характеристика: {self.item_data['order_info']['characteristic']}", color=colors.BLACK),
                Text(f"Цена: {self.item_data['order_info']['price']}", color=colors.BLACK),
                Text(f"Упаковка: {self.item_data['order_info']['packing']}", color=colors.BLACK),
            ]
        )

        # Middle Section: Product Details
        product_details = Column(
            controls=[
                Row(
                    controls=[
                        IconButton(icon=icons.ARROW_LEFT, on_click=self._prev_product),
                        Text(self.item_data['product_name'], color=colors.BLACK, size=24),
                        IconButton(icon=icons.ARROW_RIGHT, on_click=self._next_product),
                    ]
                ),
                Row(
                    controls=[
                        Text("План:", color=colors.BLACK),
                        Text(str(self.item_data['plan']), color=colors.BLACK)
                    ]
                ),
                Row(
                    controls=[
                        Text("Было:", color=colors.BLACK),
                        Text(str(self.item_data['fact']), color=colors.BLACK)
                    ]
                ),
                Row(
                    controls=[
                        Text("Будет:", color=colors.BLACK),
                        Text(str(self.item_data['to_be']), color=colors.BLACK)
                    ]
                )
            ],
            alignment=MainAxisAlignment.START
        )

        # Bottom Section: Adjustments
        adjustments = Row(
            controls=[
                ElevatedButton(text="-5", on_click=self._decrease_by_5),
                ElevatedButton(text="-1", on_click=self._decrease_by_1),
                ElevatedButton(text="...", on_click=self._decrease_by_1),
                ElevatedButton(text="+1", on_click=self._increase_by_1),
                ElevatedButton(text="+5", on_click=self._increase_by_5),
            ]
        )

        save_button = ElevatedButton(text="СОХРАНИТЬ", on_click=self._save_changes)

        # Combining all the sections
        self.controls=[order_details, product_details, adjustments, save_button]

    # Define click handlers for the buttons
    def _prev_product(self, e):
        # Navigate to the previous product
        pass

    def _next_product(self, e):
        # Navigate to the next product
        pass

    def _decrease_by_5(self, e):
        # Decrease quantity by 5
        pass

    def _decrease_by_1(self, e):
        # Decrease quantity by 1
        pass

    def _increase_by_1(self, e):
        # Increase quantity by 1
        pass

    def _increase_by_5(self, e):
        # Increase quantity by 5
        pass

    def _save_changes(self, e):
        # Save changes made to the item details
        pass
