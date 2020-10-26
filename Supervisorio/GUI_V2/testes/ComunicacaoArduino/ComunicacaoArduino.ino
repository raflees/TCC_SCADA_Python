#include <stdio.h>

float v[100][3];
char c = 'a';
int ini = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  
  Serial.begin(9600);
  for(int i=0; i<100; i++) {
    v[i][0] = i;
    for (int j=1; j<4; j++) {
      v[i][j] = (float)rand()/100;
    }
  }

  ini = millis();
}

void loop1() {
  // put your main code here, to run repeatedly:
  mandarValores();
  while(1 == 1);
}

void loop() {
  int row;
  int totalBytes = 0;
  int pot;
  if(Serial.available() > 0) {

    delay(10);
    totalBytes = Serial.available();
    pot = totalBytes-1;
    row = 0;
    
    while (pot >= 0){
      c = Serial.read();
      row += (c - '0')*pow(10, pot);
      Serial.print(c - '0');
      Serial.print("*10^");
      Serial.print(pot);
      Serial.print("\t(");
      Serial.print(row);
      Serial.print(")\t");
      Serial.print("\t\t");
      
      pot--;
    }
    
    Serial.print("Got ");
    Serial.print(totalBytes);
    Serial.print("\t\t");
    Serial.print("->\t");
    Serial.print((float)millis()/1000);
    Serial.print("s: ");
    Serial.println(row);
    /*Serial.print(v[row][0]);
    Serial.print('\t');
    Serial.print(v[row][1]);
    Serial.print('\t');
    Serial.print(v[row][2]);
    Serial.print('\t');
    Serial.print(v[row][3]);
    Serial.print('\t');*/
  }
}

float pow (int base, int exp) {
  if (base == 0 && exp == 0) return 0;
  
  float saida = 1;
  for (int i = 0; i<exp; i++)
    saida *= base;
   return saida;
}

void mandarValores() 
{
  for(int i=0; i<100; i++) {
    for (int j=0; j<4; j++) {
      Serial.print(v[i][j]);
      if (j != 3) Serial.print('\t');
    }
    Serial.print('\n');
  }
}
