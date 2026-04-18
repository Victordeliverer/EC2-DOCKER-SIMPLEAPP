from flask import Flask

app = Flask(__name__)

NAME = "Victor Deliverer"  # change this
ROLE = "DevOps Engineer in training"
SKILLS = ["AWS EC2", "Docker", "Linux", "CI/CD", "Git", "Kubernetes", "Terraform"]

@app.route('/')
def home():
    skills_html = "".join([f"<li>{skill}</li>" for skill in SKILLS])

    return f"""
    <html>
        <head>
            <title>{NAME} - DevOps Portfolio</title>
            <style>
                body {{
                    font-family: Arial;
                    background-color: #0f172a;
                    color: #e2e8f0;
                    text-align: center;
                    padding-top: 50px;
                }}
                .card {{
                    background: #1e293b;
                    padding: 30px;
                    margin: auto;
                    width: 400px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
                }}
                ul {{
                    text-align: left;
                    display: inline-block;
                }}
            </style>
        </head>

        <body>
            <div class="card">
                <h1>👋 Hi, I'm {NAME}</h1>
                <h3>{ROLE}</h3>

                <p><strong>My DevOps Skills:</strong></p>
                <ul>
                    {skills_html}
                </ul>

                <p style="margin-top:20px;">
                    Deployed on AWS EC2 🚀
                </p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
