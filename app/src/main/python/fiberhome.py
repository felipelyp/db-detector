# Importação lib do sistema
import os
import re

# Importação lib local
import telnet

class Fiberhome:
    
    def __init__(self):
        self.clean_terminal = 'clear'

    def start(self, host, port, user, passw):
        self.telnet = telnet.Telnet(host, port, user, passw)
        # Verificar se os comando é compativel
        self.telnet.send('cd gpononu')
        data = self.telnet.data()
        # Comandos versão recente da olt
        if 'can not find the dir' in data:
            self.last = True
            self.dir_gpononu = 'cd onu'
            self.dir_qinq = 'cd lan'
            self.check_slot = 'show online slot SLOT_NUM pon PON_NUM'
            self.sinal_onu = 'show optic_module slot SLOT_NUM pon PON_NUM onu ONU_NUM'
            self.onu_mode = 'show onu_servic slot SLOT_NUM pon PON_NUM onu ONU_NUM'
        else: # Comandos versão antiga da olt
            self.last = False
            self.dir_gpononu = 'cd gpononu'
            self.dir_qinq = 'cd qinq'
            self.check_slot = 'show online slot SLOT_NUM link PON_NUM'
            self.sinal_onu = 'show optic_module slot SLOT_NUM link PON_NUM onu ONU_NUM'
            self.onu_mode = 'show onu_servic slot SLOT_NUM link PON_NUM onu ONU_NUM'
    
    def cd_gpononu(self):
        self.telnet.send(self.dir_gpononu)

    def cd_qinq(self):
        self.telnet.send(self.dir_qinq)

    def cd_exit(self):
        self.telnet.send('cd ..')

    def show_online_onus(self, slot, pon, controlc = False):
        cmd = self.check_slot.replace('SLOT_NUM', str(slot))
        cmd = cmd.replace('PON_NUM', str(pon))
        
        self.telnet.send(cmd)
        
        stop = True
        data_pon = ''

        while stop:
            data = self.telnet.data()
            data_pon += data
            if controlc:
                self.telnet.send('\x03')
                break

            if 'stop' in data:
                self.telnet.send(' ', False)
            else:
                stop = False
        
        # Limpar tudo
        self.clean_terminal = 'clear'

        return data_pon
        
    def show_optic_module(self, slot, pon, onu):
        cmd = self.sinal_onu.replace('SLOT_NUM', str(slot))
        cmd = cmd.replace('PON_NUM', str(pon))
        cmd = cmd.replace('ONU_NUM', str(onu))

        self.telnet.send(cmd)
        
        data = self.telnet.data()

        return data.replace(' ', '').rstrip()

    def show_onu_mode(self, slot, pon, onu):
        cmd = self.onu_mode.replace('SLOT_NUM', str(slot))
        cmd = cmd.replace('PON_NUM', str(pon))
        cmd = cmd.replace('ONU_NUM', str(onu))

        self.telnet.send(cmd)

        return self.telnet.data()
    
    def data(self):
        return self.telnet.data()