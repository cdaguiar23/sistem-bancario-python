# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python, com funcionalidades de depósito, saque, extrato, criação de usuários e contas correntes.

## Funcionalidades

### Operações Bancárias
- **Depósito**: Permite depositar valores positivos na conta.
- **Saque**: Permite sacar valores com limites diários e por transação.
- **Extrato**: Exibe o histórico de transações e saldo atual.

### Gestão de Usuários e Contas
- **Criar Usuário**: Cadastra um novo usuário com nome, data de nascimento, CPF e endereço. O CPF é armazenado apenas com números e não permite duplicatas.
- **Criar Conta Corrente**: Cria uma conta corrente vinculada a um usuário existente via CPF. Cada conta tem agência fixa "0001" e número sequencial.
- **Listar Contas**: Exibe todas as contas cadastradas com informações de agência, número da conta e nome do usuário.

## Estrutura do Código

O código é modularizado em funções com regras específicas de passagem de parâmetros:

- `depositar(saldo, valor, extrato, /)`: Recebe argumentos apenas por posição.
- `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`: Recebe argumentos apenas por nome (keyword-only).
- `extrato(saldo, /, *, extrato)`: Recebe saldo por posição e extrato por nome.
- `criar_usuario()`: Cadastra usuário com validação de CPF único.
- `criar_conta_corrente()`: Cria conta vinculada a usuário por CPF.
- `listar_contas()`: Lista todas as contas.

## Como Executar

1. Certifique-se de ter Python instalado (versão 3.x recomendada).
2. Execute o script `sistema_bancario.py`:
   ```
   python sistema_bancario.py
   ```
3. Siga as opções do menu interativo.

## Menu de Opções

- [d] Depositar
- [s] Sacar
- [e] Extrato
- [u] Criar Usuário
- [c] Criar Conta Corrente
- [l] Listar Contas
- [x] Sair

## Regras de Negócio

- Limite de saque: R$ 500,00 por transação.
- Limite de saques diários: 3 saques.
- Usuários são identificados por CPF (apenas números).
- Não é possível cadastrar usuários com CPF duplicado.
- Contas são sequenciais e vinculadas a usuários.
- Um usuário pode ter múltiplas contas.

## Estrutura de Dados

- `usuarios`: Lista de dicionários com informações dos usuários.
- `contas`: Lista de dicionários com informações das contas.

## Dependências

- Python 3.x
- Módulo `re` (para validação de CPF).
