// the circuit can be found and simulated here:
// https://circuits.io/circuits/3381894-button-push-counter

/*
 Button Push Counter
 
 maintains a count of the number of pushes on a pushbutton
 and displays this count on the LCD
 also toggles the built-in LED each time a button push happens
 
 note: button pushes are debounced using a debounce time of DEBOUNCE_TIME
*/

#define LED_PIN LED_BUILTIN
#define ON      HIGH
#define OFF     LOW

#define BUTTON_PIN  2    // the number of the pushbutton pin
#define PRESSED     HIGH
#define NOT_PRESSED LOW

#define DEBOUNCE_TIME 0 // the debounce time; increase if the LED flickers;
                        // 0 is appropriate for circuits.io simulation
                        // try 50 for IRL execution

#define RS_PIN  4 // the RS pin of the LCD is connected to pin 4 of the Arduino
#define EN_PIN  6
#define D4_PIN  8
#define D5_PIN  9
#define D6_PIN 10
#define D7_PIN 11

#include <LiquidCrystal.h>

// initialize a LiquidCrystal object, lcd, with the numbers of the interface pins in the global scope
LiquidCrystal lcd(RS_PIN, EN_PIN, D4_PIN, D5_PIN, D6_PIN, D7_PIN);
void setupLCD() {  
  // Set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("number of pushes");
  lcd.setCursor(0, 1);
  lcd.print(0);
}

void setup() {
  
  setupLCD();
    
  pinMode(   LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT );
  
  digitalWrite(LED_PIN, OFF);
}

// initialize led and button state
int ledState= OFF;
int     buttonState= NOT_PRESSED;
int lastButtonState= NOT_PRESSED;

// the following variables are unsigned longs because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
unsigned long debouncingTimer_elapsedTime= 0;
unsigned long debouncingTimer_startTime=   0;

int count= 0; // counts the number of OFF to ON pushbutton transitions

int last_reading= LOW;

void loop() {
  
  int current_reading= digitalRead(BUTTON_PIN);
  
  if (current_reading != last_reading) {
    // reset the debouncing timer
    debouncingTimer_elapsedTime= 0;
    debouncingTimer_startTime=   millis();
  }
  else {
    
    debouncingTimer_elapsedTime= millis() - debouncingTimer_startTime;
    if (debouncingTimer_elapsedTime > DEBOUNCE_TIME) {
      // the current reading has been held for longer than the debounce time,
      // so take it as the actual current state, but first save the previous state
      lastButtonState= buttonState;
      buttonState= current_reading;
      
      // only toggle the LED if the button went from a being not pressed to being pressed
      if ( lastButtonState == NOT_PRESSED  &&  buttonState == PRESSED ) {
        // toggle the LED
        ledState= !ledState;
        // increment counter and print the new count
        lcd.setCursor(0, 1);
        lcd.print(++count);
      }
    }
  }
  
  // update the LED
  digitalWrite(LED_PIN, ledState);
  
  last_reading= current_reading;
}