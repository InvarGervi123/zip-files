### 📦 Zip Files Web App

A simple web-based Python app that allows users to upload multiple files, compress them into a ZIP archive, and download the archive.

---

### 🚀 Features

* Upload one or more files via a web interface.
* Automatically compresses all uploaded files into a single `.zip` file.
* Provides a link to download the compressed archive.
* Cleans up temporary files after download.

---

### 🛠️ Tech Stack

* **Python 3**
* **Flask** – for the web server
* **HTML/CSS** – for the frontend

---

### 📁 Project Structure

```bash
zip-files/
│
├── app.py              # Main Flask app
├── static/             # Static assets (CSS, JS, etc.)
│   └── style.css
├── templates/
│   └── index.html      # HTML form for uploading
├── uploads/            # Temporary folder for uploaded files
└── zip/                # Temporary folder for the generated ZIP files
```

---

### 🔧 Installation & Running

1. **Clone the repository:**

```bash
git clone https://github.com/InvarGervi123/zip-files.git
cd zip-files
```

2. **Install dependencies:**

```bash
pip install flask
```

3. **Run the app:**

```bash
python app.py
```

4. **Open your browser** and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 🧹 Notes

* Uploaded files are temporarily saved in the `uploads/` directory.
* ZIP files are temporarily saved in the `zip/` directory.
* Both folders are cleared automatically after the ZIP is downloaded.

---

### 📜 License

This project is open-source and available under the MIT License.
