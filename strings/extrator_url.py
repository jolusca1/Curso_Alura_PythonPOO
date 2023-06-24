import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
        
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")
        
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)


        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
            
        return valor
                    
    def get_conversao_moeda(self):  
        moeda_origem = self.get_valor_parametro(parametro_busca='moedaOrigem')
        quantidade = int(self.get_valor_parametro(parametro_busca='quantidade'))
        
        if moeda_origem == 'dolar':
            valor =  quantidade * 5.5
        elif moeda_origem == 'real':
            valor = quantidade / 5.5
            
        return valor
        
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return "URL: " + self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL BASE: " + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

print(extrator_url.get_conversao_moeda())