import tkinter as tk

def encdec(mensaje, clave, modo):
    mensaje = mensaje.upper()
    traduccion = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for simbolo in mensaje:
        if simbolo in letras:
            num = letras.find(simbolo)
            if modo == "cifrar":
                num = num + clave
            elif modo == "descifrar":
                num = num - clave

            if num >= len(letras):
                num -= len(letras)
            elif num < 0:
                num += len(letras)

            traduccion += letras[num]
        else:
            traduccion += simbolo
    return traduccion

def abrir_ventana1():
    ventana1 = tk.Toplevel()
    ventana1.title("Encriptar")
    ventana1.configure(bg="lightgray")
    ventana1.geometry("350x230")

    def obtener_texto():
        texto = entry.get()
        clave = len([c for c in texto if c.isalpha()]) + 5
        resultado.config(text=f"El mensaje encriptado es: {encdec(texto, clave, 'cifrar')}")

    label = tk.Label(ventana1, text="Introduce el mensaje a encriptar:", bg="lightgray")
    label.pack(pady=10)

    entry = tk.Entry(ventana1)
    entry.pack()

    button = tk.Button(ventana1, text="Aceptar", command=obtener_texto)
    button.pack(pady=10)

    resultado = tk.Label(ventana1, text="", bg="lightgray")
    resultado.pack()

    # Botón para regresar a la ventana principal
    button_regresar = tk.Button(ventana1, text="Regresar", command=ventana1.destroy)
    button_regresar.pack(pady=10)

def abrir_ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title("Desencriptar")
    ventana2.configure(bg="lightgray")
    ventana2.geometry("350x230")

    def obtener_texto():
        texto = entry.get()
        clave = len([c for c in texto if c.isalpha()]) + 5
        resultado.config(text=f"El mensaje desencriptado es: {encdec(texto, clave, 'descifrar')}")

    label = tk.Label(ventana2, text="Introduce el mensaje a desencriptar:", bg="lightgray")
    label.pack(pady=10)

    entry = tk.Entry(ventana2)
    entry.pack()

    button = tk.Button(ventana2, text="Aceptar", command=obtener_texto)
    button.pack(pady=10)

    resultado = tk.Label(ventana2, text="", bg="lightgray")
    resultado.pack()

    # Botón para regresar a la ventana principal
    button_regresar = tk.Button(ventana2, text="Regresar", command=ventana2.destroy)
    button_regresar.pack(pady=10)

# Crear una ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Método Cesar")
ventana_principal.geometry("350x230")
ventana_principal.configure(bg="lightgray")

etiqueta = tk.Label(ventana_principal, text="¿Qué es lo que quieres realizar?", bg="lightgray", font=("Arial", 14, "bold"))
etiqueta.pack(pady=20)

# Crear dos botones
button1 = tk.Button(ventana_principal, text="Encriptar", command=abrir_ventana1, width=15)
button1.pack(pady=10)

button2 = tk.Button(ventana_principal, text="Desencriptar", command=abrir_ventana2, width=15)
button2.pack(pady=10)

# Botón para cerrar la ventana principal y todas las ventanas secundarias
button_cerrar = tk.Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy)
button_cerrar.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana_principal.mainloop()
