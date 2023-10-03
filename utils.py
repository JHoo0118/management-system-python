def print_summary(summary):
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('RESULT'))
    print("\n".join("{}: {}".format(i, j) for i, j in summary.items()))
    print("\n")

def color_print(color, text):
    from termcolor import colored, cprint

    print_red = lambda x: cprint(x, 'red')
    print_blue = lambda x: cprint(x, 'blue')
    print_green = lambda x: cprint(x, 'green')
    print_yellow = lambda x: cprint(x, 'yellow')
    print_grey = lambda x: cprint(x, 'grey')

    if color == "red":
        print_red(text)
    elif color == "blue":
        print_blue(text)
    elif color == "green":
        print_green(text)
    elif color == "yellow":
        print_yellow(text)
    elif color == "grey":
        print_grey(text)
    else:
        print(text)

def clean_ouput_dir_by_multiple_select():
    import glob
    import os
    from simple_term_menu import TerminalMenu

    dirs = glob.glob('./services/*/*output')
    terminal_menu = TerminalMenu(
        dirs, 
        title=color_print(
            color='red', 
            text="작업 결과 내용물을 삭제할 디렉토리를 선택하세요.", 
        ),
        multi_select=True,
        show_multi_select_hint=True,
    )
    color_print(color='grey', text="뒤로 가시려면 'ctrl + c'를 눌러주세요.")
    # (0, 1, 2)
    menu_entry_indices = terminal_menu.show()

    delete_options = [
        "[y] 예", 
        "[n] 아니요", 
    ]
    delete_menu = TerminalMenu(
        delete_options, 
        title=color_print(
            color='red', 
            text="정말 선택하신 디렉토리의 결과 내용물을 모두 삭제하시겠습니까?", 
        ),
    )
    menu_entry_index = delete_menu.show()
    if menu_entry_index == 0:
        # ('./services/pdf_to_docx/pdf_to_docx_output', './services/img_to_pdf/img_to_pdf_output', './services/merge_pdf/merge_pdf_output')
        for target_dir in terminal_menu.chosen_menu_entries:
            for filename in os.listdir(target_dir):
                file_path = os.path.join(target_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print('파일 삭제 실패: %s. 원인: %s' % (file_path, e))
    
    
def create_dir_if_not_exist(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)