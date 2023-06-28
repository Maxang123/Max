class MathExpression:
    def __init__(self, a, k):
        self.a = abs(a)  
        self.k = k  

    def is_proper_noun(self):
        return self.a == 0

    def find_max_exponent(self):
        return max(self.k)

    def is_constant(self):
        return all(exponent == 0 for exponent in self.k)

    def find_total_variables(self):
        return len(self.k)
    
    def __str__(self):
        expression = f"{self.a}"
        for i, exponent in enumerate(self.k):
            if exponent > 0:
                expression += f"x_{i}^{exponent}"
            elif exponent < 0:
                expression += f"x_{i}^{-abs(exponent)}"
        return expression
a = -0.5
k = [2, 1, 6]

math_expr = MathExpression(a, k)

print(math_expr.is_proper_noun())  # False
print(math_expr.find_max_exponent())  # 6
print(math_expr.is_constant())  # False
print(math_expr.find_total_variables())  # 3
print(str(math_expr))  # "-0.5x_0^2x_1x_2^6"
