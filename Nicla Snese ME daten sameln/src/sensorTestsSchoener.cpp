#include <Arduino.h>
#include "Arduino_BHY2.h"
#include "qspi_api.h"


// put function declarations here:
Sensor temperature(SENSOR_ID_TEMP); // Deklaration des Temperatursensors
Sensor gas(SENSOR_ID_GAS);         // Deklaration des Gassensors
Sensor humidity(SENSOR_ID_HUM);     // Deklaration des Feuchtigkeitssensors
Sensor pressure(SENSOR_ID_BARO);   // Deklaration des Drucksensors
SensorBSEC bsec(SENSOR_ID_BSEC);  // Deklaration des BSEC Sensors

// 
float satVaporPressure(float T_C) {
    return 6.112f * exp((17.62f * T_C) / (T_C + 243.12f));
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);               // Serielle Kommunikation starten
  BHY2.begin();                     // Beginn der BHY2 Kommunikation
  bsec.begin();                     // Beginn des BSEC Sensors

  temperature.begin();              // Initialisierung des Temperatursensors
  gas.begin();                      // Initialisierung des Gassensors
  humidity.begin();                 // Initialisierung des Feuchtigkeitssensors
  pressure.begin();                 // Initialisierung des Drucksensors

  delay(10000);

  // in python script ausgelagert 
  //Serial.println("temperature;gas;humidity;barometer;IAQ;IAQ_S;VOCS;accuracy"); 
}

void loop() {
  // put your main code here, to run repeatedly:
  static auto lastCheck= millis();   // Variableninitialisierung für die Zeitmessung
  BHY2.update();                    // Aktualisierung der BHY2 Daten
  // Check sensor values every second  
  if (millis() - lastCheck >= 1000) { // Überprüfung, ob eine Sekunde vergangen ist
    lastCheck = millis();            // Zurücksetzen des Zeitstempels

    float temp_sens= temperature.value();
    float temp_ref = temp_sens -6.0;
    float hum_sens = humidity.value();

    // Sättigungsdampfdruck und  relative luftfeuchtigkeit korregiert 
    float es_meas = satVaporPressure(temp_sens); // sens      (spzifischer dampf druck)
    float es_ref = satVaporPressure(temp_ref); // korrigiert (spzifischer dampf druck)
    float rh_correcteted = hum_sens * (es_meas/es_ref);

    Serial.print(String(temp_sens + String(";"))); // Temperatur ausgeben
    Serial.print(String(gas.value() + String(";")));                     // Gaswert ausgeben
    Serial.print(String(hum_sens + String(";")));           // Feuchtigkeit ausgeben
    Serial.print(String(pressure.value() + String(";")));           // Druck ausgeben
    Serial.print(String(bsec.iaq()) +String(";")+  String(bsec.iaq_s() + String(";"))); // IAQ Werte ausgeben
    Serial.print(String(bsec.b_voc_eq()+ String(";")));                 // VOCS Wert ausgeben
    Serial.print(String(bsec.accuracy()+ String(";")));
    Serial.print(String(rh_correcteted)+String(";"));
    Serial.print(String(temp_ref));
    //Serial.print(String("BSEC info: ") + bsec.toString());    
    //Serial.println(";");        // BSEC Informationen ausgeben
    Serial.println(" ");
  }
}