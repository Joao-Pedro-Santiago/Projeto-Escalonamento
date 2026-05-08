from processo import Processo
from relatorios import mostrar_execucao_passo_a_passo, mostrar_gantt, mostrar_tabela
from Escalonador.rr_escalonador import escalonamento_round_robin
from Escalonador.sjf_escalonador import escalonamento_sjf


def main():
    print("=" * 80)
    print("SIMULADOR INTERATIVO DE ESCALONAMENTO ROUND-ROBIN")
    print("=" * 80)

    while True:
        tipo = input("Qual o tipo de escalonamento?(rr/sjf)")
        if tipo == "sjf" or tipo == "rr":
            break
            
    n = int(input("Quantos processos deseja inserir? "))
    if tipo == "rr":
        quantum = int(input("Qual o valor do Quantum? "))

    processos = []
    for i in range(n):
        pid = i
        print(f"\nProcesso {i + 1} (PID = {pid})")
        chegada = int(input("Tempo de chegada: "))
        tempo_cpu = int(input("Tempo de CPU: "))
        processos.append(Processo(pid, chegada, tempo_cpu))
    
    if tipo == "rr":
        processos, gantt = escalonamento_round_robin(processos, quantum)
    if tipo == "sjf":
        processos, gantt = escalonamento_sjf(processos)
    
    mostrar_tabela(processos)
    mostrar_gantt(gantt)
    mostrar_execucao_passo_a_passo(gantt)


if __name__ == "__main__":
    main()
