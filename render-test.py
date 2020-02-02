#!/usr/bin/python3

import unittest
import render

class RenderTest(unittest.TestCase):

	def testLatex(self):
		yaml = 'test.yaml'
		template = 'templates/tech-resume.tex'
		output = 'test_output/resume.tex'
		env = render.getEnvForTemplate(template)
		render.renderTemplate(yaml, template, output, env)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RenderTest('testLatex'))
    return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())