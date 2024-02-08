import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jonathan Adrian
apellido: Aguirre
tutor: Alejandro
---
Ejercicio: entrada_salida_09bis
---
Enunciado:
Al presionar el botón 'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo_a_text = self.txt_sueldo.get()
        sueldo_a_numero = int(sueldo_a_text)
        incremento_a_text = self.txt_incremento.get()
        incremento_a_numero = int(incremento_a_text)
        incremento = sueldo_a_numero * incremento_a_numero / 100
        importe_de_sueldo_Actualizado = int(sueldo_a_numero + incremento)
        mensaje = "El incremento de sueldo da: {1}".format(sueldo_a_numero,importe_de_sueldo_Actualizado)
        alert("resultado", mensaje)
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()