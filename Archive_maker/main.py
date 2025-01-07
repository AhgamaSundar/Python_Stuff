import FreeSimpleGUI as sg 
import zipcreator as zp

label=sg.Text("Choose the file")
oinput=sg.Input(tooltip="Select the source")
button=sg.FilesBrowse("Choose",key="source")
dlabel=sg.Text("Choose the Destination")
dinput=sg.Input(tooltip="Select the Destination")
dbutton=sg.FolderBrowse("Choose",key="Destination")
reslabel=sg.Text("Result Archive name")
archive_name=sg.Input(tooltip="Give the result Name",key="resname",size=(14,5))
outputtxt=sg.Text(key="output")

window=sg.Window("Compressor",layout=[[label],[oinput,button],
                                      [dlabel],[dinput,dbutton],
                                      [reslabel,archive_name],
                                      [sg.Button("Compress")],[outputtxt]],element_justification= 'l')
while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    print(event)
    filepaths=values['source'].split(";")
    folder=values['Destination']
    
    
    if event=="Compress":
        a=zp.make_archive(filepaths,folder,values['resname'])
        if a:
            window['output'].update(value="The Compression is done",text_color="green")
    
        
        
        
    
    
window.close()
