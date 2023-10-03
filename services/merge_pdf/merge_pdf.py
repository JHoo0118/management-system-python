def merge_pdf():
    import fitz
    import os
    from utils import print_summary
    
    try:
        print("병합 결과 PDF 이름을 입력해 주세요:", end = ' ')
        ouput_filename = input().strip()

        base_path = 'services/merge_pdf'
        base_input_path = os.path.abspath(f'{base_path}/merge_pdf_input')
        base_output_path = os.path.abspath(f'{base_path}/merge_pdf_output')
        create_dir_if_not_exist(base_output_path)
        file_list = os.listdir(base_input_path)
        file_list.sort()
        
        result = fitz.open()

        for pdf in file_list:
            open_file_path = f'{base_input_path}/{pdf}'
            with fitz.open(open_file_path) as mfile:
                result.insert_pdf(mfile)

        output_file = f'{base_output_path}/{ouput_filename}.pdf'
        result.save(output_file)
        summary = {
            "병합된 PDF 파일 개수": len(file_list), 
            "병합 결과 파일": output_file, 
        }
        print_summary(summary)
    except fitz.fitz.FileNotFoundError: 
        print("해당 파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    merge_pdf()