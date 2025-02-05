from ebooklib import epub
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    # Extract text content from the PDF
    text = extract_text(pdf_path)
    # Clean and preprocess the text (remove extra line breaks, if necessary)
    processed_text = text.replace('\n', ' ').strip()
    return processed_text


def create_epub(title, author, content, output_file):
    # Initialize a new EPUB book
    book = epub.EpubBook()
    book.set_title(title)
    book.add_author(author)

    # Create a new chapter
    chapter = epub.EpubHtml(title='Chapter 1', file_name='chapter_1.xhtml', lang='en')
    chapter.set_content(f'<html><head></head><body><h1>{title}</h1><p>{content}</p></body></html>')
    book.add_item(chapter)

    # Add CSS for styling
    style = '''body { font-family: Arial, sans-serif; }'''
    style_item = epub.EpubItem(uid='style', file_name='style.css', media_type='text/css', content=style)
    book.add_item(style_item)

    # Define the spine (reading order)
    book.spine = ['nav', chapter]  # Include navigation and chapter in reading order

    # Add navigation items (table of contents, etc.)
    book.add_item(epub.EpubNav())

    # Save the EPUB file
    epub.write_epub(output_file, book)


# Paths and metadata
pdf_path = 'KRSNA-the-Reservoir-of-Pleasure-1970.pdf'
output_epub = 'KRSNA-the-Reservoir-of-Pleasure-1970.epub'
book_title = 'KRSNA: The Reservoir of Pleasure'
book_author = 'Srila Prabhupada'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)
if pdf_text:
    # Create an EPUB book
    create_epub(book_title, book_author, pdf_text, output_epub)
    print(f"> EPUB file created successfully: {output_epub}")
else:
    print("> Text extraction failed. The EPUB file was not created.")
