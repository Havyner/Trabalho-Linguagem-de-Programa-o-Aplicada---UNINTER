# Havyner Jalles Siqueira RU: 5079616
# Importando a biblioteca
import pygame as pg
# Iniciando o pygame
pg.init()
# Abrindo uma janela
window = pg.display.set_mode(size = (600, 480))

# Mantendo a janela aberta
while True:
    # iniciando os eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # Fechar a janela
            quit() # Finalizando a pygame