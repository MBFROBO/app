import flet as ft
import multiprocessing as mp
from multiprocessing import Value, Queue, Pipe


async def main(page: ft.Page, q):
    
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    async def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        await page.update_async()

    async def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        await page.update_async()

    await page.add_async(
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
    parent_conn, child_conn = Pipe()
    proc1 = mp.Process(target=ft.app, kwargs={'target':main})
    proc2 = mp.Process(target = ft.app, kwargs=dict(target=main, view=ft.AppView.WEB_BROWSER))
    
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()