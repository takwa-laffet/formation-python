from fpdf import FPDF

pdf=FPDF("P",'mm','A4')
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="Hello World",ln=1,align='C')
pdf.cell(200,10,txt="takwa",ln=1,align='C')
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="Hello World page 2",ln=1,align='C')
pdf.output("ex1.pdf")
print("ok")