import flet as ft

def startSpeaking(page: ft.Page):
    page.controls[1].controls[1].icon = ft.icons.MIC
    page.controls[1].controls[1].icon_color = "red"
    page.update()

def stopSpeaking(page: ft.Page):
    page.controls[1].controls[1].icon = ft.icons.MIC_NONE
    page.controls[1].controls[1].icon_color = page.controls[1].controls[2].icon_color
    page.update()
