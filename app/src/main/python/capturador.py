import fiberhome

fiberhome = fiberhome.Fiberhome()

def start(host, ip, user, passw):
    fiberhome.start(host, ip, user, passw)

def cd_gpononu():
    fiberhome.cd_gpononu()
    return fiberhome.data()