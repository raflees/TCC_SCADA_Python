
#include <stdlib.h>

float Ca;
float Cb;
float Cc;
float Fin;
float Cacarga;
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
      Ca = Serial.parseFloat();   
      Cb = Serial.parseFloat();
      Cc = Serial.parseFloat();   
      flag = 1;
      }
    else{
      float ts1 = 0;
      float ts2 = 0;
      
      ts1 = millis();
      // Getting data from Serial    

      float dumb = Serial.parseFloat();
      float Fin  = Serial.parseFloat();
      float Cacarga   = Serial.parseFloat();
      float Ts   = Serial.parseFloat();

      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
        
        Ca = (Fin*60/3.5*(Cacarga-Ca)+(-50.*Ca-10*pow(Ca,2)))*(Ts_simul/60.)+Ca;
        if (Ca<0){
          Ca = 0;
        } 
        Cb = (Fin*60/3.5*(-Cb)+(50*Ca-70*pow(Cb,1.1)))*(Ts_simul/60.)+Cb;
        if (Cb<0){
          Cb = 0;
        }
        Cc = (Fin*60/3.5*(-Cc) + 70*pow(Cb,1.1))*(Ts_simul/60.)+Cc;
        if (Cc<0){
          Cc = 0;
        }
      }
      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
      }
      
      Serial.print(Ca + (float) random(-1,1)/15.,2);  
      Serial.print('&');
      Serial.print(Cb + (float) random(-1,1)/15.,2);
      Serial.print('&');
       Serial.print(Cc + (float) random(-1,1)/20.,2);
      Serial.print('&');
      Serial.print(Fin,2);
      Serial.print('&');
      Serial.println(Cacarga,2);
    
    }
  }
}
