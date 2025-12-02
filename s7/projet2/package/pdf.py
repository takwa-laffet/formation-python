from fpdf import FPDF
def create_pdf(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)
create_pdf("output.pdf", "Hello, this is a sample PDF generated using FPDF in Python.")
