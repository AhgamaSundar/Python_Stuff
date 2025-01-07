import FreeSimpleGUI as sg                        
import testli
# Define the window's contents
label=sg.Text("Todo")
inp_bx=sg.InputText(tooltip="Enter the Content",key="Addi")
editbutton=sg.Button("Edit")
listbox=sg.Listbox(values=[i for i in testli.Realtd()],size=[45,10],enable_events=True,key="listbox")
add_button=sg.Button("Add")
layout = [ [label],
          [inp_bx,add_button],
         [listbox,editbutton],
                    
          ]


# Create the window
window = sg.Window("Todo List",layout,
                   font=("TimesNewRoman",23))      # Part 3 - Window Defintion

while True:
    
    event,value=window.read()
    if event==sg.WIN_CLOSED:
        break 
    elif event=="Add":
        testli.writeltd(value["Addi"]+"\n")
        window['listbox'].update(values=[i for i in testli.Realtd()])
    elif event=="Edit":
        testli.edit_txt(value["listbox"],value["Addi"]+"\n")
        window['listbox'].update(values=[i for i in testli.Realtd()])
    elif event=="listbox":
        window['Addi'].update(value=value['listbox'][0])
    
                       
# Do something with the information gathered
    print(event)
    print(value)
# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window