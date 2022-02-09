import os

def formata_tamanho(tamanho):
    base = 1024
    kilo  = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

def procura_caminho():
    caminho_procura = input('Digite o caminho: ')
    termo_procura = input('Digite um termo: ')
    conta = 0
    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if termo_procura in arquivo:
                try:
                    conta += 1
                    caminho_completo = os.path.join(raiz,arquivo)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    tamanho = os.path.getsize(caminho_completo)
                    
                    print()
                    print('Encontrei o arquivo: ', arquivo)
                    print('Caminho: ', caminho_completo)
                    print('Nome: ', nome_arquivo)
                    print('Extensão: ', ext_arquivo)
                    print('Tamanho formatado:', formata_tamanho(tamanho))
                except PermissionError as e:
                    print('Sem permissões.')
                except FileNotFoundError as e:
                    print('Arquivo não encontrado.')
                except Exception as e:
                    print('Erro desconhecido', e)

    print()
    print(f'{conta} arquivo(s) encontrado')
    
    if conta == 0:
        print('Verifique se o caminho ou termo foi digitado corretamente')
    
    conta = 0
    print()

procura_caminho()
    
while True:
    print('Deseja continuar usando o programa? [s] sim ou [n] não? ')
    resposta = input()
    resposta = resposta.lower()

    if resposta == 'n':
        break
    elif resposta == 's':
        procura_caminho()
    else:
        print('DIGITE APENAS s OU n')
        print()
        continue   