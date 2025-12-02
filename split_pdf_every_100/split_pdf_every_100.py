# split_pdf_every_100.py
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path: str, pages_per_file: int = 100, output_dir: str | None = None):
    input_path = Path(input_path)
    if output_dir:
        outdir = Path(output_dir)
    else:
        outdir = input_path.parent / f"{input_path.stem}_parts"
    outdir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)

    if total_pages == 0:
        print("الملف فارغ (0 صفحات).")
        return

    part = 1
    for start in range(0, total_pages, pages_per_file):
        end = min(start + pages_per_file, total_pages)
        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        output_file = outdir / f"{input_path.stem}_part{part:02d}.pdf"
        with open(output_file, "wb") as f_out:
            writer.write(f_out)

        print(f"Created: {output_file} (pages {start+1}–{end})")
        part += 1

    print("Finished. Files saved in:", outdir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf_every_100.py input.pdf [pages_per_file] [output_dir]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    pages_per = int(sys.argv[2]) if len(sys.argv) >= 3 else 100
    out_dir = sys.argv[3] if len(sys.argv) >= 4 else None

    split_pdf(input_pdf, pages_per, out_dir)
