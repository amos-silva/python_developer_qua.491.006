import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def vel_media(vi, vf):
    vm = vf-vi
    return vm

def tempo_medio(tf, ti):
    tm = tf-ti
    return tm

def acel_media(vm, tm):
    am = vm/tm
    return am

def mru(si, v, t):  # MOVIMENTO UNIFORME
    s = si + v * t
    return s
