# File: problem_generator.py
from fractions import Fraction
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
    
    problem = f"Solve for x: {a}x {sign} {abs(b)} = {c}"
    answer = f"x = {x}"
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

    problem = f"Simplify the expression: {a}({b}x + {d}) - {c}x"
    answer = f"{final_x_coeff}x + {final_const}"
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
    
    problem = f"Factor the trinomial: x^2 {b_sign} {abs(b)}x {c_sign} {abs(c)}"
    
    # Format the answer string (x - r1)(x - r2)
    r1_sign = "-" if r1 > 0 else "+"
    r2_sign = "-" if r2 > 0 else "+"
    answer = f"(x {r1_sign} {abs(r1)})(x {r2_sign} {abs(r2)})"
    
    return problem, answer

def generate_slope_from_points():
    """Generates a problem for finding the slope between two points."""
    # Generate two distinct points (x1, y1) and (x2, y2)
    x1 = random.randint(-5, 5)
    y1 = random.randint(-5, 5)
    x2 = random.randint(-5, 5)
    y2 = random.randint(-5, 5)

    # Ensure the points are not the same to avoid a 0/0 slope
    while x1 == x2 and y1 == y2:
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)

    problem = f"Find the slope between the points ({x1}, {y1}) and ({x2}, {y2})."

    # Calculate the slope and handle the undefined case
    if x1 == x2:
        answer = "The slope is undefined (vertical line)."
    else:
        # To display a nice fraction, we can simplify it
        # This is a bit more advanced, but makes the answers look cleaner
        from fractions import Fraction
        slope = Fraction(y2 - y1, x2 - x1)
        answer = f"The slope is {slope}."
        
    return problem, answer

def generate_evaluate_function():
    """Generates a problem for evaluating a linear function."""
    m = random.randint(-5, 5)
    b = random.randint(-10, 10)
    x_val = random.randint(-5, 5)

    # Avoid m=0 to keep it interesting
    if m == 0: m = 1

    # Format b for the function string
    b_sign = "+" if b >= 0 else "-"
    
    problem = f"Given f(x) = {m}x {b_sign} {abs(b)}, find the value of f({x_val})."
    
    # Calculate the answer
    answer_val = m * x_val + b
    answer = f"f({x_val}) = {answer_val}"
    
    return problem, answer

def generate_multistep_equation_fractions():
    """Generates a multi-step equation with distribution and fractions."""
    # Work backwards from an integer solution to keep it clean
    x = random.randint(-6, 6)
    
    # Coefficients for a(bx + c) = d
    a_num = random.randint(1, 5)
    a_den = random.randint(1, 5)
    a = Fraction(a_num, a_den)

    b = random.randint(2, 5)
    c = random.randint(-10, 10)
    
    # Calculate d based on the other values
    d = a * (b * x + c)
    
    # Format the fraction for display
    a_str = f"{a_num}/{a_den}" if a_den != 1 else str(a_num)
    
    problem = f"Solve for x: {a_str}({b}x + {c}) = {d}"
    answer = f"x = {x}"
    
    return problem, answer

def generate_multistep_inequality():
    """Generates a multi-step inequality where the sign might flip."""
    # Structure: ax + b > c
    # We'll make 'a' negative sometimes to force a sign flip
    a = random.randint(-7, 7)
    x = random.randint(-5, 5)
    b = random.randint(-10, 10)
    
    # Ensure 'a' is not zero
    if a == 0: a = -1

    # Choose a random inequality symbol
    symbol = random.choice(['<', '>', '≤', '≥'])
    
    # Calculate the right side of the inequality
    c = a * x + b - random.randint(1,5) # Ensure it's not an equality
    
    # Format the problem string
    b_sign = "+" if b >= 0 else "-"
    problem = f"Solve the inequality: {a}x {b_sign} {abs(b)} {symbol} {c}"
    
    # Determine the correct answer, flipping the sign if 'a' is negative
    final_symbol = symbol
    if a < 0:
        if symbol == '<': final_symbol = '>'
        elif symbol == '>': final_symbol = '<'
        elif symbol == '≤': final_symbol = '≥'
        elif symbol == '≥': final_symbol = '≤'
            
    answer = f"x {final_symbol} {x}"

    return problem, answer

def generate_system_of_equations():
    """Generates a 2x2 system of linear equations with a unique integer solution."""
    # Start with a clean integer solution
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    
    # Generate random coefficients for two equations: ax + by = e, cx + dy = f
    # Ensure the determinant (ad-bc) is not zero, which guarantees a unique solution
    a, b, c, d = 0, 0, 0, 0
    while (a * d - b * c) == 0:
        a = random.randint(-4, 4)
        b = random.randint(-4, 4)
        c = random.randint(-4, 4)
        d = random.randint(-4, 4)
        # Avoid all zero coefficients
        if a==0 and b==0 and c==0 and d==0: a=1

    # Calculate the constants e and f
    e = a * x + b * y
    f = c * x + d * y
    
    # Build the problem string nicely, handling signs and coefficients
    eq1 = f"{a}x + {b}y = {e}".replace('+ -', '- ').replace('1x', 'x')
    eq2 = f"{c}x + {d}y = {f}".replace('+ -', '- ').replace('1x', 'x')
    
    problem = f"Solve the system of equations:\n{eq1}\n{eq2}"
    answer = f"({x}, {y})"
    
    return problem, answer

def generate_write_equation_from_points():
    """Generates a problem for writing a linear equation from two points."""
    # Generate two distinct points (x1, y1) and (x2, y2)
    x1 = random.randint(-5, 5)
    y1 = random.randint(-5, 5)
    x2 = random.randint(-5, 5)
    y2 = random.randint(-5, 5)
    
    # Ensure x-coordinates are different to avoid vertical lines for now
    while x1 == x2:
        x2 = random.randint(-5, 5)

    problem = f"Write the equation of the line that passes through the points ({x1}, {y1}) and ({x2}, {y2})."
    
    # Calculate slope and y-intercept
    m = Fraction(y2 - y1, x2 - x1)
    b = y1 - m * x1
    
    # Format the answer string y = mx + b
    m_str = f"{m.numerator}/{m.denominator}" if m.denominator != 1 else str(m.numerator)
    b_sign = "+" if b >= 0 else "-"
    answer = f"y = {m_str}x {b_sign} {abs(b)}"
    
    return problem, answer

def generate_parallel_perpendicular_line():
    """Generates a problem for finding a parallel or perpendicular line."""
    # Original line: y = mx + b
    m = Fraction(random.randint(-5, 5), random.randint(1, 5))
    b = random.randint(-10, 10)
    
    # Point the new line passes through
    px = random.randint(-6, 6)
    py = random.randint(-6, 6)
    
    # Choose between parallel and perpendicular
    task = random.choice(["parallel", "perpendicular"])
    
    # Determine the new slope
    if task == "parallel":
        new_m = m
    else: # Perpendicular
        if m == 0: # Handle horizontal original line
            # Perpendicular line is vertical, cannot be in y=mx+b form
            problem = f"Write the equation of the line perpendicular to y = {b} that passes through ({px}, {py})."
            answer = f"x = {px}"
            return problem, answer
        new_m = -1 / m
        
    # Calculate the new y-intercept: b = y - mx
    new_b = py - new_m * px
    
    # Format problem and answer strings
    m_str = f"{m.numerator}/{m.denominator}" if m.denominator != 1 else str(m.numerator)
    b_sign = "+" if b >= 0 else "-"
    
    problem = f"Write the equation of the line {task} to y = {m_str}x {b_sign} {abs(b)} that passes through ({px}, {py})."
    
    new_m_str = f"{new_m.numerator}/{new_m.denominator}" if new_m.denominator != 1 else str(new_m.numerator)
    new_b_sign = "+" if new_b >= 0 else "-"
    
    answer = f"y = {new_m_str}x {new_b_sign} {abs(new_b)}"
    
    return problem, answer

def generate_factoring_binomials():
    """Generates a problem for factoring a binomial, like GCF or Difference of Squares."""
    task = random.choice(["gcf", "diff_squares"])
    
    if task == "diff_squares":
        # Format: a^2 * x^2 - b^2 = (ax - b)(ax + b)
        a = random.randint(2, 7)
        b = random.randint(2, 7)
        
        problem = f"Factor the binomial: {a*a}x² - {b*b}"
        answer = f"({a}x - {b})({a}x + {b})"
        
    else: # GCF
        # Format: g*a*x + g*b = g(ax + b)
        g = random.randint(2, 10) # Greatest Common Factor
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        
        # Ensure a and b don't share a common factor with each other
        from math import gcd
        while gcd(a, b) != 1:
            a = random.randint(2, 8)

        problem = f"Factor the binomial: {g*a}x + {g*b}"
        answer = f"{g}({a}x + {b})"
        
    return problem, answer

def generate_polynomial_operations():
    """Generates a problem for adding, subtracting, or multiplying polynomials."""
    task = random.choice(["add", "subtract", "multiply"])
    
    # Generate coefficients for two simple polynomials: P1 = ax^2+bx+c, P2 = dx^2+ex+f
    a, b, c = random.randint(1, 5), random.randint(-7, 7), random.randint(-7, 7)
    d, e, f = random.randint(1, 5), random.randint(-7, 7), random.randint(-7, 7)

    # Helper to format a polynomial string from coefficients
    def format_poly(coeffs):
        x_sq, x, const = coeffs
        return f"{x_sq}x² + {x}x + {const}".replace('+ -', '- ')

    poly1_str = f"({format_poly([a, b, c])})"
    poly2_str = f"({format_poly([d, e, f])})"

    if task == "add":
        problem = f"Add the polynomials: {poly1_str} + {poly2_str}"
        ans_coeffs = [a + d, b + e, c + f]
        answer = format_poly(ans_coeffs)

    elif task == "subtract":
        problem = f"Subtract the polynomials: {poly1_str} - {poly2_str}"
        ans_coeffs = [a - d, b - e, c - f]
        answer = format_poly(ans_coeffs)
        
    else: # Multiply two binomials: (ax+b)(cx+d)
        a, b = random.randint(1, 6), random.randint(-7, 7)
        c, d = random.randint(1, 6), random.randint(-7, 7)
        
        # Format binomial strings
        bin1_str = f"({a}x + {b})".replace('+ -', '- ')
        bin2_str = f"({c}x + {d})".replace('+ -', '- ')
        
        problem = f"Multiply the binomials: {bin1_str}{bin2_str}"
        
        # FOIL method: (ac)x^2 + (ad+bc)x + bd
        ans_coeffs = [a*c, a*d + b*c, b*d]
        answer = format_poly(ans_coeffs)

    return problem, answer

def generate_exponent_rules():
    """Generates a problem using exponent rules like product, power, or negative exponents."""
    task = random.choice(["product", "power", "negative", "quotient"])
    base = random.randint(2, 6)
    
    if task == "product":
        # Rule: x^a * x^b = x^(a+b)
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        problem = f"Simplify the expression: {base}² * {base}³"
        answer = f"{base}^{a + b}"
        
    elif task == "power":
        # Rule: (x^a)^b = x^(a*b)
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        problem = f"Simplify the expression: ({base}^{a})^{b}"
        answer = f"{base}^{a * b}"
        
    elif task == "negative":
        # Rule: x^-a = 1 / x^a
        a = random.randint(2, 5)
        problem = f"Rewrite the expression with a positive exponent: {base}^-{a}"
        answer = f"1 / {base}^{a}"
        
    else: # Quotient
        # Rule: x^a / x^b = x^(a-b)
        a = random.randint(5, 9)
        b = random.randint(2, 4) # Ensure a > b for a positive result
        problem = f"Simplify the expression: {base}^{a} / {base}^{b}"
        answer = f"{base}^{a - b}"
        
    return problem, answer

def generate_radical_operations():
    """Generates a problem for simplifying or multiplying square roots."""
    task = random.choice(["simplify", "multiply"])
    
    if task == "simplify":
        # Work backwards: answer is outside * sqrt(inside)
        # Problem is sqrt(inside * outside^2)
        outside = random.randint(2, 5)
        inside = random.choice([2, 3, 5, 6, 7]) # Non-perfect squares
        
        problem_radicand = inside * (outside ** 2)
        problem = f"Simplify the radical: √{problem_radicand}"
        answer = f"{outside}√{inside}"
        
    else: # Multiply
        # (a√b) * (c√d)
        a = random.randint(2, 5)
        b = random.randint(2, 3)
        c = random.randint(2, 5)
        d = random.choice([2, 3, 5])
        
        problem = f"Multiply and simplify: ({a}√{b}) * ({c}√{d})"
        
        # Multiply outsides and insides
        new_coeff = a * c
        new_radicand = b * d
        
        # Now simplify the result (e.g., 6√12 -> 12√3)
        # Find largest perfect square factor of new_radicand
        final_coeff = new_coeff
        final_radicand = new_radicand
        for i in range(4, 0, -1): # Check for factors 16, 9, 4
            if new_radicand % (i*i) == 0:
                final_coeff = new_coeff * i
                final_radicand = new_radicand // (i*i)
                break
        
        answer = f"{final_coeff}√{final_radicand}"

    return problem, answer

# Add these imports to the TOP of your problem_generator.py file
import matplotlib.pyplot as plt
import numpy as np

# Add this new function to the end of the file
def generate_graphing_linear_equation():
    """Generates a problem for graphing a linear equation in y=mx+b form."""
    # Generate a simple slope and y-intercept
    m = random.randint(-3, 3)
    b = random.randint(-5, 5)
    
    # Avoid a slope of zero to keep it interesting
    if m == 0: m = 1
        
    # Format the problem string
    b_sign = "+" if b >= 0 else "-"
    problem = f"Graph the linear equation: y = {m}x {b_sign} {abs(b)}"
    
    # --- Create the Graph ---
    fig, ax = plt.subplots(figsize=(6, 6)) # You can adjust size if you like
    
    # Create a range of x-values for our line
    x_vals = np.linspace(-10, 10, 400)
    y_vals = m * x_vals + b
    
    # Plot the line
    ax.plot(x_vals, y_vals)
    
    # --- Format the Coordinate Plane ---
    ax.axhline(0, color='black', linewidth=0.7)
    ax.axvline(0, color='black', linewidth=0.7)
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    # --- NEW LINES TO SET TICKS ---
    ax.set_xticks(np.arange(-10, 11, 1)) # Add this line
    ax.set_yticks(np.arange(-10, 11, 1)) # Add this line
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_title("Correct Graph")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    
    return problem, fig
# A dictionary to easily access the functions by name
TOPICS = {
    "Two-Step Linear Equations": generate_linear_equation,
    "Simplify Expressions": generate_simplify_expression,
    "Factor Simple Quadratics": generate_factoring_quadratic,
    "Slope Between Two Points": generate_slope_from_points,
    "Evaluating Functions": generate_evaluate_function,
    "Multi-Step Equations (Fractions)": generate_multistep_equation_fractions,
    "Multi-Step Inequalities": generate_multistep_inequality,
    "Systems of Equations": generate_system_of_equations,
    "Equation from Two Points": generate_write_equation_from_points,
    "Parallel & Perpendicular Lines": generate_parallel_perpendicular_line,
    "Factoring Binomials": generate_factoring_binomials,
    "Polynomial Operations": generate_polynomial_operations,
    "Exponent Rules": generate_exponent_rules, # Add this
    "Radical Operations": generate_radical_operations,
    "Graphing Linear Equations": generate_graphing_linear_equation,

}
