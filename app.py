from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
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
                padding: 50px 20px;
                background: #111827;
                color: white;
            }

            .caixa {
                max-width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 20px;
                background: #1f2937;
            }

            h1 {
                font-size: 32px;
            }

            p {
                font-size: 18px;
                color: #d1d5db;
            }

            .status {
                margin-top: 25px;
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

            <div class="status">
                🟢 Sistema iniciado com sucesso!
            </div>

            <p>
                🤖 Alex Image Lab está online.
            </p>

        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=porta
    )
