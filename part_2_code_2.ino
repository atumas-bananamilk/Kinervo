#include <Servo.h>
   
Servo servo;
   
void setup() {
   Serial.begin(9600);
   servo.attach(13);
}
   
void loop() {
   if (Serial.available() > 0)
   {
      float receivedFloat = Serial.parseFloat();           // Receiving a float from the Kinect (5 digit X coordinate).
      if (receivedFloat > -0.8 && receivedFloat < 0.8)     // If coordinate is in required range.
      {
         receivedFloat = receivedFloat*100+80;             // Convert it to degrees.
         int servoDegrees = 180 - (int)receivedFloat;      // Invert the spin (servo normally would point to the opposite of '''our X''').
         servo.write(servoDegrees);                        // Spin servo to our given degrees.
      }
   }
   delay(10);
}