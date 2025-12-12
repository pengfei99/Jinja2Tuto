from jinja2 import Environment, FileSystemLoader
from pathlib import Path

template_path = "C:/Users/pliu/Documents/git/Jinja2Tuto/jinja2Tuto/templates/"
template_name = "hello.html"

data = {
    "user": {
        "name": "Dalia",
        "roles": ["admin", "editor", "developer"],
    }
}


env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template(template_name)

html = template.render(data)
print(html)


output_path = Path("C:/Users/Public/Documents") / "hello_pengfei.html"
output_path.mkdir(parents=True, exist_ok=True)
output_path.write_text(html, encoding="utf-8")

