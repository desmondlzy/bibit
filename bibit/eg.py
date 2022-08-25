import os
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import as_text

def process(filename):
	bparser = BibTexParser(common_strings=True, interpolate_strings=False)
	name, ext = os.path.splitext(filename)
	with open(filename, encoding="utf-8") as fp:
		bibdb = bparser.parse_file(fp)

	def process_entry(entry):
		field_list = ["author", "title", "journal", "pages", "doi", "isbn", "year", "month", "booktitle", "publisher", "address", "ENTRYTYPE", "ID"]
		filtered_entries = {k: v for k, v in entry.items() if k in field_list}
		filtered_entries["ID"] = filtered_entries["ID"].replace("_", "-")
		return filtered_entries


	new_entries = list(map(process_entry, bibdb.entries))
	bibdb.entries = new_entries

	bwriter = BibTexWriter()
	bwriter.indent="    "
	with open(f"{name}-out{ext}", "w", encoding="utf-8") as fp:
		string = bwriter.write(bibdb)
		fp.write(string)