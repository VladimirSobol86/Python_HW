import os


def sort_files(dir_path: str, video_dir: str = 'Video', image_dir: str = 'Image', music_dir: str = 'Music',
               doc_dir: str = 'Documents'):
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    video_extensions = ['mov', 'mp4', 'mkv', 'avi']
    image_extensions = ['png', 'jpeg', 'bmp', 'psd']
    music_extensions = ['mp3', 'wav', 'ogg']
    documents_extensions = ['txt', 'doc', 'xls']
    all_extensions = {video_dir: video_extensions,
                      image_dir: image_extensions,
                      music_dir: music_extensions,
                      doc_dir: documents_extensions}

    def sort_files(current_file: str, dist_dir: str):
        _, cur_ext = current_file.split('.')
        if cur_ext in all_extensions.get(dist_dir):
            if not os.path.isdir(os.path.join(dir_path, dist_dir)):
                os.mkdir(os.path.join(dir_path, dist_dir))
            os.replace(os.path.join(dir_path, current_file), os.path.join(dir_path, dist_dir, current_file))

    for cur_file in file_list:
        for directory in all_extensions:
            sort_files(cur_file, directory)

    return f'Файлы в папке {dir_path} отсортированы по типам'

sort_files('Lesson7/Example_files')