
/* 
 Adapted from:
 Arduino Dice :)
 This example shows how to simulate throwing a dice with 6 LEDs.
 The circuit:
 * 6 LEDs attached to consecutive digital pins (with 220 Ohm resistors)
 * Button switch connected to digital pin (see circuit on https://www.arduino.cc/en/Tutorial/Button)
 Created 5 Jan 2017
 By Esther van der Stappen
 
 This example code is in the public domain.
*/

// Liquid crystal is a library used for controlling the LCD screen
#include <LiquidCrystal.h>

// Pin number for the button
// This must be either pin 2 or 3 for the type of board we are using (Arduino Uno)
int button_pin = 2;

/* Step 1:
 * Declare 6 integers, setting pin numbers as their values.
 * The first led pin number should be set to 0 and the last should be set to 6.
 */

// Interger to store the buzzer pin.
int buzzer_pin = 7;

// Value to check state of button switch.
int pressed = LOW;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  /* Step 2:
   * Set button pin to INPUT
   */

  /* Step 3:
   * Set all LED pins to OUTPUT
   */

  // Set lcd screen to 16 columns and 2 rows.
  lcd.begin(16, 2);
  
  /* Step 8:
   * Set buzzer pin to OUTPUT 
   */

  // Initialize random seed.
  randomSeed(analogRead(0));
}

void DiceNoise() {
  for (int i = 1; i < 11; i++) {
    tone(buzzer_pin, 400 + 7*i);
    delay(250/i);
    noTone(buzzer_pin);
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

void PrintNoRollMessage() {
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Press the button");
  lcd.setCursor(0,1);
  lcd.print("to roll the die!");
  lcd.display();
}

void loop() {
  // If the button was pressed, pressed will equal HIGH.
  // If the button was not pressed, pressed will equal LOW.
  
  pressed = digitalRead(button_pin);
  
  /* Step 4:
   * remove true and replace it with a conditional to see if the button is pressed. 
   */
  if (true) {
    
    /* Step 5:
     * turn off all of the lights to reset. 
     */

    /* Step 9:
     * call the DiceNoise function. 
     */
    
    // Get a random number in the range [1,6]
    int thrownNumber = random(1,7);
    
    /* Step 6:
     * Write if statements to light up the lights based on what thrownNumber's value is.
     * For example, if thrownNumber is 3, the first three lights should light up.
     */

    /* Step 7:
     * PrintRolledMessage to inform the user what number was rolled.
     */
  }
}
