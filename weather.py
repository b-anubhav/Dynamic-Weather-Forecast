import PySimpleGUI as sg
import requests

def createGUI():

    left_col = [
        [sg.Text("Enter Your City?")],
        [sg.In(key="-input-")],
        [sg.Button("ok")]
    ]
    right_col = [
        [sg.Text("Weather In Your City : "), sg.Text(size=(10, 1), key="-city-")],
        [sg.Text(key="-output-",size=(45,15),background_color="#343434")]
    ]
    layout = [
        [sg.Column(left_col, element_justification='l'),
        sg.VSeparator(),
        sg.Column(right_col, element_justification='c')]
    ]

    window = sg.Window('Weather Gui App', layout, resizable= True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "ok":
            if values["-input-"]:
                    getDataFromApi(values["-input-"], window)

def getDataFromApi(city, window):

    window["-city-"].update(city)
    url = f"http://api.weatherapi.com/v1/current.json?key=da042aa7a3d24b06a03163903210301&q={city}"
    res = requests.get(url).json()

    data = {
        "City" : res["location"]["name"],
        "Region" : res["location"]["region"],
        "Country" : res["location"]["country"],
        "Temp to C" : res["current"]["temp_c"],
        "Temp to F" : res["current"]["temp_f"],
        "Condition" : res["current"]["condition"]["text"],
        
    }
 
    output = ""

    for x, y in data.items():
        output += f"    {x} :   {y} \n"

        window["-output-"].update(output)



if __name__ == "__main__":
    createGUI()