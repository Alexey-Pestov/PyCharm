from fpdf import FPDF
from datetime import datetime

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('fon.jpg', h = 297, w = 210, x=0, y=0)
pdf.add_font('Comic Sans MS', '', 'c:\Windows\Fonts\comic.ttf', uni=True)
pdf.set_font('Comic Sans MS', size = 37)
pdf.set_text_color(0,0,0)

friend_name = input('Введи имя поздравляемого человека:\n')
pdf.cell(0,50,ln=1)
pdf.cell(0,20, txt = 'Дорогой, ' + friend_name + '!', align='C', ln=1)

pdf.cell(0,30,ln=1)

pdf.set_font('Comic Sans MS', size = 18)
message = 'Траляля Траляля Траляля Траляля ТраляляТраляля Траляля Траляля Траляля'
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.multi_cell(0,20, txt=message, align='C')

pdf.cell(0,5,ln=1)

today = datetime.today().strftime('%d.%m.%Y')
pdf.set_text_color(124,30,150)
pdf.set_font('', size = 14)
pdf.cell(0, 10, txt = today, align='R', ln=1)







pdf.output('bday_card.pdf')