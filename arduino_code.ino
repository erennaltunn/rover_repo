/*
    Author: erennaltunn
    Email: eren0altun@gmail.com
    Date: 04/09/2020
    License: Public Domain
*/

int M1V = 150;         // Motor 1 Velocity  
int M2V = 100;         // Motor 2 Velocity 
int M3V = 90;         // Motor 3 Velocity
int M4V = 103;        // Motor 4 Velocity

int M1D = 1;        // Motor 1 Direction 
int M2D = 0;        // Motor 2 Direction
int M3D = 1;        // Motor 3 Direction
int M4D = 0;        // Motor 4 Direction

long randNumber;
int i;



void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  String mes;
  M1D = random(2);
  M1V = random(0,255);
  M2D = random(2);
  M2V = random(0,255);
  M3D = random(2);
  M3V = random(0,255);
  M4D = random(2);
  M4V = random(0,255);

  
  mes = "S";
  mes += String(M1D);
  mes += add(M1V);  //We don't know if the random number is 3 digits. So I have put a control function.
  mes += String(M2D);
  mes += add(M2V);
  mes += String(M3D);
  mes += add(M3V);
  mes += String(M4D);
  mes += add(M4V);
  mes += "F";

  
  Serial.println(mes);


  delay(2000);
}

String add(int a){ //Function to make random motor velocity data in 3 digits.
 String s;
 if(a<10)
 s = "00" + String(a);
 else if (a<100)
 s = "0" + String(a);
 else
 s = String(a);

 return s;

}
  
  
