#!/usr/bin/python3

import unittest
import render
from jinja2_ext_custom_autoescaping import CustomAutoescapeExtension

class RenderTest(unittest.TestCase):

	def testLatex(self):
		yaml = 'test.yaml'
		template = 'templates/tech-resume.tex'
		output = 'test_output/tech-resume.tex'
		env = render.getEnvForTemplate(template)
		self.assertEqual(env.autoescape, render.BUILT_IN_LATEX_AUTOESCAPE)
		render.renderTemplate(yaml, template, output, env)

	def testHtml(self):
		yaml = 'test.yaml'
		template = 'templates/tech-resume.html'
		output = 'test_output/tech-resume.html'
		env = render.getEnvForTemplate(template)
		render.renderTemplate(yaml, template, output, env)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RenderTest('testLatex'))
    suite.addTest(RenderTest('testHtml'))
    return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())