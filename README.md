# 🔐 Password Strength Detector

A web-based **Password Strength Detector** built using **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**. The application analyzes a user's password and evaluates its strength based on common security practices.

---

## 🚀 Features

* Checks password length (minimum 8 characters)
* Detects uppercase letters
* Detects lowercase letters
* Detects numbers
* Detects special characters
* Calculates a password strength score (0–5)
* Classifies password strength (Weak, Fair, Medium, Strong)
* Provides suggestions to improve weak passwords
* Modern responsive UI with a dark glassmorphism design
* Show/Hide password functionality

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript

---

## 📂 Project Structure

```text
Password-Strength-Detector/
│
├── app.py
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-strength-detector.git
```

### 2. Navigate to the project folder

```bash
cd password-strength-detector
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 Password Evaluation Criteria

| Requirement                | Score |
| -------------------------- | ----: |
| Minimum 8 characters       |    +1 |
| Contains uppercase letter  |    +1 |
| Contains lowercase letter  |    +1 |
| Contains number            |    +1 |
| Contains special character |    +1 |

### Strength Levels

* **0–1** → Weak
* **2** → Fair
* **3–4** → Medium
* **5** → Strong

---

## 📚 Concepts Practiced

* Variables
* String Handling
* Boolean Logic
* Loops
* Conditional Statements (`if`, `elif`, `else`)
* Lists and List Methods
* Functions
* Flask Routing
* HTTP GET & POST Requests
* HTML Forms
* Jinja2 Templates
* Frontend and Backend Integration

---

## 💡 Future Improvements

* Real-time password strength analysis
* Password entropy calculation
* Common password detection
* Password generator
* Animated strength meter
* Password history using a database

---

## 👨‍💻 Author

**ABHINAV SINGH**

This project was developed as part of my internship learning journey to strengthen my understanding of Python, Flask, and full-stack web development.


