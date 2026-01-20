# Customer Segmentation Web App (Deployed on Render)

This project is **not a toy demo**. It is a production-style Flask web application deployed on **Render**, built to demonstrate real-world customer segmentation using **K-Means clustering**.

If you’re expecting magic without understanding the basics of deployment, stop here. This README tells you exactly what works, what doesn’t, and why.

---

## 🔗 Live Demo

**Render URL:** [https://<your-render-app-name>.onrender.com](https://customer-segmentation-rxsd.onrender.com/)
(Replace this with the actual deployed link. If you don’t, recruiters will assume you didn’t deploy it.)

---

## 🚀 Features

* User authentication (Login & Register)
* Customer data preprocessing using Python
* K-Means clustering for customer segmentation
* PCA for dimensionality reduction
* Cluster visualization
* MySQL / SQLite database integration
* Fully deployed Flask app on Render

**Reality check:**

* This is backend-heavy.
* UI is functional, not fancy.

---

## 🧠 Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (K-Means, PCA)
* **Database:** MySQL / SQLite
* **Frontend:** HTML, CSS, Bootstrap
* **Deployment:** Render

If you claim “full-stack” and can’t explain how Flask talks to the database on Render, you’re bluffing.

---

## 📦 Project Structure

```
Customer-Segmentation/
│── app.py
│── requirements.txt
│── render.yaml (optional)
│── templates/
│── static/
│── models/
│── database/
│── README.md
```

If your structure doesn’t look close to this, expect deployment issues.

---

## ⚙️ Deployment on Render (What Actually Matters)

### 1️⃣ Requirements File

Your `requirements.txt` **must** exist.

Example:

```
flask
numpy
pandas
scikit-learn
matplotlib
seaborn
mysql-connector-python
```

**Mistake #1:** Forgetting gunicorn → app fails to start.

Example fix:

```
gunicorn
```

---

### 2️⃣ Start Command (Critical)

Render does NOT guess your entry point.

Correct:

```
gunicorn app:app
```

Wrong:

```
python app.py
```

If you use the wrong command, deployment succeeds but the app crashes. Silent failure.

---

### 3️⃣ Environment Variables

Set these in Render Dashboard:

* `FLASK_ENV=production`
* `SECRET_KEY=your_secret_key`
* `DATABASE_URL=...`

**Example 1:** Missing SECRET_KEY → login breaks

**Example 2:** Hardcoding DB credentials → instant rejection by reviewers

---

## ▶️ Run Locally

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

If it doesn’t run locally, it will NOT magically work on Render.

---

## 📊 ML Logic (Short & Honest)

* Data cleaned using Pandas
* Features scaled
* K-Means used to form clusters
* PCA used to reduce dimensions for visualization

**Example 1:** Without scaling → garbage clusters
**Example 2:** Random k value → meaningless segmentation

---

## ❌ Common Deployment Failures (You Should Know These)

1. Missing `requirements.txt`
2. Wrong start command
3. App bound to `localhost` instead of `0.0.0.0`
4. Free Render instance sleeping (cold start delay)

If any of these surprise you, you’re not deployment-ready.

---

## 📌 Why This Project Matters

This project proves:

* You can build ML logic
* You can integrate it into a web app
* You can deploy it publicly

Many candidates fail at **step 3**.

---

## 👤 Author

**Kalyan Dakkili**
Full Stack Developer
GitHub: [https://github.com/KalyanDakkili](https://github.com/KalyanDakkili)

---

## ⚠️ Final Note (Blunt Truth)

Deployment is not optional anymore.

If your project isn’t live, recruiters assume:

* You copied it
* Or you don’t understand DevOps basics

This Render deployment removes that doubt.
