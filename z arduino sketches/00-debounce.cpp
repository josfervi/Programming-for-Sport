/*
 Debounce
 inspired by: https://www.arduino.cc/en/Tutorial/Debounce 

 direct quote:
 "Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
 press), the output pin is toggled from LOW to HIGH or HIGH to LOW.  There's
 a minimum delay between toggles to debounce the circuit (i.e. to ignore
 noise).
 
 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground
 
 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example."
*/

// set some useful constants and initialize global variables

// use define instead of constants
#define LED_PIN LED_BUILTIN
#define ON      HIGH
#define OFF     LOW

#define BUTTON_PIN  2    // the number of the pushbutton pin
#define PRESSED     HIGH
#define NOT_PRESSED LOW

#define DEBOUNCE_TIME 50 // the debounce time; increase if the LED flickers,

// variables will change
int ledState= OFF;

int     buttonState= NOT_PRESSED;
int lastButtonState= NOT_PRESSED;

// the following variables are unsigned long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
unsigned long debouncingTimer_elapsedTime= 0;
unsigned long debouncingTimer_startTime=   0;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(   LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT );
  
  // start with the LED off
  digitalWrite(LED_PIN, OFF);
  
  Serial.begin(9600);
}

int count= 0; // counts the number of OFF to ON pushbutton transitions

int last_reading= LOW;
// the loop function runs over and over again forever
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
        // increment counter
        count++;
        Serial.println("ON");
        Serial.println("number of button pushes: ");
        Serial.println(count);
      }
      else {
        Serial.println("OFF");
      }
    }
  }
  
  // update the LED
  digitalWrite(LED_PIN, ledState);
  
  last_reading= current_reading;
}