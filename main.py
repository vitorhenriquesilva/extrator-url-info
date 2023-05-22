url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = " "

#Sanitização da URL
#Também é possível utilizar o .strip, .rstrip e .lstrip para remoção de \t, \n e etc.
url = url.replace(" ", "")

#Retornando uma exceção para o usuário
#if url == "":
#    raise ValueError("A URL informada está vazia")

#print(url)

#Fatiando a URL de modo estático4
#url_base = url[0:19]
#print(url_base)

#url_parametros = url[20:36]
#print(url_parametros)

#Fatiando a URL de modo dinâmico
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#Buscando o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

if url.endswith("/cambio"):
    print("entrou no if")
else:
    print("else")