from services import *
def main():
    import sys
    from simple_term_menu import TerminalMenu
    from pyfiglet import Figlet
    from utils import color_print, clean_ouput_dir_by_multiple_select
    
    try:
        f = Figlet(font='slant')
        color_print(color='yellow', text=f.renderText('Management'))
        color_print(color='green', text=f.renderText('System'))
        menus = [
            "[a] 여러개의 이미지를 pdf로 변환", 
            "[b] PDF를 DOCX로 변환", 
            "[c] XLSX의 특정 시트를 DOCX 테이블로 변환",
            "[d] XLSX를 DOCX로 변환(작업 중...)",
            "[e] XLSX를 PDF로 변환(작업 중...)",
            "[f] PDF 병합",
            "[g] 작업 결과 내용물 삭제",
            "[x] 종료"
        ]

        terminal_menu = TerminalMenu(menus, title=color_print(color='blue', text="작업을 선택하세요."))

        while True:
            menu_entry_index = terminal_menu.show()
            print('\n')

            if menu_entry_index == None:
                color_print(color='grey', text='작업을 종료합니다.')
                break
            
            if menu_entry_index == len(menus) - 1:
                break
            elif menu_entry_index == 0:
                img_to_pdf()
            elif menu_entry_index == 1:
                pdf_to_docx()
            elif menu_entry_index == 2:
                xlsx_sheet_to_docx_table()
            elif menu_entry_index == 3:
                xlsx_to_docx()
            elif menu_entry_index == 4:
                xlsx_to_pdf()
            elif menu_entry_index == 5:
                merge_pdf()
            elif menu_entry_index == 6:
                clean_ouput_dir_by_multiple_select()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()