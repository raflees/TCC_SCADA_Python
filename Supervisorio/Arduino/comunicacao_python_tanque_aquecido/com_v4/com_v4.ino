
#include <stdlib.h>

float h;
float T;
float Tc;
float T_;
float Tc_;
float qin;
float qout;
float qc;
float Tin;
float Tcin;
float Ts;     
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
      h = Serial.parseFloat();  
      T = Serial.parseFloat()+273.15;  
      Tc = Serial.parseFloat()+273.15;  

      flag = 1;
      }
    else{
      float ts1 = 0;
      float ts2 = 0;
      
      ts1 = millis();
      // Getting data from Serial    

      float dumb = Serial.parseFloat();
      float qin  = Serial.parseFloat();
      float qout = Serial.parseFloat();
      float qc   = Serial.parseFloat();
      float Tin  = Serial.parseFloat()+273.15;
      float Tcin = Serial.parseFloat()+273.15;
      float Ts   = Serial.parseFloat();
      
      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
      
        h = (qin/3.14 - qout/3.14)*Ts_simul + h;
        
        if (h<0){
          h = 0;
        } else if(h> 3.){
          h = 3.;
        }
        
        T_ = (qin/(3.14*h)*(Tin - T) + 0.0798574066147487/h*(Tc - T))*Ts_simul+T;
        
        Tc_ = (qc/2.*(Tcin-Tc) + 0.12406024365431854*(T - Tc))*Ts_simul + Tc;
  
        T = T_;
        Tc = Tc_;
        
        if (T<0.){
          T = 0;
        } 
  
        if (Tc<0.){
          Tc = 0;
        } 
      }

      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
      }
 
      Serial.print(h + (float) random(-2,2)/100.,2);
      Serial.print('&');
      Serial.print(T-273.15+(float) random(-1,1)/2.,2);
      Serial.print('&');
      Serial.print(Tc-273.15+(float) random(-1,1)/4.,2);
      Serial.print('&');
      Serial.print(qin);
      Serial.print('&');
      Serial.print(qout,2);
      Serial.print('&');
      Serial.print(qc,2);
      Serial.print('&');
      Serial.print(Tin-273.15,2);
      Serial.print('&');
      Serial.println(Tcin-273.15,2);
    }
  }
}
