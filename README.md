# NSIS-Script-Maker-for-Windows-
NSIS Script Maker (Windows) - Uses a template and a Python script to generate a NSIS script.  

Use a template to build a NSIS (Nullsoft Scriptable Install System) script. This script installs your application in the Windows users folder, creates a shortcut on the start menu and on the deskotp. It also creates entries for uninstall in the Control Panel.

# Usage  

Leave the nsis_make.py and nsis_template.txt files in the same folder.  
Edit the variables at the beginning of the nsis_make.py file.  
After executing it, a .txt file will be created in the same folder with the NSIS script.  
Copy this .txt file and a license file called LICENSE.txt to the root of your application folder.  
Run the NSIS application (https://nsis.sourceforge.io/Main_Page), click on "Compile NSIS scripts" and drag the generated file to the screen.  
The .exe installation file will be generated inside your application folder.  
