import random

class Jokenpo(object):

    def jogada(self, jogada1, jogada2):
        if jogada1 == jogada2:
            return 'empate'

        elif jogada1 == 'pedra' and jogada2 == 'papel':
            return 'papel_ganha'

        elif jogada1 == 'pedra' and jogada2 == 'tesoura':
            return 'pedra_ganha'

        elif jogada1 == 'papel' and jogada2 == 'pedra':
            return 'papel_ganha'

        elif jogada1 == 'papel' and jogada2 == 'tesoura':
            return 'tesoura_ganha'

        elif jogada1 == 'tesoura' and jogada2 == 'papel':
            return 'tesoura_ganha'

        elif jogada1 == 'tesoura' and jogada2 == 'pedra':
            return 'pedra_ganha'
