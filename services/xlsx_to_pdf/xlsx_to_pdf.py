def xlsx_to_pdf():
    import fitz
    from utils import print_summary, create_dir_if_not_exist
    import os
    import openpyxl as op
    import pandas as pd

    base_path = 'services/xlsx_to_pdf'
    base_input_path = os.path.abspath(f'{base_path}/xlsx_to_pdf_input')
    base_output_path = os.path.abspath(f'{base_path}/xlsx_to_pdf_output')
    create_dir_if_not_exist(base_output_path)

    def init_console():
        print("변환하려는 XLSX 파일 이름을 입력해 주세요:", end = ' ')
        input_filename = f'{base_input_path}/{input().strip()}.xlsx'
        print("변환 결과 PDF 파일 이름을 입력해 주세요:", end = ' ')
        output_filename = f'{base_output_path}/{input().strip()}.docx'

        return (input_filename, output_filename)
    
    try:
        (input_filename, output_filename) = init_console()

        summary = {
            "변환 대상 파일": input_filename, 
            "변환 결과 파일": output_filename
        }
        print_summary(summary)
    except FileNotFoundError: 
        print("해당 파일을 찾을 수 없습니다.")
    except fitz.fitz.FileNotFoundError: 
        print("해당 파일을 찾을 수 없습니다.")
    except KeyError:
        print("올바른 파일인지 확인해 주세요.")
    except UnicodeDecodeError as e:
        print(e)

if __name__ == "__main__":
    xlsx_to_pdf()