import wikipedia as wiki
from tkinter import *

from wikipedia.wikipedia import search


## Estrutura da API
wiki.set_lang("pt")

#print(wikipedia.search("Bebeto"))




########################################################################################


## Janela TKinter

Application = Tk()
Application.title('PCA Sistemas de Informação Distribuida')
Application.geometry("700x675")
Application.configure(background= '#7B68EE')


#Clear
def clear():
      my_entry.delete(0, END)
      my_text.delete(0.0, END)
    
# Searcj
def search():
    data = wiki.summary(my_entry.get())
    #limpar tela
    clear()
    # Resultado wikipedia
    my_text.insert(0.0, data)
    



my_label_frame = LabelFrame(Application, text="Pesquisar", font=("Arial",19 ,),fg="#F8F8FF" ,background="#7B68EE")
my_label_frame.pack(pady=20)


#Caixa de Entrada
my_entry = Entry(my_label_frame, font=("Arial", 14), width=47)
my_entry.pack(pady=20, padx=20)


#Caixa de texto

my_frame = Frame(Application)
my_frame.pack(pady=5)

# Scroll verticl

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Scroll horizontal

hor_scroll =Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# text box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

#configuração da Scroll Bar
text_scroll.config(command=my_text.yview)
text_scroll.config(command=my_text.xview)

# Botões
button_frame = Frame(Application)
button_frame.pack(pady=10)

search_button = Button(button_frame, text='Pesquisar', font=("Arial", 20), fg="#F8F8FF", bg = "#BA55D3", command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text='Limpar', font=("Arial", 20), fg="#F8F8FF", bg = "#3CB371", command=clear)
clear_button.grid(row=0, column=1)





Application.mainloop()