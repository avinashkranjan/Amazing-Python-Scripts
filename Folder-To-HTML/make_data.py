import os

data_folder = 'td_data'
static_folder = 'td_static'
html_file = 'data_view.html'
data_dir_path = os.path.dirname(os.path.abspath(__file__))


class DataView():

    def __init__(self, data_folder, html_file):
        self.data_folder = data_folder
        self.html_file = html_file

        self.all_tags = set()
        self.objects = {
            '.mp4': [],
            '.mp3': [],
            '.pdf': [],
            'other': []
        }

        self.allowed_data_types = ['.mp4', '.mp3', '.pdf']
        self.data_types = {
            '.mp4': """
                    <video class="td-video" controls>
                        <source src="{src_info}" type="video/mp4">
                    </video>
                    """,
            '.mp3': """
                    <audio class="td-audio" controls>
                        <source src="{src_info}" type="audio/ogg">
                    </audio>
                    """,
            ".pdf": """
                    <a class="td-pdf" href="file://""" + data_dir_path + """/{src_info}" target="_blank" >OPEN</a>
                    """

        }
        self.list_of_files = {}

    def find_all_files(self):
        for (dirpath, dirnames, filenames) in os.walk(data_folder):
            for filename in filenames:
                self.list_of_files[filename] = os.sep.join([dirpath, filename])

    def write_first_html(self, src_tags):
        with open(self.html_file, 'w') as h_file:
            h_file.write(
                """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">

                    <!-- ALL THE OUTSIDE CSS -->

                    <!-- ALL CUSTOM CSS -->
                    <link rel="stylesheet" href=" """ + static_folder + """/css/main/data_view.css">

                    <title>Data View</title>

                </head>
                <body>
                <div class="_td-s">
                    <div id="search">
                        <input id="td-input" type="text" placeholder="Find data...">
                    </div>
                </div>
                <div class="td-main">
                    <div class="td-right">
                        <div class="_td-t">
                            <div class="_td-te tag-active">#all</div>
                            {src_tags}
                        </div>
                    </div>
                    <div class="td-left">
                        <div class="_td-c">
                """.format(src_tags=src_tags)
            )

    def write_middle_html(self, object):
        ext = object['ext']
        src_info = object['src_info']
        src_name = object['src_name']
        src_tags = object['src_tags']

        with open(self.html_file, 'a') as h_file:
            h_file.write(
                """
                <div class="td-element">
                    {src_info}
                    <div class="_tde-info">{src_name}</div>
                    <div class="_tde-tags">{src_tags}</div>
                </div>
                """.format(src_info=self.data_types[ext].format(src_info=src_info), src_name=src_name, src_tags=src_tags)
            )

    def write_end_html(self):
        with open(self.html_file, 'a') as h_file:
            h_file.write(
                """
                        </div>
                    </div>
                </div>
                <!-- ALL OUTSIDE SCRIPTS -->
                <script src=" """ + static_folder + """/js/outside/jquery-3.6.1.min.js"></script>

                <!-- ALL MAIN SCRIPTS-->
                <script src=" """ + static_folder + """/js/main/data_view.js"></script>
                </body>
                </html>
                """
            )

    def work_on_files(self):
        for file_name in self.list_of_files:
            file_path = self.list_of_files[file_name]
            name, ext = os.path.splitext(file_name)

            tags = file_path.split('/')
            tags.remove(self.data_folder)
            tags.remove(file_name)

            self.all_tags.update(tags)

            src_tags = '\n'.join(
                '<span class="_td-te2">#{}</span>'.format(t) for t in tags)

            if ext in self.allowed_data_types:
                object = {
                    'ext': ext,
                    'src_info': file_path,
                    'src_name': name,
                    'src_tags': src_tags,
                }

                self.objects[ext].append(object)

        src_tags = '\n'.join('<div class="_td-te">#{}</div>'.format(t)
                             for t in list(self.all_tags))

        self.write_first_html(src_tags)

        for ext, object_list in self.objects.items():
            for object_dict in object_list:
                self.write_middle_html(object_dict)

        self.write_end_html()


data_obj = DataView(data_folder, html_file)
data_obj.find_all_files()
data_obj.work_on_files()
