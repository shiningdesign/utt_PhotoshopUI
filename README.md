# utt_PhotoshopUI

created based on universal_tool_template.py, together with module_photoshop.py,

it allow you to run a cross-platform, cross-application Qt UI to scripting Photoshop in Javascript like Script Editor in Maya.

the technology is based on "Photoshop theCustomScript.jsx" method, which is compatible for all versions of Photoshop, both on Windows and Mac; which also means similar method can be used for all adobe applications.

## screenshot

in Windows as standalone and embeded in Maya.

![PhotoshopUI_v0.1_screenshot.png](screenshot/PhotoshopUI_v0.1_screenshot.png?raw=true)

# PhotoshopUI.py

a simple quick UI based on universal_tool_template.py for the module_photoshop.py

# module_photoshop.py, process.jsx, process_output.txt

the core functions for get everything working, it supports windows and mac, and auto detect all photoshop versions.

the other 2 blank files for catch and pass data use.

# other files

  * PhotoshopUI.bat: the bat file to quickly let you run the ui version

# known issue
  * dont put alert('') in the last line of input commands, it will freeze for some reason, although you can put alert('') command alone or as first line, it runs fine,


