/*
  LiquidCrystal Library - Hello World

 Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
 library works with all LCD displays that are compatible with the
 Hitachi HD44780 driver. There are many of them out there, and you
 can usually tell them by the 16-pin interface.
 
 adapted from: https://www.arduino.cc/en/Tutorial/HelloWorld
*/

#define RS_PIN  4 // the RS pin of the LCD is connected to pin 4 of the Arduino
#define EN_PIN  6
#define D4_PIN  8
#define D5_PIN  9
#define D6_PIN 10
#define D7_PIN 11

// include the library code:
#include <LiquidCrystal.h>

// initialize a LiquidCrystal object, lcd, with the numbers of the interface pins
LiquidCrystal lcd(RS_PIN, EN_PIN, D4_PIN, D5_PIN, D6_PIN, D7_PIN);

// the setup function runs once when you press reset or power the board
void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello world");
}

// the loop function runs over and over again forever
void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of milliseconds since reset:
  lcd.print( millis() );
}