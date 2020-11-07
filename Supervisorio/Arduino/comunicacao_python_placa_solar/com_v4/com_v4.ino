
#include <stdlib.h>

float Tout;
float D;
float Tin;
float Ta;
float meq;
float I;
float Ts_simul = 0.01;

bool flag = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  Serial.println("Initializing...");
    
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    if (!flag){
      Tout = Serial.parseFloat();  
      D = Serial.parseFloat();   
      flag = 1;
      }
    else{
      float ts1 = 0;
      float ts2 = 0;
      
      ts1 = millis();
      // Getting data from Serial    

      float dumb = Serial.parseFloat();
      float Tin  = Serial.parseFloat();
      float Ta = Serial.parseFloat();
      float meq   = Serial.parseFloat();
      float I   = Serial.parseFloat();
      float Ts   = Serial.parseFloat();

      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
        Tout = (0.000311818*I - 0.001247272*(Tout + Tin - 2.*Ta)-2.304334269*meq*(Tout-Tin))*Ts_simul + Tout;
        D = (0.019*(Tout-60.0243) - (D-5.))*(Ts_simul/60.)+D;
      }

      if (Tout<0){
        Tout = 0;
      } else if(Tout> 100.){
        Tout = 100.;
      }

      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
      }
      
      Serial.print(Tout + (float) random(-2,2)/40.,2);
      Serial.print('&');
      Serial.print(D +(float) random(-1,1)/20.,2);  
      Serial.print('&');
      Serial.print(Tin,2);
      Serial.print('&');
      Serial.print(Ta,2);
      Serial.print('&');
      Serial.print(meq,2);
      Serial.print('&');
      Serial.println(I,2);
    
    }
  }
}
