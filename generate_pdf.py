import pdfkit

def html_to_pdf(html_string, output_path):
    pdfkit.from_string(html_string, output_path)
