# Simulador de Escalonamento de Processos

Um simulador interativo de algoritmos de escalonamento de processos em sistemas operacionais, implementando os algoritmos **Round-Robin (RR)** e **Shortest Job First (SJF)**.

## 📋 Descrição

Este projeto simula o comportamento de diferentes algoritmos de escalonamento de CPU, permitindo comparar o desempenho e compreender como cada algoritmo gerencia a execução de múltiplos processos. O simulador fornece visualizações detalhadas através de tabelas de resultados, gráficos de Gantt e simulação passo a passo da execução.

## 🎯 Funcionalidades

- **Escalonamento Round-Robin (RR)**: Algoritmo preemptivo com quantum configurável
- **Escalonamento SJF**: Algoritmo não-preemptivo que executa o processo com menor tempo de CPU primeiro
- **Cálculo de métricas**: Tempo de espera, turnaround e outros indicadores de desempenho
- **Visualização interativa**:
  - Tabela com resultados de cada processo
  - Gráfico de Gantt para visualizar a sequência de execução
  - Simulação passo a passo mostrando o estado da CPU em cada unidade de tempo

## 📁 Estrutura do Projeto

```
Projeto-Escalonamento/
├── main.py                 # Interface principal interativa
├── processo.py             # Classe Processo com atributos de escalonamento
├── relatorios.py          # Funções para visualização dos resultados
├── README.md              # Este arquivo
└── Escalonador/
    ├── rr_escalonador.py  # Implementação do algoritmo Round-Robin
    └── sjf_escalonador.py # Implementação do algoritmo SJF
```

## 🚀 Como Usar

### Requisitos
- Python 3.6 ou superior
- Nenhuma dependência externa

### Executar o Simulador

```bash
python main.py
```

### Passos de Interação

1. **Escolha o algoritmo**: Digite `rr` para Round-Robin ou `sjf` para SJF
2. **Defina a quantidade de processos**: Insira um número inteiro
3. **Se Round-Robin**: Informe o valor do quantum (fatia de tempo)
4. **Para cada processo**, forneca:
   - **Tempo de chegada**: Quando o processo chega na fila
   - **Tempo de CPU**: Quanto tempo o processo precisa ser executado

### Exemplo de Execução

```
================================================================================
SIMULADOR INTERATIVO DE ESCALONAMENTO ROUND-ROBIN
================================================================================
Qual o tipo de escalonamento?(rr/sjf) rr
Quantos processos deseja inserir? 3
Qual o valor do Quantum? 2

Processo 1 (PID = 0)
Tempo de chegada: 0
Tempo de CPU: 4

Processo 2 (PID = 1)
Tempo de chegada: 1
Tempo de CPU: 3

Processo 3 (PID = 2)
Tempo de chegada: 2
Tempo de CPU: 2
```

## 📊 Saídas

O simulador gera três visualizações:

### 1. Tabela de Resultados
Exibe para cada processo:
- **PID**: Identificador do processo
- **Chegada**: Tempo de chegada
- **Tempo CPU**: Tempo total necessário
- **Início**: Quando iniciou a execução
- **Fim**: Quando finalizou
- **Espera**: Tempo total aguardando na fila
- **Turnaround**: Tempo total desde chegada até fim

Também mostra as **médias de espera e turnaround** para comparação.

### 2. Gráfico de Gantt
Visualização ASCII que mostra:
- Sequência de execução dos processos
- Períodos de CPU ociosa (OCIOSO)
- Duração de cada execução

### 3. Simulação Passo a Passo
Lista o estado da CPU em cada unidade de tempo, mostrando qual processo está executando ou se está ociosa.

## 🔧 Componentes Principais

### `processo.py`
Define a classe `Processo` que armazena:
- `pid`: Identificador único do processo
- `chegada`: Tempo de chegada na fila
- `tempo_cpu`: Tempo necessário de CPU
- `tempo_restante`: Tempo ainda a ser executado
- `inicio`: Tempo quando iniciou
- `fim`: Tempo quando terminou
- `espera`: Tempo em espera
- `turnaround`: Tempo total no sistema

### `rr_escalonador.py`
Implementa o algoritmo **Round-Robin**:
- Processa cada processo por no máximo `quantum` unidades de tempo
- Se o processo não terminar, volta para o final da fila
- Processa todos os processos em rotação até que todos terminem

### `sjf_escalonador.py`
Implementa o algoritmo **Shortest Job First**:
- Seleciona sempre o processo com menor tempo de CPU restante
- Não é preemptivo (não interrompe o processo em execução)
- Reduz o tempo médio de espera em comparação ao FIFO

### `relatorios.py`
Funções de visualização:
- `mostrar_tabela()`: Exibe resultados em formato tabular
- `mostrar_gantt()`: Desenha o gráfico de Gantt
- `mostrar_execucao_passo_a_passo()`: Mostra a execução em tempo

## 💡 Conceitos de Escalonamento

### Round-Robin (RR)
- **Preemptivo**: Processo pode ser interrompido
- **Justo**: Todos os processos recebem fatia igual de tempo
- **Quantum**: Fatia de tempo máxima por execução
- **Ideal para**: Sistemas time-sharing

### Shortest Job First (SJF)
- **Não-preemptivo**: Processo não é interrompido
- **Eficiente**: Minimiza tempo médio de espera
- **Problema**: Pode criar inanição para processos longos
- **Ideal para**: Processamento em batch

## 📈 Análise de Desempenho

O simulador permite comparar os dois algoritmos através de:
- **Tempo médio de espera**: Quanto menor, melhor
- **Turnaround médio**: Tempo total no sistema
- **Utilização de CPU**: Percentual de tempo ocupado vs. ocioso

## ✅ Exemplo de Caso de Uso

Comparar qual algoritmo é mais eficiente para um conjunto específico de processos:
1. Execute a simulação com Round-Robin (teste com diferentes quantums)
2. Execute a mesma entrada com SJF
3. Compare as médias de espera e turnaround
4. Analise o gráfico de Gantt para entender o comportamento

## 📝 Notas

- Os processos são identificados por PID numéricos iniciados em 0
- O simulador assume que o sistema tem apenas uma CPU
- As unidades de tempo são abstratas (podem representar milissegundos, segundos, etc.)
- Não há tratamento de prioridades ou I/O operations

## 🎓 Fins Educacionais

Este projeto foi desenvolvido como material educacional para entender:
- Algoritmos de escalonamento de CPU
- Estruturas de dados (filas)
- Análise de desempenho de algoritmos
- Simulação de sistemas operacionais