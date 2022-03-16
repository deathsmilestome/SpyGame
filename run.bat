@echo off

call [path to bot]\spy\venv\Scripts\activate

cd [path to bot]\spy

set TOKEN= [your bot's token]

python [path to bot]\spy\spy.py

pause 
