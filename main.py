from modulos import add_contato
from modulos import vizualizar_contato
from modulos import atualiza_contato
from modulos import marcar_favorito
from modulos import vizualizar_favoritos
from modulos import deleta_contato

contatos = []
while True:
    print('\nAGENDA TELEFONICA:'\
          '\n1 - ADICIONAR CONTATO'\
          '\n2 - VIZUALIZAR LISTA DE CADASTRADOS'\
          '\n3 - EDITAR CONTATO'\
          '\n4 - MARCAR COMO FAVORITO'\
          '\n5 - VER FAVORITOS'\
          '\n6 - APAGAR CONTATO'\
          '\n7 - SAIR')
    
    op = int(input('DIGITE A OPÇÃO: '))

    if op == 1:
        print(f'\nOPÇÃO {op} ADICIONAR CONTATO:')
        nome = input('DIGITE O NOME DO CONTATO: ')
        telefone = int(input('DIGITE O NUMERO: '))
        email = input('DIGITE O EMAIL: ')
        add_contato(contatos,nome,telefone,email)
    elif op == 2:
        print(f'\nOPÇÃO {op} LISTA DE CONTATOS:')
        vizualizar_contato(contatos)
    elif op == 3:
        print(f'OPÇÃO {op} ALTERAR CONTATO:')
        vizualizar_contato(contatos)
        indice_contato = int(input('DIGITE O INDICE DO CONTATO QUE DESEJA ATUALIZAR:'))
        novo_nome = input('DIGITE O NOME DO CONTATO: ')
        novo_telefone = int(input('DIGITE O NUMERO: '))
        novo_email = input('DIGITE O EMAIL: ')
        atualiza_contato(contatos,indice_contato,novo_nome,novo_telefone,novo_email)
    elif op == 4:
        print(f'OPÇÃO {op} FAVORITAR')
        vizualizar_contato(contatos)
        indice_contato = int(input('DIGITE O INDICE DO CONTATO QUE DESEJA ATUALIZAR:'))
        marcar_favorito(contatos,indice_contato,nome)
    elif op == 5:
        vizualizar_favoritos(contatos,indice_contato)
    elif op == 6:
        print(f'OPÇÃO {op} DELETAR CONTATO')
        vizualizar_contato(contatos)
        indice_contato = int(input('DIGITE O INDICE DO CONTATO QUE DESEJA DELETAR:'))
        deleta_contato(contatos, indice_contato)
    elif op == 7:
        print('FECHANDO AGENDA...')
        break