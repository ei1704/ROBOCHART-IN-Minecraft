import mcpi.minecraft as minecraft
from time import sleep

def main():

    mc = minecraft.Minecraft.create()
    mc.postToChat("Hello")

    #mc.setBlocks(-100,1,-100,100,100,100,0)
    #mc.setBlocks(-100,0,-100,100,0,100,2)
    #mc.player.setPos(0,10,0)

    x=0
    z=0
    mc.setBlock(x,0,z,35,14)

    for i in range(10):
        mc.setBlock(x,0,z,2)
        x+=1
        mc.setBlock(x,0,z,35,14)
        sleep(1)

if __name__ == "__main__":
        main()
