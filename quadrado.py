import pygame
import random

class Quadrado:
    def __init__(self, largura, altura, cor=(255, 0, 0)):
        self.tamanho = 60
        self.largura_tela = largura
        self.altura_tela = altura
        self.cor = cor
        self.x = random.randint(0, largura - self.tamanho)
        self.y = random.randint(0, altura - self.tamanho)

    def mover(self):
        self.x = random.randint(0, self.largura_tela - self.tamanho)
        self.y = random.randint(0, self.altura_tela - self.tamanho)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.tamanho, self.tamanho))

    def foi_clicado(self, pos_mouse):
        x, y = pos_mouse
        return (self.x <= x <= self.x + self.tamanho) and (self.y <= y <= self.y + self.tamanho)