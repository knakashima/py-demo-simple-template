from jinja2 import Template
import yaml

datavars = yaml.load(open('l2circuit.yml').read())
template = Template(open('l2circuit.j2').read())
print template.render(datavars)

