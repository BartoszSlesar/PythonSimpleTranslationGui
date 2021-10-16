import PySimpleGUI as sg
import json
from src.utils.utils_func import Language, load_data


class Layout:
    def __init__(self):
        self.languages = load_data(r"..\..\resources\comboData.pickle")

    def get_layout(self):
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.

        # TODO Stworzyc ComboBox zmieniajacy jezyk do ktorego mozna tlumaczyc na podstawie wybranego jezyka
        input_column = [[sg.Text('Original Text')], [sg.Multiline(size=(40, 20), enter_submits=True)]]

        output_column = [[sg.Text('Translated Text')],
                         [sg.Multiline(size=(40, 20), key="-OUT-" + sg.WRITE_ONLY_KEY, no_scrollbar=True,
                                       reroute_cprint=True)]]

        data = list(self.languages.keys())
        default_value_from = data[0]
        default_value_to = self.get_data(default_value_from)
        language_from = sg.Column(
            [[sg.Text('from')],
             [sg.Combo(data, size=(19, 5), key="_FROM_", enable_events=True, default_value=default_value_from)]])
        language_to = sg.Column(
            [[sg.Text('to')],
             [sg.Combo(default_value_to, size=(19, 5), key="_TO_", default_value=default_value_to[0])]])

        return [[sg.Column(input_column), sg.Column(output_column)],
                [sg.T(' '), sg.Button('Capture speech'), sg.Button('Record'), sg.Button("Translate"),
                 sg.Frame('Select Language', [[language_from, language_to]])]]

    def get_data(self, key):
        return self.languages[key]
