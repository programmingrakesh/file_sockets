from  file_sockets import Client

def main():
    client = Client(IP='localhost', PORT=9090, SIZE=10240, FORMAT='utf-8')
    client.connect_server()
    client.recv_file(FILEPATH=r'downloading path(must)')
    client.send_file(PATH='Path of the File to be sended.')
main()    
