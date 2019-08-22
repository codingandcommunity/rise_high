/* 
 Arduino Dice :)
 This example shows how to simulate throwing a dice with 6 LEDs.
 The circuit:
 * 6 LEDs attached to consecutive digital pins (with 220 Ohm resistors)
 * Button switch connected to digital pin (see circuit on https://www.arduino.cc/en/Tutorial/Button)
 Created 5 Jan 2017
 By Esther van der Stappen
 
 This example code is in the public domain.
*/

#include <LiquidCrystal.h>

// 6 consecutive digital pins for the LEDs
int first = 0;
int second = 1;
int third = 3;
int fourth = 4;
int fifth = 5;
int sixth = 6;

// pin for the button switch
int button = 2;

// pin for buzzer
int buzzer = 7;

// value to check state of button switch
int pressed = LOW;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  
  // set all LED pins to OUTPUT
  pinMode(first, OUTPUT);
  pinMode(second, OUTPUT);
  pinMode(third, OUTPUT);
  pinMode(fourth, OUTPUT);
  pinMode(fifth, OUTPUT);
  pinMode(sixth, OUTPUT);
  
  // set button pin to INPUT
  pinMode(button, INPUT);

  // set buzzer pin to OUTPUT
  pinMode(buzzer, OUTPUT);
  
  lcd.begin(16, 2);

  // initialize random seed by noise from analog pin 0 (should be unconnected)
  randomSeed(analogRead(0));
}

void DiceNoise() {
  for (int i = 1; i < 11; i++) {
    tone(buzzer, 400 + 7*i);
    delay(250/i);
    noTone(buzzer);
    delay(250/i);
  }
}

void PrintRolledMessage(int thrownNumber) {
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("You rolled a ");
  lcd.print(thrownNumber);
  lcd.display();
}

void loop() {
  // if button is pressed - throw the dice
  pressed = digitalRead(button);

  if (pressed == HIGH) {
    digitalWrite(first, LOW);
    digitalWrite(second, LOW);
    digitalWrite(third, LOW);
    digitalWrite(fourth, LOW);
    digitalWrite(fifth, LOW);
    digitalWrite(sixth, LOW);
    
    DiceNoise();
    
    // get a random number in the range [1,6]
    int thrownNumber = random(1,7);
    
    // write IF statements to light up the lights
    digitalWrite(first, HIGH);
    
    if (thrownNumber >= 2) {
      digitalWrite(second, HIGH);
    }
    if (thrownNumber >= 3) {
      digitalWrite(third, HIGH);    
    }
    if (thrownNumber >= 4) {
      digitalWrite(fourth, HIGH);    
    }
    if (thrownNumber >= 5) {
      digitalWrite(fifth, HIGH);    
    }
    if (thrownNumber == 6) {
      digitalWrite(sixth, HIGH);     
    }

    PrintRolledMessage(thrownNumber);
  }
}
