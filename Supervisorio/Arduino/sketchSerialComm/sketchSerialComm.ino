float input;
float output;
int row = 0;

int ledpin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledpin, OUTPUT);
  wait_for_comm();
  randomSeed(analogRead(0));
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledpin, HIGH);
  Serial.flush();
  output = millis() / 10000.0 * 2;
  Serial.print(output);
  Serial.print('\t');
  Serial.print(random(10));
  Serial.print('\t');
  Serial.print(random(8));
  Serial.println("");
 //wait_for_comm(); 
 delay(200);
}

void wait_for_comm() {
  char c;
  while (true) {
    if (Serial.available() > 0)
      c = Serial.read();
    if (c == 97)
      Serial.write("Got it!\n");
      break;
    //Serial.println("Waiting for input");
    delay(800);
  }
  return;
}
