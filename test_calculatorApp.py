import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 9)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)
        
        
    def test_check_user_inputPass(self):
        self.assertEqual(check_user_input(2), 2)
            
    def test_check_user_inputInvalid(self):
        self.assertNotEqual(check_user_input(2), 3)
        
    def test_check_user_inputInvalid(self):
        self.assertEqual(check_user_input('2.1'), 2.1)
        
    def test_check_user_inputNullInput(self):
        self.assertRaises(ValueError, check_user_input,'')
                
    def test_check_user_inputInvalidInput(self):
        self.assertRaises(ValueError, check_user_input,'W')
        
    def test_check_user_inputInvalidInputRegex(self):
        with self.assertRaisesRegex(ValueError, "Input can't be empty"):
             check_user_input('')
                
    def test_check_user_inputInvalidInputRegex2(self):
        with self.assertRaisesRegex(ValueError, " input is not a number!"):
             check_user_input('w')
#########            
    
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9) 
           
    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 6)
        
    def test_AddNullInput(self):
        self.assertRaises(ValueError, calculate, '1','','3')
                
    def test_AddInvalidInput(self):
        self.assertRaises(ValueError, calculate, '1','3','w')
        
    def test_addInvalidInputRegex(self):
        with self.assertRaisesRegex(ValueError, " input is not a number!"):
             calculate('1','3','v')
        
###############################

    def test_subtractPass(self):
        self.assertEqual(subtract(6,3), 3)
        with mock.patch('calculatorApp.subtract', return_value = 2):
            result = calculate('2',6,4)
        self.assertEqual(result, 2)
         
        

    def test_subtractInvalid(self):
        with mock.patch('calculatorApp.subtract', return_value = 2):
            result = calculate('2',6,4)
        self.assertNotEqual(result, 3)
   
        
    def test_subtractNullInput(self):
        self.assertRaises(ValueError, calculate, '2','3','')
                
    def test_subtractInvalidInput(self):
        self.assertRaises(ValueError, calculate, '2','3','w') 
        
    def test_subtractInvalidInputRegex(self):
        with self.assertRaisesRegex(ValueError, " input is not a number!"):
             calculate('2','3','v')   
###############################

    def test_multiplyPass(self):
        self.assertEqual(multiply(6,3), 18)
        with mock.patch('calculatorApp.multiply', return_value = 18):
            result = calculate('3',6,3)
        self.assertEqual(result, (6, '*', 3, '=', 18))
         
        

    def test_multiplyInvalid(self):
        with mock.patch('calculatorApp.multiply', return_value = 2):
            result = calculate('3',6,4)
        self.assertNotEqual(result, 20)
   
        
    def test_multiplyNullInput(self):
        self.assertRaises(ValueError, calculate, '3','3','')
     
    def test_multiplyNullInput(self):
        self.assertRaises(ValueError, calculate, '3','3',None)
        
    def test_multiplyInvalidInput(self):
        self.assertRaises(ValueError, calculate, '3','3','w') 

    
    def test_subtractInvalidInputRegex(self):
        with self.assertRaisesRegex(ValueError, " input is not a number!"):
             calculate('3','3','v')
                
###############################

    def test_DividPass(self):
        self.assertEqual(divide(6,3), 2)
        with mock.patch('calculatorApp.divide', return_value = 2):
            result = calculate('4',6,3)
        self.assertEqual(result, (6, '/', 3, '=', 2))

    def test_DividByZero(self):
        self.assertRaises(ZeroDivisionError, divide, 6,0)  
        
    def test_DividPass2(self):
        self.assertEqual(divide(6,3), 2)
        
    def test_DividNullInput(self):
        self.assertRaises(ValueError, calculate, '4','3',None)  

    def test_DividInvalid(self):
        with mock.patch('calculatorApp.divide', return_value = 2):
            result = calculate('4',6,4)
        self.assertNotEqual(result, (6, '/', 3, '=', 5))
        
    def test_DividPass(self):
        self.assertEqual(divide(0,3), 0) 
        
        
    def test_DividByZerrorEx1(self):
        with self.assertRaises(ZeroDivisionError):
             calculate('4','3','0')
    
    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ZeroDivisionError, "You can't divide by zero!"):
             calculate('4','3','0')
                
    def test_DividByNullValue(self):
        with self.assertRaises(ValueError):
             calculate('4','3','')
                
    def test_DividByNullRegex(self):
        with self.assertRaisesRegex(ValueError, "inputs can not be null"):
             calculate('4','3','')
                
    def test_DividByInvalidInput(self):
        with self.assertRaises(ValueError):
             calculate('4','3','W')
                
    def test_DividByInvalidInputRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')
                
    def test_InvalidChoice(self):
        self.assertRaises(Exception, calculate, '5','3','1')

    def test_InvalidChoiceRegex(self):
        with self.assertRaisesRegex(Exception, "Invalid choice!"):
             calculate('5','3','2')
###############################

    def test_isExitTrue(self):
        self.assertEqual(isExit("no"), True)
        
    def test_isExitFalse(self):
        self.assertEqual(isExit("yes"), False)
    
    def test_InvalidChoiceRegex1(self):
        with self.assertRaisesRegex(ValueError, "Invalid choice"):
             isExit("Hi")
                
    def test_InvalidChoice2(self):
        self.assertRaises(ValueError, isExit, 'Hi')
        
    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9)

if __name__ == '__main__':
	unittest.main()