# 🐍 PDFly CLI – Complete Command Guide

**`pdfly`** is a command-line tool powered by [`pypdf`](https://github.com/py-pdf/pypdf), built for performing powerful PDF manipulations like merging, extracting, compressing, converting, and more — all straight from your terminal.

---

## ⚙️ Installation

Install `pdfly` using pip:

```bash
pip install pdfly
```

Check that it's working:

```bash
pdfly --help
```

---

## 📋 Available Commands & What They Do

| Command             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `extract-images`    | Extracts **raw images** from a PDF without altering resolution or quality.  |
| `2-up`              | Creates a PDF where **two pages are combined** side by side. Great for print.|
| `cat`               | **Concatenates (merges)** multiple PDFs into a single file.                 |
| `booklet`           | Reorders pages for **booklet-style printing** (e.g., fold + staple).        |
| `rm`                | **Removes selected pages** from a PDF.                                      |
| `meta`              | Shows **metadata** such as title, author, creation date, etc.               |
| `pagemeta`          | Shows **detailed info** (size, rotation, etc.) of a specific page.          |
| `extract-text`      | Extracts **all text content** from a PDF file.                              |
| `compress`          | **Reduces file size** by optimizing PDF content.                            |
| `uncompress`        | Unpacks PDF streams to make content **human-readable**.                     |
| `update-offsets`    | Repairs internal structure and **offset errors** in manually edited PDFs.   |
| `x2pdf`             | Converts images or text files into a **multi-page PDF**.                    |

---

## 🧪 Example Usages

Here are some quick real-world examples you can run:

### ✅ Merge PDFs
```bash
pdfly cat --output merged.pdf file1.pdf file2.pdf
```

### ✅ Remove a Specific Page (e.g., page 2)
```bash
pdfly rm file1.pdf --page-ranges 1 --output trimmed.pdf
```

### ✅ Extract Text to a File
```bash
pdfly extract-text file1.pdf > output.txt
```

### ✅ Compress a PDF
```bash
pdfly compress file1.pdf file1_compressed.pdf
```

### ✅ Extract Images from PDF
```bash
pdfly extract-images file1.pdf --output extracted_images/
```

### ✅ View PDF Metadata
```bash
pdfly meta file1.pdf
```

### ✅ View Metadata of a Specific Page
```bash
pdfly pagemeta file1.pdf --page 0
```

### ✅ Make 2-Pages-Per-Sheet PDF
```bash
pdfly 2-up file1.pdf file1_2up.pdf
```

### ✅ Format PDF for Booklet Printing
```bash
pdfly booklet file1.pdf file1_booklet.pdf
```

### ✅ Convert Files to PDF
```bash
pdfly x2pdf --output new.pdf image1.jpg textfile.txt
```

### ✅ Uncompress a PDF
```bash
pdfly uncompress file1.pdf file1_uncompressed.pdf
```

### ✅ Fix Broken Offsets (advanced use)
```bash
pdfly update-offsets file1_uncompressed.pdf file1_fixed.pdf
```

---

## 🔍 Detailed Help for Each Command

You can always see detailed options and syntax by running:

```bash
pdfly --help
```

For specific command help:

```bash
pdfly <command> --help
```

Example:
```bash
pdfly cat --help
```

---

## 📝 Notes

- **Page numbers are zero-based**, so page 0 = first page, 1 = second, etc.
- Many commands need `--output` to specify where to save the result.
- Some commands (like `cat`) also support `>` redirection if you prefer.

---

## 💡 Tips

- For full programmatic control, use [`pypdf`](https://pypdf.readthedocs.io/en/stable/) directly in Python scripts.
- `pdfly` is perfect for **quick one-liner terminal jobs**.
- Always test commands on copies of your files to avoid accidental overwrites.

---

## 👤 Credits

Built with ❤️ by the [PyPDF Community](https://github.com/py-pdf)  
Wrapped up for CLI magic via [`pdfly`](https://github.com/py-pdf/pdfly)

---

## 📜 License

MIT License
