#!/bin/bash

cd ~/
source env/bin/activate
echo "Virtual Env. Iniated!"

googlesamples-assistant-hotword
echo "Initializing Google-Assistant..."

echo "Ford Multimidia GUI V2.23"
python3 gui.py
echo "Starting..."
exit 0
