def escalonamento_round_robin(processos, quantum):
    tempo_atual = 0
    concluidos = 0
    n = len(processos)
    gantt = []
    fila_prontos = []

    # Ordena inicialmente por tempo de chegada
    processos.sort(key=lambda p: p.chegada)

    processos_adicionados = [False] * n

    while concluidos < n:
        # Adiciona processos que chegaram no tempo_atual a fila
        for i in range(n):
            if processos[i].chegada <= tempo_atual and not processos_adicionados[i]:
                fila_prontos.append(processos[i])
                processos_adicionados[i] = True

        if not fila_prontos:
            # CPU Ociosa
            if gantt and gantt[-1][0] == "OCIOSO":
                gantt[-1][2] += 1
            else:
                gantt.append(["OCIOSO", tempo_atual, tempo_atual + 1])
            tempo_atual += 1
            continue

        # Remove o primeiro da lista (Simula o Deque)
        atual = fila_prontos.pop(0)

        if atual.inicio is None:
            atual.inicio = tempo_atual

        # Define o tempo de execucao (menor entre o restante e o quantum)
        tempo_exec = min(atual.tempo_restante, quantum)

        # Registro para o grafico de Gantt
        gantt.append([f"P{atual.pid}", tempo_atual, tempo_atual + tempo_exec])

        # Incrementa o tempo passo a passo para checar novas chegadas durante o quantum
        for _ in range(tempo_exec):
            tempo_atual += 1
            for i in range(n):
                if processos[i].chegada <= tempo_atual and not processos_adicionados[i]:
                    fila_prontos.append(processos[i])
                    processos_adicionados[i] = True

        atual.tempo_restante -= tempo_exec

        if atual.tempo_restante > 0:
            # Se ainda tem tempo, volta para o FIM da fila
            fila_prontos.append(atual)
        else:
            # Finalizado
            atual.fim = tempo_atual
            atual.turnaround = atual.fim - atual.chegada
            atual.espera = atual.turnaround - atual.tempo_cpu
            concluidos += 1

    return processos, gantt
