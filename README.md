# MayaGPT

![Screenshot of MayaGPT running inside Maya](https://i.ibb.co/ynW6b2j/Capturar.png)

A simple script to integrate the openai API in Maya and use the ChatGPT to generate python scripts for Maya using natural language prompts. Basically it send the prompt to openai through API, asking for a python script for Maya, and once received the script in response, execute it.

## How to use
You have to generate a new API Key to use the ChatGPT api. You can do it [here](https://platform.openai.com/account/api-keys) after create an account.
Also to make it work you have to install openai python module inside Maya:
- In the "Autodesk/maya/bin" directory: run "mayapy -m pip install openai".

Inside the script, insert yout API KEY into the "openai.api_key" variable.

Example:
https://www.youtube.com/watch?v=ZHKOR4yvfek

## FAQ
### Is it pratical?
No, there are some issues, and sometime it doesn't generate a workable script. It's still a proof-of-concept, but it's something. :)

### Can I try or use it in my works?
Definitely yes, you are free to use, improve or use in your professional work environment.
