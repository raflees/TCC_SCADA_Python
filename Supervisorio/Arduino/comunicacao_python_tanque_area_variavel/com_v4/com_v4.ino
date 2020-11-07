
#include <stdlib.h>

float h1;
float h2;
float u1;
float u2;
float Ts;
float pi = 3.1415926535897932384626433832795;
bool flag = 0;
float B = 1.;
float A = 4.;
float hM = 4.;
float gamma = ((A/2.)-(B/2.))/2.;
float k = 0.001;
float g = 9.8;
float rho = 1000;
float c = k*pow(rho*g,0.5);
float Ts_simul = 0.01;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  Serial.println("Initializing...");
    
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    if (!flag){
      h1 = Serial.parseFloat();  
      h2 = Serial.parseFloat();  
      flag = 1;
      }
    else{
      float ts1 = 0;
      float ts2 = 0;
      
      ts1 = millis();
      // Getting data from Serial    
      float dumb = Serial.parseFloat();
      float u1 = Serial.parseFloat();  
      float u2 =  Serial.parseFloat();
      float Ts = Serial.parseFloat();

      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
        h2 = (1./(pi*pow(gamma,2)*pow(h2+(B/2)/gamma,2))*(u2-c*pow(h2,0.5)))*Ts_simul+h2;
  
        if (h2<0){
          h2 = 0;
        } else if(h2>hM){
          h2 = hM;
        }
        
        h1 = (1./(pi*pow(gamma,2)*pow(h1+(B/2)/gamma,2))*(u1+c*pow(h2,0.5)-c*pow(h1,0.5)))*Ts_simul+h1;
        
        if (h1<0.){
          h1 = 0;
        } else if(h1>hM){
          h1 = hM;
          } 
      }
      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
        }
      
      Serial.print(h1+(float) random(-1,1)/80.,2);
      Serial.print('&');
      Serial.print(h2+(float) random(-1,1)/80.,2);
      Serial.print('&');
      Serial.print(u1,2);
      Serial.print('&');
      Serial.println(u2,2);
      
        
    }
  }
}
