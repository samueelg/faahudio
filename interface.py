import customtkinter as ctk
from builder import gerar_faah
from tkinter import filedialog


def selecionar_audio():
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo de áudio",
        filetypes=[
            ("Arquivos de áudio", "*.mp3 *.wav *.ogg"),
            ("MP3", "*.mp3"),
            ("WAV", "*.wav"),
            ("OGG", "*.ogg"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if caminho:
        audio_entry.delete(0, "end")
        audio_entry.insert(0, caminho)


def atualizar_volume(valor):
    volume_label.configure(text=f"{int(float(valor))}%")


def atualizar_chance(valor):
    chance_label.configure(text=f"{int(float(valor))}%")


def gerar_executavel():
    audio = audio_entry.get()
    volume = volume_slider.get()
    chance = chance_slider.get()

    if not audio:
        print("Selecione um áudio.")
        return

    destino = filedialog.askdirectory(
        title="Escolha onde salvar o Faah.exe"
    )

    if not destino:
        return

    try:
        exe = gerar_faah(
            audio_path=audio,
            chance=chance,
            volume=volume,
            destino=destino
        )

        print(f"Faah gerado em: {exe}")

    except Exception as erro:
        print(f"Erro ao gerar: {erro}")


# Configuração da aplicação
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Faah Builder")
app.geometry("650x500")
app.resizable(False, False)


# =========================
# TÍTULO
# =========================

titulo = ctk.CTkLabel(
    app,
    text="Faah Builder",
    font=("Arial", 30, "bold")
)

titulo.pack(pady=(30, 5))


subtitulo = ctk.CTkLabel(
    app,
    text="Configure seu Faah",
    font=("Arial", 14)
)

subtitulo.pack(pady=(0, 25))


# =========================
# ÁUDIO
# =========================

audio_label = ctk.CTkLabel(
    app,
    text="Arquivo de áudio",
    font=("Arial", 15, "bold")
)

audio_label.pack(anchor="w", padx=50)


audio_frame = ctk.CTkFrame(app, fg_color="transparent")
audio_frame.pack(fill="x", padx=50, pady=(5, 25))


audio_entry = ctk.CTkEntry(
    audio_frame,
    placeholder_text="Selecione um arquivo de áudio...",
    height=40
)

audio_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)


audio_button = ctk.CTkButton(
    audio_frame,
    text="Selecionar",
    width=110,
    height=40,
    command=selecionar_audio
)

audio_button.pack(side="right")


# =========================
# VOLUME
# =========================

volume_header = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

volume_header.pack(
    fill="x",
    padx=50
)


volume_title = ctk.CTkLabel(
    volume_header,
    text="Volume",
    font=("Arial", 15, "bold")
)

volume_title.pack(side="left")


volume_label = ctk.CTkLabel(
    volume_header,
    text="5%",
    font=("Arial", 15)
)

volume_label.pack(side="right")


volume_slider = ctk.CTkSlider(
    app,
    from_=0,
    to=100,
    number_of_steps=100,
    command=atualizar_volume
)

volume_slider.set(5)

volume_slider.pack(
    fill="x",
    padx=50,
    pady=(5, 30)
)


# =========================
# CHANCE
# =========================

chance_header = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

chance_header.pack(
    fill="x",
    padx=50
)


chance_title = ctk.CTkLabel(
    chance_header,
    text="Chance de ativação",
    font=("Arial", 15, "bold")
)

chance_title.pack(side="left")


chance_label = ctk.CTkLabel(
    chance_header,
    text="20%",
    font=("Arial", 15)
)

chance_label.pack(side="right")


chance_slider = ctk.CTkSlider(
    app,
    from_=0,
    to=100,
    number_of_steps=100,
    command=atualizar_chance
)

chance_slider.set(20)

chance_slider.pack(
    fill="x",
    padx=50,
    pady=(5, 35)
)


# =========================
# BOTÃO GERAR
# =========================

botao = ctk.CTkButton(
    app,
    text="GERAR FAAH.EXE",
    height=45,
    font=("Arial", 15, "bold"),
    command=gerar_executavel
)

botao.pack(
    padx=50,
    fill="x"
)


app.mainloop()