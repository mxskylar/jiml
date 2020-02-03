#!/usr/bin/python3

import os
import yaml
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_ext_custom_autoescaping import CustomAutoescapeExtension, enable_custom_autoescaping # https://github.com/mbello/jinja2-ext-custom-autoescaping

# LATEX
# Escapes special characters in Latex file       
def escapeLatexChars(val):
	# \ first to avoid double escpaing
	LATEX_SPECIAL_CHARACTERS = ['\\', '&', '{', '}', '%']
	LATEX_ESCAPED_CHARACTERS = ['/\\', '\&', '\{', '\}', '\%']
	if isinstance(val, str):
		for i in range(0, len(LATEX_SPECIAL_CHARACTERS)):
			val = val.replace(LATEX_SPECIAL_CHARACTERS[i], LATEX_ESCAPED_CHARACTERS[i])
	return val

# Taken from http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
CUSTOM_LATEX_AUTOESCAPE = select_autoescape(
	enabled_extensions=['tex'],
    disabled_extensions=[],
    default_for_string=False,
    default=False
)

BUILT_IN_LATEX_AUTOESCAPE = select_autoescape(
	enabled_extensions=['html', 'htm', 'xml'],
    disabled_extensions=['tex'],
    default_for_string=True,
	default=True
)

LATEX_OPS = {
	'custom_select_autoescape': CUSTOM_LATEX_AUTOESCAPE,
   	'custom_autoescape_filter_name': 'escapeLatexChars',
    'custom_autoescape_filter_func': escapeLatexChars
}

# JINJA
# Gets Jinja environment for given template
def getEnvForTemplate(template):
	templateExt = os.path.basename(os.path.splitext(template)[1])[1:]
	templateDir = os.path.dirname(template)

	if templateExt == 'tex':
		latexEnv = Environment(
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
		    loader=FileSystemLoader(templateDir, followlinks=True),
			autoescape=BUILT_IN_LATEX_AUTOESCAPE
		)
		enable_custom_autoescaping(latexEnv, **LATEX_OPS)
		return latexEnv
	elif templateExt == 'html' or templateExt == 'xml':
		return Environment(
			loader=FileSystemLoader(templateDir, followlinks=True),
			autoescape=select_autoescape(['html', 'xml'])
		)
	else:
		return Environment(
			loader=FileSystemLoader(templateDir, followlinks=True)
		)

# Renders template for given yaml file
def renderTemplate(yamlFile, template, outputFile, env):
	yamlInput = yaml.load(open(yamlFile, 'r').read(), Loader=yaml.FullLoader)
	env = getEnvForTemplate(template)
	templateFile = os.path.basename(template)

	rendered = env.get_template(templateFile).render(yamlInput)
	with open(outputFile, 'w') as output:
		output.write(rendered)
	print('%s rendered to %s' % (yamlFile, outputFile))

if __name__ == '__main__':
	# Arguments
	parser = ArgumentParser(description='Generates Jinja template from YAML file.')
	parser.add_argument('--yaml', '-y', help='YAML config file.')
	parser.add_argument('--template', '-t', help='Jinja2 LaTeX template.')
	parser.add_argument('--output', '-o', help='LaTeX file to render.')
	args = parser.parse_args()

	env = getEnvForTemplate(args.template)
	renderTemplate(args.yaml, args.template, args.output, env)