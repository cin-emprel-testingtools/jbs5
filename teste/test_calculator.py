import pytest
from src.calculator import Calculator

class TestCalculator():
    


    def setup_class(self):
        self.calc = Calculator()

 

    def teardown_method(self):
        print(" fim do test")


    @pytest.mark.skip(reason=" funcionadidade ainda não implementada") 
    def test_addition(self):
       
        assert self.calc.addition(2,2) == 4
    

    @pytest.mark.skip(reason=" funcionadidade ainda não implementada") 
    def test_subtraction(self):
       
          assert self.calc.subtraction(10,1) == 9, "Esperava 3, mas o resultado foi {}".format(self.calc.subtraction(10,1))
    
    @pytest.mark.skip(reason=" funcionadidade ainda não implementada") 
    def test_multiplication(self):
        
        assert self.calc.multiplication(3,4) == 12

    def test_additionDois(self):
        assert self.calc.addition(6,6) == 12

    def test_division(self):
       
      assert self.calc.division(10,2) == 5