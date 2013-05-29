#include "Timer.h"

Timer t;

#define BLINK_SIZE 70
#define BLINK_LENGTH 500

char state[2];
int blink_pins[BLINK_SIZE];

void setup() {                
  Serial.begin(115200);
    
  for (int i = 3 ; i < 70 ; i++) {
    pinMode(i, OUTPUT);  
  }
  
  for (int i = 0 ; i < 70 ; i++) {
    blink_pins[i] = 0;  
  }
  
  t.every(1000, blink);  
}


// the loop routine runs over and over again forever:
void loop() {
  if (Serial.available()) {
    Serial.readBytes(state, 2);
    if (state[1] == 1) {
      blink_pins[state[0]] = 0;
      digitalWrite(state[0],HIGH);
    }
    if (state[1] == 0) {
      blink_pins[state[0]] = 0;
      digitalWrite(state[0],LOW);
    }
    if (state[1] == 2) {
      blink_pins[state[0]] = 1;
    }
  }
  t.update();
}

void blink() {
    for (int i = 0 ; i < BLINK_SIZE ; i++) {
      if (blink_pins[i]) {
        if (digitalRead(i) == LOW) {
          digitalWrite(i, HIGH);
        }
        else {
          digitalWrite(i, LOW);
        }
      }
  }
}
