'''
by ying: 2016.11.22 http://shining-lucy.com/wiki
note: make sure you have these empty 2 files next to it,
"process.jsx" and "process_output.txt"
'''
def ps_loc_win():
    import _winreg
    regKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\Photoshop.exe")
    regPath = _winreg.QueryValueEx(regKey, 'Path')[0] + 'Photoshop.exe'
    return regPath

def readFormatFile(file):
    with open(file) as f:
        txt = f.read()
    return txt
def writeFormatFile(txt, file):    
    with open(file, 'w') as f:
        f.write(txt)

import subprocess # for call Photoshop exe
import os # for file read and process
import sys # for os detection
import time # for timer to check file
def ps_cmd(cmd_txt, timer=1):
    location = os.path.dirname(os.path.realpath(__file__))
    jsx_file = os.path.join(location, "process.jsx")
    result_file = os.path.join(location, "process_output.txt")
    # step 1: record old result date
    old_output_timestamp = os.path.getmtime(result_file)
    
    txt=cmd_txt
    txt+="""
        var output_file = new File('{0}'); 
        output_file.open("w"); 
        if(typeof result !== "undefined") output_file.writeln(String(result));
        else output_file.writeln("");
        output_file.close();
        """.format(result_file.replace("\\","/"))
    writeFormatFile(txt, jsx_file)
    # step 2: process cmd
    if sys.platform in ['win32','win64']:
        ps_loc = ps_loc_win()
        subprocess.Popen(ps_loc+" "+jsx_file)
    elif sys.platform == 'darwin':
        subprocess.Popen('open -b com.adobe.Photoshop --args "{0}"'.format(jsx_file))
    # step 3: wait and get result
    timeout = time.time() + 60*timer  # default 1 minutes from now
    while True:
        time.sleep(0.1)
        if time.time() > timeout:
            print("Time Out after 1 minute and no change on result file.")
            break
        cur_output_timestamp = os.path.getmtime(result_file)
        if cur_output_timestamp > old_output_timestamp:
            print("Result completed.")
            break
    if cur_output_timestamp > old_output_timestamp:
        return readFormatFile(result_file)
    else:
        return None

# actual test example, code below can be removed
def main():
    my_cmd = """
    app.activeDocument.artLayers.add();
    activeDocument.activeLayer.name='Pass by jsx';
    result = app.activeDocument.layers.length;
    result = "layer_count:"+result;
    """

    my_result = ps_cmd(my_cmd)
    print(my_result)

if __name__ == "__main__":
    main()
