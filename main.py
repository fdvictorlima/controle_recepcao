# main.py
import sys
import socket
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QCheckBox
)

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulário")
        self.setGeometry(100, 100, 400, 250)
        self.init_ui()

    def init_ui(self):
        self.label_info = QLabel("Preencha os campos abaixo:")
        self.label_resultado = QLabel("")
        self.label_resultado.hide()

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome Completo")

        self.input_motivo = QLineEdit()
        self.input_motivo.setPlaceholderText("Motivo")

        # Botões com checkbox
        self.checkbox_esperar = QCheckBox("Esperar")
        self.checkbox_esperar.setChecked(True)  # Marcado por padrão

        self.checkbox_atender = QCheckBox("Atender")
        self.checkbox_atender.setChecked(True)  # Marcado por padrão

        self.input_opcao = QLineEdit()
        self.input_opcao.setPlaceholderText("Outra Opção (deixe em branco se não precisar)")

        # Layout dos checkboxes
        layout_checkbox = QHBoxLayout()
        layout_checkbox.addWidget(self.checkbox_esperar)
        layout_checkbox.addWidget(self.checkbox_atender)

        # Layout dos botões
        self.botao_enviar = QPushButton("Enviar")
        self.botao_enviar.clicked.connect(self.enviar_callback)

        self.botao_cancelar = QPushButton("Cancelar")
        self.botao_cancelar.clicked.connect(self.close)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.label_info)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.input_motivo)
        layout.addLayout(layout_checkbox)
        layout.addWidget(self.input_opcao)

        botoes_layout = QHBoxLayout()
        botoes_layout.addWidget(self.botao_enviar)
        botoes_layout.addWidget(self.botao_cancelar)

        layout.addLayout(botoes_layout)
        layout.addWidget(self.label_resultado)
        self.setLayout(layout)

    def enviar_callback(self):
        nome = self.input_nome.text()
        motivo = self.input_motivo.text()

        # Coletando as opções
        opcoes = []
        if self.checkbox_esperar.isChecked():
            opcoes.append("Esperar")
        if self.checkbox_atender.isChecked():
            opcoes.append("Atender")
        if self.input_opcao.text():
            opcoes.append(self.input_opcao.text())

        # Criando a estrutura JSON com as informações do formulário
        dados_json = {
            "nome": nome,
            "motivo": motivo,
            "opcoes": opcoes
        }

        texto_resultado = f"Nome: {nome}\nMotivo: {motivo}\nOpções: {', '.join(opcoes)}"
        self.label_resultado.setText(texto_resultado)
        self.label_resultado.show()

        try:
            # Enviar a estrutura JSON para o servidor via socket
            self.enviar_para_servidor(dados_json)
            QMessageBox.information(self, "Sucesso", "Dados enviados e recebidos com sucesso!")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível enviar: {e}")

    def enviar_para_servidor(self, dados):
        # Conexão com o servidor via socket
        servidor_ip = '127.0.0.1'  # Altere para o IP do servidor se necessário
        servidor_porta = 5000

        # Cria o socket e se conecta ao servidor
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((servidor_ip, servidor_porta))

        # Envia os dados JSON para o servidor
        cliente_socket.send(json.dumps(dados).encode('utf-8'))

        # Fecha a conexão
        cliente_socket.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Formulario()
    janela.show()
    sys.exit(app.exec_())
