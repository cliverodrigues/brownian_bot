import pygame
from brownian_bot import Simulation, Arena, Robot

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    arena = Arena(500, 500)
    robot = Robot(250, 250)
    sim = Simulation(robot, arena)

    path = []

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds per frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sim.step(dt)
        path.append((int(robot.x), int(robot.y)))

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 500), 2)
        for p in path:
            pygame.draw.circle(screen, (200, 200, 200), p, 1)
        pygame.draw.circle(screen, (255, 0, 0), (int(robot.x), int(robot.y)), int(robot.radius))
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
