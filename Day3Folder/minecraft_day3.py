# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

def Teleport():
    agent.teleport_to_player()


player.on_chat("come", Teleport)

def Moveforward(steps):
    agent.move(FORWARD,steps)


player.on_chat("front", Moveforward)

def Movebackwords(steps):
    agent.move(BACK,steps)

player.on_chat("Back", Movebackwords)


def Moveup(fly):
    agent.move(UP,fly)

player.on_chat("fly", Moveup)


def Movedown(descend):
    agent.move(DOWN,descend)

player.on_chat("down", Movedown)

def Turnleft():
    agent.turn(LEFT)

    
player.on_chat("left", Turnleft)


def turnright():
    agent.turn(RIGHT)

player.on_chat("right", turnright)



def movedsteps():
    agent.move(FORWARD,5)
    agent.turn(LEFT)
    agent.move(FORWARD,5)
    agent.turn(RIGHT)
    agent.move(FORWARD,4)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)

player.on_chat("complete course",movedsteps)

def chop(blocks):
    for i in range(blocks):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN,blocks)
    agent.collect_all()
    agent.teleport_to_player()
    agent.attack(FORWARD)

player.on_chat("collect",chop)


def mine(length):
    for i in range(length):    
        agent.destroy(DOWN)
        agent.destroy(FORWARD) 
        agent.destroy(LEFT)
        agent.destroy(UP)
        agent.collect_all()
        agent.move(FORWARD,1)
        agent.move(DOWN,1)
player.on_chat("mine", mine)






def buildwall(height,width):
    for j in range (width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP,1)
        agent.move(DOWN,height)
        agent.move(RIGHT,1)



    
player.on_chat("build",buildwall)



def buildroof(length,width):
    for a in range (width):
        for g in range(length):
            agent.place (UP)
            agent.move(FORWARD,1)
        agent.move(BACK,length)
        agent.move(LEFT,1)

player.on_chat("roof", buildroof)
    

