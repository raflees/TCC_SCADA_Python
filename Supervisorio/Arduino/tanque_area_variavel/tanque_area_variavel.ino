
#include <stdlib.h>

//Variables
float dh1dt;
float dh2dt;
float h1;
float h2;
float u1;
float u2;
float t0;
float t;

//Parameters
float pi = 3.1415926535897932384626433832795;
float B = 1.;
float A = 4.;
float hM = 4.;
float gamma = ((A/2.)-(B/2.))/2.;
float k = 0.001;
float g = 9.8;
float rho = 1000;
float c = k*pow(rho*g,0.5);
//sample time in miliseconds
float tstep = 100;


void wait_for_comm() {
  while (true) {
    if (Serial.available() > 0) {
      break;
    }
  }
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
  
  h1 = 0.0;
  h2 = 0.0;
  u1 = 0;
  u2 = 0;

  wait_for_comm();
  t0 = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    u1 = Serial.parseFloat();
    u2 = Serial.parseFloat();
    clearSerial();
  }

  t = millis() - t0;
  t0 = millis();
  for (int i = 0; i < ceil(t/tstep); i++) {
      dh1dt = (1./(pi*pow(gamma,2)*pow(h1+(B/2)/gamma,2))*(u1+c*pow(h2,0.5)-c*pow(h1,0.5)));
      dh2dt = (1./(pi*pow(gamma,2)*pow(h2+(B/2)/gamma,2))*(u2-c*pow(h2,0.5)));

      h1 += dh1dt*tstep/1000;
      h2 += dh2dt*tstep/1000;
      
      /*if (h2<0){
        h2 = 0;
      } else if(h2>hM){
        h2 = hM;
      }
      
      if (h1<0.){
        h1 = 0;
      } else if(h1>hM){
        h1 = hM;
      }*/
    }

    Serial.print(t0/1000);
    Serial.print('\t');
    Serial.print(h1, 2);//+(float) random(-1,1)/80.,2);
    Serial.print('\t');
    Serial.print(h2, 2);//+(float) random(-1,1)/80.,2);
    Serial.print('\t');
    Serial.print(u1,2);
    Serial.print('\t');
    Serial.println(u2,2);

    u1 = 1;
    u2 = 1;
}
