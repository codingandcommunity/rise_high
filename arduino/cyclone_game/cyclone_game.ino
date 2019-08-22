
/* 
 Arduino Cyclone Game
 */
#include <LiquidCrystal.h>

// 6 consecutive digital pins for the LEDs
int led_pins[] = {0, 1, 3, 4, 5, 6};

// pin for the button
int button = 2;

// pin for buzzer
int buzzer = 7;

// value to check state of button switch
int pressed = LOW;

// STEP 1: Declare a variable to keep track of the player's score.

// STEP 2: Declare a variable to keep track of what light is on.

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // STEP 3: set all LED pins to OUTPUT
  
  // STEP 4: set button pin to INPUT

  // STEP 5: set buzzer pin to OUTPUT
  
  // Anytime the signal from the button pin goes from LOW to HIGH, the interrupt
  // command is called.
  attachInterrupt(digitalPinToInterrupt(button), interrupt, RISING);

  lcd.begin(16, 2);
}

void Buzzer(int frequency) {
  tone(buzzer, 300);
  delay(1000);
  noTone(buzzer);
  delay(1000);
}

void loop() {
  int delayTime = 300; // can decrease to make game harder
  
  while(true) {
    // STEP 6: add code to light up each light, one at a time.

    // STEP 7: add code to increment the current light counter
    // that you declared in STEP 2.
    // For example if the first light in led_pins is lit, then
    // your variable should be equal to 0.

    // Display the users score on the screen.
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Your score: ");
    // STEP 8: display the player's score to the screen.
    lcd.display();
  }
}

void interrupt(){
  lcd.clear();
  lcd.display();
  lcd.setCursor(0,1);

  // STEP 9: check to see if the button is pressed or not.

  // STEP 10: replace true with a condtional to check if the button
  // is pressed and the jackpot light is lit.
  if (true) {
    // STEP 11:
    // If pressed and the currentLight is the jackpot light,
    // they win and the player should:
    // - get one more point
    // - see a winning message displayed to the screen
    // - hear a noise.
  }

  // STEP 12: replace true with a condtional to check if the button
  // is pressed and the jackpot light is not lit.
  else if (true) {
    // STEP 13:
    // If pressed and the currentLight is not the jackpot light,
    // they lose and the player should:
    // - lose one point
    // - see a losing message displayed to the screen
    // - hear a different noise than if they win.
  }
  
  // If the button is not pressed do nothing.
}
