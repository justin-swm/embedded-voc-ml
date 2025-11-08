import serial
import time

# Konfigurieren Sie die serielle Verbindung (Pfad zum COM-Port und Baudrate)
ser = serial.Serial('COM5', 115200)  # Ersetzen Sie 'COM3' durch den tatsächlichen COM-Port Ihres Arduino

# Datei zum Schreiben der Daten öffnen (mit 'a' statt 'w' für Anhängen)
file_path = r'C:\Users\justi\OneDrive\Dokumente\PlatformIO\Projects\Nicla Snese ME erste tests\sensor_data.txt'

# Schreibe Header-Zeile beim Start des Skripts
header = "timestamp;temperature;gas;humidity;barometer;IAQ;IAQ_S;VOCS;accuracy;humidty_corrected;temp_corrected"
with open(file_path, 'a') as file:  # Behalte den Append-Modus
    file.write(header + '\n')
    file.flush()

with open(file_path, 'a') as file:  # Behalte den Append-Modus für Daten
    while True:
        if ser.in_waiting > 0: 
            line = ser.readline().decode('utf-8').rstrip()

            try:
                # Füge Timestamp zur Zeile hinzu
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                line_with_timestamp = f"{timestamp};{line}"
                print(line_with_timestamp)  # Optional: Zeile im Terminal ausgeben
                file.write(line_with_timestamp + '\n')
                file.flush()
            except Exception as e:
                print(f"Fehler beim Schreiben in die Datei: {e}")
        time.sleep(0.1)



