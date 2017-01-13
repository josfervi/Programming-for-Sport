/*
 Six Timers - button 1 working
 
 push button 1 to increment task 1 duration by 15
 LCD displays the duration of each task
 LEDs are not configured
 
 note: button pushes are debounced using a debounce time of DEBOUNCE_TIME
*/

// define button pin definitions and Setup //
#define TASK1_BUTTON_PIN 11
#define TASK2_BUTTON_PIN 12
#define TASK3_BUTTON_PIN 13
// #define TASK4_BUTTON_PIN NA
// #define TASK5_BUTTON_PIN NA
// #define TASK6_BUTTON_PIN NA

#define PRESSED     HIGH
#define NOT_PRESSED LOW

#define DEBOUNCE_TIME 0UL // the debounce time; increase if the LED flickers;
                          // 0 is appropriate for circuits.io simulation
                          // try 50 for IRL execution

#define INCREMENT_TASK_DURATION_BY_THIS_AMOUNT 15

void setButtonPinsToOutput() {
  pinMode(TASK1_BUTTON_PIN, OUTPUT);
  pinMode(TASK2_BUTTON_PIN, OUTPUT);
  pinMode(TASK3_BUTTON_PIN, OUTPUT);
  //pinMode(TASK4_BUTTON_PIN, OUTPUT);
  //pinMode(TASK5_BUTTON_PIN, OUTPUT);
  //pinMode(TASK6_BUTTON_PIN, OUTPUT);
}

// Shift Register Pin Defintions and Setup//
#define SR_DATA_PIN  0    //The Arduino Pin connected to DS of 74HC595
#define SR_LATCH_PIN 1    //The Arduino Pin connected to ST_CP of 74HC595
#define HOLD      LOW
#define GO        HIGH
#define SR_CLOCK_PIN 2    //The Arduino Pin connected to SH_CP of 74HC595

void setupShiftRegister() {
  //set Arduino pins to output so you can control the shift register
  pinMode(SR_DATA_PIN,  OUTPUT);
  pinMode(SR_LATCH_PIN, OUTPUT);
  pinMode(SR_CLOCK_PIN, OUTPUT);
  
  // this SR is a rising edge SR so start with the clock low
  digitalWrite(SR_CLOCK_PIN, LOW);
}

// define LED pin definitions //
#define TASK1_LED_PIN 4//  Task 1 LED is connected to pin Q1 of the Shift Register
#define TASK2_LED_PIN 5
#define TASK3_LED_PIN 6
#define TASK4_LED_PIN 1
#define TASK5_LED_PIN 2
#define TASK6_LED_PIN 3

#define ON  HIGH
#define OFF LOW

// define LCD pin definitions and Setup //
#define LCD_RS_PIN 3 // The Arduino Pin connected to the RS pin of the LCD
#define LCD_EN_PIN 4
#define LCD_D4_PIN 5
#define LCD_D5_PIN 6
#define LCD_D6_PIN 7
#define LCD_D7_PIN 8

#include <LiquidCrystal.h>

// initialize a LiquidCrystal object, lcd, with the numbers of the interface pins
// do this in a global scope, so that the object, lcd, is global
LiquidCrystal lcd(LCD_RS_PIN, LCD_EN_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

void setupLCD() {  
  // Set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("T1 T2 T3 T4 T5"); // task 6, " T6", omitted because at most 16 chars can be printed per line on the LCD and we're already at 14 chars
  lcd.setCursor(0, 1);         // set cursor at the second line of the LCD
  lcd.print(" 0  0  0  0  0");
}

void setup() {
  setButtonPinsToOutput();
  setupShiftRegister();
  setupLCD();
}

// initialize led and button state
int ledState= OFF;
int     buttonState= NOT_PRESSED;
int lastButtonState= NOT_PRESSED;

// the following variables are unsigned longs because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
unsigned long debouncingTimer_elapsedTime= 0;
unsigned long debouncingTimer_startTime=   0;

int task1Duration= 0; // increments by INCREASE_TASK_DURATION_BY_THIS_AMOUNT each time the task 1 button is pressed

int last_reading= LOW;
int current_reading;

void loop() {
  
  current_reading= digitalRead(TASK1_BUTTON_PIN);
  
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
        // increment task1Duration and print the new duration
        task1Duration+= INCREMENT_TASK_DURATION_BY_THIS_AMOUNT;
        lcd.setCursor(0, 1);
        lcd.print(task1Duration);
      }
    }
  }
  
  // update the LED
  
  last_reading= current_reading;
}