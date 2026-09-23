import os
import re
import shutil
import subprocess
import sys
import tempfile


def substituir_constante(codigo, nome, valor):
    codigo, total = re.subn(
        rf"^{nome}\s*=.*$",
        f"{nome} = {valor}",
        codigo,
        flags=re.MULTILINE
    )

    if total != 1:
        raise ValueError(f"Constante {nome} não encontrada no template.")

    return codigo


def gerar_faah(audio_path, chance, volume, destino):
    with tempfile.TemporaryDirectory() as temp_dir:

        audio_destino = os.path.join(
            temp_dir,
            "audio.mp3"
        )

        shutil.copy2(
            audio_path,
            audio_destino
        )

        template_path = os.path.join(
            os.path.dirname(__file__),
            "template.py"
        )

        with open(
            template_path,
            "r",
            encoding="utf-8"
        ) as arquivo:

            codigo = arquivo.read()

        codigo = substituir_constante(
            codigo,
            "CHANCE",
            round(chance / 100, 4)
        )

        codigo = substituir_constante(
            codigo,
            "VOLUME",
            round(volume / 100, 4)
        )

        main_path = os.path.join(
            temp_dir,
            "main.py"
        )

        with open(
            main_path,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(codigo)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "PyInstaller",

                "--onefile",
                "--noconsole",

                "--name",
                "Faah",

                "--add-data",
                "audio.mp3;.",

                "main.py"
            ],
            cwd=temp_dir,
            check=True
        )

        exe_origem = os.path.join(
            temp_dir,
            "dist",
            "Faah.exe"
        )

        exe_destino = os.path.join(
            destino,
            "Faah.exe"
        )

        shutil.copy2(
            exe_origem,
            exe_destino
        )

        return exe_destino