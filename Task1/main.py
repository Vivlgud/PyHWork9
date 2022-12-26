from kivy.app import App
 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
 
from kivy.uix.button import Button
from kivy.config import Config

from kivy.core.window import Window

Window.size=(350,350)
Window.clearcolor=(50/255,255/255,180/255,1)
 
 
class General(App):
    def build(self):
        """Игровое поле"""
        self.title = "Игра Крестики-нолики"
 
        root = BoxLayout(orientation="vertical", padding=5)
 
        grid = GridLayout(cols=3)
        self.buttons = []
        for _ in range(9):
            button = Button(
                color = [0,0,0,1],
                font_size = 24,
                disabled = False,
                on_press = self.krest_nol
            )
            self.buttons.append(button)
            grid.add_widget(button)
 
        root.add_widget(grid)
 
        root.add_widget(
            Button(
               text = "Сброс",
               size_hint = [1,.1],
               on_press = self.restart
            )
        )
 
        return root

    def __init__(self):
        super().__init__()
        self.switch = True
 
    def krest_nol(self, arg):
        """Логика игры""" 
        arg.disabled = True 
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch
 
        coordinate = (
            (0,1,2), (3,4,5), (6,7,8), # выигрыш по горизонтали
            (0,3,6), (1,4,7), (2,5,8), # выигрыш по вертикали
            (0,4,8), (2,4,6),          # выигрыш по диагонали
        )
 
        vector = lambda item: [self.buttons[x].text for x in item]
        color = [1,0,0,1]
 
        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break
 
    def restart(self, arg): 
        """Перезапуск игры"""
        self.switch = True
 
        for button in self.buttons:
            button.color = [0,0,0,0]
            button.text = ""
            button.disabled = False
 
    
 
# Запуск программы
if __name__ == "__main__":
    General().run()