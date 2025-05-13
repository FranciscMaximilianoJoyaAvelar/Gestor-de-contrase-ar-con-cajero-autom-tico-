import tkinter as tk
from tkinter import simpledialog, messagebox
import random

#  PIN de 4 números
def generar_pin():
    numeros = "0123456789"
    pin = ''.join(random.choice(numeros) for _ in range(4))
    messagebox.showinfo("PIN generado", f"Tu PIN es: {pin}")
    return pin

# Variables 
saldo = 1000
intentos = 0
pin_correcto = None

# PIN oculto con entrada personalizada
def pedir_pin_oculto():
    pin_window = tk.Toplevel(ventana)
    pin_window.title("Ingresa tu PIN")
    tk.Label(pin_window, text="PIN:").pack(pady=5)
    pin_entry = tk.Entry(pin_window, show="*", justify='center')
    pin_entry.pack(pady=5)

    def validar():
        pin = pin_entry.get()
        pin_window.destroy()
        verificar_pin(pin)

    tk.Button(pin_window, text="Aceptar", command=validar).pack(pady=5)
    pin_window.transient(ventana)
    pin_window.grab_set()
    ventana.wait_window(pin_window)

# Verificar PIN 
def verificar_pin(pin_ingresado):
    global intentos
    if pin_ingresado == pin_correcto:
        messagebox.showinfo("Acceso", "PIN correcto")
        mostrar_menu()
    else:
        intentos += 1
        if intentos >= 3:
            messagebox.showerror("Bloqueado", "Demasiados intentos.")
            ventana.destroy()
        else:
            messagebox.showwarning("Error", f"PIN incorrecto. Intento {intentos}/3")
            pedir_pin_oculto()  # Reintentar PIN si fue incorrecto

# Funciones del cajero
def consultar_saldo():
    messagebox.showinfo("Saldo", f"Tu saldo es: ${saldo:.2f}")

def depositar():
    global saldo
    cantidad = simpledialog.askfloat("Depósito", "¿Cuánto deseas depositar?")
    if cantidad and cantidad > 0:
        saldo += cantidad
        messagebox.showinfo("Depósito", f"Nuevo saldo: ${saldo:.2f}")
    else:
        messagebox.showerror("Error", "Cantidad inválida")

def retirar():
    global saldo
    cantidad = simpledialog.askfloat("Retiro", "¿Cuánto deseas retirar?")
    if cantidad and 0 < cantidad <= saldo:
        saldo -= cantidad
        messagebox.showinfo("Retiro", f"Nuevo saldo: ${saldo:.2f}")
    else:
        messagebox.showerror("Error", "Cantidad inválida o saldo insuficiente")

    #  menú principal
def mostrar_menu():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Cajero Automático", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana, text="Consultar saldo", command=consultar_saldo, width=30).pack(pady=5)
    tk.Button(ventana, text="Depositar dinero", command=depositar, width=30).pack(pady=5)
    tk.Button(ventana, text="Retirar dinero", command=retirar, width=30).pack(pady=5)
    tk.Button(ventana, text="Salir", command=ventana.destroy, width=30).pack(pady=10)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cajero Automático")
ventana.geometry("300x300")

# Iniciar flujo
pin_correcto = generar_pin()
pedir_pin_oculto()

ventana.mainloop()
# Fin del programa
# Este código es un cajero automático simple que permite al usuario consultar saldo, depositar y retirar dinero.
# Se utiliza tkinter para la interfaz gráfica y random para generar un PIN aleatorio.
# El PIN se oculta al ingresarlo y se valida con un máximo de 3 intentos.
# El saldo inicial es de $1000 y se actualiza después de cada operación.
# El programa finaliza si el usuario ingresa el PIN incorrecto 3 veces o cierra la ventana.
# Se pueden agregar más funcionalidades como transferencias, historial de transacciones, etc.