import shutil, os, filecmp

def get_good_filename(fname):
    """
    fname - это имя png-файла.
    Пока имя файла существует, добавь к нему символ _,
    прямо перед частью png имени файла, то есть 9595.png -> 9595_.png.
    
    Верни получившееся имя файла.
    """
    while os.path.exists(fname):
        return fname.replace('.png', '_.png')
    return fname

def make_copy(src, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for file in os.listdir(target_dir):
        import pdb; pdb.set_trace()
        if filecmp.cmp(src, os.path.join(target_dir, file)):
            return
    shutil.copy(src, get_good_filename(os.path.join(target_dir, os.path.basename(src))))

def make_copies(dirs, target_dir):
    """
    dirs - это список каталогов с файлами.
    target_dir - это каталог, куда нужно скопировать файлы.
    Сравни файлы в каждом каталоге dirs с файлами в target_dir.
    Если файлы не идентичны, то скопируйте их в target_dir.
    """
    for directory in dirs:
        for file in os.listdir(directory):
            make_copy(os.path.join(directory, file), target_dir)
            
# файлы лежат в каталоге ch9
make_copies(['ch9/pictures1', 'ch9/pictures2'], 'ch9/pictures_combined')

