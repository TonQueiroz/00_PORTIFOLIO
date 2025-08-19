''' Codigo bruto de  busca em lista '''


def buscaLista(k,L,n):
    il = 0
    indicel=-1

    while il<n:
        if L[il]==k:

            indicel=il

            il=n+1
        il=il+1
    return indicel


nomes =['Arthur', 'Joao', 'Maria', 'Ana']
i = buscaLista ('Ana', nomes, len(nomes))
print ('A busca desejada esta no indice', i)
print (nomes[i])


#Codigo simples de  busca em lista

nomes =['Arthur', 'Joao', 'Maria', 'Ana']
i=nomes.index('Joao')

print('A busca desejada esta no indice',i)
print (nomes[i])
