class ClockTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minute = minutes
        self.seconds = seconds

    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self, seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minute = minutes
        self.seconds = seconds

    def showTime(self):
        print("The time you have set is {0}:{1}:{2}".format(self.hours, self.minutes, self.seconds))

# initialize clock
userClock = ClockTime(0, 0, 0)

# loop until user wants to quit
while True:
    # prompt user to input hours
    hours = int(input("Input the hour you want to set it to: "))
    # if hours > 24
    if hours > 24:
        print("You cannot set hours greater than 24")
    else:
        # set hour if it is < 24
        userClock.setHours(hours)
        # prompt user to input minutes
        minutes = int(input("Input the minutes you want to set it to: "))
        # if minutes > 60
        if minutes > 60:
            print("You cannot set minutes greater than 60")
        else:
            # set minutes if it is < 60
            userClock.setMinutes(minutes)
            # prompt user to input seconds
            seconds = int(input("Input the seconds you want to set it to: "))
            # if seconds > 60
            if seconds > 60:
                print("You cannot set seconds greater than 60")
            else:
                # set seconds if it is < 60
                userClock.setSeconds(seconds)
                # show time
                userClock.showTime()
    # ask if user wants to continue
    option = input("Do you want to set a new time? press any to continue or q to quit: ")
    # break the loop if input q
    if option == 'q':
        break