import socket
import time

def creatinglog(ipadres):

    log = open('log.txt','a')
    log.write(str(time.ctime())+': '+str(ipadres)+'\n')


def savingrequest(request):

    requests = open('requests.txt','a')
    requests.write(request)
    requests.write('\n\n\n')
    

    
header = 'HTTP/1.1 200 OK\r\n'+str(time.ctime())+'server:Python\ncontent-Type:text/html\r\n\n\n'
#print header

index = open('index.html','r')

serve = header+index.read()
#print server

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('192.168.0.7',80))

sock.listen(5)

print 'python server started.....'

while True:

    connection, addresses = sock.accept()

    creatinglog(addresses)
    request = connection.recv(4096)

    if ('GET' in request) and ('HTTP/1.1' in request):

        savingrequest(request)

        connection.send(serve)
      
    connection.close()
    
index.close()
