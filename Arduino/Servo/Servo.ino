/*
 Working of a servo motor
*/
#include <Servo.h>
Servo serv_mot;  // create servo object to control a servo

void setup() 
{
  serv_mot.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() 
{
  serv_mot.write(30);                  // sets the servo position according to the scaled value
  delay(1000);                       // waits for the servo to get there (1 second)
  serv_mot.write(150);                  // sets the servo position according to the scaled value
  delay(1000);                       // waits for the servo to get there (1 second)
}
