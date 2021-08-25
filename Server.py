from File_SC import Server


def main():
    server = Server(IP='localhost', PORT=9090, SIZE=10240, FORMAT='utf-8')
    server.connect_client()
    server.send_file(PATH=r'Path of the File To be sended')
    server.recv_file(FILEPATH=r'downloading path(must)')

while True:
    main()
