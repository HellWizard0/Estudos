import pprint

# Lista de usuários com status ativo ou inativo
usuarios = [
    {"id": 1, "nome": "Carlos", "ativo": True},
    {"id": 2, "nome": "Ana", "ativo": False},
    {"id": 3, "nome": "João", "ativo": True},
    {"id": 4, "nome": "Lucas", "ativo": True},
    {"id": 5, "nome": "Mariana", "ativo": False},
    {"id": 6, "nome": "Fernanda", "ativo": True},
    {"id": 7, "nome": "Bruno", "ativo": False},
]

# IDs dos usuários que queremos ativar
ids_para_ativar = [1, 2, 5, 6, 10]


def ativar_usuarios(usuarios: list[dict], ids_para_ativar: list[int]) -> list[dict]:
    """
    Ativa os usuários cujos IDs estão na lista `ids_para_ativar`.

    Para cada usuário da lista original que está com `ativo=False` e que possui
    o ID na lista de ativação, cria uma cópia do dicionário do usuário,
    define o campo 'ativo' como True e adiciona à nova lista de retorno.

    A função não altera a lista original de usuários.

    Args:
        usuarios (list[dict]): Lista de usuários
        com campos 'id', 'nome' e 'ativo'.
        ids_para_ativar (list[int]): Lista de IDs
        dos usuários que devem ser ativados.

    Returns:
        list[dict]: Nova lista contendo cópias dos usuários ativados.
    """
    # Conversão da lista para set para melhorar
    # performance de busca (de O(n) para O(1))
    ids_ativos_set = set(ids_para_ativar)

    nova_lista = []
    for usuario in usuarios:
        # Verifica se o ID está na lista e se o usuário ainda está inativo
        if usuario["id"] in ids_ativos_set and not usuario["ativo"]:
            usuario_copia = usuario.copy()
            usuario_copia["ativo"] = True
            nova_lista.append(usuario_copia)

    return nova_lista


# Resultado da função
pprint.pprint(ativar_usuarios(usuarios, ids_para_ativar))

print("\n---\n")
""
# Verificação de que a lista original permanece inalterada
pprint.pprint(usuarios)

# MELHORIA EXPLICADA:
# Na versão anterior, era usada uma lista
#  para verificar se o ID estava presente,
# o que resultava em complexidade O(N*M),
#  onde N é o número de usuários e M o número de IDs.
# Ao usar um `set`, a verificação `id in set`
#  passa a ser O(1), resultando em O(N + M) no total.
# Isso reduz drasticamente o tempo de execução
# quando lidamos com grandes volumes de dados.
# FUNCIONANDO COMMIT?
