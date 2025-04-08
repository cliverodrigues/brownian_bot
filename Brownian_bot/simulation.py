import time

class Simulation:
    def __init__(self, robot, arena):
        self.robot = robot
        self.arena = arena

    def step(self, dt):
        self.robot.update(dt)
        self.robot.check_collision(self.arena)

    def run(self, duration, timestep=0.05):
        steps = int(duration / timestep)
        for _ in range(steps):
            self.step(timestep)
            time.sleep(timestep)
