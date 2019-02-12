class Phone(object):
    def__init__(self, carrier, charge_left):
    # There are attributes that a phone has.
    # There should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

            def make_call(self, duration):
                if not self.screen:
                    print("You can't make a phone call.")
                    print("Your screen is broke")
                    return
            battery_loss_per_minute = 5
            if self.battery_left <= 0:
                print("You can't. The phone is dead")
                return
            self.battery_left -= duration *  battery_loss_per_minute
            if self self.battery_left < 0:
                self. battery_left = 0
                print("You can't. The phone is dead")
                return
            elif self.battery_left == 0:
                print("Your phone dies at the end of the conversation")
            else:
                print("You successfully make the phonecall.")
                print("Your phone isnow at %s" % self.battery_left)

my_phone = Phone("ATT", 100)
your_phone = Phone("bell", 0)