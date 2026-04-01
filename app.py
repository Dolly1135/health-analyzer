from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        hb = float(request.form['hb'])
        sugar = float(request.form['sugar'])

        result = ""

        # Hemoglobin check
        if hb < 12:
            result += "⚠️ Low Hemoglobin → Risk of Anemia\n"
        else:
            result += "✅ Hemoglobin is Normal\n"

        # Sugar check
        if sugar > 140:
            result += "⚠️ High Sugar → Risk of Diabetes\n"
        else:
            result += "✅ Sugar Level is Normal\n"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)