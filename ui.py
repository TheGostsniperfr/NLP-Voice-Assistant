import flet as ft
from nlp import *
import asyncio

async def type_text(page, text_field, text, delay=0.1):
    for char in text:
        text_field.value += char
        await page.update_async()
        await asyncio.sleep(delay)


def chatting(page: ft.Page):
    page.title = "NLP Project"
    chat = ft.Column()
    new_message = ft.TextField(label="Message to send", hint_text="")
    
    chatBot = ChatBotLogic(conversation)

    def hear(e):
        query = chatBot.takeCommand()
        asyncio.run(type_text(page, new_message, query))

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        chat.controls.append(ft.Text(""))
        query = new_message.value

        new_message.value = ""
        page.update()
        newText = chatBot.process(query = query)
        asyncio.run(type_text(page, chat.controls[len(chat.controls) - 1], newText))
    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Speak", on_click=hear), ft.ElevatedButton("Send", on_click=send_click)])
    )

