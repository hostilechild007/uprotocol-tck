start python ../dispatcher/dispatcher.py
timeout /t 1
start python ./service.py
timeout /t 1
start python ./client_door.py