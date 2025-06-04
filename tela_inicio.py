import pygame

class TelaInicio:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        self.fonte = pygame.font.SysFont(None, 48)
        self.fonte_botao = pygame.font.SysFont(None, 36)
        self.cor_botao = (0, 200, 0)
        self.cor_texto = (255, 255, 255)
        self.botao_rect = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)

    def mostrar(self):
        rodando = True
        while rodando:
            self.tela.fill((240, 240, 240))
            
            # Título
            titulo = self.fonte.render("Caça ao Quadrado", True, (0, 0, 0))
            self.tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, self.altura // 2 - 100))
            
            # Botão "Jogar"
            pygame.draw.rect(self.tela, self.cor_botao, self.botao_rect, border_radius=10)
            texto_botao = self.fonte_botao.render("Jogar", True, self.cor_texto)
            self.tela.blit(texto_botao, (self.botao_rect.x + 70, self.botao_rect.y + 15))
            
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao_rect.collidepoint(evento.pos):
                        return True  # Inicia o jogo

        return False