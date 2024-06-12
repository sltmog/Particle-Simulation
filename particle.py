import numpy as np

class Particle:
    def __init__(self, x, y, color='white'):
        self.position_current = np.array([x,y])
        self.position_old = np.array([x,y])
        self.acceleration = np.array([0,0])
        self.radius = 10
        self.color = color

    def updatePosition(self, dt):
        velocity = self.position_current - self.position_old
        # save current position
        self.position_old = self.position_current
        # performe verlet integration
        self.position_current = self.position_current + velocity + 0.5*self.acceleration*dt*dt
        # reset acceleration
        self.acceleration = np.array([0,0])

    def accelerate(self, acc):
        self.acceleration += acc