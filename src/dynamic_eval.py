class dynamic_eval(object):
    """
    a class to run dynamic eval tests
    """

    def __init__(self):
        pass

    @classmethod
    def class_divide(cls,x,y):
        return x/y
    
    def minus(self,x,y):
        return x-y
    
    def simple1(self):
        exp1 = "2*3+4"
        res1 = eval(exp1)
        print(res1)

        a,b = 2,3
        exp2 = "a + b"
        res2 = eval(exp2)        
        print(res2)

        res3 = self.minus(2,3)
        print(res3)

        print(eval("self.minus(b,a)"))
        print(dynamic_eval.class_divide(15, 4))
        print(eval("dynamic_eval.class_divide(15, 4) + self.minus(b, a)"))


        global_vars = {"x" : 12, "y" : 17, "dynamic_eval" : dynamic_eval, "self" : self}
        local_vars = {"a" : 84, "b" : 43}
        print(eval("dynamic_eval.class_divide(a,b) + self.minus(a,b)", globals = global_vars, locals = local_vars))

        exp3 = "[x for x in range(20) if x%2 == 0]"
        print(eval(exp3, {"range" : range}))

        exp4 = "x*y"
        comp_exp4 = compile(exp4, "<str>", 'eval')
        x, y = 4, 10
        print(eval(comp_exp4))
        x,y = 77, 31
        print(eval(comp_exp4))

    def calculator(self):
        while True:
            expr = input("Enter an expression ('q' to quit)")
            if expr.lower() == 'q':
                break
            try:
                print(f"Result: {eval(expr)}")
                # wrong,print(f"Result: eval(expr)")
            except (SystemError, NameError, ZeroDivisionError, TypeError) as e:
                print(f"Error: {e}")




# test = dynamic_eval()
# test.simple1()

dynamic_eval().calculator()