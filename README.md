# embedded-voc-ml  

Entwicklung und Test neuronaler Netze mithilfe von Edge Impulse auf einem Mikrocontroller zur Detektion und Klassifikation von flüchtigen organischen Verbindungen (VOCs)

## Allgemeine Informationen  

[Edge Impulse Projekt](https://studio.edgeimpulse.com/public/729880/live)

Das Repository besteht aus drei Unterordnern. Die beiden Code-Projekte sind PlatformIO-Projekte, die einzeln in PlatformIO geöffnet werden sollten. Ggf. sind Abhängigkeiten zu Bibliotheken zu beachten.

Im Abschnitt *anderes* finden sich die Dateien des FlexPro-Projekts. Außerdem ist dort eine als HTML exportierte Version von FlexPro enthalten, mit der das Betrachten aller Daten auch ohne FlexPro im Browser möglich ist.

## Daten sammeln  

Das Projekt [Nicla Sense ME Daten sammeln](https://github.com/justin-swm/embedded-voc-ml/tree/main/Nicla%20Snese%20ME%20daten%20sameln) besteht aus einer Reihe von Dateien. Die wichtigste Datei ist dabei [sensorTestsSchoener.cpp](https://github.com/justin-swm/embedded-voc-ml/blob/main/Nicla%20Snese%20ME%20daten%20sameln/src/sensorTestsSchoener.cpp), der Code, der für die Erfassung der Sensordaten verantwortlich ist. Er wird auf dem Arduino ausgeführt.

Zum Speichern der Daten in TXT-Dateien dient das Python-Skript [serial_logger.py](https://github.com/justin-swm/embedded-voc-ml/blob/main/Nicla%20Snese%20ME%20daten%20sameln/serial_logger.py).

Zudem gibt es einige weitere Dateien, die im Laufe der Entwicklung hinzugekommen sind, wie die Korrektur der Luftfeuchtigkeitsmessung [HumidtyKorrektur.cpp](https://github.com/justin-swm/embedded-voc-ml/blob/main/Nicla%20Snese%20ME%20daten%20sameln/HumidtyKorrektur.cpp), um Tests durchzuführen, oder Skripte, um ältere Textdateien in ein neues Format zu überführen ([file_reconstructer.py](https://github.com/justin-swm/embedded-voc-ml/blob/main/Nicla%20Snese%20ME%20daten%20sameln/file_reconstructer.py)).

Die [platformio.ini](https://github.com/justin-swm/embedded-voc-ml/blob/main/Nicla%20Snese%20ME%20daten%20sameln/platformio.ini)-Datei enthält Konfigurationen für das Projekt.

Die gesammelten Trainings- und Testdaten befinden sich unter [Used_data](https://github.com/justin-swm/embedded-voc-ml/tree/main/Nicla%20Snese%20ME%20daten%20sameln/Used_data).

Die Ergebnisse des späteren Tests des fertigen Modells sind teilweise unter [finale_tests](https://github.com/justin-swm/embedded-voc-ml/tree/main/Nicla%20Snese%20ME%20daten%20sameln/finale_tests) zu finden.

## Modellausführung  

Das Projekt zur Modellausführung besteht im Kern aus dem [main_workingCode.cpp](https://github.com/justin-swm/embedded-voc-ml/blob/main/nicla_sense_ingestion/src/main_workingCode.cpp), der ausgeführt wird. Er wurde auf Basis von Edge Impulse erstellt und lediglich modifiziert bzw. erweitert. Ein wesentlicher Bestandteil zur Ausführung ist die von Edge Impulse generierte Bibliothek [TestForSmokeRekognition_inferencing](https://github.com/justin-swm/embedded-voc-ml/tree/main/nicla_sense_ingestion/lib/TestForSmokeRekognition_inferencing). Sie enthält auch das Code-Beispiel, das modifiziert wurde: [nicla_sense_fusion.ino](https://github.com/justin-swm/embedded-voc-ml/blob/main/nicla_sense_ingestion/lib/TestForSmokeRekognition_inferencing/examples/nicla_sense/nicla_sense_fusion/nicla_sense_fusion.ino). Die Bibliothek enthält den gesamten Impulse, in diesem Fall in der deployten Version 11. Der Code ist spezifisch auf den Nicla Sense ME ausgelegt und nicht mit anderen Geräten kompatibel.

Die Konfigurationen des Impulses sind in [model-parameters](https://github.com/justin-swm/embedded-voc-ml/blob/main/nicla_sense_ingestion/lib/TestForSmokeRekognition_inferencing/src/model-parameters/model_metadata.h) enthalten, wie z. B. Sample Länge, Anzahl der Processing-Blöcke usw.

Das eigentliche Modell liegt im Ordner [tflite-model](https://github.com/justin-swm/embedded-voc-ml/tree/main/nicla_sense_ingestion/lib/TestForSmokeRekognition_inferencing/src/tflite-model).

Der Code, der die eigentliche Logik enthält, befindet sich im Ordner [edge-impulse-sdk](https://github.com/justin-swm/embedded-voc-ml/tree/main/nicla_sense_ingestion/lib/TestForSmokeRekognition_inferencing/src/edge-impulse-sdk).

## Weitere Materialien  

In diesem Ordner befinden sich zusätzliche Daten, die nicht direkt zu Code gehören. Dazu gehört die Projektdatei von FlexPro.

Damit die Daten auch ohne FlexPro betrachtet werden können, wurden sie als [FlexPro_Export](https://github.com/justin-swm/embedded-voc-ml/tree/main/anderes/Flexpro_Export) als HTML-Dateien exportiert, sodass die erstellten Grafiken im Browser betrachtet werden können. Hierbei liegt eine grobe Einteilung nach gemessenen Klassen vor.

Zum Betrachten der Daten sollte die Datei heruntergeladen werden und der Zugriff über die [default.htm](https://github.com/justin-swm/embedded-voc-ml/blob/main/anderes/Flexpro_Export/default.htm) gestartet werden, da dort auf der linken Seite eine Menüansicht verfügbar ist.

Alternativ können auch nur die jeweiligen PNG-Dateien im [abs_box_werte](https://github.com/justin-swm/embedded-voc-ml/tree/main/anderes/Flexpro_Export/abs_box_werte) Ordner oder dessen Unterordnern betrachtet werden.

## Hinweis

Das Readme wurde händisch erstellt und mithifle KI tool in der rechtschreibung korgiert.
Bei fehlern oder problemen und zum code verständniss wurde ein KI Coding Assistent (ChatGpt) verwendet.

---
