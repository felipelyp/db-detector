# Importação lib do sistema
import os
import re

# Importação lib local
import telnet

tn = telnet.Telnet()

""" Comandos geral """
dir_gpononu = 'cd onu'
dir_qinq = 'cd lan'
check_slot = 'show online slot SLOT_NUM pon PON_NUM'
sinal_onu = 'show optic_module slot SLOT_NUM pon PON_NUM onu ONU_NUM'
onu_mode = 'show onu_servic slot SLOT_NUM pon PON_NUM onu ONU_NUM'

def connect(host, port, user, passw):
    global dir_gpononu, dir_qinq, check_slot
    global sinal_onu, onu_mode

    tn.connect(host, port, user, passw)
    # Verificar se os comando é compativel
    tn.send('cd gpononu')
    data = tn.data()
    # Comandos versão anterior da olt
    if '\\gpononu#' in data:
        """ Aplicar comandos novos """
        dir_gpononu = 'cd gpononu'
        dir_qinq = 'cd qinq'
        check_slot = 'show online slot SLOT_NUM link PON_NUM'
        sinal_onu = 'show optic_module slot SLOT_NUM link PON_NUM onu ONU_NUM'
        onu_mode = 'show onu_servic slot SLOT_NUM link PON_NUM onu ONU_NUM'

def cd_gpononu():
    tn.send(dir_gpononu)
    return tn.data()

def cd_qinq():
    tn.send(dir_qinq)

def cd_exit():
    tn.send('cd ..')

def show_online_onu(slot, pon, controlc = False):
    cmd = check_slot.replace('SLOT_NUM', str(slot))
    cmd = cmd.replace('PON_NUM', str(pon))
    
    tn.send(cmd)
    
    stop = True
    data_pon = ''

    while stop:
        data = tn.data()
        data_pon += data
        if controlc:
            tn.send('\x03')
            break

        if 'stop' in data:
            tn.send(' ', False)
        else:
            stop = False
    
    # Limpar tudo
    tn.send('clear')

    return data_pon
        
def show_optic_module(slot, pon, onu):
    cmd = sinal_onu.replace('SLOT_NUM', str(slot))
    cmd = cmd.replace('PON_NUM', str(pon))
    cmd = cmd.replace('ONU_NUM', str(onu))

    tn.send(cmd)
        
    return tn.data()

def show_onu_mode(slot, pon, onu):
    cmd = onu_mode.replace('SLOT_NUM', str(slot))
    cmd = cmd.replace('PON_NUM', str(pon))
    cmd = cmd.replace('ONU_NUM', str(onu))

    tn.send(cmd)

    return tn.data()
    
def data():
    return tn.data()