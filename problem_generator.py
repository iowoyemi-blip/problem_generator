# File: problem_generator.py

import random

def generate_linear_equation():
    """Generates a two-step linear equation like ax + b = c."""
    a = random.randint(2, 9)
    b = random.randint(1, 10)
    # Choose a simple integer solution for x first
    x = random.randint(-5, 5)
    
    # Calculate c based on a, b, and x
    c = a * x + b
    
    # Ensure b is positive for the initial problem format
    sign = "+" if b > 0 else "-"
    
    problem = f"Solve for x: ${a}x {sign} {abs(b)} = {c}$"
    answer = f"$x = {x}$"
    return problem, answer

def generate_simplify_expression():
    """Generates an expression to simplify like 3(2x + 4) - 5x."""
    a = random.randint(2, 5)
    b = random.randint(2, 6)
    c = random.randint(1, 5)
    d = random.randint(1, 9)

    # Simplified form coefficients
    final_x_coeff = a * b - c
    final_const = a * d

    problem = f"Simplify the expression: ${a}({b}x + {d}) - {c}x$"
    answer = f"${final_x_coeff}x + {final_const}$"
    return problem, answer

def generate_factoring_quadratic():
    """Generates a simple quadratic to factor: x^2 + bx + c."""
    # Start with the roots to ensure nice integer factoring
    r1 = random.randint(-9, 9)
    r2 = random.randint(-9, 9)
    
    # Avoid roots that are zero to keep it a trinomial
    if r1 == 0: r1 = 10
    if r2 == 0: r2 = -10
        
    # Calculate coefficients b and c for x^2 + bx + c = (x - r1)(x - r2)
    b = -(r1 + r2)
    c = r1 * r2
    
    # Determine signs for the problem string
    b_sign = "+" if b > 0 else "-"
    c_sign = "+" if c > 0 else "-"
    
    problem = f"Factor the trinomial: $x^2 {b_sign} {abs(b)}x {c_sign} {abs(c)}$"
    
    # Format the answer string (x - r1)(x - r2)
    r1_sign = "-" if r1 > 0 else "+"
    r2_sign = "-" if r2 > 0 else "+"
    answer = f"$(x {r1_sign} {abs(r1)})(x {r2_sign} {abs(r2)})$"
    
    return problem, answer

# A dictionary to easily access the functions by name
TOPICS = {
    "Two-Step Linear Equations": generate_linear_equation,
    "Simplify Expressions": generate_simplify_expression,
    "Factor Simple Quadratics": generate_factoring_quadratic,
}