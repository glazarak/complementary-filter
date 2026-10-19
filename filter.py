import matplotlib.pyplot as plt
import random

dt = 0.1
steps = 200
target = 10.0
position = 0.0
velocity = 0.0
Kp = 2.0
Kd = 1.5
velocity_error = 0.1
a = 0.9

times = []
true_positions = []
measurements = []
estimate = 0.0
predictions = []

for i in range(steps):
    error = target - position
    acceleration = Kp * error - Kd * velocity
    velocity += acceleration * dt
    position += velocity * dt
    times.append(i * dt)
    true_positions.append(position)
    measurement = position + random.gauss(0, 1)
    measurements.append(measurement)
    sensed_velocity = velocity + velocity_error
    prediction = estimate + sensed_velocity * dt
    estimate = a * prediction + (1 - a) * measurement
    predictions.append(prediction)


plt.plot(times, true_positions, label='True Position')
plt.plot(times, measurements, label='Sensor')
plt.plot(times, predictions, label='Physics Prediction')
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.title("Complementary filter, a = 0.9")
plt.legend()
plt.savefig("plot.png")
plt.show()    