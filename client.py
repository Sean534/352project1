# client.py
import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    
    #Send hello
    message = "HELLO"
    print(f"[C]: Sending to server: {message} ")
    cs.send(message.encode('utf-8'))
    
    #Opening text and sending it to the server
    with open('in-proj.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                # Sending string to the server
                print(f"[C]: Sending to server: {line}")
                cs.send(line.encode('utf-8'))
                
    #Shutdown which means that are done sending data
    cs.shutdown(socket.SHUT_WR)
    

    # Receive data from the server
    data_from_server = cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    
    #String from server to client
    
    
    server_string = ""
    while True:
        string_from_server = cs.recv(100).decode('utf-8')
        if not string_from_server:
            print(f"[C]: Client is now breaking out of while loop")
            break
        server_string += string_from_server
        
    lines = server_string.split('\n')
    for line in lines:
        print(f"[C]: Data received from server: {line}")
    
        

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    client()
