#!/usr/bin/python3

import unittest
import subprocess
import os
import render
from jinja2_ext_custom_autoescaping import CustomAutoescapeExtension

class RenderTest(unittest.TestCase):

	projectPath = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
	templatesDir = os.path.join(projectPath, "templates")

	def testLatex(self):
		yaml = os.path.join(self.projectPath, 'demo.yaml')
		template = os.path.join(self.templatesDir, 'tech-resume.tex')
		output = os.path.join(self.projectPath, 'demo-resume.tex')
		env = render.getEnvForTemplate(template)
		self.assertEqual(env.autoescape, render.BUILT_IN_LATEX_AUTOESCAPE)
		render.renderTemplate(yaml, template, output, env)

	def testHtml(self):
		yaml = os.path.join(self.projectPath, 'demo.yaml')
		template = os.path.join(self.templatesDir, 'tech-resume.html')
		output = os.path.join(self.projectPath, 'demo-resume.html')
		env = render.getEnvForTemplate(template)
		render.renderTemplate(yaml, template, output, env)

	def testDefault(self):
		yaml = os.path.join(self.projectPath, 'demo.yaml')
		template = os.path.join(self.templatesDir, 'unescaped-resume-demo.txt')
		output = os.path.join(self.projectPath, 'demo-unescaped.txt')
		env = render.getEnvForTemplate(template)
		render.renderTemplate(yaml, template, output, env)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RenderTest('testLatex'))
    suite.addTest(RenderTest('testHtml'))
    suite.addTest(RenderTest('testDefault'))
    return suite

if __name__ == '__main__':
    unittest.main(failfast=True)
    runner = unittest.TextTestRunner()
    runner.run(suite())
