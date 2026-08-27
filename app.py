from flask import Flask, request, render_template_string
import os
import base64

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Alex Image Lab</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 30px 15px;
            background: #111827;
            color: white;
        }

        .caixa {
            max-width: 650px;
            margin: auto;
            padding: 25px;
            border-radius: 20px;
            background: #1f2937;
        }

        h1 {
            font-size: 30px;
        }

        p {
            color: #d1d5db;
        }

        input[type="file"] {
            margin: 20px 0;
            width: 100%;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }

        .imagem {
            max-width: 100%;
            margin-top: 25px;
            border-radius: 15px;
        }

        .sucesso {
            margin-top: 20px;
            padding: 15px;
            border-radius: 12px;
            background: #065f46;
        }
    </style>
</head>

<body>

    <div class="caixa">

        <h1>🎨 Alex Image Lab</h1>

        <p>
            Laboratório de desenvolvimento de motores de IA
        </p>

        <hr>

        <h2>📷 Teste de imagem</h2>

        <form method="POST"
              enctype="multipart/form-data">

            <input
                type="file"
                name="imagem"
                accept="image/*"
                required
            >

            <br>

            <button type="submit">
                🖼️ Carregar imagem
            </button>

        </form>

        {% if imagem %}

            <div class="sucesso">
                🟢 Imagem recebida com sucesso!
            </div>

            <img
                class="imagem"
                src="data:{{ tipo }};base64,{{ imagem }}"
            >

        {% endif %}

    </div>

</body>

</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():

    imagem = None
    tipo = None

    if request.method == "POST":

        arquivo = request.files.get("imagem")

        if arquivo and arquivo.filename:

            dados = arquivo.read()

            imagem = base64.b64encode(
                dados
            ).decode("utf-8")

            tipo = (
                arquivo.mimetype
                or "image/jpeg"
            )

    return render_template_string(
        HTML,
        imagem=imagem,
        tipo=tipo
    )


if __name__ == "__main__":

    porta = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(
        host="0.0.0.0",
        port=porta
    )
