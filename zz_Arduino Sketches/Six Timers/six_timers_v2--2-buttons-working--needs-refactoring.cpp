/*
 Six Timers
 
 note: button pushes are debounced using a debounce time of DEBOUNCE_TIME
*/

typedef unsigned char BYTE;

// define bitmasks //
#define BIT1 ((const unsigned char) 1<<1)
#define BIT2 ((const unsigned char) 1<<2)
#define BIT3 ((const unsigned char) 1<<3)
#define BIT4 ((const unsigned char) 1<<4)
#define BIT5 ((const unsigned char) 1<<5)
#define BIT6 ((const unsigned char) 1<<6)

// define button pin definitions and Setup //
#define TASK1_BUTTON_PIN 11
#define TASK2_BUTTON_PIN 12
#define TASK3_BUTTON_PIN 13
// #define TASK4_BUTTON_PIN NA
// #define TASK5_BUTTON_PIN NA
// #define TASK6_BUTTON_PIN NA

// #define PRESSED     HIGH
// #define NOT_PRESSED LOW

#define DEBOUNCE_TIME 0UL // the debounce time; increase if the LED flickers;
                          // 0 is appropriate for circuits.io simulation
                          // try 50 for IRL execution

#define INCREMENT_TASK_DURATION_BY_THIS_AMOUNT 15

void configureEachButtonPinAsAnInput() {
  pinMode(TASK1_BUTTON_PIN, INPUT);
  pinMode(TASK2_BUTTON_PIN, INPUT);
  pinMode(TASK3_BUTTON_PIN, INPUT);
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
  configureEachButtonPinAsAnInput();
  setupShiftRegister();
  setupLCD();
}

// initialize led and button states
BYTE ledStates= 0;
BYTE     buttonStates= 0;
BYTE lastButtonStates= 0;

// TODO: consider making the timer an object with a startTime field, an elapsedTime field, and a resetTimer procedure
//       however, this will add a performance penalty, which is specially detrimental when executing on a 2KB 16MHz MCU

// the following variables are unsigned longs because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
unsigned long debouncingTimer1_elapsedTime= 0;
unsigned long debouncingTimer2_elapsedTime= 0;

unsigned long debouncingTimer1_startTime=   0;
unsigned long debouncingTimer2_startTime=   0;

int task1Duration= 0; // increments by INCREMENT_TASK_DURATION_BY_THIS_AMOUNT each time the task 1 button is pressed
int task2Duration= 0;

BYTE last_readings= 0;
BYTE current_readings= 0;

void setNthBitToX(unsigned char* byte_ptr, int n, signed char x) {
  // PRECONDITION: x is 0 or x is 1
  // sets the nth bit of byte to x
  // if the individual bits of byte where addressable, this function would be equivalent to byte[n]= x, where byte[n] accesses the nth bit of byte
  *byte_ptr^= (-x^*byte_ptr) & (1 << n);
}

void loop() {
  
  // TODO: this can be as small as a byte, but there is no byte primitive type in C++
  BYTE button1_reading= digitalRead(TASK1_BUTTON_PIN); // dbg
  setNthBitToX(&current_readings, 1, button1_reading);
  BYTE button2_reading= digitalRead(TASK2_BUTTON_PIN); // dbg
  setNthBitToX(&current_readings, 2, button2_reading);

  BYTE readings_changed= current_readings ^ last_readings; // TODO: this can be as small as a byte, but there is no byte primitive type in C++
  
  // first determine if a button's reading changed
  bool button1_reading_changed= readings_changed & BIT1;
  bool button2_reading_changed= readings_changed & BIT2;
  
  if (button1_reading_changed) { debouncingTimer1_elapsedTime= 0; debouncingTimer1_startTime= millis(); }
  else {
    debouncingTimer1_elapsedTime= millis() - debouncingTimer1_startTime;
    if (debouncingTimer1_elapsedTime > DEBOUNCE_TIME) {
      // the current reading has been held for longer than the debounce time,
      // so take it as the actual current state, but first save the previous state
      
      BYTE button1State= (buttonStates & BIT1) >> 1; // dbg
      setNthBitToX(&lastButtonStates, 1, button1State);

      BYTE current_button1_reading= (current_readings & BIT1) >> 1; // dbg
      setNthBitToX(&buttonStates, 1, current_button1_reading);
	  
      
      // only toggle the LED if the button went from being not pressed to being pressed
      if ( !(lastButtonStates & BIT1) && (buttonStates & BIT1) ) {
        // toggle the LED state
        ledStates^= BIT1;
        // increment task1Duration and print the new duration to the LCD
        task1Duration+= INCREMENT_TASK_DURATION_BY_THIS_AMOUNT;
        lcd.setCursor(0,1);
        lcd.print(task1Duration);
      }
    }
  }
  if (button2_reading_changed) { debouncingTimer2_elapsedTime= 0; debouncingTimer2_startTime= millis(); }
  else {
    debouncingTimer2_elapsedTime= millis() - debouncingTimer2_startTime;
    if (debouncingTimer2_elapsedTime > DEBOUNCE_TIME) {
      // the current reading has been held for longer than the debounce time,
      // so take it as the actual current state, but first save the previous state
      
      BYTE button2State= (buttonStates & BIT2) >> 2; // dbg
      setNthBitToX(&lastButtonStates, 2, button2State);
	  
      BYTE current_button2_reading= (current_readings & BIT2) >> 2; // dbg
      setNthBitToX(&buttonStates, 2, current_button2_reading);
	  
      // only toggle the LED if the button went from being not pressed to being pressed
      if ( !(lastButtonStates & BIT2) && (buttonStates & BIT2) ) {
        ledStates^= BIT2;
        // increment task2Duration and print the new duration to the LCD
        task2Duration+= INCREMENT_TASK_DURATION_BY_THIS_AMOUNT;
        lcd.setCursor(3,1);
        lcd.print(task2Duration);
      }
    }
  }
  
  // TODO: update the LED
  
  last_readings= current_readings;
}