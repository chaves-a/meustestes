def criar_arquivo(nome):
    a = open(nome, 'wt+')
    a.close()


def cadastrar(arq, nome, idade):
    a = open(arq, 'at')
    a.write(f'{nome};{idade}\n')
    a.close()


def arquivo_existe(nome):
    try:
        open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True
