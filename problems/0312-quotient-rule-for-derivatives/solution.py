import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def eval_poly_and_derivative(coeffs, x):
        value = coeffs[0]
        derivative = 0.0

        for coeff in coeffs[1:]:
            derivative = derivative * x + value
            value = value * x + coeff

        return value, derivative

    g, g_prime = eval_poly_and_derivative(g_coeffs, x)
    h, h_prime = eval_poly_and_derivative(h_coeffs, x)

    return (g_prime * h - g * h_prime) / (h ** 2)