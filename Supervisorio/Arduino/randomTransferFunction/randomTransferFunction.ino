float u[2];
float y[2];
float y0[2];
float p[2][2] = {{0.1, 0.5}, {-0.12, 0.2}};
float t;
float t0;
float tstep = 100;  //in milliseconds

/*
dy[0]dt = p[0][0]*y[0] + p[0][1]*y[1] + u[0]
dy[1]dt = p[1][0]*y[0] + p[1][1]*y[1] + u[1]
*/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  wait_for_comm();
  
  t0 = millis();
  y[0] = 1.5;
  y[1] = 2.0;
  u[0] = 0;
  u[1] = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    u[0] = Serial.parseFloat();
    u[1] = Serial.parseFloat();
    Serial.flush();
  }
  
  t = millis() - t0;
  
  for (int i = 0; i < ceil(t/tstep); i++) {
    y0[0] = y[0];
    y0[1] = y[1];
    y[0] += (p[0][0]*y0[0] + p[0][1]*y0[1] + u[0])*tstep/1000;
    y[1] += (p[1][0]*y0[0] + p[1][1]*y0[1] + u[1])*tstep/1000;
    t0 = millis();
  }
  
  Serial.print(t0/1000);
  Serial.print('\t');
  for (int i=0; i<2; i++) {
    Serial.print(y[i], 2);
    Serial.print('\t');
  }
  Serial.println("");
}

void wait_for_comm() {
  while (true) {
    if (Serial.available() > 0) {
      break;
    }
  }
  return;
}

void cleanSerial() {
  char c;
  while (Serial.available() > 0) {
    c = Serial.read();
  }
}
