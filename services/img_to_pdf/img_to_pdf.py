"""
변환하려는 이미지들을 img_to_pdf_input
경로에 넣어주세요.
"""
def img_to_pdf():
    import os
    import shutil
    from PIL import Image
    from utils import print_summary, create_dir_if_not_exist

    def convert_rgb(file):
        image_path = f'{base_input_path}/{file}'
        target_image = Image.open(image_path)
        # wpercent = basewidth / float(target_image.size[0])
        # hsize = int((float(target_image.size[1]) * float(wpercent)))
        # target_image = target_image.resize((basewidth,hsize), Image.Resampling.LANCZOS)
        
        return target_image.convert('RGB')
        # jpg_image = Image.new("RGB", target_image.size, (255, 255, 255))
        # jpg_image.paste(target_image, target_image)

        # new_file_name = file.split('.')[0]
        # jpg_image.save(f'./tmp/{new_file_name}.jpg')
        # jpg_image = Image.open(f'./tmp/{new_file_name}.jpg')
        
        # return jpg_image
    try:

        print("변환 결과 PDF 이름을 입력해 주세요:", end = ' ')
        ouput_filename = input().strip()

        basewidth = 300
        base_path = 'services/img_to_pdf'
        base_input_path = os.path.abspath(f'{base_path}/img_to_pdf_input')
        base_output_path = os.path.abspath(f'{base_path}/img_to_pdf_output')
        create_dir_if_not_exist(base_output_path)

        copy_path = os.path.abspath('services/pdf_to_docx/pdf_to_docx_input')
        file_list = os.listdir(base_input_path)
        file_list.sort()

        image_list = []

        for file in file_list:
            cvt_rgb = convert_rgb(file)
            image_list.append(cvt_rgb)

        output_file = f'{base_output_path}/{ouput_filename}.pdf'
        image_list[0].save(
            output_file, 
            resolution=100.0, 
            save_all=True, 
            dpi=(150, 150),
            append_images=image_list[1:],
        )

        shutil.copyfile(output_file, f'{copy_path}/{ouput_filename}.pdf')

        summary = {
            "이미지 파일 개수": len(image_list), 
            "변환 결과 파일": output_file, 
        }
        print_summary(summary)
    except FileNotFoundError: 
        print("해당 파일을 찾을 수 없습니다.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    img_to_pdf()