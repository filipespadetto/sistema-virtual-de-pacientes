from tkinter import *
import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS paciente (idpaciente int, nome text)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS agenda (idpaciente int, data text, horario text, tempo text, tipo text, valor real)""")
conn.commit()
class Application:
	def __init__(self, master=None):
	
		self.fontePadrao = ("Arial", "10")
		
		self.container1 = Frame(master)
		self.container1["pady"] = 10
		self.container1.pack()

		self.container2 = Frame(master)
		self.container2["pady"] = 10
		self.container2.pack()

		self.container3 = Frame(master)
		self.container3["pady"] = 10
		self.container3.pack()

		self.container4 = Frame(master)
		self.container4["pady"] = 10
		self.container4.pack()

		self.container5 = Frame(master)
		self.container5["pady"] = 10
		self.container5.pack()

		self.container6 = Frame(master)
		self.container6["pady"] = 10
		self.container6.pack()

		self.container7 = Frame(master)
		self.container7["pady"] = 10
		self.container7.pack()

		self.container8 = Frame(master)
		self.container8["pady"] = 10
		self.container8.pack()

		self.container9 = Frame(master)
		self.container9["pady"] = 10
		self.container9.pack()

		self.container10 = Frame(master)
		self.container10["pady"] = 10
		self.container10.pack()

		self.titulo = Label(self.container1, text="Dados do paciente")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		self.idLabel = Label(self.container2,text="ID       ", font=self.fontePadrao)
		self.idLabel.pack(side=LEFT)

		self.txtidpaciente = Entry(self.container2)
		self.txtidpaciente["width"] = 30
		self.txtidpaciente["font"] = self.fontePadrao
		self.txtidpaciente.pack(side=LEFT)

		self.nomeLabel = Label(self.container3, text="Nome   ", font=self.fontePadrao)
		self.nomeLabel.pack(side=LEFT)

		self.txtnome = Entry(self.container3)
		self.txtnome["width"] = 30
		self.txtnome["font"] = self.fontePadrao
		self.txtnome.pack(side=LEFT)

		self.dataLabel = Label(self.container4, text="Data    ", font=self.fontePadrao)
		self.dataLabel.pack(side=LEFT)
		
		self.txtdata = Entry(self.container4)
		self.txtdata["width"] = 30
		self.txtdata["font"] = self.fontePadrao
		self.txtdata.pack(side=LEFT)

		self.horarioLabel = Label(self.container5, text="Horario", font=self.fontePadrao)
		self.horarioLabel.pack(side=LEFT)
		
		self.txthorario = Entry(self.container5)
		self.txthorario["width"] = 30
		self.txthorario["font"] = self.fontePadrao
		self.txthorario.pack(side=LEFT)

		self.tempoLabel = Label(self.container6, text="Tempo ", font=self.fontePadrao)
		self.tempoLabel.pack(side=LEFT)
		
		self.txttempo = Entry(self.container6)
		self.txttempo["width"] = 30
		self.txttempo["font"] = self.fontePadrao
		self.txttempo.pack(side=LEFT)
		
		self.tipoLabel = Label(self.container7, text="Tipo     ", font=self.fontePadrao)
		self.tipoLabel.pack(side=LEFT)
		
		self.txttipo = Entry(self.container7)
		self.txttipo["width"] = 30
		self.txttipo["font"] = self.fontePadrao
		self.txttipo.pack(side=LEFT)
		
		self.valorLabel = Label(self.container8, text="Valor   ", font=self.fontePadrao)
		self.valorLabel.pack(side=LEFT)
		
		self.txtvalor = Entry(self.container8)
		self.txtvalor["width"] = 30
		self.txtvalor["font"] = self.fontePadrao
		self.txtvalor.pack(side=LEFT)

		self.mensagem = Label(self.container9, text="", font=self.fontePadrao)
		self.mensagem.pack()
		
		self.btnins = Button(self.container10)
		self.btnins["text"] = "Inserir"
		self.btnins["font"] = ("Arial", "10", "bold")
		self.btnins["width"] = 12
		self.btnins["command"] = self.insereDados
		self.btnins.pack(side=LEFT)

		self.btnins = Button(self.container10)
		self.btnins["text"] = "Buscar"
		self.btnins["font"] = ("Arial", "10", "bold")
		self.btnins["width"] = 12
		self.btnins["command"] = self.buscaDados
		self.btnins.pack(side=LEFT)

		self.btnalt = Button(self.container10)
		self.btnalt["text"] = "Alterar"
		self.btnalt["font"] = ("Arial", "10", "bold")
		self.btnalt["width"] = 12
		self.btnalt["command"] = self.alteraDados
		self.btnalt.pack(side=LEFT)

		self.btndel = Button(self.container10)
		self.btndel["text"] = "Deletar"
		self.btndel["font"] = ("Arial", "10", "bold")
		self.btndel["width"] = 12
		self.btndel["command"] = self.deletaDados
		self.btndel.pack(side=LEFT)

	#Método inserir usuário
	def insereDados(self):
		vidpaciente = self.txtidpaciente.get()
		vnome = self.txtnome.get()
		vdata = self.txtdata.get()
		vhorario = self.txthorario.get()
		vtempo = self.txttempo.get()
		vtipo = self.txttipo.get()
		vvalor = self.txtvalor.get()
		try: 
			cursor.execute("INSERT INTO paciente (idpaciente, nome) VALUES (?, ?)", (vidpaciente, vnome))
			cursor.execute("INSERT INTO agenda (idpaciente, data, horario, tempo, tipo, valor) VALUES (?, ?, ?, ?, ?, ?)", (vidpaciente, vdata, vhorario, vtempo, vtipo, vvalor))
			conn.commit()
			conn.close()
			self.mensagem["text"] = "Dados inseridos com sucesso"
		except:
			self.mensagem["text"] = "Erro de inserção"
	
	#Método buscar usuário
	def buscaDados(self):
		top = Toplevel()
		top.title("Busca de dados")
		self.fontePadrao1 = ("Arial", "10", "bold")
		self.fontePadrao2 = ("Arial", "10")
		
		vidpaciente = self.txtidpaciente.get()
		
		self.text1Label = Label(top, text="Resultado da sua busca", font=self.fontePadrao1) 
		self.text1Label.pack()
		
		try:
			cursor.execute("SELECT idpaciente, nome FROM paciente WHERE idpaciente == idpaciente")
			for linha1 in cursor.fetchall():
				self.text2Label = Label(top, text = linha1, font=self.fontePadrao2)
				self.text2Label.pack()
				
			cursor.execute("SELECT data, horario, tempo, tipo, valor FROM agenda WHERE idpaciente == idpaciente")
			for linha2 in cursor.fetchall():
				self.text3Label = Label(top, text = linha2, font=self.fontePadrao2)
				self.text3Label.pack()
			conn.close()
			
			btnsair = Button(top, text="Sair", command=top.destroy)
			btnsair["font"] = ("Arial", "10", "bold")
			btnsair["width"] = 12
			btnsair.pack()
			
			self.mensagem["text"] = "Busca feita com sucesso"
		except:
			self.mensagem["text"] = "Erro de busca"
	
	#Método alterar usuário
	def alteraDados(self):
		vidpaciente = self.txtidpaciente.get()
		vnome = self.txtnome.get()
		vdata = self.txtdata.get()
		vhorario = self.txthorario.get()
		vtempo = self.txttempo.get()
		vtipo = self.txttipo.get()
		vvalor = self.txtvalor.get()
		try:
			cursor.execute("UPDATE paciente SET nome = ? WHERE idpaciente = ?", (vnome, vidpaciente))
			cursor.execute("UPDATE agenda SET data = ?, horario = ?, tempo = ?, tipo = ?, valor = ? WHERE idpaciente = ?", (vdata, vhorario, vtempo, vtipo, vvalor, vidpaciente))
			conn.commit()
			conn.close()
			self.mensagem["text"] = "Dados alterados com sucesso"
		except:
			self.mensagem["text"] = "Erro de alteração"	

	#Método deletar usuário
	def deletaDados(self):
		vidpaciente = self.txtidpaciente.get()
		try:
			cursor.execute("DELETE FROM paciente WHERE idpaciente = ?", (vidpaciente,))
			cursor.execute("DELETE FROM agenda WHERE idpaciente = ?", (vidpaciente,))
			conn.commit()
			conn.close()
			self.mensagem["text"] = "Dados deletados com sucesso"
		except:
			self.mensagem["text"] = "Erro de deletação"

janela = Tk()
Application(janela)
janela.mainloop()
