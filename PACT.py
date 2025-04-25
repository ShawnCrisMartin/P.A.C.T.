import random
import time

# Simulate data for 4 sensors, each with 3 axis (X, Y, Z)
def get_sensor_data():
    # Generate random values for X, Y, Z of each sensor
    sensor_data = {
        "shoulder_1": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        "shoulder_2": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        "neck": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        "back": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
    }
    return sensor_data

# Posture check function using X, Y, Z data
def check_posture(sensor_data):
    # Extract each sensor's data
    shoulder_1 = sensor_data["shoulder_1"]
    shoulder_2 = sensor_data["shoulder_2"]
    neck = sensor_data["neck"]
    back = sensor_data["back"]

    # Example condition for good posture:
    # - neck and back should be aligned within a range
    # - shoulders should be similarly aligned on X and Y axis
    if abs(shoulder_1[0] - shoulder_2[0]) < 2.0 and abs(shoulder_1[1] - shoulder_2[1]) < 2.0 and \
       abs(neck[2] - back[2]) < 2.0:
        return True
    else:
        return False

# Simulate Vibrator (Turn on or off based on posture)
def control_vibrator(posture_correct):
    if posture_correct:
        print("Vibrator OFF: Good Posture")
    else:
        print("Vibrator ON: Posture Needs Correction")

# Main loop
def main():
    while True:
        sensor_data = get_sensor_data()
        print("Sensor Data:", sensor_data)  # Print the sensor data to see the random values
        
        # Check posture and control vibrator
        posture_correct = check_posture(sensor_data)
        control_vibrator(posture_correct)
        
        time.sleep(2)  # Simulate a 2-second delay for next posture check

if __name__ == "__main__":
    main()
