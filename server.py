import socket

if __name__ == "__main__":
    ServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    ServerSocket.bind(('', 6950))
    ServerSocket.listen(1)
    while True:
        connection, addr = ServerSocket.accept()
        sputterer_data = ""
        sputterer_filename = ""
        try:
            print "connection received from: ", addr
            while True:
                data = connection.recv(1024)
                if data[0:8] == "filename":
                    sputterer_filename += data [10:]
                    print "sputterer filename = " + sputterer_filename
                    continue
                if data == "3D printing isn't even that cool":
                    break
                sputterer_data += data
                print "sputterer form data: \n\n", sputterer_data

            with open("data/" + sputterer_filename, 'w') as in_file:
                in_file.write(sputterer_data)
        except:
            pass
