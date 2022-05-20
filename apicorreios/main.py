#Requer a biblioteca requests: py -m pip install requests
import requests

def main():
    codigo = input("Informe o código do objeto: ")
    dados = {}
    r = requests.get("https://proxyapp.correios.com.br/v1/sro-rastro/"+codigo)
    dados = r.json()
    for x in dados['objetos'][0]['eventos']:
        try:
            print(x['dtHrCriado']+" > "+ x['descricao'] + '->' + x['unidade']['endereco']['cidade'])
        except:
            print(x['dtHrCriado']+" > "+ x['descricao'])
    
if __name__ == '__main__':
    main()
