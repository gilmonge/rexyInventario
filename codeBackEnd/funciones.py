import io
import xlsxwriter
from django.http import HttpResponse


def estructuraExcel(titulos, datos, nombre):
    # create our spreadsheet. I will create it in memory with a StringIO
    output = io.BytesIO()
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Escribe los titulos del excel
    for row_num, columns in enumerate(titulos):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, cell_data, bold)

    # Write some simple text.
    for row_num, columns in enumerate(datos):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()

    # Responde con el excel
    response = HttpResponse(content_type='application/vnd.ms-excel')

    # tell the browser what the file is named
    response['Content-Disposition'] = 'attachment;filename="'+nombre+'.xlsx"'

    # put the spreadsheet data into the response
    response.write(output.getvalue())

    return response
