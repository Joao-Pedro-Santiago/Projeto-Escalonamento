class Processo:
    def __init__(self, pid, chegada, tempo_cpu):
        self.pid = pid
        self.chegada = chegada
        self.tempo_cpu = tempo_cpu
        self.tempo_restante = tempo_cpu
        self.inicio = None
        self.fim = 0
        self.espera = 0
        self.turnaround = 0
