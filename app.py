from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        uploaded_file = request.files.get("photo")

        if uploaded_file:
            # Placeholder AI result
            result = {
                "age": 18,
                "gender": "Male"
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
