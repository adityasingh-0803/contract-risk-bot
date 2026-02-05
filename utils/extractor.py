import pdfplumber
import docx

def extract_text(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        return extract_pdf(file)

    elif name.endswith(".docx"):
        return extract_docx(file)

    elif name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        return ""


def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join(p.text for p in doc.paragraphs)
