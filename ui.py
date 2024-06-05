import flet as ft

import asyncio
async def type_text(page, text_field, text, delay=0.1):
    for char in text:
        text_field.value += char
        await page.update_async()
        await asyncio.sleep(delay)


def chatting(page: ft.Page):
    page.title = "NLP Project"
    chat = ft.Column()
    new_message = ft.TextField()

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

