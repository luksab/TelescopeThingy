#define X_STEP_PIN         61
#define X_DIR_PIN          62
#define X_ENABLE_PIN       60

#define Y_STEP_PIN         64
#define Y_DIR_PIN          65
#define Y_ENABLE_PIN       63

char receivedChar;

void setup() {
  pinMode(X_STEP_PIN, OUTPUT);
  pinMode(X_DIR_PIN, OUTPUT);
  pinMode(X_ENABLE_PIN, OUTPUT);
  pinMode(Y_STEP_PIN, OUTPUT);
  pinMode(Y_DIR_PIN, OUTPUT);
  pinMode(Y_ENABLE_PIN, OUTPUT);
  digitalWrite(X_ENABLE_PIN, LOW);
  digitalWrite(X_DIR_PIN, HIGH);
  digitalWrite(Y_ENABLE_PIN, LOW);
  digitalWrite(Y_DIR_PIN, HIGH);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    receivedChar = Serial.read();
    if (receivedChar == 'X') {
      digitalWrite(X_DIR_PIN, HIGH);
      stepX();
    }
    else if (receivedChar == 'x') {
      digitalWrite(X_DIR_PIN, LOW);
      stepX();
    }
    else if (receivedChar == 'Y') {
      digitalWrite(X_DIR_PIN, HIGH);
      stepY();
    }
    else if (receivedChar == 'y') {
      digitalWrite(X_DIR_PIN, LOW);
      stepY();
    }
  }
}

void stepY() {
  digitalWrite(Y_STEP_PIN, HIGH);
  delay(1);
  digitalWrite(Y_STEP_PIN, LOW);
  delay(1);
}

void stepX() {
  delay(1);
  digitalWrite(X_STEP_PIN, HIGH);
  delay(1);
  digitalWrite(X_STEP_PIN, LOW);
}
