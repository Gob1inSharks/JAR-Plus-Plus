import pybullet as pybullet
import pybullet_data
import time 

BOT_PATH = "assets/Example-CADs/Simple-Six-Motor/Simple-Six-Motor.urdf"
#BOT_PATH = "r2d2.urdf"

physicsClient = pybullet.connect(pybullet.GUI)#or p.DIRECT for non-graphical version

pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

pybullet.setGravity(0,0,-10)
planeID = pybullet.loadURDF("plane.urdf")

botStartPos = [0,0,1]
botStartOrientation = pybullet.getQuaternionFromEuler([0,0,0])
botID = pybullet.loadURDF(BOT_PATH,botStartPos, botStartOrientation)

pybullet.setTimeStep(0.1) #THe lower this is, more accurate the simulation 
pybullet.setRealTimeSimulation(0)  # we want to be faster than real time :

position, orientation = pybullet.getBasePositionAndOrientation(botID)

print(position,orientation)

while True:
    position, orientation = pybullet.getBasePositionAndOrientation(botID)
    print(position,orientation)
    time.sleep(.1)

pybullet.disconnect()