# FUNÇÃO CERTA DE SOMAR ITENS DE UMA LISTA
def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

# FUNÇÃO ERRADA DE SOMAR ITENS DE UMA LISTA
def soma2(lista):
    for e in lista:
        e += e
    return e
# não soma todos os itens da lista
# vai somar o valor atual do for e dobrar ele. sobrescreve com o proximo item da lista
# dobra ele e por fim vai retornar o ultimo item da lista dobrado

lista = [100, 250, 390]
soma1 = soma2(lista)
print(soma1)

soma2 = soma2([900, 900])
print(soma2)





