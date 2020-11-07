
#include <stdlib.h>

float x1; //Nível
float x2; //Concentration of B
float x3; // Concentration of C
float u1; // Flow rate 1
float u2; // Flow rate 2
float Cb1; // Concentration of B in u1
float Cb2; // Concentration of B in u2
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
      x1 = Serial.parseFloat();  
      x2 = Serial.parseFloat();   
      x3 = Serial.parseFloat();   
      flag = 1;
      }
    else{
      float ts1 = 0;
      float ts2 = 0;
      
      ts1 = millis();
      // Getting data from Serial    

      float dumb = Serial.parseFloat();
      float u1  = Serial.parseFloat();
      float u2 = Serial.parseFloat();
      float Cb1  = Serial.parseFloat();
      float Cb2 = Serial.parseFloat();
      float Ts   = Serial.parseFloat();


      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {

      float aux = 10.*x2/pow(1.+0.99*x2,1.5);
    
        x1 = (u1+u2-0.5*pow(x1,0.5))*(Ts_simul) + x1;
        if (x1<0){
          x1 = 0;
        } else if(x1> 4.){
          x1 = 4.;
        }
        x2 = ((Cb1-x2)*u1/x1+(Cb2-x2)*u2/x1-aux)*(Ts_simul)+x2;
        if (x2<0){
          x2 = 0;
        } 
        x3 = ((-x3)*u1/x1+(-x3)*u2/x1+aux)*(Ts_simul)+x3;
        if (x3<0){
          x3 = 0;
        }
        
      }
      
      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
      }
                  
      Serial.print(x1 + (float) random(-2,2)/5.,2);
      Serial.print('&');
      Serial.print(x2 + (float) random(-1,1)/4.,2);  
      Serial.print('&');
      Serial.print(x3 + (float) random(-1,1)/5.,2);
      Serial.print('&');
      Serial.print(u1,2);
      Serial.print('&');
      Serial.print(u2,2);
      Serial.print('&');
      Serial.print(Cb1,2);
      Serial.print('&');
      Serial.println(Cb2,2);
    }
  }
}
