# FH5 Sniping Script (DVIX-DEV FORK)

Script de automatización en Python para Forza Horizon 5, diseñado para realizar ciclos de compra (“sniping”) **con mecanismos de seguridad** que evitan enviar inputs a otras aplicaciones por error.

⚠️ **Úsalo bajo tu responsabilidad**. Este script automatiza entradas de teclado.

---

## ✅ Características principales

- 🔒 **Protección por foco de ventana**
  - El script **solo funciona** si la ventana activa es *Forza Horizon 5*.
  - Si el foco cambia (Xbox App, navegador, escritorio, etc.), el script se detiene inmediatamente.

- 🛑 **Kill switch manual**
  - Pulsa **ESC** en cualquier momento para detener el script de forma segura.

- 📊 Contadores en tiempo real
  - Número de intentos
  - Tiempo total de ejecución (segundos y minutos)

---

## 🧠 Cómo funciona la seguridad

### Opción A — Control de foco
Antes de **cada ciclo de inputs**, el script:
1. Comprueba la ventana activa.
2. Verifica que el título contenga `Forza Horizon 5`.
3. Si no coincide → **termina el programa**.

Esto previene compras, denuncias o acciones accidentales en otras apps.

### Opción B — Escape de emergencia
- La tecla **ESC** detiene el script desde cualquier estado (menú, countdown, loop principal).

---

## 📦 Requisitos

- Windows 10 / 11
- Python 3.9 o superior
- Forza Horizon 5 en **modo ventana o sin bordes** (recomendado)

---

## 📥 Instalación

1. Clona o descarga el repositorio
2. Instala dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

1. Abre **Forza Horizon 5**
2. Selecciona el coche y el precio máximo
3. Ejecuta el script:

```bash
python FH5-SnipingScript.py
```

4. Cuando empiece la cuenta atrás:
   - Asegúrate de que **FH5 tiene el foco**
5. Para detener:
   - Cambia de ventana ❌  
   - o pulsa **ESC** ✅

---

## ⚠️ Advertencias importantes

- No ejecutes el script en segundo plano.
- No lo dejes sin supervisión.
- No modifiques los delays sin entender el flujo del juego.
- El uso de macros puede violar los términos del juego.

---

## 🛠️ Posibles mejoras futuras

- Detección por PID en lugar de título de ventana
- Modo pausa/reanudación
- Logs a archivo
- Configuración por archivo `.ini`

---

## 📜 Licencia

Uso personal y educativo.  
No se ofrece ninguna garantía.
