import matplotlib.pyplot as plt
import random

dt = 0.1
steps = 200
target = 10.0
position = 0.0
velocity = 0.0
Kp = 2.0
Kd = 1.5

times = []
true_positions = []
measurements = []

for i in range(steps):
    error = target - position
    acceleration = Kp * error - Kd * velocity
    velocity += acceleration * dt
    position += velocity * dt
    times.append(i * dt)
    true_positions.append(position)
    measurement = position + random.gauss(0, 1)
    measurements.append(measurement)

plt.plot(times, true_positions, label='True Position')
plt.plot(times, measurements, label='sensor')
plt.legend()
plt.show()    