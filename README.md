# softmarket-refactoring
# SoftMarket S.A. - Refactorización y Buenas Prácticas de Desarrollo

Este repositorio contiene la propuesta técnica y la simulación del módulo de facturación refactorizado para **SoftMarket S.A.**, abordando los problemas de mantenibilidad, acoplamiento y falta de control de versiones.

---

## 📋 Diagnóstico del Problema

El análisis del estado inicial identificó:
- **Alta duplicación de código** y falta de adherencia a principios DRY y SOLID.
- **Acoplamiento elevado** en el módulo de facturación (múltiples responsabilidades en una sola clase).
- **Ausencia de un flujo de trabajo formal en Git**, causando colisiones de código y falta de trazabilidad.
- **Inexistencia de pruebas unitarias automatizadas** y revisiones de código.

---

## 🌿 Modelo de Ramas (Git Flow)

Adoptamos la estrategia **Git Flow** para garantizar la estabilidad del software:

- `main`: Código estable y listo para producción (etiquetado con versiones `v1.0.0`).
- `develop`: Rama principal de integración continua donde se consolidan los cambios probados.
- `feature/*`: Desarrollo de nuevas funcionalidades (ejemplo: `feature/integracion-stripe`).
- `fix/*`: Corrección de errores detectados en desarrollo (ejemplo: `fix/validacion-correo-factura`).
- `hotfix/*`: Parches de emergencia para fallos críticos en producción (ejemplo: `hotfix/v1.0.1-error-monto`).

---

## 📝 Convención de Mensajes (Conventional Commits)

Todos los commits deben seguir el estándar de **Conventional Commits**:

- `feat:` Nuevas características o funcionalidades.
- `fix:` Correcciones de errores o bugs.
- `refactor:` Reestructuración de código sin alterar su comportamiento externo.
- `test:` Adición o modificación de pruebas unitarias.
- `docs:` Actualizaciones en la documentación.

---

## 🛠️ Refactorización con Principios SOLID

El módulo `facturacion.py` fue refactorizado aplicando:
1. **SRP (Single Responsibility):** Clases independientes para pasarela de pago, persistencia y notificaciones.
2. **OCP (Open/Closed):** Permite agregar nuevas pasarelas de pago (PayPal, Stripe) mediante la interfaz `IPagoProcessor` sin alterar la clase de servicio.
3. **LSP (Liskov Substitution):** Cualquier clase que implemente `IPagoProcessor` puede sustituir a otra sin romper la lógica.
4. **ISP (Interface Segregation):** Interfaces pequeñas y enfocadas (`IPagoProcessor`, `INotificador`, `IFacturaRepository`).
5. **DIP (Dependency Inversion):** `ServicioFacturacion` depende de abstracciones y no de implementaciones concretas.

---

## 🧪 Ejecución de Pruebas Unitarias

Para ejecutar las pruebas del proyecto localmente:

```bash
# 1. Instalar pytest
pip install pytest

# 2. Ejecutar la suite de pruebas
pytest
