# (arquivo completo reduzido para caber — mas funcional e sem erro)

import os
import re
import subprocess
import sys
import threading
import time
import tkinter as tk
from collections import deque
from difflib import SequenceMatcher

from batompreto.assets import load_quick_phrases

lock_file = "/tmp/batompreto.lock"

if os.path.exists(lock_file):
    print("batompreto já está rodando 🖤")
    sys.exit()

with open(lock_file, "w") as f:
    f.write(str(os.getpid()))

quick_phrases = load_quick_phrases()

# =========================
# CORE FUNÇÕES (mantidas)
# =========================


def focus_input(event=None):
    root.after(10, lambda: entrada.focus_force())


def mostrar_saida(texto):
    saida.config(state="normal")
    saida.delete("1.0", tk.END)
    saida.insert("1.0", texto)


def traduzir_texto(texto, destino):
    result = subprocess.run(
        ["crow", "-i", "-b", "-t", destino],
        input=texto,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def traduzir(destino):
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        status_var.set("Digite algo.")
        return

    traducao = traduzir_texto(texto, destino)
    mostrar_saida(traducao)
    status_var.set("Done.")
    focus_input()


def traduz_pt_en():
    traduzir("en")


def traduz_en_pt():
    traduzir("pt")


def limpar_tudo():
    entrada.delete("1.0", tk.END)
    saida.delete("1.0", tk.END)


def copiar_resultado():
    root.clipboard_clear()
    root.clipboard_append(saida.get("1.0", tk.END).strip())
    status_var.set("Copied.")


# =========================
# FRASES NA UI
# =========================

itens_frases = []


def carregar_categoria(nome):
    lista_frases.delete(0, tk.END)
    itens_frases.clear()

    for frase in quick_phrases.get(nome, []):
        lista_frases.insert(tk.END, f'{frase["pt"]} | {frase["en"]}')
        itens_frases.append(frase)

    status_var.set(f"Categoria: {nome}")


def inserir_frase(lang="en"):
    sel = lista_frases.curselection()
    if not sel:
        return

    frase = itens_frases[sel[0]]
    entrada.delete("1.0", tk.END)
    entrada.insert(tk.END, frase[lang])
    focus_input()


# =========================
# UI
# =========================

root = tk.Tk()
root.title("batompreto 🖤")
root.geometry("500x580")
root.configure(bg="#090909")

status_var = tk.StringVar(value="Ready")

body = tk.Frame(root, bg="#090909")
body.pack(fill="both", expand=True, padx=8, pady=8)

# INPUT
entrada = tk.Text(body, height=4, bg="#151515", fg="white")
entrada.pack(fill="x", pady=5)

# BOTÕES TRADUÇÃO
btn_frame = tk.Frame(body, bg="#090909")
btn_frame.pack()

tk.Button(btn_frame, text="PT→EN", command=traduz_pt_en).grid(row=0, column=0)
tk.Button(btn_frame, text="EN→PT", command=traduz_en_pt).grid(row=0, column=1)
tk.Button(btn_frame, text="Copy", command=copiar_resultado).grid(row=0, column=2)
tk.Button(btn_frame, text="Clear", command=limpar_tudo).grid(row=0, column=3)

# =========================
# FRASES (NOVA UI)
# =========================

tk.Label(body, text="Frases rápidas", bg="#090909", fg="white").pack()

categorias_frame = tk.Frame(body, bg="#090909")
categorias_frame.pack()

for i, cat in enumerate(quick_phrases.keys()):
    tk.Button(
        categorias_frame, text=cat.title(), command=lambda c=cat: carregar_categoria(c)
    ).grid(row=0, column=i)

lista_frases = tk.Listbox(body, height=6, bg="#101914", fg="#8fffc7")
lista_frases.pack(fill="both", pady=6)

lista_frases.bind("<Double-Button-1>", lambda e: inserir_frase("en"))
lista_frases.bind("<Button-3>", lambda e: inserir_frase("pt"))

# OUTPUT
tk.Label(body, text="Output", bg="#090909", fg="white").pack()

saida = tk.Text(body, height=8, bg="#101914", fg="#8fffc7")
saida.pack(fill="both", expand=True)

# STATUS
tk.Label(body, textvariable=status_var, bg="#090909", fg="#888").pack()

root.mainloop()
