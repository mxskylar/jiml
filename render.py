#!/usr/bin/python3

import yaml
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_ext_custom_autoescaping import CustomAutoescapeExtension, enable_custom_autoescaping # https://github.com/mbello/jinja2-ext-custom-autoescaping

# Escapes special characters in Latex file       
def escape_latex_characters(val):
	# \ first to avoid double escpaing
	LATEX_SPECIAL_CHARACTERS = ['\\', '&', '{', '}', '%']
	LATEX_ESCAPED_CHARACTERS = ['/\\', '\&', '\{', '\}', '\%']
	if isinstance(val, str):
		for i in range(0, len(LATEX_SPECIAL_CHARACTERS)):
			val = val.replace(LATEX_SPECIAL_CHARACTERS[i], LATEX_ESCAPED_CHARACTERS[i])
	return val

TEMPLATES_DIR = 'templates'

if __name__ == '__main__':
	# Arguments
	parser = ArgumentParser(description='Generates Jinja template from YAML file.')
	parser.add_argument('--yaml', '-y', help='YAML config file.')
	parser.add_argument('--template', '-t', help='Jinja2 LaTeX template. Located in ' + TEMPLATES_DIR + ' directory.')
	parser.add_argument('--output', '-o', help='LaTeX file to render.')
	args = parser.parse_args()

	# Prepare template
	built_in_select_autoescape = select_autoescape(
		enabled_extensions=['html', 'htm', 'xml'],
	    disabled_extensions=['tex'],
	    default_for_string=True,
		default=True
	)
	custom_select_autoescape = select_autoescape(
		enabled_extensions=['tex'],
	    disabled_extensions=[],
	    default_for_string=False,
	    default=False
	)
	yamlInput = yaml.load(open(args.yaml, 'r').read(), Loader=yaml.FullLoader)
	# Taken from http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
	env = Environment(
	    block_start_string='\BLOCK{',
	    block_end_string='}',
	    variable_start_string='\VAR{',
	    variable_end_string='}',
	    comment_start_string='\#{',
	    comment_end_string='}',
	    line_statement_prefix='%%',
	    line_comment_prefix='%#',
	    trim_blocks=True,
	    extensions=[CustomAutoescapeExtension],
	    loader=FileSystemLoader(TEMPLATES_DIR, followlinks=True),
		autoescape=built_in_select_autoescape
	)
	opts = {
		'custom_select_autoescape': custom_select_autoescape,
	   	'custom_autoescape_filter_name': 'escape_latex_characters',
	    'custom_autoescape_filter_func': escape_latex_characters
	}
	enable_custom_autoescaping(env, **opts)

	# Render template
	latex = env.get_template(args.template).render(yamlInput)
	with open(args.output, 'w') as output:
		output.write(latex)
	print('%s rendered to %s' % (args.yaml, args.output))
