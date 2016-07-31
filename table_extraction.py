import sys,os
sys.path.append('code')

from pdftables import pdftables,get_pdf_page, page_to_tables, TableDiagnosticData,converter
reload(sys)
sys.setdefaultencoding('utf8')
fh = open('waters.pdf', 'rb')
#pdf_page = get_pdf_page(fh, 12)
#table, table_diagnostic_data = page_to_tables(pdf_page)
tables= pdftables.get_tables(fh)
if os.path.isfile("tables.html"):                   # clear the json file if already present
    with open('tables.html','w+') as outfile:
        outfile.write("")
for table in tables:
     with open('tables.html', 'a') as outfile:
        outfile.write(converter.to_html(table))