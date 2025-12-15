from pathlib import Path

from jinja2 import FileSystemLoader, Environment, TemplateNotFound


class ReportGenerator:

    def __init__(self, template_dir: str):
        self.template_env = self._build_template_env(template_dir)

    @staticmethod
    def _build_template_env(template_dir: str) -> Environment:
        """
        This function build a jinja template environment.
        :param template_dir:
        :return:
        """
        return Environment(loader=FileSystemLoader(template_dir))

    def generate_source(self, template_name: str, template_params: dict) -> str | None:
        """
        This function generate a source file based on the given jinja template and parameters.
        :param template_name: file name of the jinja2 template
        :param template_params: a dict of template parameters
        :return: the generated source in str or none
        """
        try:
            template = self.template_env.get_template(template_name)
            return template.render(template_params)
        except Exception as e:
            error_msg = f"Can not generate the resource based on the giving template name and parameters. {e}"
            print(error_msg)
            return None

    def display_generated_source(self, template_name: str, template_params: dict) -> None:
        """
        This function display the generated source file.
        :param template_name: file name of the jinja2 template
        :param template_params: a dict of template parameters
        :return:
        """
        source = self.generate_source(template_name, template_params)
        if source is not None:
            print(source)
        else:
            print("Something went wrong, can't display the generated source.")

    def persist_generated_source(self, template_name: str, template_params: dict, output_path: str) -> bool:
        """
        This function generate a source file based on the given jinja template and parameters, then persist it to disk.
        :param template_name: file name of the jinja2 template
        :param template_params:
        :param output_path: The path of the output file.
        :return: if the source file was successfully persisted return true, otherwise false.
        """
        # step 1: create the folder with given path, if it not exists.
        out_file_path = Path(output_path)
        parent_dir = out_file_path.parent
        try:
            parent_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            error_msg = f"Failed to create parent directory {parent_dir}. Error: {e}"
            print(error_msg)
            return False

        # step 2: generate the source based on the template and parameters
        source = self.generate_source(template_name, template_params)

        # step3: write the generated source to a file.
        if source is None:
            print("Something went wrong, can't generate the source.")
            return False
        else:
            out_file_path.write_text(source, encoding="utf-8")
            return True
