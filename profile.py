import PySimpleGUI as sg
sg.theme("banana")
sg.theme_text_color("#007FFF")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                    font=("Arinal",25,"italic","bold","underline"))],
        [sg.Text("NPM       : 2210010599")],
        [sg.Text("Nama      : Ahmad Ramadhani")],
        [sg.Text("Kelas     : 5M")],
        [sg.Text("Matkul    : Pemrograman Visual 3")],
        ],
    size=(510,200),
    font=("Times", 18))

window()
window.close()