import pygame
import math
import sys
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cañón Animado')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, tiempo):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)
        self.velocidad_inicial = 330  # 330 metros por segundo
        self.tiempo = tiempo
        self.distance = self.velocidad_inicial * self.tiempo
        self.velocidad = self.velocidad_inicial / self.tiempo

    def update(self):
        self.rect.x += self.velocidad_inicial * self.tiempo * math.cos(self.angle)
        self.rect.y -= self.velocidad_inicial * self.tiempo * math.sin(self.angle)


def main():
    num_balas = 1000
    balas = pygame.sprite.Group()
    clock = pygame.time.Clock()
    restart_time = 5000  # 5000 ms = 5 seconds
    elapsed_time = 0

    mediciones = []  # Lista para almacenar mediciones de cada bala

    for _ in range(num_balas):
        x, y = random.randint(50, 750), height
        angle = random.uniform(30, 60) if random.random() < 0.5 else random.uniform(120, 150)
        tiempo = random.uniform(0.1, 2.0)  # Tiempo entre 0.1 y 2.0 segundos
        balas.add(Bala(x, y, angle, tiempo))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(BLACK)

        balas.update()
        balas.draw(window)

        elapsed_time += clock.get_rawtime()
        pygame.display.flip()
        clock.tick(60)

        if elapsed_time >= restart_time:
            print("Mediciones:")
            for idx, bala in enumerate(balas):
                medicion = {
                    "Bala": idx + 1,
                    "Distancia recorrida": bala.distance,
                    "Velocidad": bala.velocidad,
                    "Ángulo": math.degrees(bala.angle),
                    "Tiempo": bala.tiempo
                }
                mediciones.append(medicion)
                print(medicion)

            pygame.time.wait(2000)  # Pause for 2 seconds before restart
            balas.empty()
            for _ in range(num_balas):
                x, y = random.randint(50, 750), height
                angle = random.uniform(30, 60) if random.random() < 0.5 else random.uniform(120, 150)
                tiempo = random.uniform(0.1, 2.0)
                balas.add(Bala(x, y, angle, tiempo))

            elapsed_time = 0


if __name__ == "__main__":
    main()