#!/usr/bin/python3

import unittest
import render

class RenderTest(unittest.TestCase):

	def testLatex(self):
		self.assertEquals(render.env, render.LATEX_ENVIRONMENT)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RenderTest('testLatex'))
    return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())