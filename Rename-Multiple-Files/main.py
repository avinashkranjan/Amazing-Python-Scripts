import os
import platform


ROOT_DIR = os.getcwd() + '/root'
PATH_DELIMITER = ''
DESTINATION_FILE_DELIMITER = '-'
COUNTER = 0


if (platform.system() == 'Linux') or (platform.system() == 'Darwin'):
    PATH_DELIMITER = '/'
elif (platform.system() == 'Windows'):
    PATH_DELIMITER = '\\'

for current_dir in os.listdir(ROOT_DIR):
    subdir = ROOT_DIR + PATH_DELIMITER + current_dir
    if os.path.isdir(subdir):
        print('Now working with: "' + subdir + '" directory')
        COUNTER = 0
        for current_file in os.listdir(subdir):
            COUNTER += 1
            current_file_full_path = subdir + PATH_DELIMITER + current_file
            renamed_file_full_path = subdir + PATH_DELIMITER + current_dir + DESTINATION_FILE_DELIMITER + str(COUNTER) + '.' + current_file.split('.')[-1]
            try:
                os.rename(current_file_full_path, renamed_file_full_path)
            except Exception as e:
                print('Error occurred because: ' + e)
