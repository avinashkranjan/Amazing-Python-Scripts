import moviepy.editor as mp

clip = mp.AudioFileClip("insert_path_to_webm_file").subclip()
clip.write_audiofile("insert_path_to_save_mp3_file")
clip.close()
