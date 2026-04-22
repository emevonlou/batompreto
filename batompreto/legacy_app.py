import os
import subprocess
import sys
import tkinter as tk

# =========================
# LOCK
# =========================
lock_file = "/tmp/batompreto.lock"

if os.path.exists(lock_file):
    print("batompreto já está rodando 🖤")
    sys.exit()

with open(lock_file, "w") as f:
    f.write(str(os.getpid()))

# =========================
# CONFIG
# =========================
AUTO_TRANSLATE_DELAY_MS = 600
auto_translate_after_id = None


# =========================
# CORE
# =========================
def get_target_lang():
    return mode_var.get()


def focus_input(event=None):
    root.after(10, lambda: entrada.focus_force())


def mostrar_saida(texto):
    saida.delete("1.0", tk.END)
    saida.insert("1.0", texto)


def traduzir_texto(texto, destino):
    result = subprocess.run(
        ["crow", "-i", "-b", "-t", destino],
        input=texto,
        text=True,
        capture_output=True,
    )

    traducao = result.stdout.strip()
    erro = result.stderr.strip()

    if erro and not traducao:
        return f"Error: {erro}"

    return traducao


def fade_in(alpha=0.0, target=0.78, step=0.05, delay=20):
    if alpha < target:
        root.attributes("-alpha", alpha)
        root.after(delay, lambda: fade_in(alpha + step, target, step, delay))
    else:
        root.attributes("-alpha", target)


# =========================
# LIVE TRANSLATE
# =========================
def agendar_traducao(event=None):
    global auto_translate_after_id

    if event is not None and event.keysym in (
        "Return",
        "Shift_L",
        "Shift_R",
        "Control_L",
        "Control_R",
    ):
        return

    if auto_translate_after_id is not None:
        root.after_cancel(auto_translate_after_id)

    auto_translate_after_id = root.after(
        AUTO_TRANSLATE_DELAY_MS,
        executar_traducao_live,
    )


def executar_traducao_live():
    global auto_translate_after_id
    auto_translate_after_id = None

    texto = entrada.get("1.0", tk.END).strip()
    if len(texto) < 2:
        saida.delete("1.0", tk.END)
        status_var.set("Ready")
        return

    traducao = traduzir_texto(texto, get_target_lang())
    mostrar_saida(traducao)
    status_var.set(f"Live translate: {get_target_lang().upper()}")


# =========================
# TRADUÇÃO MANUAL
# =========================
def traduzir(destino):
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        status_var.set("Digite algo primeiro.")
        return

    traducao = traduzir_texto(texto, destino)
    mostrar_saida(traducao)

    if destino == "en":
        status_var.set("Translated to English.")
    else:
        status_var.set("Traduzido para português.")

    focus_input()


def traduz_pt_en():
    mode_var.set("en")
    traduzir("en")


def traduz_en_pt():
    mode_var.set("pt")
    traduzir("pt")


def traduzir_modo_atual(event=None):
    traduzir(get_target_lang())
    return "break"


def traduzir_pt_en_atalho(event=None):
    traduzir("en")
    return "break"


def traduzir_en_pt_atalho(event=None):
    traduzir("pt")
    return "break"


# =========================
# ACTIONS
# =========================
def copiar_resultado():
    texto = saida.get("1.0", tk.END).strip()
    if not texto:
        status_var.set("Nothing to copy.")
        return

    root.clipboard_clear()
    root.clipboard_append(texto)
    status_var.set("Copied.")


def limpar_tudo():
    global auto_translate_after_id

    if auto_translate_after_id is not None:
        try:
            root.after_cancel(auto_translate_after_id)
        except Exception:
            pass
        auto_translate_after_id = None

    entrada.delete("1.0", tk.END)
    saida.delete("1.0", tk.END)
    status_var.set("Cleared.")
    focus_input()


def iniciar_movimento(event):
    root._drag_start_x = event.x
    root._drag_start_y = event.y


def mover_janela(event):
    x = event.x_root - root._drag_start_x
    y = event.y_root - root._drag_start_y
    root.geometry(f"+{x}+{y}")


def on_close(event=None):
    try:
        if os.path.exists(lock_file):
            os.remove(lock_file)
    except Exception:
        pass

    try:
        root.quit()
    except Exception:
        pass

    try:
        root.destroy()
    except Exception:
        pass

    os._exit(0)


# =========================
# UI
# =========================
root = tk.Tk()
root.title("batompreto")

try:
    root.iconphoto(
        True,
        tk.PhotoImage(file=os.path.expanduser("~/github-projects/batompreto/icon.png")),
    )
except Exception as e:
    print("Erro ao carregar ícone:", e)

# Modelo de transparência da versão antiga
root.overrideredirect(False)
root.after(50, lambda: root.overrideredirect(True))
root.attributes("-topmost", True)
root.attributes("-alpha", 0.0)
root.configure(bg="#090909")
root.geometry("470x310+3360+40")
root.minsize(450, 295)

mode_var = tk.StringVar(value="en")
status_var = tk.StringVar(value="Ready")

outer = tk.Frame(
    root,
    bg="#141414",
    highlightthickness=1,
    highlightbackground="#2d2d2d",
)
outer.pack(fill="both", expand=True)

top_bar = tk.Frame(outer, bg="#101010", height=26)
top_bar.pack(fill="x")
top_bar.pack_propagate(False)

top_bar.bind("<Button-1>", iniciar_movimento)
top_bar.bind("<B1-Motion>", mover_janela)

title_label = tk.Label(
    top_bar,
    text="batompreto",
    bg="#101010",
    fg="#d8d8d8",
    font=("Arial", 10, "bold"),
)
title_label.pack(side="left", padx=8)
title_label.bind("<Button-1>", iniciar_movimento)
title_label.bind("<B1-Motion>", mover_janela)

close_btn = tk.Button(
    top_bar,
    text="✕",
    command=on_close,
    bg="#101010",
    fg="#d8d8d8",
    activebackground="#8d1f1f",
    activeforeground="white",
    relief="flat",
    borderwidth=0,
    padx=8,
    pady=1,
)
close_btn.pack(side="right", padx=2)

body = tk.Frame(outer, bg="#090909")
body.pack(fill="both", expand=True, padx=6, pady=6)

# INPUT
entrada_label = tk.Label(
    body,
    text="Input",
    bg="#090909",
    fg="#d0d0d0",
    font=("Arial", 9, "bold"),
)
entrada_label.pack(anchor="w")

entrada = tk.Text(
    body,
    height=3,
    bg="#111111",
    fg="#ffffff",
    insertbackground="white",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#2b2b2b",
    highlightcolor="#3a3a3a",
    padx=6,
    pady=6,
)
entrada.pack(fill="x", pady=(3, 5))

entrada.bind("<Button-1>", focus_input)
entrada.bind("<FocusIn>", lambda e: status_var.set("Typing..."))
entrada.bind("<KeyRelease>", agendar_traducao)
entrada.bind("<Return>", traduzir_modo_atual)
entrada.bind("<Control-Return>", traduzir_pt_en_atalho)
entrada.bind("<Shift-Return>", traduzir_en_pt_atalho)
entrada.bind("<Escape>", on_close)

# MODE
mode_frame = tk.Frame(body, bg="#090909")
mode_frame.pack(anchor="w", pady=(0, 4))

mode_en = tk.Radiobutton(
    mode_frame,
    text="PT→EN",
    variable=mode_var,
    value="en",
    bg="#090909",
    fg="white",
    selectcolor="#151515",
    activebackground="#090909",
    activeforeground="white",
)
mode_en.grid(row=0, column=0, padx=(0, 6))

mode_pt = tk.Radiobutton(
    mode_frame,
    text="EN→PT",
    variable=mode_var,
    value="pt",
    bg="#090909",
    fg="white",
    selectcolor="#151515",
    activebackground="#090909",
    activeforeground="white",
)
mode_pt.grid(row=0, column=1, padx=(0, 6))

# BUTTONS
btn_frame = tk.Frame(body, bg="#090909")
btn_frame.pack(fill="x", pady=(0, 4))

btn_pt_en = tk.Button(
    btn_frame,
    text="PT→EN",
    command=traduz_pt_en,
    bg="#1a1a1a",
    fg="white",
    activebackground="#2c2c2c",
    activeforeground="white",
    width=10,
    relief="flat",
    borderwidth=0,
)
btn_pt_en.grid(row=0, column=0, padx=2, pady=2)

btn_en_pt = tk.Button(
    btn_frame,
    text="EN→PT",
    command=traduz_en_pt,
    bg="#1a1a1a",
    fg="white",
    activebackground="#2c2c2c",
    activeforeground="white",
    width=10,
    relief="flat",
    borderwidth=0,
)
btn_en_pt.grid(row=0, column=1, padx=2, pady=2)

btn_copy = tk.Button(
    btn_frame,
    text="Copy",
    command=copiar_resultado,
    bg="#1a1a1a",
    fg="white",
    activebackground="#2c2c2c",
    activeforeground="white",
    width=10,
    relief="flat",
    borderwidth=0,
)
btn_copy.grid(row=0, column=2, padx=2, pady=2)

btn_clear = tk.Button(
    btn_frame,
    text="Clear",
    command=limpar_tudo,
    bg="#1a1a1a",
    fg="white",
    activebackground="#2c2c2c",
    activeforeground="white",
    width=10,
    relief="flat",
    borderwidth=0,
)
btn_clear.grid(row=0, column=3, padx=2, pady=2)

hint = tk.Label(
    body,
    text="Live translate | Enter=current mode | Ctrl+Enter=PT→EN | Shift+Enter=EN→PT | Esc=close",
    bg="#090909",
    fg="#7a7a7a",
    font=("Arial", 7),
    wraplength=440,
    justify="left",
)
hint.pack(anchor="w", pady=(0, 4))

# OUTPUT
saida_label = tk.Label(
    body,
    text="Output",
    bg="#090909",
    fg="#d0d0d0",
    font=("Arial", 9, "bold"),
)
saida_label.pack(anchor="w")

saida = tk.Text(
    body,
    height=3,
    bg="#081710",
    fg="#9cffc7",
    insertbackground="white",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#193126",
    highlightcolor="#244636",
    padx=6,
    pady=6,
)
saida.pack(fill="x", pady=(3, 4))

status = tk.Label(
    body,
    textvariable=status_var,
    bg="#090909",
    fg="#8a8a8a",
    anchor="w",
    font=("Arial", 8),
)
status.pack(fill="x", pady=(1, 0))

for widget in (btn_pt_en, btn_en_pt, btn_copy, btn_clear):
    widget.bind("<Enter>", lambda e, w=widget: w.configure(bg="#2a2a2a"))
    widget.bind("<Leave>", lambda e, w=widget: w.configure(bg="#1a1a1a"))

close_btn.bind("<Enter>", lambda e: close_btn.configure(bg="#8d1f1f"))
close_btn.bind("<Leave>", lambda e: close_btn.configure(bg="#101010"))

root.protocol("WM_DELETE_WINDOW", on_close)
root.bind("<Escape>", on_close)
root.after(120, focus_input)
root.after(180, lambda: fade_in(target=0.78))

root.mainloop()
