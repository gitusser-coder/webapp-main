from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
from io import BytesIO

app = Flask(__name__)

NAMEN = [

{
  'id': 1,
  'name': 'Darius',
  'Beruf': 'Softwareentwickler',
  'Alter': '24',
  'Größe': '1.82'

},

{

  'id': 2,
  'name': 'Danial',
  'Beruf': 'TikToker',
  'Alter': '22',
  'Größe': '1.71'

},

{

  'id': 3,
  'name': 'Timon',
  'Beruf': 'TikToker',
  'Alter': '22',
  'Größe': '1.70'

},

{

  'id': 4,
  'name': 'Kourosch',
  'Beruf': 'TikToker',
  'Alter': '20',
  'Größe': '1.70'

},

{

  'id': 5,
  'name': 'Nikan',
  'Beruf': 'Autohersteller',
  'Alter': '22',
  'Größe': '1.69'

}


]

@app.route('/')
def index():
  return render_template('index.html', namen=NAMEN, Geschäftsführer='Darius')


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')


@app.route('/pdf-datei', methods=['GET', 'POST'])
def pdf():
    return render_template("pdf.html")

@app.route('/fill_pdf', methods=['POST'])
def fill_pdf():
    try:
        # Formulardaten abrufen
        vorname = request.form.get('vorname', '')
        nachname = request.form.get('nachname', '')
        geburtsdatum = request.form.get('geburtsdatum', '')
        geburtsort = request.form.get('geburtsort', '')
        
        # Hier würde normalerweise die PDF-Bibliothek verwendet werden
        # Für jetzt erstellen wir eine einfache Text-"PDF" als Beispiel
        pdf_content = f"""
PDF FORMULAR - AUSGEFÜLLT

Vorname: {vorname}
Nachname: {nachname} 
Geburtsdatum: {geburtsdatum}
Geburtsort: {geburtsort}

Erstellt mit der Flask PDF-App
        """.strip()
        
        # Erstelle einen BytesIO-Stream für die "PDF"
        pdf_buffer = BytesIO()
        pdf_buffer.write(pdf_content.encode('utf-8'))
        pdf_buffer.seek(0)
        
        return send_file(
            pdf_buffer,
            as_attachment=False,
            download_name=f'{nachname}_{vorname}_formular.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/vorschau')
def vorschau():
    return render_template('vorschau.html')





if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5001, debug=True)
