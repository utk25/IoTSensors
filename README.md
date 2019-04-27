# IoTSensors

Pre-requisites:
  
  Disable 2 step verification on your google account (if enabled)
  
  Give permissions to less secure apps to enable email sending
  
  Install paho mqtt client by running command 
  
    pip install paho-mqtt
  
    if pip is not found then add <PYTHON_HOME>\Scripts in your path (for Windows)
  
  Or clone the repo https://github.com/eclipse/paho.mqtt.python 
    
    cd paho.mqtt.python
    
    python setup.py install

Steps to run:
  
  Initialize the values of variables in publish.py and subscribe.py
    
    most of it is defaulted. Enter emails in subscribe.py
  
  Open 2 cmd shell / powershell (for windows) or login to 2 sessions on linux
  
  Run command
    
    python publish.py in one shell
    
    python subscribe.py in other shell
    
  NOTE: The values have been defaulted for a small timeframe for quick testing
