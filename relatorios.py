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


def mostrar_execucao_passo_a_passo(gantt):
    print("\nSIMULACAO PASSO A PASSO")
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
