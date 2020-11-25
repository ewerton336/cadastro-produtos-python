from PyQt5 import uic,QtWidgets

def funcao_principal():
         linha1 = formulario.lineEdit.text()
         linha2 = formulario.lineEdit_2.text()
         linha3 = formulario.dateEdit.text()
         linha4 = formulario.lineEdit_3.text()
        
         print ('*** CADASTRO INICIADO ***')    
         print ("Produto:", linha1)
         print ("Fornecedor:", linha2)       
         print ("Data de compra:", linha3)    
         print ("Valor R$",linha4)

         
         if formulario.radioButton.isChecked():
                print("Categoria Informática")
         elif formulario.radioButton_2.isChecked():
                print ("Categoria Papelaria")
         print ('*** CADASTRO CONCLUÍDO ***')   



app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(exit)
formulario.show()
app.exec()