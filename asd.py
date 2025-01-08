import FreeSimpleGUI as sg                        
import testli
import time



# Define the window's contents
dlabel=sg.Text('',key='clock' ,text_color="white",background_color="black")
label=sg.Text("Todo" ,background_color="black")
inp_bx=sg.InputText(tooltip="Enter the Content",key="Addi")
editbutton=sg.Button("Edit")
listbox=sg.Listbox(values=[i[:-1] for i in testli.Realtd()],size=[45,10],enable_events=True,key="listbox")
add_button=sg.Button("Add")
complete_button=sg.Button("Complete")
exitbut=sg.Button("Exit",button_color="Red")

sg.theme("Black")
layout = [ [label ],[dlabel],
          [inp_bx,add_button],
         [listbox,editbutton],
         [complete_button,exitbut]
                    
          ]


# Create the window
window = sg.Window("Todo List",layout,
                   font=("TimesNewRoman",23))      

while True:
    
    event,value=window.read(timeout=10)
    if event==sg.WIN_CLOSED or event=="Exit":
        break 
   
    elif event=="Add":
        if value["Addi"]:
               
            testli.writeltd(value["Addi"]+"\n")
            window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
        else:
            sg.popup("Enter a Value",font=("TimesNewRoman",20))
    elif event=="Edit":
        testli.edit_txt(value["listbox"],value["Addi"]+"\n")
        window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
    elif event=="listbox":
        window['Addi'].update(value=value['listbox'][0])
    elif event=="Complete":
        if value['listbox']:
            
            testli.complete(value['listbox'][0]+"\n")
            window['listbox'].update(values=[i[:-1] for i in testli.Realtd()])
        else:
            sg.popup("Please select a task",font=20)
    
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
                       
    
    
# Finish up by removing from the screen
window.close()                                 