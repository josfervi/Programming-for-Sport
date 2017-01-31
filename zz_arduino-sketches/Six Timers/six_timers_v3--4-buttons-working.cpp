/*
 Six Timers
 
 note: button pushes are debounced using a debounce time of DEBOUNCE_TIME
*/

// possible bug: BUILT_IN led turns on when I press the button connected to pin 13 and turns off when I click on another button
//         note: At this time, it is unknown whethere this bug is present only in simulation

typedef unsigned char BYTE;

// define button pin definitions and Setup //

#define NUMBER_OF_TASKS 4

#define TASK1_BUTTON_PIN 10
#define TASK2_BUTTON_PIN 11
#define TASK3_BUTTON_PIN 12
#define TASK4_BUTTON_PIN 13
// #define TASK5_BUTTON_PIN NA
// #define TASK6_BUTTON_PIN NA

const int BUTTON_PIN_OF_TASK[NUMBER_OF_TASKS] = {TASK1_BUTTON_PIN, TASK2_BUTTON_PIN, TASK3_BUTTON_PIN, TASK4_BUTTON_PIN};

#define PRESSED     HIGH
#define NOT_PRESSED LOW

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

#define LCD_SECOND_LINE 1

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
BYTE ledStates=        0b00000000;
BYTE     buttonStates= 0b00000000;
BYTE lastButtonStates= 0b00000000;

// TODO: consider making the timer an object with a startTime field, an elapsedTime field, and a resetTimer procedure
//       however, this will add a performance penalty, which is specially detrimental when executing on a 2KB 16MHz MCU

// the following variables are unsigned longs because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.

unsigned long debouncingTimer_elapsedTime [NUMBER_OF_TASKS] = {0UL, 0UL, 0UL, 0UL}; // TODO: is the default array value 0?
unsigned long debouncingTimer_startTime   [NUMBER_OF_TASKS]=  {0UL, 0UL, 0UL, 0UL}; // TODO: is the default array value 0?

int taskDuration [NUMBER_OF_TASKS] = {0, 0, 0, 0}; // task 1 duration increments by INCREMENT_TASK_DURATION_BY_THIS_AMOUNT each time the task 1 button is pressed, same is true for each button

BYTE last_readings=    0b00000000;
BYTE current_readings= 0b00000000;

void loop() {
  
  for (int task_number= 1; task_number <= NUMBER_OF_TASKS; task_number++) {
    
    const BYTE BITN= 1 << task_number;
    
    BYTE current_reading= digitalRead(BUTTON_PIN_OF_TASK[ task_number -1]);
    setNthBitToX(&current_readings, task_number, current_reading);
    
    BYTE last_reading= ( last_readings & BITN ) >> task_number;
    bool reading_changed= current_reading != last_reading;
    if (reading_changed) {
      // reset the debounce timer
      debouncingTimer_elapsedTime[task_number -1]= 0;
      debouncingTimer_startTime[task_number -1]=   millis();
    }
    else {
      debouncingTimer_elapsedTime[task_number -1]= millis() - debouncingTimer_startTime[task_number -1];
      
      if (debouncingTimer_elapsedTime[task_number -1] > DEBOUNCE_TIME) {
        // the current reading has been held for longer than the debounce time,
        // so take it as the actual current state, but firtst save the previous state
        
        BYTE lastButtonState= ( buttonStates & BITN ) >> task_number;
        setNthBitToX(&lastButtonStates, task_number, lastButtonState);
        
        BYTE buttonState= current_reading;
        setNthBitToX(&buttonStates, task_number, buttonState);
        
        // only toggle the LED if the button went from being not pressed to being pressed
        if ( (lastButtonState == NOT_PRESSED) && (buttonState == PRESSED) ) {
          // toggle the LED state
          ledStates^= BITN;
          // increment task duration and print the new duration to the lcd
          taskDuration[task_number -1]+= INCREMENT_TASK_DURATION_BY_THIS_AMOUNT;
          int col_num= (task_number - 1) * 3; 
          lcd.setCursor(col_num, LCD_SECOND_LINE);
          lcd.print(taskDuration[task_number -1]);
        }
      }
    }
    
  }
  
  // TODO: update LEDs
  

  last_readings= current_readings;
}

void setNthBitToX(unsigned char* byte_ptr, int n, signed char x) {
  // PRECONDITION: x is 0 or x is 1
  // sets the nth bit of byte to x
  // if the individual bits of byte where addressable, this function would be equivalent to byte[n]= x, where byte[n] accesses the nth bit of byte
  *byte_ptr^= (-x^*byte_ptr) & (1 << n);
}