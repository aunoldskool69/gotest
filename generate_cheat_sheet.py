import os
from fpdf import FPDF
from fpdf.fonts import FontFace

# Define custom FPDF class with page header and footer
class OCSCCheatSheet(FPDF):
    def header(self):
        # We only draw the large cover header on page 1
        if self.page_no() == 1:
            # Main Banner Background
            self.set_fill_color(27, 54, 93)  # Deep Navy Blue
            self.rect(0, 0, 210, 42, "F")
            
            # Sub-banner strip
            self.set_fill_color(74, 144, 226)  # Cool Accent Blue
            self.rect(0, 42, 210, 3, "F")
            
            # Title Text
            self.set_y(8)
            self.set_font("tahoma", "B", 18)
            self.set_text_color(255, 255, 255)
            self.cell(0, 10, "คู่มือเตรียมสอบ ก.พ. (ภาค ก) - วิชาคอมพิวเตอร์พื้นฐาน", align="C", new_x="LMARGIN", new_y="NEXT")
            
            # Subtitle Text
            self.set_font("tahoma", "", 11.5)
            self.cell(0, 8, "สรุปย่อ 'นามสกุลไฟล์' และ 'คีย์ลัดคีย์บอร์ด' ยอดฮิตที่ออกสอบบ่อยที่สุด", align="C", new_x="LMARGIN", new_y="NEXT")
            self.cell(0, 6, "รวบรวมเนื้อหาและแนวข้อสอบสำหรับใช้ทบทวนก่อนเข้าห้องสอบ", align="C", new_x="LMARGIN", new_y="NEXT")
            
            # Set cursor below header for the actual content
            self.set_y(52)
        else:
            # Standard Header for Page 2+
            self.set_fill_color(27, 54, 93)  # Deep Navy Blue
            self.rect(0, 0, 210, 14, "F")
            
            self.set_fill_color(74, 144, 226)  # Cool Accent Blue
            self.rect(0, 14, 210, 1, "F")
            
            self.set_y(2.5)
            self.set_font("tahoma", "B", 9.5)
            self.set_text_color(255, 255, 255)
            self.cell(0, 8, "สรุปวิชาคอมพิวเตอร์เพื่อสอบ ก.พ. | นามสกุลไฟล์และคีย์ลัด", align="C")
            
            # Reset cursor position below header
            self.set_y(20)

    def footer(self):
        # Position at 15 mm from bottom
        self.set_y(-15)
        self.set_font("tahoma", "", 8.5)
        self.set_text_color(128, 128, 128)
        # Page number
        self.cell(0, 10, f"หน้า {self.page_no()}/{{nb}} | จัดทำเพื่อใช้เตรียมสอบ ก.พ. วิชาคอมพิวเตอร์พื้นฐาน", align="C")

def draw_section_header(pdf, title):
    pdf.ln(3)
    pdf.set_font("tahoma", "B", 13)
    pdf.set_text_color(27, 54, 93)  # Navy Blue
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    
    # Underline
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.set_fill_color(74, 144, 226)
    pdf.rect(x, y - 1, 45, 1.2, "F")
    pdf.ln(3)

def draw_tip_box(pdf, title, text, line_height=5.5):
    pdf.ln(2)
    full_text = f"{title}\n{text}"
    pdf.set_font("tahoma", "", 9.5)
    
    # Calculate lines to dynamically figure out the height
    lines = pdf.multi_cell(w=170, h=line_height, text=full_text, dry_run=True, output="LINES")
    num_lines = len(lines)
    box_height = num_lines * line_height + 6
    
    # Add a page break if it exceeds page boundary
    if pdf.get_y() + box_height > pdf.page_break_trigger:
        pdf.add_page()
        
    x = pdf.get_x()
    y = pdf.get_y()
    
    # Light blue background container
    pdf.set_fill_color(242, 246, 250)
    pdf.rect(x, y, 180, box_height, "F")
    
    # Left border strip
    pdf.set_fill_color(27, 54, 93)
    pdf.rect(x, y, 2.5, box_height, "F")
    
    # Print Title
    pdf.set_xy(x + 6, y + 3)
    pdf.set_font("tahoma", "B", 9.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(170, line_height, title, new_x="LMARGIN", new_y="NEXT")
    
    # Print Body Text
    pdf.set_x(x + 6)
    pdf.set_font("tahoma", "", 9.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(170, line_height, text, new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(3)

def generate_pdf(filename="กพ_คอมพิวเตอร์_สรุปนามสกุลไฟล์.pdf"):
    # Setup document: A4 size, portrait, margins 15mm
    pdf = OCSCCheatSheet(orientation="P", unit="mm", format="A4")
    pdf.set_margins(15, 15, 15)
    
    # Register Tahoma unicode fonts
    pdf.add_font("tahoma", "", r"C:\Windows\Fonts\tahoma.ttf")
    pdf.add_font("tahoma", "B", r"C:\Windows\Fonts\tahomabd.ttf")
    
    # Enable automatic page breaks (margin 15mm from bottom)
    pdf.set_auto_page_break(True, margin=15)
    pdf.alias_nb_pages()
    
    # Page 1
    pdf.add_page()
    pdf.set_font("tahoma", "", 10)
    pdf.set_text_color(51, 51, 51)
    
    # Document Intro
    pdf.write(5.5, "วิชาเทคโนโลยีสารสนเทศและคอมพิวเตอร์พื้นฐานในข้อสอบ ก.พ. (ภาค ก) มักออกสอบความรู้รอบตัวเกี่ยวกับเทคโนโลยีคอมพิวเตอร์ที่เราใช้งานในชีวิตประจำวัน โดยเฉพาะเรื่อง ")
    pdf.set_font("tahoma", "B", 10)
    pdf.write(5.5, "ประเภทและนามสกุลของไฟล์ (File Extensions) ")
    pdf.set_font("tahoma", "", 10)
    pdf.write(5.5, "ซึ่งช่วยระบุประเภทข้อมูลและโปรแกรมที่ต้องใช้เปิด คู่มือเล่มนี้สรุปประเด็นหลักและจุดเน้นสำคัญเพื่อให้นำไปท่องจำและทำข้อสอบได้ทันที\n")
    
    draw_section_header(pdf, "1. ตารางสรุปนามสกุลไฟล์ที่ออกสอบบ่อย (แยกตามหมวดหมู่)")
    
    pdf.set_font("tahoma", "", 9.5)
    
    # Table Setup Styles
    headings_style = FontFace(color=(255, 255, 255), fill_color=(27, 54, 93))
    row_style_even = FontFace(fill_color=(245, 248, 252))
    row_style_odd = FontFace(fill_color=(255, 255, 255))
    
    # Width distribution: Total 180mm
    col_widths = (20, 38, 62, 60)
    
    # Categories Data
    # 1. Documents
    doc_files = [
        [".docx / .doc", "Microsoft Word Document", "ไฟล์เอกสารข้อความ รายงาน หนังสือราชการ จัดรูปแบบตัวอักษร แทรกรูปภาพได้", "มักถามเรื่องเวอร์ชัน: .doc (เวอร์ชัน 2003 ลงไป - Binary) ต่างจาก .docx (เวอร์ชัน 2007 ขึ้นไป - OpenXML มาตรฐานเปิด)"],
        [".xlsx / .xls", "Microsoft Excel Spreadsheet", "ไฟล์ตารางคำนวณ ทำบัญชี สูตรการคำนวณ วิเคราะห์ข้อมูลตัวเลขและกราฟ", "ตัวสะกด 'x' ท้ายสุดย่อมาจาก XML สำหรับระบบ Office รุ่นใหม่ 2007+"],
        [".pptx / .ppt", "Microsoft PowerPoint Presentation", "ไฟล์สไลด์นำเสนอผลงาน งานมัลติมีเดีย มีลูกเล่นและภาพเคลื่อนไหวประกอบ", "ใช้ในการนำเสนอสไลด์ สามารถรันนำเสนอทันทีด้วยคีย์ลัด F5"],
        [".pdf", "Portable Document Format", "ไฟล์เอกสารข้ามแพลตฟอร์ม รักษาโครงสร้างเอกสาร ฟอนต์ และรูปภาพให้คงเดิม", "ข้อสอบชอบออกคุณสมบัติ: เหมาะแก่การพิมพ์ จัดรูปแบบคงที่ และแก้ไขยากที่สุด"],
        [".txt", "Plain Text File", "ไฟล์ข้อความบริสุทธิ์ ไม่มีข้อมูลการตกแต่งตัวอักษร (เช่น ตัวหนา สี ขนาด)", "ขนาดไฟล์เล็กที่สุด ใช้พื้นที่น้อยที่สุด เปิดด้วย Notepad ได้ทุกระบบปฏิบัติการ"],
        [".rtf", "Rich Text Format", "ไฟล์เอกสารข้อความที่จัดรูปแบบอักษรพื้นฐานได้ เพื่อเป็นมาตรฐานแชร์ข้อมูล", "เป็นตัวกลางระหว่างโปรแกรมจัดเอกสารต่างๆ ที่พัฒนาโดย Microsoft"],
        [".csv", "Comma-Separated Values", "ไฟล์ข้อความเก็บข้อมูลตาราง โดยแบ่งแต่ละคอลัมน์ด้วยเครื่องหมายจุลภาค (,)", "นิยมใช้ในการส่งออกหรือนำเข้าข้อมูลระหว่างฐานข้อมูลหรือโปรแกรมที่ต่างกัน"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 1: ไฟล์เอกสารและสำนักงาน (Document & Office Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        # Header
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        # Data
        for i, row_data in enumerate(doc_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])
            
    pdf.ln(5)
    
    # 2. Image files
    image_files = [
        [".jpg / .jpeg", "Joint Photographic Experts Group", "ไฟล์ภาพถ่าย ภาพธรรมชาติ ภาพบนเว็บ บีบอัดข้อมูลแบบสูญเสียรายละเอียด (Lossy)", "ขนาดไฟล์เล็กเพราะบีบอัดมาก ไม่รองรับพื้นหลังโปร่งใส (Transparency)"],
        [".png", "Portable Network Graphics", "ไฟล์ภาพกราฟิก โลโก้ ไอคอน บีบอัดแบบไม่สูญเสียคุณภาพ (Lossless)", "จุดเด่นที่ออกสอบบ่อยสุด: รองรับพื้นหลังโปร่งใส (Transparent Background)"],
        [".gif", "Graphics Interchange Format", "ไฟล์ภาพจำกัดจำนวนสี 256 สี (8-bit) บันทึกเป็นภาพเคลื่อนไหวสั้นๆ ได้", "คำสำคัญในข้อสอบ: ภาพเคลื่อนไหว (Animation) และ มีการจำกัดจำนวนสี"],
        [".svg", "Scalable Vector Graphics", "ไฟล์ภาพลายเส้น (Vector) เขียนด้วยภาษา XML ย่อขยายขนาดแล้วภาพไม่แตก", "เป็นภาพแบบ Vector เหมาะสำหรับเว็บไซต์ ขยายหน้าจอเท่าใดภาพก็ยังคมชัด"],
        [".psd", "Photoshop Document", "ไฟล์ต้นฉบับแก้ไขแยกเลเยอร์ (Layer) ได้ของโปรแกรม Adobe Photoshop", "เป็นไฟล์ตระกูล Raster คุณภาพอิงตามความละเอียดพิกเซล แก้ไขงานออกแบบได้"],
        [".ai", "Adobe Illustrator Artwork", "ไฟล์ต้นฉบับภาพลายเส้นเวกเตอร์ของโปรแกรม Adobe Illustrator", "เป็นไฟล์ประเภท Vector แท้ สามารถยืดหดลวดลายได้โดยคงความคมชัดไว้"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 2: ไฟล์รูปภาพและกราฟิก (Image & Graphic Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        for i, row_data in enumerate(image_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])
            
    # Page 2
    pdf.add_page()
    
    # 3. Audio & Video
    media_files = [
        [".mp3", "MPEG Audio Layer III", "ไฟล์เสียงยอดนิยม บีบอัดแบบสูญเสียข้อมูลบางส่วน (Lossy) โดยตัดช่วงเสียงที่หูคนไม่ค่อยได้ยิน", "มีขนาดไฟล์เล็กมาก เหมาะกับฟังเพลงและดาวน์โหลดผ่านเน็ต"],
        [".wav", "Waveform Audio File Format", "ไฟล์เสียงคุณภาพสูงแบบไม่บีบอัดข้อมูล (Lossless/Uncompressed) เสียงเหมือนจริง", "เป็นมาตรฐานของ Microsoft Windows ขนาดไฟล์ใหญ่กว่า MP3 หลายเท่า"],
        [".mp4", "MPEG-4 Part 14", "ไฟล์วิดีโอมาตรฐานสากล สามารถรวมวิดีโอ เสียง ซับไตเติล และภาพนิ่งไว้ด้วยกัน", "ได้รับความนิยมสูงสุด เล่นได้เกือบทุกเบราว์เซอร์ โทรศัพท์ และระบบปฏิบัติการ"],
        [".avi", "Audio Video Interleave", "ไฟล์วิดีโอดั้งเดิมของ Windows บีบอัดน้อย คุณภาพภาพและเสียงดีมาก", "ขนาดไฟล์ใหญ่มาก และการเล่นบนเครื่องบางเครื่องอาจต้องลง Codec เพิ่มเติม"],
        [".mkv", "Matroska Video File", "ไฟล์ตู้คอนเทนเนอร์วิดีโอ (Container Format) ใส่ซับไตเติลและเสียงได้หลายภาษา", "นิยมใช้แพร่หลายในไฟล์ภาพยนตร์คุณภาพสูงระดับ HD หรือ Blu-ray"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 3: ไฟล์เสียงและวิดีโอ (Audio & Video Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        for i, row_data in enumerate(media_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])
            
    pdf.ln(5)
    
    # 4. Compressed files
    compressed_files = [
        [".zip", "ZIP Archive", "ไฟล์รวมและบีบอัดข้อมูลยอดนิยม เพื่อประหยัดเนื้อหาและส่งต่อไฟล์ได้สะดวกขึ้น", "เป็นมาตรฐานสากล ระบบปฏิบัติการรองรับทันทีโดยไม่ต้องลงแอปพลิเคชันเพิ่มเติม"],
        [".rar", "Roshal Archive", "ไฟล์บีบอัดด้วยอัลกอริทึมลิขสิทธิ์ของ WinRAR บีบอัดได้ดีกว่า ZIP", "หากต้องการใช้ต้องลงโปรแกรมเฉพาะ เช่น WinRAR หรือ WinZip เท่านั้น"],
        [".7z", "7-Zip Archive", "ไฟล์บีบอัดข้อมูลแบบรหัสเปิด (Open Source) ที่ให้คุณภาพการบีบอัดสูงมาก", "สร้างและใช้งานผ่านโปรแกรม 7-Zip ซึ่งใช้งานได้ฟรี ไม่มีค่าใช้จ่าย"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 4: ไฟล์บีบอัดข้อมูล (Compressed & Archive Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        for i, row_data in enumerate(compressed_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])

    pdf.ln(5)
    
    # 5. Executable & System
    system_files = [
        [".exe", "Executable File", "ไฟล์โปรแกรมสำเร็จรูปใน Windows ดับเบิลคลิกเพื่อรันการทำงานโปรแกรมทันที", "เป็นไฟล์ปฏิบัติการหลักของโปรแกรม และมักเป็นพาหะหลักของมัลแวร์/ไวรัส"],
        [".bat", "Batch File", "ไฟล์รวมคำสั่งระบบปฏิบัติการ Windows (Command-line scripts) รันงานอัตโนมัติ", "เขียนด้วยข้อความธรรมดาแต่ใช้รันคำสั่ง CMD เรียงตามลำดับขั้น"],
        [".dll", "Dynamic Link Library", "ไฟล์แชร์โค้ดฟังก์ชันของ Windows เพื่อรันโปรแกรมระบบร่วมกัน", "หากสูญหายจะขึ้น Error รันโปรแกรมนั้นๆ ไม่ได้ (เช่น Error Missing DLL)"],
        [".sys", "Windows System File", "ไฟล์ระบบหลักของ Windows หรือไฟล์ควบคุมการเชื่อมต่อฮาร์ดแวร์ (Driver)", "มีความสำคัญสูงมาก ห้ามลบเด็ดขาดเนื่องจากอาจส่งผลให้ระบบบูตไม่ขึ้น"],
        [".apk", "Android Package Kit", "ไฟล์ที่รวบรวมส่วนประกอบเพื่อใช้ในการลงแอปพลิเคชันบนสมาร์ทโฟน", "ใช้ติดตั้งแอปเฉพาะของระบบปฏิบัติการ Android เท่านั้น (ไม่ทำงานบน Windows)"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 5: ไฟล์โปรแกรมและระบบปฏิบัติการ (Executable & System Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        for i, row_data in enumerate(system_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])

    # Page 3
    pdf.add_page()
    
    # 6. Web & Database
    web_db_files = [
        [".html / .htm", "Hypertext Markup Language", "ไฟล์เอกสารหน้าเว็บเพจพื้นฐาน แสดงผลโครงสร้างผ่านเบราว์เซอร์", "ภาษามาตรฐานที่ใช้สร้างหน้าเว็บ แสดงผลรูปภาพ ลิงก์ และข้อความ"],
        [".css", "Cascading Style Sheets", "ไฟล์กำหนดรูปแบบ สี ฟอนต์ และการตกแต่งภายนอกของหน้าเว็บ HTML", "ช่วยแยกรูปแบบสไตล์ความสวยงามออกจากหน้าโครงสร้างข้อมูล HTML"],
        [".js", "JavaScript File", "ไฟล์สคริปต์ทำงานฝั่งผู้ใช้ (Client-Side) สร้างลูกเล่นและระบบโต้ตอบในหน้าเว็บ", "ทำงานบนเว็บเบราว์เซอร์ช่วยให้หน้าเว็บมีการเคลื่อนไหว ตอบสนองได้ดีขึ้น"],
        [".accdb / .mdb", "Microsoft Access Database", "ไฟล์ฐานข้อมูลของโปรแกรม Microsoft Access เก็บตารางและความสัมพันธ์", ".accdb (เวอร์ชัน 2007 ขึ้นไป) ส่วน .mdb เป็นไฟล์เวอร์ชันเก่า (2003 ลงไป)"],
        [".sql", "Structured Query Language File", "ไฟล์ข้อความเก็บโค้ดคิวรี่คำสั่งสำหรับรันจัดการข้อมูลในระบบ DBMS", "ใช้สร้าง โคลน นำเข้า หรือจัดการโครงสร้างตารางข้อมูลในระบบจัดการฐานข้อมูล"]
    ]
    
    pdf.set_font("tahoma", "B", 10.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 7, "หมวดหมู่ที่ 6: ไฟล์หน้าเว็บและฐานข้อมูล (Web & Database Files)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    with pdf.table(col_widths=col_widths, text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=2) as table:
        row = table.row()
        row.cell("นามสกุล")
        row.cell("ชื่อเต็มภาษาอังกฤษ")
        row.cell("การใช้งาน / คำอธิบาย")
        row.cell("จุดเน้นข้อสอบ ก.พ.")
        
        for i, row_data in enumerate(web_db_files):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])
            row.cell(row_data[3])

    pdf.ln(3)

    draw_section_header(pdf, "2. ประเด็นวิเคราะห์และจุดเน้นสำคัญในข้อสอบ (High-Yield Exam Focus)")
    
    draw_tip_box(pdf, "วิเคราะห์ประเด็นที่ 1: ความแตกต่างระหว่างภาพแบบ Vector กับ Raster (Bitmap)",
                 "• ภาพ Raster (เช่น .jpg, .png, .gif, .psd): เป็นภาพที่ประกอบขึ้นด้วยจุดสีขนาดเล็ก (Pixel) เรียงต่อกัน หากขยายขนาดภาพจะเกิดอาการภาพแตกหรือเห็นจุดสีเหลี่ยมๆ ชัดเจน คุณภาพภาพขึ้นกับความละเอียดกล้องถ่ายรูป\n"
                 "• ภาพ Vector (เช่น .svg, .ai): เป็นภาพที่เกิดจากสูตรทางคณิตศาสตร์คำนวณลายเส้น รูปทรง และสี จุดเด่นคือ 'ย่อหรือขยายเท่าใดภาพก็จะไม่แตกและคงความคมชัดไว้ได้เสมอ' เหมาะสำหรับภาพโลโก้ ฟอนต์อักษร หรือภาพประกอบเว็บ")
                 
    draw_tip_box(pdf, "วิเคราะห์ประเด็นที่ 2: ความแตกต่างของการบีบอัดข้อมูลแบบ Lossy กับ Lossless",
                 "• Lossy Compression (เช่น .jpg, .mp3, .mp4): การบีบอัดที่ยอมตัด/ทำลายข้อมูลบางส่วนเพื่อลดขนาดไฟล์ลงให้มากที่สุด เช่น เสียงเกินหูมนุษย์ได้ยิน หรือ สีที่ใกล้เคียงกัน ทำให้ไฟล์ขนาดเล็กมากแต่ไม่สามารถดึงข้อมูลเดิมกลับมา 100% ได้\n"
                 "• Lossless Compression (เช่น .png, .gif, .wav, .zip, .rar): การบีบอัดโดยคงข้อมูลดั้งเดิมไว้ครบถ้วน 100% เมื่อคลายบีบอัดจะได้ข้อมูลดิบดั้งเดิมไม่มีความเสียหายหรือคุณภาพลดลงเลย")

    draw_tip_box(pdf, "วิเคราะห์ประเด็นที่ 3: ทำไม Microsoft Office 2007+ ถึงเติมอักษร 'x' ท้ายนามสกุลไฟล์?",
                 "• โครงสร้างเก่า (.doc, .xls, .ppt): เป็นโครงสร้างแบบ Binary ขนาดใหญ่ บ่อยครั้งไฟล์เสียหายแล้วเปิดไม่ได้เลย และเป็นระบบปิด\n"
                 "• โครงสร้างใหม่ (.docx, .xlsx, .pptx): อักษร 'x' ย่อมาจาก XML (Extensible Markup Language) ซึ่งเป็นมาตรฐานการเก็บข้อมูลแบบข้อความเปิด มีความยืดหยุ่น ขนาดไฟล์เล็กลงมาก ปลอดภัยจากการฝังไวรัสข้ามโปรแกรม และกู้คืนไฟล์เสียได้ง่ายกว่า")

    # Page 4
    pdf.add_page()

    draw_section_header(pdf, "3. คีย์ลัดยอดฮิตบนคีย์บอร์ดที่ออกสอบบ่อย (Keyboard Shortcuts)")
    pdf.set_font("tahoma", "", 10)
    pdf.write(5.5, "ข้อสอบ ก.พ. พื้นฐานคอมพิวเตอร์มักจะออกคีย์ลัดคีย์บอร์ดควบคู่ไปด้วยเสมอ แนะนำให้ท่องจำเซตคำสั่งสำคัญต่อไปนี้:\n\n")
    
    shortcuts = [
        ["Ctrl + C", "Copy", "คัดลอกข้อความ/ไฟล์ที่เลือกไว้ลงในคลิปบอร์ด"],
        ["Ctrl + V", "Paste", "วางข้อความ/ไฟล์ที่คัดลอกหรือตัดมาล่าสุด"],
        ["Ctrl + X", "Cut", "ตัดข้อความ/ไฟล์ที่เลือก (ลบที่เดิมและย้ายไปคลิปบอร์ด)"],
        ["Ctrl + Z", "Undo", "ยกเลิกหรือย้อนกลับการทำคำสั่งล่าสุด (ย้อนอดีต)"],
        ["Ctrl + Y", "Redo", "ทำซ้ำคำสั่งล่าสุดที่พึ่งถูกยกเลิกไปด้วย Undo (ก้าวไปหน้า)"],
        ["Ctrl + A", "Select All", "เลือกข้อความ ไฟล์ หรือวัตถุทั้งหมดในหน้าจอนั้นทันที"],
        ["Ctrl + S", "Save", "บันทึกเอกสารหรือโครงการที่กำลังทำอยู่ลงบนเครื่อง"],
        ["Ctrl + P", "Print", "เปิดหน้าต่างคำสั่งสั่งพิมพ์เอกสารออกทางเครื่องพิมพ์"],
        ["Ctrl + F", "Find", "เปิดแถบค้นหาเพื่อค้นหาคำหรือคำสำคัญในหน้าเอกสาร/หน้าเว็บ"],
        ["Ctrl + H", "Replace", "เปิดหน้าต่าง ค้นหาและแทนที่คำ ในเอกสาร Office"],
        ["Ctrl + N", "New", "เปิดสร้างหน้าเอกสารใหม่ หรือเปิดหน้าต่างโปรแกรมใหม่"],
        ["Ctrl + O", "Open", "เปิดเมนูเพื่อเปิดหาไฟล์เอกสารที่มีอยู่เดิมขึ้นมาใช้"],
        ["F5 / Ctrl + R", "Refresh / Slideshow", "โหลดข้อมูลหน้าเว็บใหม่ หรือเริ่มการนำเสนอ PowerPoint ตั้งแต่หน้าแรก"],
        ["Alt + Tab", "Switch Window", "กดค้างและกดแท็บเพื่อเลือกสลับหน้าต่างที่เปิดทำงานค้างไว้อย่างรวดเร็ว"],
        ["Alt + F4", "Close Program", "ปิดหน้าต่างหรือปิดการใช้งานโปรแกรมปัจจุบันทันที (หรือสั่งปิดเครื่อง Windows)"],
        ["Win + D", "Show Desktop", "กดเพื่อซ่อนหน้าต่างโปรแกรมทั้งหมดลง และกลับมาหน้าเดสก์ท็อปทันที"],
        ["Win + E", "File Explorer", "เปิดหน้าต่าง File Explorer หรือ My Computer ค้นหาไฟล์สะดวกรวดเร็ว"],
        ["Win + L", "Lock Computer", "ล็อกหน้าจอความปลอดภัย ล็อกบัญชีผู้ใช้ทันทีก่อนเดินออกจากโต๊ะทำงาน"]
    ]
    
    with pdf.table(col_widths=(30, 40, 110), text_align="LEFT", headings_style=headings_style, line_height=4.5, padding=1.8) as table:
        row = table.row()
        row.cell("ปุ่มคีย์ลัด")
        row.cell("ชื่อคำสั่งหลัก")
        row.cell("คำอธิบายการทำงานและประโยชน์การใช้งาน")
        
        for i, row_data in enumerate(shortcuts):
            style = row_style_even if i % 2 == 0 else row_style_odd
            row = table.row(style=style)
            row.cell(row_data[0])
            row.cell(row_data[1])
            row.cell(row_data[2])

    # Page 5
    pdf.add_page()
    
    draw_section_header(pdf, "4. แนวข้อสอบเสมือนจริงวิชาคอมพิวเตอร์ (ก.พ. ภาค ก)")
    pdf.set_font("tahoma", "", 10)
    pdf.write(5.5, "ทบทวนเนื้อหาโดยลองทำแบบทดสอบ 10 ข้อด้านล่างนี้ (เฉลยพร้อมคำอธิบายอยู่ท้ายสุด)\n\n")
    
    questions = [
        ("ข้อที่ 1", "ไฟล์ข้อความชนิดใดต่อไปนี้มีขนาดไฟล์น้อยที่สุดเมื่อเปรียบเทียบในปริมาณเนื้อหาข้อความที่เท่ากัน?", 
         "ก. docx", "ข. rtf", "ค. txt", "ง. pdf"),
        ("ข้อที่ 2", "หากต้องการเซฟรูปภาพให้มีคุณสมบัติพื้นหลังโปร่งใส (Transparent Background) เพื่อนำไปใช้งานออกแบบเว็บไซต์ ควรเลือกเซฟไฟล์ในนามสกุลใด?", 
         "ก. jpg", "ข. png", "ค. bmp", "ง. tiff"),
        ("ข้อที่ 3", "นามสกุลไฟล์เอกสารของ Microsoft Word ตั้งแต่เวอร์ชัน 2007 ขึ้นไป คือข้อใด และตัวอักษรตัวสุดท้ายย่อมาจากเทคโนโลยีใด?", 
         "ก. doc, c = Computer", "ข. docx, x = XML", "ค. docw, w = Word", "ง. docx, x = Extension"),
        ("ข้อที่ 4", "ไฟล์รูปภาพนามสกุลใดจัดอยู่ในกลุ่มไฟล์ภาพประเภท Vector (ภาพที่สามารถย่อขยายขนาดได้โดยคุณภาพไม่สูญเสียและภาพไม่แตก)?", 
         "ก. png", "ข. jpg", "ค. svg", "ง. bmp"),
        ("ข้อที่ 5", "นามสกุลไฟล์ใดจัดอยู่ในกลุ่ม 'ไฟล์เสียงดิบแบบไม่มีการบีบอัดข้อมูล' (Uncompressed) ส่งผลให้มีคุณภาพเสียงสูงสุดแต่ไฟล์มีขนาดใหญ่?", 
         "ก. mp3", "ข. wav", "ค. wma", "ง. aac"),
        ("ข้อที่ 6", "หากไฟล์ระบบปฏิบัติการ Windows นามสกุลใดสูญหายไป อาจส่งผลให้ระบบหรือแอปพลิเคชันส่วนใหญ่รันไม่ขึ้น เนื่องจากเป็นแหล่งรวบรวมฟังก์ชันใช้งานร่วมกัน?", 
         "ก. .exe", "ข. .sys", "ค. .dll", "ง. .bat"),
        ("ข้อที่ 7", "นามสกุลไฟล์ฐานข้อมูลดั้งเดิมของ Microsoft Access ในรุ่นปี 2003 หรือเก่ากว่าคือข้อใด?", 
         "ก. accdb", "ข. mdb", "ค. dbf", "ง. sql"),
        ("ข้อที่ 8", "หากต้องการแก้ไขสไตล์ สีสัน ฟอนต์ และการจัดแต่งความสวยงามของเว็บเพจโดยแยกออกจากหน้าโครงสร้าง HTML ควรบันทึกเป็นไฟล์นามสกุลใด?", 
         "ก. css", "ข. js", "ค. php", "ง. xml"),
        ("ข้อที่ 9", "ในการทำสไลด์นำเสนอด้วยโปรแกรม Microsoft PowerPoint หากต้องการเริ่มการนำเสนอสไลด์ในทันที ควรใช้ปุ่มลัดคีย์บอร์ดปุ่มใด?", 
         "ก. F1", "ข. F5", "ค. Ctrl + P", "ง. Alt + Enter"),
        ("ข้อที่ 10", "ข้อใดกล่าวถูกต้องเกี่ยวกับการบีบอัดไฟล์ภาพและวิดีโอแบบสูญเสียข้อมูลบางส่วน (Lossy Compression)?", 
         "ก. ให้ภาพที่คมชัดกว่าไฟล์ต้นฉบับ 100%", "ข. สามารถบีบอัดให้ไฟล์มีขนาดเล็กลงมากโดยการตัดข้อมูลเสียงหรือย่านสีใกล้เคียงทิ้ง", 
         "ค. สามารถดึงข้อมูลที่สูญเสียกลับมาได้เสมอเมื่อคลายไฟล์", "ง. นามสกุลไฟล์ที่ใช้การบีบอัดลักษณะนี้คือ .zip และ .rar")
    ]
    
    for q_no, q_txt, a, b, c, d in questions:
        # Check if question fits on page
        # Simple estimation: question + options takes about 35mm
        if pdf.get_y() + 32 > pdf.page_break_trigger:
            pdf.add_page()
            
        pdf.set_font("tahoma", "B", 10)
        pdf.set_text_color(27, 54, 93)
        pdf.write(5.5, f"{q_no}: {q_txt}\n")
        pdf.set_font("tahoma", "", 9.5)
        pdf.set_text_color(51, 51, 51)
        pdf.set_x(20)
        pdf.write(5, f"{a}           {b}\n")
        pdf.set_x(20)
        pdf.write(5, f"{c}           {d}\n")
        pdf.ln(3)

    pdf.ln(3)
    if pdf.get_y() + 60 > pdf.page_break_trigger:
        pdf.add_page()
        
    pdf.set_fill_color(240, 240, 240)
    pdf.set_draw_color(27, 54, 93)
    pdf.set_line_width(0.3)
    
    # We will print the answers in a nice bordered table/list
    pdf.set_font("tahoma", "B", 11)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 8, "เฉลยและคำอธิบายแนวข้อสอบ", new_x="LMARGIN", new_y="NEXT")
    pdf.set_fill_color(27, 54, 93)
    pdf.rect(pdf.get_x(), pdf.get_y() - 1, 45, 1, "F")
    pdf.ln(3)
    
    answers = [
        ("ข้อ 1 ตอบ ค. txt", "เพราะเป็น Plain Text ที่ไม่มีข้อมูลการตกแต่งหรือฟอร์แมตตัวอักษรใดๆ ทำให้เก็บเฉพาะตัวรหัสอักษรเพียวๆ ขนาดจึงเล็กที่สุดในกลุ่มตัวเลือก"),
        ("ข้อ 2 ตอบ ข. png", "มีคุณสมบัติเด่นในการบีบอัดแบบไม่สูญเสียความละเอียดและรองรับความโปร่งใส (Alpha channel) เหมาะสำหรับนำไปวางทับองค์ประกอบอื่นๆ บนเว็บ"),
        ("ข้อ 3 ตอบ ข. docx, x = XML", "ตั้งแต่ MS Office 2007 เป็นต้นมามีการใช้มาตรฐานเปิดแบบ XML แทน Binary รูปแบบเก่า ส่งผลให้ไฟล์ปลอดภัยจากการฝังโค้ดร้ายและขนาดเล็กลง"),
        ("ข้อ 4 ตอบ ค. svg", "Scalable Vector Graphics เป็นรูปแบบไฟล์รูปภาพที่คำนวณลายเส้นและพิกัดด้วยสูตรคณิตศาสตร์ (Vector) ทำให้เมื่อย่อหรือขยายภาพจะไม่แตกเบลอ"),
        ("ข้อ 5 ตอบ ข. wav", "เป็นฟอร์แมตจัดเก็บคลื่นเสียงแบบ Waveform Audio ที่ไม่บีบอัดสัญญาณเสียงดิบเลย (Uncompressed) ทำให้รายละเอียดครบครันแต่กินขนาดพื้นที่สูง"),
        ("ข้อ 6 ตอบ ค. .dll", "Dynamic Link Library เป็นไฟล์ห้องสมุดไลบรารีระบบส่วนกลางของ Windows ที่รวบรวมฟังชันให้โปรแกรมต่างๆ เข้ามาเชื่อมเรียกใช้โค้ดร่วมกัน"),
        ("ข้อ 7 ตอบ ข. mdb", "Microsoft Access Database นามสกุลเก่าคือ .mdb ส่วนในเวอร์ชันใหม่ (2007+) จะเปลี่ยนไปใช้นามสกุล .accdb เป็นหลัก"),
        ("ข้อ 8 ตอบ ก. css", "CSS หรือ Cascading Style Sheets ถูกพัฒนามาเพื่อทำหน้าที่ตกแต่ง ปรับปรุงความสวยงาม การจัดวาง สีสัน และรูปแบบฟอนต์โดยแยกจากโครงสร้าง HTML"),
        ("ข้อ 9 ตอบ ข. F5", "ใน MS PowerPoint ปุ่ม F5 คือคีย์ลัดสากลสำหรับเริ่มสไลด์โชว์ตั้งแต่นำเสนอหน้าแรกสุด ส่วนการพิมพ์เอกสารจะใช้ Ctrl + P แทน"),
        ("ข้อ 10 ตอบ ข. สามารถบีบอัดให้ไฟล์มีขนาดเล็กลงมากโดยการตัดข้อมูลเสียงหรือย่านสีใกล้เคียงทิ้ง", "Lossy เป็นการลดรูปไฟล์โดยการทำลายรายละเอียดบางส่วนที่ประสาทสัมผัสหูหรือตาของมนุษย์แยกความต่างไม่ได้อย่างเด่นชัด ทำให้ไฟล์เล็กลงแต่ลดคุณภาพลงด้วย")
    ]
    
    for ans_title, ans_desc in answers:
        pdf.set_font("tahoma", "B", 9.5)
        pdf.set_text_color(27, 54, 93)
        pdf.write(5.2, f"• {ans_title} : ")
        pdf.set_font("tahoma", "", 9.5)
        pdf.set_text_color(51, 51, 51)
        pdf.write(5.2, f"{ans_desc}\n")
        
    # Save the document
    pdf.output(filename)
    print("Generated successfully: PDF file created")

if __name__ == "__main__":
    generate_pdf()
