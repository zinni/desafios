"""
for n in range(1,101):
    x =+ n

"""

class PingPong(object):
    def imprime_saida(self, x):
        if (x % 3 == 0) and (x % 5 == 0):
            return 'ping pong'
        elif (x % 5 == 0):
            return 'pong'
        elif (x % 3 == 0):
            return 'ping'
        else:
            return x    

    def gerar_lista(self, ultimo_numero):
        output = []
        for x in range(1, ultimo_numero + 1):
            calculo = self.imprime_saida(x)
            output.append(calculo)
        return output

    def gerar_resultado(self):
        for x in self.gerar_lista(100):
            print x
      

if __name__ == '__main__':
    pp = PingPong()
    pp.gerar_resultado()
