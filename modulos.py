def add_contato(contatos,nome,telefone,email,):
    contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "favorito":False,
    "deletado":False
    }
    contatos.append(contato)
    print(f'CONTATO:{nome} ADICIONADO COM SUCESSO!')
    return

def vizualizar_contato(contatos):
    print('LISTA DE CONTATOS:')
    for indice, contato in enumerate(contatos,start=1):
        favorito = '★' if contato['favorito'] else ''
        nome_contato = contato['nome']
        numero_contato = contato['telefone']
        email = contato['email']
        print(f'\n{indice}.CONTATO - [{favorito}]FAVORITO\
              \nNOME:{nome_contato}\
              \nTELEFONE:{numero_contato}\
              \nEMAIL:{email}')
    return

def atualiza_contato(contatos,indice_contato,novo_nome,novo_telefone,novo_email):
    indice_contatos = indice_contato - 1
    if indice_contatos >= 0 and indice_contatos < len(contatos):
        contatos[indice_contatos]['nome'] = novo_nome
        contatos[indice_contatos]['telefone'] = novo_telefone
        contatos[indice_contatos]['email'] = novo_email
        print(f'CONTATO:{indice_contato} ATUALZIADO:\
              \nNOME:{novo_nome}\
              \nTELEFONE:{novo_telefone}\
              \nEMAIL:{novo_email}')
    else:
        print('INDICE DE CONTATO INVALIDO')
    return

def marcar_favorito(contatos, indice_contato,nome):
    indice_contatos = indice_contato - 1
    contatos[indice_contatos]['favorito'] = True
    print(f'CONTATO:{indice_contato} ADICIONADO AOS FAVORITOS')
    return

def vizualizar_favoritos(contatos,indice_contato):
    indice_contatos = indice_contato - 1
    favorito = contatos[indice_contatos]['favorito'] = True
    for indice, contato in enumerate(contatos,start=1):
        if indice:
            favorito = '★' 
            nome_contato = contato['nome']
            numero_contato = contato['telefone']
            email = contato['email']
            print(f'\n{indice}.CONTATO - [{favorito}]FAVORITO\
                \nNOME:{nome_contato}\
                \nTELEFONE:{numero_contato}\
                \nEMAIL:{email}')
    return

def deleta_contato(contatos,indice_contato):
    indice_contatos = indice_contato - 1
    remover =contatos[indice_contatos]['deletado'] = True
    for contato in contatos:
        if remover:
            contatos.remove(contato)
    print(f'CONTATO:{indice_contato} REMOVIDO COM SUCESSO')
    return
