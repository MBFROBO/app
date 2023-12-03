import flet as ft
import multiprocessing as mp
from multiprocessing import Value


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    
    proc1 = mp.Process(target=ft.app, kwargs={'target':main})
    proc2 = mp.Process(target = ft.app, kwargs=dict(target=main, view=ft.AppView.WEB_BROWSER))
    
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()