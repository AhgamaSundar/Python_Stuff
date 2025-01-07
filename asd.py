import FreeSimpleGUI as sg                        
import testli
# Define the window's contents
label=sg.Text("Todo")
inp_bx=sg.InputText(tooltip="Enter the Content",key="Addi")
editbutton=sg.Button("Edit")
listbox=sg.Listbox(values=[i[:-1] for i in testli.Realtd()],size=[45,10],enable_events=True,key="listbox")
add_button=sg.Button("Add")
complete_button=sg.Button("Complete")
exitbut=sg.Button("Exit")


layout = [ [label],
          [inp_bx,add_button],
         [listbox,editbutton],
         [complete_button,exitbut]
                    
          ]


# Create the window
window = sg.Window("Todo List",layout,
                   font=("TimesNewRoman",23))      

while True:
    
    event,value=window.read()
    if event==sg.WIN_CLOSED or event=="Exit":
        break 
    elif event=="Add":
        testli.writeltd(value["Addi"]+"\n")
        window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
    elif event=="Edit":
        testli.edit_txt(value["listbox"],value["Addi"]+"\n")
        window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
    elif event=="listbox":
        window['Addi'].update(value=value['listbox'][0])
    elif event=="Complete":
        print(value['listbox'][0])
        testli.complete(value['listbox'][0]+"\n")
        window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
    
                       
    print(event)
    print(value)
# Finish up by removing from the screen
window.close()                                 