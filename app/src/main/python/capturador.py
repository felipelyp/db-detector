import fiberhome

fiber = fiberhome.Fiberhome()

def start(host, ip, user, passw):
    return fiber.start(host, ip, user, passw)

def cd_gpononu():
    fiber.cd_gpononu()
    return fiber.data()