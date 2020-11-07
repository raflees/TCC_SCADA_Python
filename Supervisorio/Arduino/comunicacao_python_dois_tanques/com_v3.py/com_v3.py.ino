
#include <stdlib.h>

double h1=0.;
double h2=0.;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  Serial.println("Initializing...");
    
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    float ts1 = 0;
    float ts2 = 0;
    
    ts1 = millis();
    // Getting data from Serial    
    float v1 = Serial.parseFloat();  
    float v2 =  Serial.parseFloat();
    float Ts = Serial.parseFloat();
    
    h2 = (-0.12*pow(h2,0.5)+0.015*v2)*Ts+h2;
    h1 = (-0.10*pow(h1,0.5)+0.12*pow(h2,0.5)+0.09*v1)*Ts+h1;
    
    if (h1<0.){
      h1 = 0;
    } else if(h1>20.){
      h1 = 10.;
      } 

    if (h2<0){
      h2 = 0;
    } else if(h2> 20.){
      h2 = 10.;
    }

    Serial.print(h1+random(-0.2,0.2),6);
    Serial.print('&');
    Serial.print(h2+random(-0.15,0.15),6);
    Serial.print('&');
    Serial.print(v1,6);
    Serial.print('&');
    Serial.println(v2,6);
      
    ts2 = millis();
    delay(Ts*1000. - (ts2-ts1));
  }
}
