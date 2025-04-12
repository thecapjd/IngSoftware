# Detección de Exfiltración en Logs de Red

Script en Python para detectar posibles fugas de datos a través del análisis de logs, identificando IPs con tráfico excesivo.

## Objetivo

Detectar transferencias anómalas de datos por IP usando logs de red.

## Tecnologías

- Python 3
- re, defaultdict
- unittest

##  Uso

1. Tener Python 3 instalado.  
2. Ejecutar el script: python log_parser.py
3. Ejecutar pruebas: python test_log_parser.py

## Umbral

Valor por defecto:

```python
THRESHOLD_BYTES = 5000