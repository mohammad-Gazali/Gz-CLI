import os


class ProjectTemplate:
    @staticmethod
    def make_templates_folder():
        os.makedirs("templates")


ProjectTemplate.make_templates_folder()
