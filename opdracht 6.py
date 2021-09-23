from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

for i in range(7):
    robotArm.moveRight()
for i in range(1):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()