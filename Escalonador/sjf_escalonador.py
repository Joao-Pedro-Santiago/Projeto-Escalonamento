def escalonamento_sjf(processos):
    tempo_atual = 0
    concluidos = 0
    n = len(processos)
    gantt = []
    atual = None

    while concluidos < n:
        prontos = []

        for p in processos:
            if p.chegada <= tempo_atual and p.tempo_restante > 0:
                prontos.append(p)

        if not prontos:
            if gantt and gantt[-1][0] == "OCIOSO":
                gantt[-1][2] += 1
            else:
                gantt.append(["OCIOSO", tempo_atual, tempo_atual + 1])
            tempo_atual += 1
            continue

        if atual is None:
            atual = min(prontos, key=lambda p: p.tempo_restante)

            if atual.inicio is None:
                atual.inicio = tempo_atual

            gantt.append([f"P{atual.pid}", tempo_atual, tempo_atual])

        atual.tempo_restante -= 1
        tempo_atual += 1
        gantt[-1][2] = tempo_atual

        if atual.tempo_restante == 0:
            atual.fim = tempo_atual
            atual.turnaround = atual.fim - atual.chegada
            atual.espera = atual.turnaround - atual.tempo_cpu
            concluidos += 1
            atual = None

    return processos, gantt
