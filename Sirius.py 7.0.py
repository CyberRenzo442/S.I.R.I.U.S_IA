import datetime
import json
import tkinter as tk
from tkinter import messagebox

# --- BANCO DE DADOS JSON ---
def carregar_tarefas():
    try:
        with open("cronograma_sirius.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(lista):
    with open("cronograma_sirius.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

# --- NÚCLEO DE LÓGICA DA IA (v6.1 - Módulo de Personalidade) ---
def processar_comando_ia(comando_usuario):
    texto = comando_usuario.lower().strip()
    lista = carregar_tarefas()
    
    # 🌟 Módulo de Conversação Livre
    if texto in ["ola", "olá", "oi", "fala sirius", "siriús", "jarvis", "acorda"]:
        return "S.I.R.I.U.S.: Olá, Lorenzo! Sistemas centrais online. O que o Criador deseja planejar hoje?"
        
    elif texto in ["tudo bem?", "como voce esta?", "como você está?"]:
        return "S.I.R.I.U.S.: Executando diagnóstico interno... Hardware a 100%, banco JSON totalmente seguro. Pronto para o trabalho, Lorenzo!"

    elif texto in ["obrigado", "valeu", "obrigada"]:
        return "S.I.R.I.U.S.: Sem problemas, Criador. Próxima parada: MIT!"

    # 1. INTENÇÃO: STATUS OU VER TAREFAS
    elif "status" in texto or "ver" in texto or "listar" in texto or "tarefas" in texto:
        if not lista:
            return "S.I.R.I.U.S.: Banco de dados vazio, Lorenzo. Nenhum compromisso agendado."
        
        relatorio = "--- RELATÓRIO DE COMPROMISSOS S.I.R.I.U.S. ---\n\n"
        for i, t in enumerate(lista, 1):
            relatorio += f"🔹 {i}. {t.get('materia', 'Estudos')} | {t.get('data', '--/--')} às {t.get('horario', '--:--')}\n"
        return relatorio

    # 2. INTENÇÃO: APAGAR OU RESETAR TUDO
    elif "limpar tudo" in texto or "resetar" in texto or "deletar banco" in texto:
        salvar_tarefas([])
        return "S.I.R.I.U.S.: Protocolo de limpeza concluído. Banco JSON resetado por ordem do Criador."

    # 3. INTENÇÃO: AGENDAR AUTOMATICAMENTE
    elif "agendar" in texto or "adicionar" in texto or "criar" in texto:
        palavras = texto.split()
        try:
            materia = "Estudos"
            data = datetime.datetime.now().strftime("%d/%m")
            horario = "12:00"
            
            for p in palavras:
                if "/" in p:
                    data = p
                elif ":" in p:
                    horario = p
                elif p not in ["agendar", "adicionar", "criar", "matéria", "materia", "de", "para"]:
                    if materia == "Estudos":
                        materia = p.capitalize()
            
            nova_tarefa = {"materia": materia, "data": data, "horario": horario}
            lista.append(nova_tarefa)
            salvar_tarefas(lista)
            return f"S.I.R.I.U.S.: Entendido, Lorenzo. Adicionei '{materia}' para o dia {data} às {horario} no banco JSON."
            
        except Exception:
            return "S.I.R.I.U.S.: Erro ao processar o agendamento. Tente: 'agendar [materia] [data] [hora]'"

    # 4. RESPOSTA PADRÃO
    else:
        return "S.I.R.I.U.S.: Comando não reconhecido, Lorenzo. Meus sistemas aceitam 'Olá', 'Como você está?', 'ver tarefas' ou 'agendar [materia]'."

# --- CONFIGURAÇÃO DA INTERFACE ---
janela = tk.Tk()
janela.title("S.I.R.I.U.S. v6.1 - Núcleo de IA Stark")
janela.geometry("600x550")
janela.configure(bg="#20232a")

# Painel de Resposta da IA (Monitor Estilo Stark)
frame_monitor = tk.Frame(janela, bg="#1c1e22", bd=2, relief="solid")
frame_monitor.pack(pady=20, padx=20, fill="both", expand=True)

lbl_sirius_output = tk.Label(
    frame_monitor, 
    text="S.I.R.I.U.S. v6.1 ONLINE.\nDigite seu comando na caixa abaixo, Lorenzo.", 
    font=("Courier", 10, "bold"), 
    fg="#61dafb", 
    bg="#1c1e22", 
    justify="left", 
    wraplength=540
)
lbl_sirius_output.pack(pady=20, padx=20, anchor="w")

# Caixa de Entrada de Texto Única
frame_input_ia = tk.Frame(janela, bg="#20232a")
frame_input_ia.pack(pady=20, fill="x", padx=20)

entry_comando = tk.Entry(frame_input_ia, font=("Arial", 12), bg="#282c34", fg="white", bd=1, relief="solid")
entry_comando.pack(side="left", fill="x", expand=True, ipady=5)

def enviar_comando_para_ia():
    comando = entry_comando.get()
    if not comando:
        return
    
    resposta = processar_comando_ia(comando)
    lbl_sirius_output.config(text=resposta)
    entry_comando.delete(0, tk.END)

btn_enviar = tk.Button(
    frame_input_ia, 
    text="MANDAR COMANDO", 
    font=("Arial", 10, "bold"), 
    bg="#61dafb", 
    fg="black", 
    command=enviar_comando_para_ia
)
btn_enviar.pack(side="right", padx=10)

# Atalho: Apertar ENTER também envia o comando
janela.bind('<Return>', lambda event: enviar_comando_para_ia())

janela.mainloop()

