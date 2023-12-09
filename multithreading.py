import threading


def multithreading(funcao):
    t = threading.Thread(target=funcao)
    t.setDaemon(True)
    t.start()