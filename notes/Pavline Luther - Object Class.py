class ball(object):
    def __init__(self, bounce, soft, size):
        self.bounce = bounce
        self.soft = soft
        self.size = size
        self.strength = 100

    def throw(self):
        if self.strength <= 0:
            print("You can't throw the ball it is broken")
            return
        if self.bounce >= .5:
            print("You threw the ball and it bounced when it hit the ground")
            self.strength -= 1
            return
        elif self.bounce < .5:
            print("You threw the ball and it started to roll when it hit the ground")
            self.strength -= .01
            return

    def catch(self):
        if self.strength <= 0:
            print("You can't can't the ball it is broken")
            return
        if self.size >= .7:
            print("The ball was easy to catch")
            return
        elif self.size >= .3:
            print("You caught the ball with out too much of a challenge")
            return
        else:
            print("You didn't even see the ball falling but it happened to land in your hands")
            return
    def kick(self, force):
        if self.strength <= 0:
            print("You can't kick the ball it is broken")
            return
        if self.soft >= .4:
            print("You kicked the ball")
            self.strength -= 1
            return
        else:
            print("You kicked the ball but it hurt your foot")
            self.strength -= .5
            return


red_rubber_ball = ball(.8, .5, .8)
red_rubber_ball.throw()
