from flask import Flask, render_template, request
import os

app = Flask(**name**)

@app.route("/", methods=["GET", "POST"])
def home():
result = None

```
if request.method == "POST":
    uploaded_file = request.files.get("photo")

    if uploaded_file:
        result = {
            "age": 18,
            "gender": "Male"
        }

return render_template("index.html", result=result)
```

if **name** == "**main**":
app.run(
host="0.0.0.0",
port=int(os.environ.get("PORT", 5000))
)



