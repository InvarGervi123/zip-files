from flask import Flask, request, render_template, send_file
import zipfile
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_code():
    if request.method == 'POST':
        code_snippets = request.form.getlist("code")
        filenames = request.form.getlist("filename")
        formats = request.form.getlist("format")
        folder_names = request.form.getlist("folder")

        memory_file = io.BytesIO()

        with zipfile.ZipFile(memory_file, 'w') as zf:
            for idx, code in enumerate(code_snippets):
                filename = filenames[idx] or f"file_{idx}"
                file_format = formats[idx] or "txt"
                folder_name = folder_names[idx].strip()
                if folder_name:
                    zip_path = f"{folder_name}/{filename}.{file_format}"
                else:
                    zip_path = f"{filename}.{file_format}"

                zf.writestr(zip_path, code)

        memory_file.seek(0)
        return send_file(memory_file, download_name='code_files.zip', as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
