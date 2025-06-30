# 🛡️ Informe de Gestión de Calidad – CafféFlux

## 🗂️ Resumen

Este documento presenta las actividades realizadas para asegurar la calidad del software CafféFlux. Incluye evidencia de planificación, control de calidad, testing, verificación y validación, así como el uso justificado de herramientas en cada etapa del ciclo de desarrollo.

---

## 1.Gestión de Calidad (Planificación)

| Actividad                                | Evidencia                                                |
|------------------------------------------|----------------------------------------------------------|
| Historias de usuario con Criterios y DoD | Issues detallados en GitHub (`/issues`)                 |
| Análisis de riesgos por historia         | Riesgos registrados en cada historia de usuario          |
| Sprint cerrado con milestones            | Milestone activo con historias priorizadas y fechadas    |

---

## 2.Control de Calidad

| Actividad                                      | Evidencia                                           |
|------------------------------------------------|-----------------------------------------------------|
| Revisión de código con **Codacy**              | Reporte automático en GitHub / Captura en `docs/`   |
| Arquitectura modular según principios SOLID    | Separación clara en `/models`, `/controllers`, `/views` |
| Revisión visual y funcional (interfaz GUI)     | Capturas en `demo/` y validación manual             |

---

## 3.Testing

| Tipo de Prueba        | Evidencia                                                  |
|------------------------|------------------------------------------------------------|
| Pruebas unitarias      | Archivo `tests/test_productos.py`                         |
| Testpad (o TestRail) | Gestión de Calidad | Registro manual de pruebas realizadas, validación de criterios de aceptación.|
| Pruebas de integración | Flujo validado entre vista, controlador y persistencia JSON|
| Pruebas de sistema     | Flujo completo verificado desde el menú principal          |

---

## 4.Herramientas de Calidad

| Herramienta       | Categoría              | Justificación                                                                 |
|--------------------|------------------------|-------------------------------------------------------------------------------|
| **Codacy**         | Control de calidad     | Análisis de código Python: estilo, errores, duplicación                      |
| **GitHub Projects**| Gestión de calidad     | Planificación y seguimiento del sprint, issues y milestones                  |
| **Pruebas manuales** | Testing                | Validación directa de interfaz y flujos principales del sistema              |

---
