import re

def processar(mensagem):

    valor = re.search(r'\d+', mensagem)

    if valor:
        valor = float(valor.group())
    else:
        return None

    if "uber" in mensagem:
        categoria = "transporte"
    elif "pao" in mensagem or "pizza" in mensagem:
        categoria = "comida"
    else:
        categoria = "outros"

    descricao = mensagem

    return valor, descricao, categoria