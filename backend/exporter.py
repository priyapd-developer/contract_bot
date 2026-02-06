from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def export_pdf(text, path="report.pdf"):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    doc.build([Paragraph(text, styles["Normal"])])
