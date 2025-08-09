from flask import Flask, render_template, request, jsonify, Response
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', Geschäftsführer='Darius')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/pdf-datei', methods=['GET'])
def pdf():
    return render_template("pdf.html")

@app.route('/fillpdf', methods=['POST'])
def fill_pdf():
    try:
        # Formulardaten abrufen
        vorname = request.form.get('vorname', '')
        nachname = request.form.get('nachname', '')
        geburtsdatum = request.form.get('geburtsdatum', '')
        geburtsort = request.form.get('geburtsort', '')

        # PDF im Speicher erstellen
        pdf_buffer = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
        pdf_canvas.setTitle("Ausgefülltes Formular")

        # Überschrift
        pdf_canvas.setFont("Helvetica-Bold", 16)
        pdf_canvas.drawString(100, 750, "PDF FORMULAR - AUSGEFÜLLT")

        # Formulardaten
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(100, 700, f"Vorname: {vorname}")
        pdf_canvas.drawString(100, 680, f"Nachname: {nachname}")
        pdf_canvas.drawString(100, 660, f"Geburtsdatum: {geburtsdatum}")
        pdf_canvas.drawString(100, 640, f"Geburtsort: {geburtsort}")

        # Fußnote
        pdf_canvas.setFont("Helvetica-Oblique", 10)
        pdf_canvas.drawString(100, 600, "Erstellt mit der Flask PDF-App")

        # PDF abschließen
        pdf_canvas.showPage()
        pdf_canvas.save()

        pdf_buffer.seek(0)
        pdf_bytes = pdf_buffer.read()

        # Sauber als PDF zurückgeben
        return Response(pdf_bytes, mimetype='application/pdf')

    except Exception as e:
        app.logger.error(f"Fehler bei PDF-Erstellung: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.route('/vorschau')
def vorschau():
    return render_template('vorschau.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
