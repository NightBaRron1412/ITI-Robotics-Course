#define sensorPin A0
#define LED 11
#define Button 2

enum ButtonState {
  Pressed,
  NotPressed,
};

char ButtonLastState = NotPressed;

void setup() {
  pinMode(11, OUTPUT);
  pinMode(2, INPUT_PULLUP);
}

void loop() {
  int reading = analogRead(sensorPin);
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  float temperatureC = (voltage - 0.5) * 100;

  char ButtonState = digitalRead(Button);

  if (ButtonState == Pressed && ButtonLastState == NotPressed) {
    digitalWrite(LED, LOW);
    ButtonLastState = Pressed;
  }

  if (temperatureC > 40) {
    if (ButtonState == NotPressed && ButtonLastState == NotPressed) {
      digitalWrite(LED, HIGH);
    }
  } else {
    ButtonLastState = NotPressed;
  }
}