# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputUpperBV(self):
        self.assertEqual(classifyTriangle(201, 201, 201), "InvalidInput", "Inputs are greater than 200.")

    def testInvalidInputLowerBV(self):
        self.assertEqual(classifyTriangle(0,0,0), "InvalidInput", "Value less than or equal to 0.")

    def testInstancesA(self):
        self.assertEqual(classifyTriangle(3.1,4,5), "InvalidInput", "a not int")

    def testInstancesB(self):
        self.assertEqual(classifyTriangle(3,"4",5), "InvalidInput", "b is not int")

    def testInstanceC(self):
        self.assertEqual(classifyTriangle(3,4, True), "InvalidInput", "c is not int.")

    def testNotaTriangleA(self):
        self.assertEqual(classifyTriangle(10, 2, 3), 'NotATriangle', 'a too big')
    
    def testNotaTriangleB(self):
        self.assertEqual(classifyTriangle(2,10,3),'NotATriangle', "Large b input")

    def testNotaTriangleC(self):
        self.assertEqual(classifyTriangle(2,3,10),'NotATriangle',"Large C input.")

    def testRightBHypotenuse(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','B input is hypotenuse.')

    def testScalene(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '7 8 9 is a scalene triangle')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(7, 9, 8), 'Scalene', '7 9 8 is a scalene triangle')

    def testScaleneC(self):
        self.assertEqual(classifyTriangle(9, 8, 7), 'Scalene', '9 8 7 is a scalene triangle')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(6,5,5), "Isosceles", '6 5 5 is Isosceles')
    
    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5,6,5), 'Isosceles', '5 6 5 is isosceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(5,5,6), 'Isosceles', '5 5 6 is isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

