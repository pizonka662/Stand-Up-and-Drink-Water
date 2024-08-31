// Min and max height of my desk
#define heightMin 72.0
#define heightMax 115.0

// Min and max weight of my bottle
#define weightMin 1.0
#define weightMax 2.0

// Delay between each report
#define reportDelay 200

void setup() {
  // Start by starting the Serial function
  Serial.begin(115200);
}

void loop() {
  // Get the time now and store it
  unsigned long time = millis();
  // First, we calculate what we think the height is. Initialize it...
  float height = 0.0;
  // We're gonna use a function which starts with it low, then
  //   (non-instantaneously) raises it, keeps it high for a bit, then 
  //   (non-instantaneously) lowers it.
  // Convert the time to a position in a cycle
  unsigned long height_time = time % 20000;
  if (height_time < 9000) {
    height = heightMin;
  } else if (height_time < 10000) {
    height = int(heightMin + ((heightMax - heightMin) * (float(height_time - 9000) / 1000)));
  } else if (height_time < 19000) {
    height = heightMax;
  } else {
    height = int(heightMax - ((heightMax - heightMin) * (float(height_time - 19000) / 1000)));
  }

  //Next, the weight. Initialize it...
  float weight = 0.0;
  // The function is going to start with it full, then slowly drain it,
  //   then refill it instantaneously.
  // Sometimes, though, it's going to read close to 0, representing the bottle being picked up
  if (random(1000) < 200) {
    weight = 0.01;
  } else {
    unsigned long weight_time = time % 11000;
    if (weight_time < 1000) {
      weight = weightMax;
    } else if (weight_time < 9000) {
      weight = weightMax - ((weightMax - weightMin) * (weight_time - 1000) / 8000);
    } else {
      weight = weightMin;
    }
  }

  Serial.print(height);
  Serial.print("|");
  Serial.println(weight);

  delay(reportDelay);
}
