def mostrar_tabela(processos):
    print("\n" + "=" * 80)
    print("RESULTADO DO ESCALONAMENTO ROUND-ROBIN")
    print("=" * 80)
    print(f"{'PID':<6}{'Chegada':<10}{'Tempo CPU':<12}{'Inicio':<10}{'Fim':<10}{'Espera':<10}{'Turnaround':<12}")
    print("-" * 80)

    for p in processos:
        print(f"{p.pid:<6}{p.chegada:<10}{p.tempo_cpu:<12}{p.inicio:<10}{p.fim:<10}{p.espera:<10}{p.turnaround:<12}")

    media_espera = sum(p.espera for p in processos) / len(processos)
    media_turnaround = sum(p.turnaround for p in processos) / len(processos)

    print("-" * 80)
    print(f"Media de espera: {media_espera:.2f}")
    print(f"Media de turnaround: {media_turnaround:.2f}")
    print("=" * 80)


def mostrar_gantt(gantt):
    print("\nGRAFICO DE GANTT")
    print("=" * 80)

    linha_blocos = ""
    linha_tempos = ""

    for i, (nome, inicio, fim) in enumerate(gantt):
        duracao = fim - inicio
        bloco = f" {nome} " * duracao
        linha_blocos += "|" + bloco

        if i == 0:
            linha_tempos += str(inicio)

        espacos = len(bloco) - (len(str(fim)) - 1)
        if espacos < 1:
            espacos = 1
        linha_tempos += " " * espacos + str(fim)

    linha_blocos += "|"

    print(linha_blocos)
    print(linha_tempos)
    print("=" * 80)

def mostrar_execucao_passo_a_passo(processos, tipo_escalonador, quantum=None):
    """
    Simula a execução passo a passo mostrando o estado da CPU e da Fila.
    Funciona para RR (com preempção e quantum) e SJF (não preemptivo).
    """
    print(f"\nSIMULACAO PASSO A PASSO ({tipo_escalonador.upper()})")
    print("=" * 80)

    tempo_atual = 0
    concluidos = 0
    n = len(processos)
    fila_prontos = []
    processos_adicionados = [False] * n
    
    # Criar cópias para não alterar os objetos originais do relatório
    import copy
    processos_sim = copy.deepcopy(processos)
    for p in processos_sim:
        p.tempo_restante_sim = p.tempo_cpu
    
    processos_ordenados = sorted(processos_sim, key=lambda p: p.chegada)

    while concluidos < n:
        # 1. Chegada de novos processos
        for i in range(n):
            if processos_ordenados[i].chegada <= tempo_atual and not processos_adicionados[i]:
                fila_prontos.append(processos_ordenados[i])
                processos_adicionados[i] = True
        
        # Ordenação específica da fila para SJF (o menor tempo restante primeiro)
        if tipo_escalonador.lower() == "sjf":
            fila_prontos.sort(key=lambda p: p.tempo_restante_sim)

        if not fila_prontos:
            print(f"Tempo {tempo_atual:>2}: CPU = OCIOSA | Fila = []")
            tempo_atual += 1
            continue
            
        atual = fila_prontos.pop(0)
        
        # Define o tempo que ficará na CPU neste turno
        if tipo_escalonador.lower() == "rr":
            tempo_permanencia = min(atual.tempo_restante_sim, quantum)
        else: # SJF (neste projeto é não preemptivo)
            tempo_permanencia = atual.tempo_restante_sim
        
        # 2. Execução na CPU passo a passo
        for _ in range(tempo_permanencia):
            nomes_fila = [f"P{p.pid}" for p in fila_prontos]
            print(f"Tempo {tempo_atual:>2}: CPU = P{atual.pid:<5} | Fila = [{', '.join(nomes_fila)}]")
            
            tempo_atual += 1
            atual.tempo_restante_sim -= 1
            
            # Checa chegadas DURANTE a execução
            for i in range(n):
                if processos_ordenados[i].chegada <= tempo_atual and not processos_adicionados[i]:
                    fila_prontos.append(processos_ordenados[i])
                    processos_adicionados[i] = True
                    # Se for SJF, reordenar a fila com o novo integrante
                    if tipo_escalonador.lower() == "sjf":
                        fila_prontos.sort(key=lambda p: p.tempo_restante_sim)
        
        # 3. Lógica de saída/retorno à fila
        if atual.tempo_restante_sim > 0:
            fila_prontos.append(atual) # Volta para o final (preempção por quantum)
        else:
            concluidos += 1

    print(f"Tempo {tempo_atual:>2}: Simulação Finalizada.")
    print("=" * 80)