# -------------------------------------------------------------------------
#
# Copyright (c) 2023 General Motors GTO LLC
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------


import socket
from typing import Dict
from threading import Thread
from threading import Lock
import uuid
import logging 
import sys


PORT = 44444
IP = "127.0.0.1" 
ADDR = (IP, PORT)

logging.basicConfig(format='%(asctime)s %(message)s')
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)


# Holds all client connections
clients: Dict[str, socket.socket] = {}
# Create the shared lock
lock = Lock()

def close_socket(client_id: str, locket: Lock):
    with locket:
        clients[client_id].close()
        del clients[client_id]

def handle_client(clientsocket: socket.socket, client_id: str, locket: Lock):
    while True: 
        
        try: 
            recv_data: bytes = clientsocket.recv(32767) 

            if recv_data == b"":
                continue

            logger.info (f"received data: {recv_data}")
            
            for peer_id, peer_socket in clients.items():
                # Send if peer client is connected... 
                try:
                    peer_socket.send(recv_data) 
                    
                except ConnectionAbortedError as i_e:
                    # Close and delete peer socket if peer client closed...
                    logger.error(f"Peer socket exception: {i_e}")
                    close_socket(client_id, locket)

                    if peer_id == client_id:
                        return 
                    continue 

        except ConnectionAbortedError as o_e:
            # If client socket cannot receive, then close client 
            logger.error(f"Client socket receive exception: {o_e}")
            close_socket(client_id, locket)
            return


def run_server():
    # Create a socket object 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
    logger.info("Server Socket successfully created")

    # Prerequisite for server to listen for incoming conn. requests
    server.bind(ADDR)  
    logger.info("Socket binded to " + str(ADDR)) 

    # Put the socket into listening mode 
    # NOTE: 5 connections are kept waiting 
    # if the server is busy and if a 6th socket tries to connect, then the connection is refused.
    server.listen(5)  
    logger.info ("Socket is listening")  

    # Where server is always listening for incoming clients
    while True:
        # Establish connection with client. 
        clientsocket, addr = server.accept()   
        print(clientsocket)
        client_id: str = str(uuid.uuid4())
        clients[client_id] = clientsocket

        thread = Thread(target=handle_client, args=(clientsocket, client_id, lock))
        thread.start()
    

if __name__ == '__main__':

    print(sys.byteorder)
    run_server()