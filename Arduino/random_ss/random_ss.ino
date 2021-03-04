
#include <stdlib.h>

//Variables
float dx1dt;
float dx2dt;
float x1;
float x2;
float u1;
float u2;
float t0;
float t;

//Parameters
float A[2][2] = {{-0.05, 0.05}, {0.2, 0.1}};
float B[2][2] = {{0.1, -0.2}, {0.2, 0.2}};

//sample time in miliseconds
float tstep = 100;


void wait_for_comm() {
  while (true) {
    if (Serial.available() > 0) {
      break;
    }
  }
  clearSerial();
  return;
}

void clearSerial() {
  char c;
  while(Serial.available() > 0)
    c = Serial.read();
  return;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  x1 = 1.0;
  x2 = 1.0;
  u1 = 0;
  u2 = 0;

  wait_for_comm();
  t0 = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    //Serial.flush();
    u1 = Serial.parseFloat();
    u2 = Serial.parseFloat();
    u1 = u1*10;
    u2 = u2*10;
  }

  t = millis() - t0;
  t0 = millis();
  for (int i = 0; i < ceil(t/tstep); i++) {
      //espaco de estados
      dx1dt = A[0][0]*x1 + A[0][1]*x2 + B[0][0]*u1 + B[0][1]*u2;
      dx2dt = A[1][0]*x1 + A[1][1]*x2 + B[1][0]*u1 + B[1][1]*u2;

      x1 += dx1dt*tstep/1000;
      x2 += dx2dt*tstep/1000;
  }

    Serial.print(t0/1000);
    Serial.print('\t');
    Serial.print(x1, 3);// (float)random(-1,1)/80. ,3);
    Serial.print('\t');
    Serial.print(x2, 3);// +(float) random(-1,1)/80., 3);
    Serial.print('\t');
    Serial.print(u1, 3);
    Serial.print('\t');
    Serial.println(u2, 3);
}
