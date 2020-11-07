#include <stdlib.h>

float h;
float T;
float Tc;
float T_;
float Tc_;
float V;
float qin;
float qc;
float Tin;
float Tcin;
float Ts;

float pi = 3.1415926535897932384626433832795;
float B = 0.5;
float A = 2.;
float hM = 2.;
float gamma = ((A/2.)-(B/2.))/2.;
float k = 0.001;
float g = 9.8;
float rho = 1000;
float c = k*pow(rho*g,0.5);
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
      float qc   = Serial.parseFloat();
      float Tin  = Serial.parseFloat()+273.15;
      float Tcin = Serial.parseFloat()+273.15;
      float Ts   = Serial.parseFloat();

      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
           
        h = (1./(pi*pow(gamma,2)*pow(h+(B/2)/gamma,2))*(qin-c*pow(h,0.5)))*Ts_simul + h;
        
        if (h<0){
          h = 0;
        } else if(h> hM){
          h = hM;
        }

        V = pi*pow(gamma,2)/3.*pow(h + (B/2)/gamma,3)-pi*pow(B/2.,3)/(3.*gamma);
        
        T_ = ((qin/V)*(Tin - T) + 0.250752257/V*(Tc - T))*Ts_simul+T;
        
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
        
      Serial.print(h + (float) random(-1,1)/10.,2);
      Serial.print('&');
      Serial.print(T-273.15+(float) random(-1,1)/1.5,2);
      Serial.print('&');
      Serial.print(Tc-273.15+(float) random(-2,2)/3.,2);
      Serial.print('&');
      Serial.print(qin);
      Serial.print('&');
      Serial.print(qc,2);
      Serial.print('&');
      Serial.print(Tin-273.15,2);
      Serial.print('&');
      Serial.println(Tcin-273.15,2);

    }
  }
}
