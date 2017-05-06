from components import Report, Servo, Hand
import time

class Robot:
    def __init__(self):
        report = Report()
        self.servo = Servo(report)

        config = {
            'report': report,
            'servo': self.servo,
        }

        self.hand = Hand(config)


    def sleep(self):
        self.hand.close()
        self.servo.move_servo_to_percent(0,50)
        self.servo.move_servo_to_percent(1,30)
        self.servo.move_servo_to_percent(2,0)
        self.servo.move_servo_to_percent(3,35)
        self.servo.move_servo_to_percent(4,50)
        for i in range(5):
            self.servo.sleep(i)
            time.sleep(1)
