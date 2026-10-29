
class BattleRobot:
    total_created = 0
    active_count = 0
    total_power = 0

    def __init__(self, name="Training Bot", power=100):
        if name == "":
            name = "Training Bot"
        if power <= 0:
            power = 100

        BattleRobot.total_created += 1
        self._id = BattleRobot.total_created
        self._name = name
        self._power = power
        self._active = True

        BattleRobot.active_count += 1
        BattleRobot.total_power += power

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_power(self):
        return self._power

    def is_active(self):
        return self._active

    def set_name(self, name):
        if name == "":
            print("Invalid name. Name cannot be empty.")
        else:
            self._name = name

    def set_power(self, power):
        if power <= 0:
            print("Invalid power. Power must be greater than 0.")
        else:
            if self._active:
                BattleRobot.total_power -= self._power
                BattleRobot.total_power += power
            self._power = power

    def upgrade(self, amount):
        if amount <= 0:
            print("Upgrade amount must be greater than 0.")
        elif not self._active:
            print(self._name, "cannot be upgraded because it is inactive.")
        else:
            self.set_power(self._power + amount)
            print(self._name, "was upgraded.")

    def deactivate(self):
        if self._active:
            self._active = False
            BattleRobot.active_count -= 1
            BattleRobot.total_power -= self._power
            print(self._name, "was deactivated.")
        else:
            print(self._name, "is already inactive.")

    def show_stats(self):
        print("ID:", self.get_id(), "| Name:", self.get_name(), "| Power:", self.get_power(), "| Active:", self.is_active())


def show_global_stats():
    print("Total Created:", BattleRobot.total_created)
    print("Active Robots:", BattleRobot.active_count)
    print("Total Power:", BattleRobot.total_power)


print("=== BATTLE ROBOT TEST SUITE ===")

print("\nPhase 1: Create Robots")
robot1 = BattleRobot()
robot2 = BattleRobot("Titan", 250)
robot3 = BattleRobot("Shadow", 180)
robot1.show_stats()
robot2.show_stats()
robot3.show_stats()
show_global_stats()

print("\nPhase 2: Invalid Changes")
robot2.set_power(-50)
robot2.set_name("")
robot2.show_stats()
show_global_stats()

print("\nPhase 3: Upgrade Robot")
robot2.upgrade(50)
robot2.show_stats()
show_global_stats()

print("\nPhase 4: Deactivate Robot")
robot3.deactivate()
robot3.show_stats()
show_global_stats()

print("\nPhase 5: Deactivate Again")
robot3.deactivate()
robot3.show_stats()
show_global_stats()

print("\n=== TEST SUITE COMPLETE ===")
