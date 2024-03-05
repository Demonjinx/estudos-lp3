 # Tipos de dados


#1. numerico
* int, float, complex


#int

idade = 17
temperatura = -20

#float

altura =1.72


#2.Bool

verdade = True
mentira = False

#3.String sequencia de caracteres escolha uma delas e segue
nome = 'Thomas Stephan'
nome = "Thomas Stephan"

#multilinhas

frase = """
Salve mundao 123
palmeiras
sem mundial
"""

#interpolação de string
#f-strings para por entre {}
nome = "Rony"
idade = 39
frase = f"Olá {nome}. Você tem {idade} anos!"
print(frase)

#Char

letra = 'a'


#Acesso um caractere para String
nome = 'Thomas CArmo'
print(nome[0])
print(nome[5])

#4. List(listas)
#lista de valores

habilidades = []
habilidades = [ "python", "html", "java" ]

#acessar um item da lista
habilidades[1]

#add um item da lista
habilidades.append('c#') # python, html, java, c#

#inserir em uma posição
habilidades.insert(2,"css")
print (habilidades)

#habilidades.clear()
#print (habilidades)

for habilidade in habilidades:
    print(habilidade)
'''
def somar(n1,n2):
    return n1+n2
somar(10.0, n2=2.0)
somar(n2=10.0, n1=2.0)
'''

#5. Tuple (tupla)
#'lista' de valores
# não pode ser alterada
#inves de usar chaves como na lista, aqui vc usa o parenteses para não mudar
opcoes = ('sim', 'nao','talvez')
print(opcoes[2])

#set (conjunto de valores)
# ñ permite elementos duplicados
# ñ é indexado
habilidades = { "python", "html", "java", "java" }
print(habilidades)


#6. dict(dicionario)
# palavras -> definição
# Key -> value (chave -> valor); conjunto de chave e valor

nome = 'Leticia'
idade = 17
habilidades = ["python", "html", "java"]
empregado = True

candidato = {
    'nome': 'Leticia',
    'idade':'17',
    'habilidade':["python", "html", "java"],
    'empregado': True
}
print(candidato["nome"])
print(candidato.keys())
print(candidato.values())

#7. None (nulo)

nome = None
