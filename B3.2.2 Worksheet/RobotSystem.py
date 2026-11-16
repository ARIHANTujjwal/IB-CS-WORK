class RobotPart:
    def __init__(self, name):
        self.name = name

    def activate(self):
        print(self.name + " is activating.")


class Motor(RobotPart):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0

    def activate(self, speed=50):
        self.speed = speed
        print(self.name + " is spinning at " + str(self.speed) + "% speed.")


class Camera(RobotPart):
    def activate(self):
        print(self.name + " is taking a picture.")


class RobotSystem:
    def run(self):
        motor = Motor("Drive motor")
        camera = Camera("Robot camera")

        parts: list[RobotPart] = [motor, camera]

        print("Activating robot parts:")
        for part in parts:
            part.activate()

        print()
        print("Activating motor at a different speed:")
        motor.activate(80)


system = RobotSystem()
system.run()