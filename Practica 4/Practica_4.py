import tkinter as tk


app = tk.Tk()
app.title("Conversoe de Temperatura")

label1 = tk.Label(app, text = "Fahrenheit:")
label1.grid(row = 0, column = 0)

entry1 = tk.Entry(app)
entry1.grid(row = 0, column = 1)

button1 = tk.Button(app, text = "Convertir a Celsius")#, command = convertir_a_celsius)
button1.grid(row = 0, column = 2)

label2 = tk.Label(app, text = "Celsius:")
label2.grid(row = 1, column = 0)

entry2 = tk.Entry(app)
entry2.grid(row = 1, column = 1)

button2 = tk.Button(app, text = "Convertir a Fahrenheit")#, command = convertir_a_Fahrenheit)
button2.grid(row = 1, column = 2)

button3 = tk.Button(app, text = "Restablecer")#, command = borrar)
button3.grid(row = 2, column = 1)

app.mainloop()
