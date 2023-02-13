# CS361 Microservice Examples
Repo contains examples of two different approaches to the same basic microservice. The microservice provides 3 unique pseudorandom numbers to a client upon request. Requires [Python]("https://www.python.org/downloads/") and [PyZMQ]("https://github.com/zeromq/pyzmq#building-and-installation") to run.   

---
### Server.py: Overview: Data as string
The file server.py implements the microservice described above and returns all data as a byte string. The file client.py shows an example of a client that could connect to server.py. Any client connecting to server.py should expect all data received to be a byte string and must send data as a byte string. The client is responsible for decoding data sent by the server and manipulating it as needed.

#### Installation and running:
1. Ensure you have a valid version of Python installed. Python v. 3.11.0 is recommended. A Python version >= v. 3.4 is required.
2. Download server.py.
3. Download client.py (optional).
4. Start server.py:  
    ```python 
    python server.py
    ```
5. Start client.py (optional):  
    ```python  
    python client.py
    ```
6. If using client.py, follow the user prompts to generate 3 unique pseudorandom numbers.   
---

### Server_json_example.py: Overview: Data as JSON
The file server_json_example.py implements the microservice described above and returns all data as a JSON object. Any client connecting to server.py should expect all data received to be a valid JSON object and must send data as a **byte string**. The client is responsible for decoding data sent by the server and manipulating it as needed.

#### Installation and running:
1. Ensure you have a valid version of Python installed. Python v. 3.11.0 is recommended. A Python version >= v. 3.4 is required.
2. Download server_json_example.py.
3. Download client_json_example.py (optional).
4. Start server_json_example.py:  
    ```python 
    python server_json_example.py
    ```
5. Start client_json_example.py (optional):  
    ```python  
    python client_json_example.py
    ```
6. If using client_json_example.py, follow the user prompts to generate 3 unique pseudorandom numbers.

---
### Notes (both versions):
  * The server's default port is 5555. If a different port is needed, open the server.py or server_json_example.py file and change the PORT variable at the top of the file.
  * For ease of testing, the server will terminate the connection and shut down if it receives the data ```b'q'``` (i.e., "q" encoded as a byte string) from the client. This can be disabled by commenting out the relevant code in server.py or server_json_example.py.
  * The example client provides a simple UI, allowing the user to retrieve 3 pseudorandom numbers or quit the client program.
  * The client sends the server a termination request prior to exiting. This results in the server also closing its socket and the program exits (functionality implemented for easier testing).
