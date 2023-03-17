# MayaGPT

A simple script to integrate the openai API in Maya and use the ChatGPT to generate python scripts for Maya. Basically it send the prompt to openai through API, asking for a python script for Maya, and once received the script in response, execute it.

To make it work you have to install openai python module inside Maya:
- In the "Autodesk/maya/bin" directory: run "mayapy -m pip install openai".

Inside the script, insert yout API KEY into the "openai.api_key" variable.
