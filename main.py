from lib2to3.fixes.fix_input import context

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {


        "poem" : [
                "Его в могилу провожал насмешек шквал,",
                "Иные хохотали просто бешено.",
                "И только я, лишь я один рыдал.",
                "Я так мечтал узреть его повешенным."
        ]

    }
    return render_template("shablon.html", **context)

@app.route("/shablon/")
def films2():
    context = {
        "caption" : "гари",
        "link" : "Перейти в кинотеатр"
    }

    return render_template("index.html", **context)

@app.route("/person/")
def person():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)