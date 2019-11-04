void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  if(Serial.read() == 'e'){
    for(int i=1; i<101; i++){
      Serial.println(i);
    }
  }
}
