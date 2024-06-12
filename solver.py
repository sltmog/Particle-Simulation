import numpy as np

class Solver:
    def __init__(self, particles):
        self.gravity = np.array([0, 5000])
        self.particles = particles

    def update(self, dt):
        sub_steps = 2
        sub_dt = dt/sub_steps
        for _ in range(sub_steps, 0, -1):
            self.applyGravity()
            self.applyConstraint()
            self.solveCollision()
            self.updatePositions(sub_dt)

    def updatePositions(self, dt):
        for particle in self.particles:
            particle.updatePosition(dt)
    
    def applyGravity(self):
        for particle in self.particles:
            particle.accelerate(self.gravity)

    def applyConstraint(self):
        position = np.array([400, 400])
        radius = 350
        for particle in self.particles:
            to_object = particle.position_current - position
            distance = np.linalg.norm(to_object)
            if distance > radius-particle.radius:
                n = to_object/distance
                particle.position_current = position + n*(radius-particle.radius)       

    def solveCollision(self):
        object_count = len(self.particles)
        for i in range(object_count):
            object1 = self.particles[i]
            for j in range(i+1, object_count):
                object2 = self.particles[j]
                collision_axis = object1.position_current - object2.position_current
                dist = np.linalg.norm(collision_axis)
                min_dist = object1.radius + object2.radius
                if dist < min_dist:
                    n = collision_axis/dist
                    delta = min_dist - dist
                    np.add(object1.position_current, n*delta/2, out=object1.position_current,  casting="unsafe")
                    np.add(object2.position_current, -n*delta/2, out = object2.position_current, casting="unsafe")