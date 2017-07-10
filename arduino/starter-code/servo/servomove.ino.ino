#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);
  servoRight.attach(12);
}

void loop() {
  servoLeft.writeMicroseconds(1700); //left wheel, robot is going clockwise
  servoRight.writeMicroseconds(1500); //pause
  delay(500);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300); // right wheel, robot goes counter clockwise
  
}
