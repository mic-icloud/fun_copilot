import os
from PyPDF2 import PdfReader, PdfWriter

def add_covers(report_dir, cover_dir, final_dir):
    """
    report_dir - это каталог отчетов с именами 1.pdf, 2.pdf, 3.pdf и т.д.
    Эти файлы могут состоять из одной или нескольких страниц.
    cover_dir - это каталог обложек по одному листу на каждый отчет.
    Имена файлов в этом каталоге - cover1.pdf, cover2.pdf, cover3.pdf и т.д.
    Каждый файл содержит только одну страницу.
    Добавь обложки в начало каждого отчета и сохрани получившиеся pdf-файлы в final_dir.
    """
    for file in os.listdir(report_dir):
        report_path = os.path.join(report_dir, file)
        cover_path = os.path.join(cover_dir, 'cover' + file)
        final_path = os.path.join(final_dir, file)
        
        if not os.path.exists(cover_path):
            print(f"Cover file {cover_path} does not exist.")
            continue
        
        report = PdfReader(report_path)
        cover = PdfReader(cover_path)
        output = PdfWriter()
        output.add_page(cover.pages[0])
        
        for page in report.pages:
            output.add_page(page)
        
        with open(final_path, 'wb') as out_file:
            output.write(out_file)

if __name__ == '__main__':
    # файлы находятся в каталоге ch9
    add_covers('ch9/reports', 'ch9/covers', 'ch9/final1')