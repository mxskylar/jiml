#!/usr/bin/python3

import unittest
import subprocess
import os
import render
from jinja2_ext_custom_autoescaping import CustomAutoescapeExtension

class RenderTest(unittest.TestCase):

	projectPath = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
	templatesDir = os.path.join(projectPath, "templates")
	testOutputDir = os.path.join(projectPath, "test_output")

	def setUp(self):
		if not os.path.exists(self.testOutputDir):
			os.makedirs(self.testOutputDir)

	def testLatex(self):
		yaml = os.path.join(self.projectPath, 'test.yaml')
		template = os.path.join(self.templatesDir, 'tech-resume.tex')
		output = os.path.join(self.testOutputDir, 'tech-resume.tex')
		env = render.getEnvForTemplate(template)
		self.assertEqual(env.autoescape, render.BUILT_IN_LATEX_AUTOESCAPE)
		render.renderTemplate(yaml, template, output, env)

	def testHtml(self):
		yaml = os.path.join(self.projectPath, 'test.yaml')
		template = os.path.join(self.templatesDir, 'tech-resume.html')
		output = os.path.join(self.testOutputDir, 'tech-resume.html')
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