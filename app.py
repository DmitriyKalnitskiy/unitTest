from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    surName = request.form.get('SurName')
    age = request.form.get('age')
    gender = request.form.get('gender')
    feedback = request.form.get('feedback')

    with open("responses.txt", "a") as file:
        file.write(f"Имя: {name}\n")
        file.write(f"Фамилия: {surName}\n")
        file.write(f"Возраст: {age}\n")
        file.write(f"Пол: {gender}\n")
        file.write(f"Отзыв: {feedback}\n")
        file.write("\n")  # Добавляем пустую строку для разделения ответов

    return "Ответы успешно сохранены!"