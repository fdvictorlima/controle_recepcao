from dearpygui.core import *
from dearpygui.simple import *

# Função que será chamada ao clicar em "Enviar"
def enviar_callback(sender, data):
    nome = get_value("##nome")
    motivo = get_value("##motivo")
    log_info(f"Nome: {nome}")
    log_info(f"Motivo: {motivo}")
    # Mostra os dados em um popup
    set_value("resultado_texto", f"Nome: {nome}\nMotivo: {motivo}")
    show_item("Resultado")

with window("Formulário", width=400, height=300):
    add_text("Preencha os campos abaixo:")
    add_input_text(label="Nome Completo", source="nome", default_value="", tag="##nome", width=300)
    add_input_text(label="Motivo", source="motivo", default_value="", tag="##motivo", width=300)
    add_spacing(count=2)
    add_button("Enviar", callback=enviar_callback)
    add_same_line()
    add_button("Cancelar", callback=lambda s, d: stop_dearpygui())

    # Popup para exibir o resultado
    add_spacing()
    add_text("", tag="resultado_texto")
    hide_item("resultado_texto")
    add_text("Dados recebidos com sucesso!", tag="Resultado")
    hide_item("Resultado")

start_dearpygui()
