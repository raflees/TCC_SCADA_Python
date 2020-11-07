
//#include <stdlib.h>

float h1;
float h2;
float v1;
float v2;
float dumb;
float Ts;
float Ts_simul = 0.01;

bool flag = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  //Serial.println("Initializing...");
    
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
      float v1 = Serial.parseFloat();  
      float v2 =  Serial.parseFloat();
      float Ts = Serial.parseFloat();
      

      for (int i = 0; i <= ceil(Ts/Ts_simul); i++) {
      
        h2 = (-0.11*pow(h2,0.5)+0.03*v2)*Ts_simul+h2;
  
        if (h2<0){
          h2 = 0;
        } else if(h2> 20.){
          h2 = 20.;
        }
        
        h1 = (-0.12*pow(h1,0.5)+0.11*pow(h2,0.5)+0.09*v1)*Ts_simul+h1;
        
        if (h1<0.){
          h1 = 0;
        } else if(h1>20.){
          h1 = 20.;
          } 
      
      }
      
      ts2 = millis();
      if (Ts*1000. - (float) (ts2-ts1) >= 0){
          delay(Ts*1000. - (float) (ts2-ts1));
        } else{
          delay(Ts*1000);
      }
  
      Serial.print(h1,2);//+(float) random(-20,20)/100.,6);
      Serial.print('&');
      Serial.print(h2,2);//+(float) random(-10,10)/100.,6);
      Serial.print('&');
      Serial.print(v1,2);
      Serial.print('&');
      Serial.println(v2,2);
        
    }
  }
}
