
#include <stdlib.h>

char var[2][32];
double h1=0.;
double h2=0.;
double Ts=1.056;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  Serial.println("Initializing...");
  
//  if (Serial.available()){
//     // Getting data from Serial    
//    int i1=0;
//    int i2=0;
//
//    String x;
//    x = Serial.readString();
//    
//    int ix = 0;
//      
//    while (x[ix] != 'T' ) {
//      int hold = 0;
//      if (x[ix]=='&'||x[ix] =='T' ){
//        hold = 1;
//        i2 = 0;
//        i1++;                
//        }else if(!hold){
//          var[i1][i2] = x[ix];    
//          i2++;
//        }
//      ix++;
//    }
//
//    h1 = atof(var[0]);
//    h2 = atof(var[1]);
//    Ts = atof(var[2]);
//    Serial.println("Initial condition h1:"+String(h1)+" h2:"+String(h2));
//    Serial.println(1)
//  }
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {

    // Getting data from Serial    
    int i1=0;
    int i2=0;

    String x;
    x = Serial.parseFloat();//Serial.readString();
    
    int ix = 0;
      
    while (x[ix] != 'T' ) {
      int hold = 0;
      if (x[ix]=='&'||x[ix] =='T' ){
        hold = 1;
        i2 = 0;
        i1++;                
        }else if(!hold){
          var[i1][i2] = x[ix];    
          i2++;
        }
      ix++;
    }

    double v1 = atof(var[0]);
    double v2 = atof(var[1]);
    
    h2 = (-0.12*sqrt(h2)+0.015*v2)*Ts+h2;
    h1 = (-0.10*pow(h1,0.5)+0.12*pow(h2,0.5)+0.09*v1)*Ts+h1;
    
    if (h1<0.){
      h1 = 0;
    } else if(h1>10.){
      h1 = 10.;
      } 

    if (h2<0){
      h2 = 0;
    } else if(h2> 10.){
      h2 = 10.;
    }
   
    Serial.print(h1+random(-0.2,0.2),6);
    Serial.print('&');
    Serial.print(h2+random(-0.15,0.15),6);
    Serial.print('&');
    Serial.print(v1,6);
    Serial.print('&');
    Serial.println(v2,6);
//    delay(1);
  }
}
