from funcoes import arquivo_existe, criar_arquivo, cadastrar

arq = 'dados.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

resp1 = str(input('Deseja cadastrar uma pessoa? [S/N] ')).strip().upper()[0]
while True:
    if resp1 in 'S':
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
        resp2 = str(input('Deseja continuar cadastrando pessoas? [S/N] ')).strip().upper()[0]
        if resp2 not in 'S':
            break
    else:
        break

resp3 = str(input('Deseja imprimir o conteúdo do arquivo? [S/N] ')).strip().upper()[0]
if resp3 in 'S':
    leitura = open(arq)
    for linha in leitura:
        dado = linha.split(';')
        dado[1] = int(dado[1].replace('\n', ''))
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    leitura.close()

resp4 = str(input('Deseja excluir uma pessoa? [S/N] ')).strip().upper()[0]
if resp4 in 'S':
    nome = str(input('Informe o nome da pessoa: '))
    leitura = open(arq, 'r')  # aqui eu abri o arquivo original para leitura
    linhas = leitura.readlines()  # aqui eu li e carreguei os dados do arquivo original em memória numa variável
    escrita = open(arq, 'w')  # aqui eu apago o arquivo original e crio um novo arquivo zerado com o mesmo nome do original
    for linha in linhas:  # aqui eu faço um 'for' da variável que contém o conteúdo do arquivo original
        if linha.find(nome) == -1:  # aqui eu olho cada linha - o 'find' faz a pesquisa na string que foi iteradada pelo for, linha por linha - o resultado é -1 quando ele não acha o que foi pesquisado
            escrita.write(linha)  # aqui, quando não achar, ele escreve aquela linha no novo arquivo criado - ou seja, a linha que contiver o nome pesquisado não será adicionada ao novo arquivo
    leitura.close()
    escrita.close()
