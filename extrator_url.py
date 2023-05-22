import re
class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitizar_url(url)
        self.validar_url()

    #Método especial que precisa ser implementado, caso eu queira saber o tamanho do meu objeto
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parametros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    #O parametro "other" seria o objeto que está a direita.
    #Ex: extrator_url == extrator_url_2
    #extrator_url_2 é o valor recebido como parâmetro no método __eq__
    def __eq__(self, other):
        return self.url == other.url

    def sanitizar_url(self, url):
        #Verificando se o valor da minha variável é igual a uma string
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validar_url(self):
        #Quando não existir uma url...
        if not self.url:
            #Exibindo uma exceção
            raise ValueError("A URL está vazia")

        # Os parenteses servem para pesquisar pelo valor exato que está dentro dele
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        #.search para procurar se existe o valor dentro de uma string
        #.match utlizado para verificar se a string inteira bate com o padrão desejado
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        # Fatiando a URL de modo dinâmico
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        # Buscando o valor de um parâmetro
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)
#extrator_url2 = ExtratorURL(url)

#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)
#print("O tamanho da URL é: ", len(extrator_url))

#O valor retornado abaixo é "False" pois está sendo comparado o armazenamento em memória
# e não o valor do objeto, portanto é necessário reescrever o método "__eq__"
#print(extrator_url == extrator_url2)

#O método id() serve para verificar qual é o endereço de memória de um objeto
#print(id(extrator_url))

VALOR_DOLAR = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
print("Moeda de origem: " + moeda_origem)
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
print("Moeda de destino: " + moeda_destino)
quantidade = extrator_url.get_valor_parametro("quantidade")
print("Quantidade   " + quantidade)

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str("%.2f" % valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str("%.2f" % valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")