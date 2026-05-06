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
        # Adiciona processos que chegaram no tempo_atual à fila
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
            
        # Define o tempo de execução (menor entre o restante e o quantum)
        tempo_exec = min(atual.tempo_restante, quantum)
        
        # Registro para o gráfico de Gantt
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


def mostrar_tabela(processos):
    print("\n" + "=" * 80)
    print("RESULTADO DO ESCALONAMENTO ROUND-ROBIN")
    print("=" * 80)
    print(f"{'PID':<6}{'Chegada':<10}{'Tempo CPU':<12}{'Início':<10}{'Fim':<10}{'Espera':<10}{'Turnaround':<12}")
    print("-" * 80)

    for p in processos:
        print(f"{p.pid:<6}{p.chegada:<10}{p.tempo_cpu:<12}{p.inicio:<10}{p.fim:<10}{p.espera:<10}{p.turnaround:<12}")

    media_espera = sum(p.espera for p in processos) / len(processos)
    media_turnaround = sum(p.turnaround for p in processos) / len(processos)

    print("-" * 80)
    print(f"Média de espera: {media_espera:.2f}")
    print(f"Média de turnaround: {media_turnaround:.2f}")
    print("=" * 80)


def mostrar_gantt(gantt):
    print("\nGRÁFICO DE GANTT")
    print("=" * 80)

    linha_blocos = ""
    linha_tempos = ""

    for i, (nome, inicio, fim) in enumerate(gantt):
        duracao = fim - inicio
        bloco = f" {nome} " * duracao
        linha_blocos += "|" + bloco

        if i == 0:
            linha_tempos += str(inicio)

        linha_tempos += " " * len(bloco) + str(fim)

    linha_blocos += "|"

    print(linha_blocos)
    print(linha_tempos)
    print("=" * 80)


def mostrar_execucao_passo_a_passo(gantt):
    print("\nSIMULAÇÃO PASSO A PASSO")
    print("=" * 80)

    tempo_final = gantt[-1][2]

    for t in range(tempo_final):
        executando = "OCIOSA"

        for nome, inicio, fim in gantt:
            if inicio <= t < fim:
                executando = nome
                break

        print(f"Tempo {t:>2}: CPU = {executando}")

    print("=" * 80)

def main():
    print("=" * 80)
    print("SIMULADOR INTERATIVO DE ESCALONAMENTO ROUND-ROBIN")
    print("=" * 80)

    n = int(input("Quantos processos deseja inserir? "))
    quantum = int(input("Qual o valor do Quantum? "))

    processos = []
    for i in range(n):
        pid = i
        print(f"\nProcesso {i + 1} (PID = {pid})")
        chegada = int(input("Tempo de chegada: "))
        tempo_cpu = int(input("Tempo de CPU: "))
        processos.append(Processo(pid, chegada, tempo_cpu))

    processos, gantt = escalonamento_round_robin(processos, quantum)

    mostrar_tabela(processos)
    mostrar_gantt(gantt)
    mostrar_execucao_passo_a_passo(gantt)

if __name__ == "__main__":
    main()