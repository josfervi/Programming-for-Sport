// The circuit can be found and simulated here: (you may need to edit the circuit)
// https://circuits.io/circuits/3406860-six-timers/

//**************************************************************//
//  Name    : shiftOutCode, Hello World                                
//  Author  : Carlyn Maw, Tom Igoe, David A. Mellis 
//  Date    : 25 Oct, 2006    
//  Modified: 23 Mar 2010                                 
//  Version : 2.0                                             
//  Notes   : Code for using a 74HC595 Shift Register           //
//          : to count from 0 to 255 and display the binary in 8 LEDs
//
//  adapted by Jose Villegas
//****************************************************************

#include <math.h>

// Shift Register Pin Defintions //

#define DATA_PIN  13 //The Arduino Pin connected to DS of 74HC595
#define LATCH_PIN 12 //The Arduino Pin connected to ST_CP of 74HC595
#define HOLD      LOW
#define GO        HIGH
#define CLOCK_PIN 11 //The Arduino Pin connected to SH_CP of 74HC595

#define NUMBER_OF_LEDS 5

void setupShiftRegister() {
  //set pins to output so you can control the shift register
  pinMode(DATA_PIN,  OUTPUT);
  pinMode(LATCH_PIN, OUTPUT);
  pinMode(CLOCK_PIN, OUTPUT);
  
  // the SR is a rising edge SR so start with the clock low
  digitalWrite(CLOCK_PIN, LOW);
}

void setup() {
  setupShiftRegister();
}

void loop() {
  // count from 0 to pow(2, NUMBER_OF_LEDS) and display the binary represenation of that number 
  // on the LEDs
  for (int numberToDisplay= 0; numberToDisplay < pow(2, NUMBER_OF_LEDS); numberToDisplay++) {
    // take the LATCH_PIN low so 
    // the LEDs don't change while you're sending in bits:
    digitalWrite(LATCH_PIN, HOLD);
    // shift out the bits:
    shiftOut(DATA_PIN, CLOCK_PIN, LSBFIRST, numberToDisplay);  

    //take the latch pin high so the LEDs will light up:
    digitalWrite(LATCH_PIN, GO);
    // pause before next value:
    delay(500);
  }
}