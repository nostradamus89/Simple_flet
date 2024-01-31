import flet as ft
from flet import *
from screens.home import HomeScreen
from screens.documents import DocumentsScreen
from screens.docs_list import DocumentsListScreen
from screens.doc_details_screen import DocumentDetailsScreen
from screens.item_details_screen import ItemDetailsScreen

def views_handler(page):

    return {
        '/': HomeScreen(),
        '/documents': DocumentsScreen(),
        '/documents/docs_list' : DocumentsListScreen(),
        '/documents/docs_details' : DocumentDetailsScreen(),
        '/documents/item_details' : ItemDetailsScreen()
    }