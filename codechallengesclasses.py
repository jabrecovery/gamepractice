'''Setting up the robot'''
class DriveBot:
    all_disabled = False
    latitude = -999999
    longtitude = -999999
    robot_counter = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_counter += 1
        self.id = DriveBot.robot_counter

        

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range



robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10
robot_2 = DriveBot(35, 75, 25)
DriveBot.all_disabled = False
DriveBot.latitude = 50.0
DriveBot.longtitude = 50.0
print(robot_2.sensor_range)
print(robot_1.id)