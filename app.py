from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    strength = ""
    score = 0
    suggestions = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    length_ok = False

    if request.method == "POST":

        password = request.form.get("password", "")

        symbols = "!@#$%^&*()_+-=[]{};:',.<>/?"

        length_ok = len(password) >= 8

        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.islower():
                has_lower = True
            if ch.isdigit():
                has_digit = True
            if ch in symbols:
                has_symbol = True

        if length_ok:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1

        if score == 5:
            strength = "Strong"
        elif score >= 3:
            strength = "Medium"
        elif score == 2:
            strength = "Fair"
        else:
            strength = "Weak"

        if not length_ok:
            suggestions.append("Password should be at least 8 characters long.")

        if not has_upper:
            suggestions.append("Add at least one uppercase letter.")

        if not has_lower:
            suggestions.append("Add at least one lowercase letter.")

        if not has_digit:
            suggestions.append("Add at least one number.")

        if not has_symbol:
            suggestions.append("Add at least one special symbol.")

    return render_template(
        "index.html",
        strength=strength,
        score=score,
        progress=score * 20,
        suggestions=suggestions,
        length_ok=length_ok,
        has_upper=has_upper,
        has_lower=has_lower,
        has_digit=has_digit,
        has_symbol=has_symbol
    )


if __name__ == "__main__":
    app.run(debug=True)