#!/usr/bin/python3

import unittest
import importlib

class RenderTest(unittest.TestCase):

	def testLatex(self):
		print(render.escape_latex_characters("Foo &"))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('testLatex'))
    return suite

if __name__ == '__main__':
	render = importlib.import_module('./render', package='render')
	runner = unittest.TextTestRunner()
	runner.run(suite())