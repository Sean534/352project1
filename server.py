import socket

def reverse_swap(string):
    return string[::-1].swapcase()

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # reverse hello to client.   
    message = csockid.recv(100).decode('utf-8')
    reverse_message = reverse_swap(message)
    csockid.send(reverse_message.encode('utf-8'))
    
     #Opening the output file
    with open('out-proj.txt', 'w') as file:
        my_string = ""
        while True:
             # recieve string from client
            string_from_client = csockid.recv(100).decode('utf-8')
            my_string += string_from_client
            #print(my_string)
            if not string_from_client:
                print(f"[S]: Server is now breaking out while loop")
                break
            # inputs the string into the reverse method
            #reverse_string = reverse_swap(string_from_client)
            # writes the reverse string in the file
            #file.write(reverse_string)
            #print(f"[S]: Received and processed: {my_string}")
        #print(my_string.split('\n'))
        
        lines = my_string.split('\n') #separates every line by \n
        #print(lines)
        for line in lines:
            reverse_string = reverse_swap(line)
            file.write(reverse_string)
            if line != lines[-1]:
                file.write('\n')
                
    #Send the contents back to the client
    #Opening text and sending it to the client
    with open('out-proj.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                # Sending string to the client
                print(f"[S]: Sending to client: {line}")
                csockid.send(line.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()

if __name__ == "__main__":
    server()


   