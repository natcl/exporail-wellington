#include "Timer.h"

Timer t;

#define START_PIN 2
#define END_PIN 70
#define BLINK_LENGTH 500

char state[2];
int blink_pins[END_PIN];
int blink_state = LOW;

void setup() {                
  Serial.begin(115200);
    
  // set each pin to output
  for (int i = START_PIN ; i < END_PIN ; i++) {
    pinMode(i, OUTPUT);
  }
  
  // initialize blink pin array to 0
  for (int i = 0 ; i < END_PIN ; i++) {
    blink_pins[i] = 0;  
  }

  test_system();
  
  t.every(BLINK_LENGTH, blink);  
}

void loop() {
  if (Serial.available()) {
    Serial.readBytes(state, 2);
    // pin number + 1 turns pin on 
    if (state[1] == 1) {
      blink_pins[state[0]] = 0;
      digitalWrite(state[0],HIGH);
    }
    // pin number + 0 turns pin off
    if (state[1] == 0) {
      blink_pins[state[0]] = 0;
      digitalWrite(state[0],LOW);
    }
    // pin number + 2 makes pin blink
    if (state[1] == 2) {
      blink_pins[state[0]] = 1;
    }
    // any pin number + 3 turns off all pins
    if (state[1] == 3) {
      all_off();
    }
  }
  t.update();
}

void blink() {
    if (blink_state == LOW) {
      blink_state = HIGH;
    }
    else {
      blink_state = LOW;
    }
    for (int i = START_PIN ; i < END_PIN ; i++) {
      if (blink_pins[i]) {
        digitalWrite(i,blink_state);
      }
  }
}

void all_off() {
  for (int i = START_PIN ; i < END_PIN ; i++) {
    digitalWrite(i,LOW);
    blink_state = LOW;
    blink_pins[i] = 0;  
  }
}

void test_system() {
  for (int i = START_PIN ; i < END_PIN ; i++) {
    digitalWrite(i,HIGH);
    delay(50);
    digitalWrite(i,LOW);  
  }
}
