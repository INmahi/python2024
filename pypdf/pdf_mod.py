import os
from pypdf import PdfReader,PdfWriter

# Get the absolute path to the current script
base_dir = os.path.dirname(__file__)
#join it before the file name
pdf_path = os.path.join(base_dir, "3-Month_Python_ComputerVision_ML_WeeklyPlan.pdf")

read = PdfReader(pdf_path)

#======================== READING METADATA ==========================

meta  = read.metadata
# print(meta)

# print(meta.title)
# print(meta.author)
# print(meta.subject)
# print(meta.creator)
# print(meta.producer)
# print(meta.creation_date)
# print(meta.modification_date)


#======================== WRITING METADATA ==========================

write = PdfWriter()
for page in read.pages:
    write.add_page(page)

if meta is not None:
    write.add_metadata(meta)

write.add_metadata(
    {
        "/Author": "Mahi",
        "/Producer": "Chat-gpt",
        "/Title": "Roadmap",
        "/Subject": "DS_ML",
        "/Keywords": "ds,ml"
    }
)

##save the  edited (meta)pdf as a new file

# with open("meta-pdf.pdf","wb") as fl:

#     write.write(fl)


#read the new pdf's meta


readMeta = PdfReader("pypdf/meta-pdf.pdf")

newMeta = readMeta.metadata

print(newMeta.title)
print(newMeta.author)
print(newMeta.subject)
print(newMeta.creator)
print(newMeta.producer)
print(newMeta.creation_date)
print(newMeta.modification_date)


