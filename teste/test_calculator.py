import pytest
from src.calculator import Calculator

class TestCalculator():
    


    def setup_class(self):
        self.calc = Calculator()


    #def setup_method(self):
     #   self.calc = Calculator()
    

    def teardown_class(self):
        print("!!")


#    def teardown_method(self):
#        print("!!")


    def test_addition(self):
       
        assert self.calc.addition(2,2) == 4
    

    @pytest.mark.skip(reason="caso de teste duplicado") #notação para pulao o teste
    def test_subtraction(self):
       
        assert self.calc.subtraction(10,1) == 9, "Esperava 3, mas o resultado foi {}".format(self.calc.subtraction(10,1))
    
    def test_multiplication(self):
        
        assert self.calc.multiplication(3,4) == 12
    
    def test_division(self):
       
        assert self.calc.division(10,2) == 5

    def test_division_by_zero(self):
        
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10,0)