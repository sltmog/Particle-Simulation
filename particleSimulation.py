import pygame
import numpy as np
from particle import Particle
from solver import Solver
import random

pygame.init()

HEIGHT = 800
WIDTH = 800
FPS = 60

clock = pygame.time.Clock()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

particles = [Particle(200, 400)]
solver = Solver(particles)

balls = True

running = True
while running:
    screen.fill('grey')
    pygame.draw.circle(screen, 'black', (400, 400), 350)
    
    for particle in solver.particles:           
        pygame.draw.circle(screen, particle.color, particle.position_current, particle.radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls = False if balls else True

    if balls:
        solver.particles.append(Particle(200, 400, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
    
    num_particles = len(solver.particles)
    text = f"Number of particles: {num_particles}"
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, 'white')
    screen.blit(text_surface, (10, 10))

    solver.update(1/FPS)
    pygame.display.update()
    clock.tick(FPS)

