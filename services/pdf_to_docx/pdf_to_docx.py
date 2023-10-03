"""Converts pdf to docx"""
def pdf_to_docx():
    import fitz
    from pdf2docx import parse
    from utils import print_summary, create_dir_if_not_exist
    import os

    def init_console():
        base_path = 'services/pdf_to_docx'
        base_input_path = os.path.abspath(f'{base_path}/pdf_to_docx_input')
        base_output_path = os.path.abspath(f'{base_path}/pdf_to_docx_output')
        create_dir_if_not_exist(base_output_path)

        print("변환하려는 PDF 파일 이름을 입력해 주세요:", end = ' ')
        input_filename = f'{base_input_path}/{input().strip()}.pdf'
        print("변환 결과 DOCX 파일 이름을 입력해 주세요:", end = ' ')
        output_filename = f'{base_output_path}/{input().strip()}.docx'

        return (input_filename, output_filename)
    
    try:
        (input_filename, output_filename) = init_console()
        parse(input_filename, output_filename, start=0, end=None)

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
    # import sys
    # input_filename = sys.argv[1]
    # output_filename = sys.argv[2]
    # pdf_to_docx(f'./pdf_to_docx_input/{input_filename}.pdf', f'./pdf_to_docx_output/{output_filename}.docx')
    pdf_to_docx()