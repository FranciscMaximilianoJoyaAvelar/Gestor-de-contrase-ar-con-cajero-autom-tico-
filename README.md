# Gestor-de-contrase-ar-con-cajero-autom-tico-
Proyecto de Programación estructurada 
# Cajero Automático en Python 🏧

Este es un proyecto de simulación de un cajero automático con una interfaz gráfica utilizando la biblioteca `tkinter` en Python. El sistema permite al usuario generar un PIN de seguridad y realizar operaciones básicas como consultar el saldo, depositar y retirar dinero.

## 📝 Descripción del Proyecto

El programa simula un cajero automático sencillo que:
- Genera un PIN aleatorio de 4 caracteres al iniciar.
- Solicita el PIN al usuario para acceder al menú principal.
- Permite realizar operaciones básicas bancarias.
- Cuenta con un sistema de seguridad que bloquea el acceso tras tres intentos fallidos.

El proyecto fue desarrollado como parte de una práctica de programación con interfaces gráficas.

---

## ⚙️ Instrucciones para Ejecutarlo

### Requisitos

- Python 3.x instalado en tu sistema.
- No se requieren librerías externas, ya que `tkinter` y `random` vienen con la biblioteca estándar de Python.

### Ejecución

1. Descarga o clona este repositorio:

```bash
git clone https://github.com/tu-usuario/cajero-python.git
cd cajero-python
```

2. Ejecuta el archivo principal:

```bash
python cajero.py
```

> Al iniciar, se mostrará tu PIN generado. Guárdalo, ya que lo necesitarás para acceder al menú.

---

## ✅ Funcionalidades Implementadas

- 🔐 **Generación de PIN aleatorio** (letras, números y símbolos).
- 🔁 **Verificación del PIN** con hasta 3 intentos.
- 💰 **Consulta de saldo**.
- ➕ **Depósito de dinero** con validación de entrada.
- ➖ **Retiro de dinero** con verificación de saldo disponible.
- ❌ **Bloqueo del sistema** tras 3 intentos fallidos.
- 🖥️ **Interfaz gráfica amigable** creada con `tkinter`.

---

## 📌 Notas
- No se guardan los datos (el saldo se reinicia cada vez que se ejecuta).
- Ideal para prácticas académicas o como base para proyectos más complejos.

---

## 🧑‍💻 Autores
- Francisco Maximiliano Joya Avelar
- francisco.joya3394@alumnos.udg.mx
- Alejandro Navarro Gómez
- alejandro.navarro8776@alumnos.udg.mx
- CuALTOS(Programacion estructurada)

