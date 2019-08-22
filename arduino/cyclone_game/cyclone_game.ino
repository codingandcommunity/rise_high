
/* 
 Arduino Cyclone Game
 */
#include <LiquidCrystal.h>

// 6 consecutive digital pins for the LEDs
int led_pins[] = {0, 1, 3, 4, 5, 6};

// pin for the button switch
int button = 2;

// pin for buzzer
int buzzer = 7;

// value to check state of button switch
int pressed = LOW;

int score = 0;

int currentLight = 0;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set all LED pins to OUTPUT
  for(int i = 0; i < 6; i++) {
    pinMode(led_pins[i], OUTPUT);
  }
  
  // set button pin to INPUT
  pinMode(button, INPUT);

  // set buzzer pin to OUTPUT
  pinMode(buzzer, OUTPUT);
  
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
    digitalWrite(led_pins[currentLight], HIGH);
    delay(delayTime);
    digitalWrite(led_pins[currentLight], LOW);
    delay(delayTime);

    if (currentLight == 5){
      currentLight = 0;
    } else {
      currentLight++;
    }
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Your score: ");
    lcd.print(score);
    lcd.display();
  }
}

void interrupt(){
  lcd.clear();
  lcd.display();
  lcd.setCursor(0,1);
  
  pressed = digitalRead(button);

  // If pressed and the currentLight is the jackpot light,
  // they win and get one more point.
  if (pressed == HIGH && currentLight == 5) {
    score++;
    lcd.print("You win!");
    Buzzer(1000);
    delay(500);
  }
  // If pressed and the currentLight is not the jackpot light,
  // they lose and get one less point.
  else if (pressed == HIGH && currentLight != 5) {
    score--;
    lcd.print("You lose :(");
    Buzzer(1000);
    delay(500);
  }
  // If button not pressed do nothing
}
