import re
from datetime import datetime, timedelta

# Einstellungen
input_file = r"xalte_messungen\alte_abs_messung1.txt"
output_file = "druckdata_abs_alt.txt"
start_timestamp = datetime(2025, 9, 23, 12, 0, 0)  # Beispiel-Datum
interval_seconds = 30

def parse_line(line):
    """Einzelne Zeile parsen: 'temperature: 31' -> {'temperature': '31'}"""
    if ':' in line:
        key, value = line.split(':', 1)
        return {key.strip(): value.strip()}
    return {}

def parse_section(lines):
    """Ein Sektion (mehrere Zeilen) parsen"""
    data = {}
    for line in lines:
        if line.strip():
            parsed = parse_line(line)
            data.update(parsed)
    return data

# Hauptteil des Skripts
with open(input_file, 'r') as f:
    content = f.read()

# Teile den Inhalt in Abschnitte (durch Leerzeilen getrennt)
sections = [s.strip() for s in content.split('\n\n') if s.strip()]

with open(output_file, 'w') as out_f:
    # Schreibe Header
    out_f.write("timestamp;temperature;gas;humidity;barometer;IAQ;IAQ_S;VOCS;accuracy\n")
    
    current_time = start_timestamp
    
    for section in sections:
        lines = section.split('\n')
        data = parse_section(lines)
        
        # Werte extrahieren
        temperature = data.get('temperature', '0')
        gas = data.get('gas', '0')
        humidity = data.get('humidity', '0')
        pressure = data.get('pressure', '0')
        
        # IAQ und IAQ_S extrahieren
        iaq_line = data.get('IAQ', '0, 0')
        if isinstance(iaq_line, str) and ',' in iaq_line:
            parts = iaq_line.split(',')
            iaq = parts[0].strip().split(':')[-1].strip() if len(parts) > 0 else '0'
            iaq_s = parts[1].strip().split(':')[-1].strip() if len(parts) > 1 else '0'
        else:
            iaq = '0'
            iaq_s = '0'
        
        vocs = data.get('VOCS', '0')
        
        # accuracy extrahieren
        bsec_info = data.get('BSEC info', '')
        accuracy = '0'  # Standardwert
        
        if 'accuracy:' in bsec_info:
            try:
                # Finde den Wert nach "accuracy:"
                match = re.search(r'accuracy:\s*(\d+)', bsec_info)
                if match:
                    accuracy = match.group(1)
            except:
                pass
        
        # Formatieren des Timestamps
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Schreibe eine Zeile in der neuen Formatierung
        out_f.write(f"{timestamp};{temperature};{gas};{humidity};{pressure};{iaq};{iaq_s};{vocs};{accuracy}\n")
        
        # Nächster Timestamp (30 Sekunden später)
        current_time += timedelta(seconds=interval_seconds)
print("Finesched File: "+ output_file)