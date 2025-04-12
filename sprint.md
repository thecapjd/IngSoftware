# Planificación del Sprint 1

**Sprint de 1 semana – objetivo: tener un script funcional con alerta básica**

## Historias del Sprint
- HU-01: Análisis de tráfico en logs  
- HU-02: Detección de exfiltración por umbral de bytes  
- HU-03: Reporte de uso por IP

---

## Tareas desglosadas

### Para HU-01
- **Tarea 1.1:** Leer el archivo `network.log`. *(0.5 días)*  
- **Tarea 1.2:** Extraer IP y cantidad de bytes usando expresión regular. *(0.5 días)*

---

### Para HU-02
- **Tarea 2.1:** Definir un umbral de bytes (ej. 5000). *(0.25 días)*  
- **Tarea 2.2:** Detectar si alguna IP supera el umbral. *(0.5 días)*  
- **Tarea 2.3:** Mostrar mensaje de alerta por consola. *(0.25 días)*

---

### Para HU-03
- **Tarea 3.1:** Guardar la suma total de bytes transferidos por cada IP. *(0.5 días)*  
- **Tarea 3.2:** Imprimir el reporte general al final. *(0.25 días)*

---

## Tiempo total estimado:
**3.25 días** (de los 5 laborales en un sprint semanal)  
→ Esto deja margen para **imprevistos, revisiones o mejoras** (como empezar HU-04).

---

## Objetivo del Sprint:
Tener una primera versión funcional del programa que:

- Analice el archivo de log  
- Detecte comportamientos sospechosos  
- Entregue un reporte final simple y útil