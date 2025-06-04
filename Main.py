import pygame
import sys
import random
from quadrado import Quadrado
from tela_inicio import TelaInicio

class Main:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)
        self.tempo_limite = 30_000  # 30 segundos
        self.pontuacao = 0
        self.quadrado = Quadrado(self.largura, self.altura)

    def mostrar_texto(self, texto, x, y):
        texto_surface = self.fonte.render(texto, True, (0, 0, 0))
        self.tela.blit(texto_surface, (x, y))

    def executar_jogo(self):
        inicio = pygame.time.get_ticks()
        rodando = True

        while rodando:
            self.tela.fill((255, 255, 255))
            tempo_restante = max(0, (self.tempo_limite - (pygame.time.get_ticks() - inicio)) // 1000)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if self.quadrado.foi_clicado(evento.pos):
                        self.pontuacao += 1
                        self.quadrado.cor = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                        if self.pontuacao % 5 == 0 and self.quadrado.tamanho > 20:
                            self.quadrado.tamanho -= 5
                        self.quadrado.mover()

            self.quadrado.desenhar(self.tela)
            self.mostrar_texto(f"Pontos: {self.pontuacao}", 10, 10)
            self.mostrar_texto(f"Tempo: {tempo_restante}s", 10, 50)

            if tempo_restante <= 0:
                self.mostrar_texto("FIM DE JOGO!", self.largura // 2 - 100, self.altura // 2 - 30)
                self.mostrar_texto(f"Pontuação: {self.pontuacao}", self.largura // 2 - 100, self.altura // 2 + 20)
                pygame.display.update()
                pygame.time.wait(3000)
                rodando = False

            pygame.display.update()
            self.relogio.tick(60)

    def executar(self):
        tela_inicio = TelaInicio(self.largura, self.altura)
        if tela_inicio.mostrar():  # Mostra a tela de início e espera o clique em "Jogar"
            self.executar_jogo()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Main()
    jogo.executar()