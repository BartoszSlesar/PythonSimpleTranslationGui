import PySimpleGUI as sg
import threading

import my_layout
from src.utils.utils_func import translate

THREAD_EVENT = '-THREAD-'

cp = sg.cprint


def run_gui(title, layout, events: dict = None, **kwargs):
    window = sg.Window(title, layout.get_layout(), **kwargs)
    while True:
        event, values = window.read()
        if event == '_FROM_':
            item = values[event]
            combo_values = layout.get_data(item)
            window['_TO_'].update(value=combo_values[0], values=combo_values)
        if event == "Translate":
            model = f"{values['_FROM_'].get_model()}-{values['_TO_'].get_model()}"
            print(model)
            threading.Thread(target=translate, args=(window, values[0], model,), daemon=True).start()
        if event == THREAD_EVENT:
            window["-OUT-" + sg.WRITE_ONLY_KEY].Update('')
            cp(f'{values[THREAD_EVENT]}')
        if event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    myLayout = my_layout.Layout()
    run_gui("Test_Run", myLayout, finalize=True)
