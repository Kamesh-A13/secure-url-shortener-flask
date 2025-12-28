# 🔗 Secure URL Shortener (Flask + Hash + Base64)

A **secure, deterministic, and production-style URL shortener** built using **Python Flask**, **MySQL**, **SHA-256 hashing**, and **Base64 encoding**.  
This project focuses on **clean backend logic**, **predictable behavior**, and a **professional inline-CSS UI**, similar to real-world systems.

---

## 🌟 Key Highlights

- 🔐 Secure URL generation using **SHA-256**
- 🔁 Deterministic output (same URL → same short link)
- 🔤 Base64 encoding for URL-safe characters
- ⚡ Fast redirects with minimal latency
- 🎨 Professional **inline-CSS UI**
- 📢 Clickable sponsored advertisement layout
- 📞 Integrated contact section
- ❌ No user authentication required
- 🧠 Interview-ready architecture

---

## 🧠 How It Works

Original Long URL
↓
SHA-256 Hash (hashlib)
↓
Base64 Encoding
↓
Remove special characters
↓
Truncate to 6 characters
↓
Short URL

yaml
Copy code

### Why this approach?
- More secure than random strings
- No collisions in normal usage
- Predictable and consistent
- Commonly used in real systems

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend     | Python Flask |
| Database    | MySQL |
| Security    | hashlib (SHA-256) |
| Encoding    | Base64 |
| Frontend    | HTML + Inline CSS |
| Icons       | Font Awesome |

---

## 📂 Project Structure

secure-url-shortener-flask/
│
├── app.py
├── database.sql
├── requirements.txt
├── README.md
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
├── mv glob.png
├── queen construction.png
├── new queen tailor.png
└── ppconstruction.jpg

yaml
Copy code

---

## 🚀 Features Explained

### 🔐 Secure Hashing
Uses **SHA-256** to generate a cryptographic hash of the URL.

### 🔤 URL-Safe Encoding
Base64 encoding converts binary hash into readable characters.

### 🔁 Deterministic Mapping
The same long URL always generates the same short URL.

### 🎨 Professional UI
- Inline CSS (no external stylesheet)
- Responsive layout
- Sponsored ads on both sides
- Clean contact section

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Create the database
bash
Copy code
mysql -u root -p < database.sql
3️⃣ Run the application
bash
Copy code
python app.py
4️⃣ Open in browser
cpp
Copy code
http://127.0.0.1:5000


🧪 Example Output
bash
Copy code
Original URL:
https://example.com/very/long/url

Short URL:
http://localhost:5000/xZmHks


👨‍💻 Developed By

MVGlobe Development Team By Kamesh A 🌐 Visit: https://mvglobe.in

⭐ Support

If you like this project, don’t forget to star the repo ⭐ on GitHub!

📞 Contact Details

📧 Email:
kameshanbu13@gmail.com

📱 Phone / WhatsApp:
+91 98947 38057

🤝 Contributions

Contributions, suggestions, and improvements are welcome.
Feel free to fork the repository and submit a pull request.
