
start python ../dispatcher/dispatcher.py
timeout /t 2
start python tck_interoperability/test_socket_tm.py
timeout /t 2
start python tck_interoperability/test_socket_ta.py