# utt_PhotoshopUI

created based on my [universal_tool_template.py](https://github.com/shiningdesign/universal_tool_template.py), together with module_photoshop.py,

it allow you to run a cross-platform, cross-application Qt UI to scripting Photoshop in Javascript like Script Editor in Maya.

the technology is based on "Photoshop theCustomScript.jsx" method, which is compatible for all versions of Photoshop, both on Windows and Mac; which also means similar method can be used for all adobe applications.

For more details, please feel free to check my Photoshop Scripting note on my wiki:
[http://www.shining-lucy.com/wiki/page.php?id=appwiki:photoshop:ps_script](http://www.shining-lucy.com/wiki/page.php?id=appwiki:photoshop:ps_script)

## screenshot

in Windows as standalone and embeded in Maya.

![PhotoshopUI_v0.1_screenshot.png](screenshot/PhotoshopUI_v0.1_screenshot.png?raw=true)

# PhotoshopUI.py

a simple quick UI based on universal_tool_template.py for the module_photoshop.py

# module_photoshop.py, process.jsx, process_output.txt

the core functions for get everything working, it supports windows and mac, and auto detect all photoshop versions.

the other 2 blank files for catch and pass data use.

How it works
----
1. it takes user command text
2. then it combine the command with result output command, 
  * if the user have not use the "result" variable in the user command text to catch the return data, then nothing is returned
  * if the user have use the "result" variable in user command text, then the return will be put into the process_out.txt file
3. then it will put the command text into process.jsx file
4. then, subprocess photoshop to run that jsx
5. then, inside photoshop, it runs the script and the last step of the javascript will write the return data into process_output.txt file
6. then the module_photoshop.py will check modified date of that file and try default 1min checking, and get result from text file into python data

# other files

  * PhotoshopUI.bat: the bat file to quickly let you run the ui version
  * LNTextEdit.py: the ui module used in universal tool template, v3.2 used, for line numbered text editor

# known issue
  * dont put alert('') in the last line of input commands, it will freeze for some reason, although you can put alert('') command alone or as first line, it runs fine,


