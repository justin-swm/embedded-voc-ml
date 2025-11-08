#include "Nicla_System.h"
#include "Arduino_BHY2.h"


unsigned long previousMillis = 0;  // will store last time the sensor was updated

const long interval = 1000;

SensorBSEC bsec(SENSOR_ID_BSEC);    // 4-in-1 sensor.

void setup() {

  Serial.begin(9600);
  nicla::begin();
  BHY2.begin(NICLA_I2C);
  bsec.begin();
}

void loop() {

  BHY2.update();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {

    previousMillis = currentMillis;

    Serial.println(bsec.toString());
  }
}