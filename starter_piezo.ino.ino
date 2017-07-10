#define NOTE_C4 262
#define NOTE_G3 196
#define NOTE_A3 220

int speakerPin = 8;
// notes for melody
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_A3
};

int noteDurations[] {
  4,8,8
};

void setup() {
  // put your setup code here, to run once:
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int thisNote = 0; thisNote < 3; thisNote++) {
    // Calculate note duration, take one second and divide it by the note type
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(speakerPin, melody[thisNote], noteDuration);

    // pause between your notes, notes duration + 30% works
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    noTone(speakerPin);
  }
}
