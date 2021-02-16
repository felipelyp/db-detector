import time
import telnetlib

class Telnet:
    
    #
    # Desenvolvido por Felipe Lyp
    #

    def __init__(self, host, port, username, password):
        self.telnet = telnetlib.Telnet(host, port)
            
        self.telnet.read_until(b"Login:")
        self.telnet.write(username.encode('ascii') + b"\n")

        if password:
            self.telnet.read_until(b"Password:") 
            self.telnet.write(password.encode('ascii') + b"\n")

        self.send('en')
        self.send(password)

    def send(self, cmd, encode_ascii = True):
        if encode_ascii:
            self.telnet.write(cmd.encode('ascii') + b"\n")
        else:   
            self.telnet.write(cmd.encode())
        time.sleep(1)

    def data(self):
        return str(self.telnet.read_very_eager().decode('ascii'))