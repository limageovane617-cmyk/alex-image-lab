from flask import Flask, request, render_template_string
import os
import base64

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

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

h2 {
    margin-top: 25px;
}

p {
    color: #d1d5db;
}

input[type="file"] {
    margin: 20px 0;
    width: 100%;
}

textarea {
    width: 100%;
    min-height: 100px;
    margin-top: 15px;
    padding: 12px;
    box-sizing: border-box;
    border-radius: 10px;
    border: none;
    resize: vertical;
    font-size: 16px;
}

button {
    margin-top: 15px;
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

.comando {
    margin-top: 15px;
    padding: 15px;
    border-radius: 12px;
    background: #374151;
    text-align: left;
}

/* 🧠 PAINEL DO MOTOR */

.motor {
    margin-top: 25px;
    padding: 20px;
    border-radius: 15px;
    background: #111827;
    border: 1px solid #374151;
    text-align: left;
}

.motor-titulo {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}

.motor-status {
    padding: 12px;
    border-radius: 10px;
    background: #450a0a;
    margin-bottom: 12px;
}

.motor-info {
    padding: 12px;
    border-radius: 10px;
    background: #374151;
    margin-top: 10px;
}

.motor-futuro {
    margin-top: 10px;
    color: #d1d5db;
    font-size: 14px;
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

<!-- 🧠 STATUS DO MOTOR -->

<div class="motor">

<div class="motor-titulo">
🧠 Status do Motor
</div>

<div class="motor-status">
🔴 <strong>Motor desconectado</strong>
</div>

<div class="motor-info">
<strong>Motor planejado:</strong>
<br>
SmolVLM-256M
</div>

<div class="motor-futuro">
🔬 O motor será conectado somente após os testes
de compatibilidade e estabilidade.
</div>

</div>

<!-- 📷 IMAGEM + COMANDO -->

<h2>📷 Imagem + comando</h2>

<form
method="POST"
enctype="multipart/form-data"
>

<input
type="file"
name="imagem"
accept="image/*"
required
>

<textarea
name="comando"
placeholder="Digite o que você quer fazer com a imagem..."
required
></textarea>

<br>

<button type="submit">
🚀 Enviar para o laboratório
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

{% if comando %}

<div class="comando">

<strong>
✏️ Comando recebido:
</strong>

<br><br>

{{ comando }}

</div>

{% endif %}

{% if imagem and comando %}

<div class="sucesso">

🧪 Imagem + comando recebidos.

<br><br>

🧠 O motor de IA ainda será conectado
nesta próxima etapa.

</div>

{% endif %}

</div>

</body>

</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():

    imagem = None
    tipo = None
    comando = None

    if request.method == "POST":

        arquivo = request.files.get("imagem")

        comando = request.form.get(
            "comando",
            ""
        ).strip()

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
        tipo=tipo,
        comando=comando
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
