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
    a = random.randint(-7, 7)
    x = random.randint(-5, 5)
    b = random.randint(-10, 10)
    
    if a == 0: a = -1

    symbol = random.choice(['<', '>', '≤', '≥'])
    
    c = a * x + b - random.randint(1,5)
    
    b_sign = "+" if b >= 0 else "-"
    problem = f"Solve the inequality: {a}x {b_sign} {abs(b)} {symbol} {c}"
    
    # --- MODIFIED SECTION ---
    
    # Determine the correct final symbol, flipping if 'a' is negative
    final_symbol = symbol
    if a < 0:
        if symbol == '<': final_symbol = '>'
        elif symbol == '>': final_symbol = '<'
        elif symbol == '≤': final_symbol = '≥'
        elif symbol == '≥': final_symbol = '≤'
    
    # Create the inequality part of the answer
    inequality_notation = f"x {final_symbol} {x}"
    
    # Determine the interval notation based on the final symbol
    if final_symbol == '>':
        interval_notation = f"({x}, ∞)"
    elif final_symbol == '≥':
        interval_notation = f"[{x}, ∞)"
    elif final_symbol == '<':
        interval_notation = f"(-∞, {x})"
    else: # Must be '≤'
        interval_notation = f"(-∞, {x}]"
            
    # Combine both notations for the final answer
    answer = f"Inequality: {inequality_notation} | Interval: {interval_notation}"

    return problem, answer

def generate_compound_inequality():
    """Generates both conjunction and disjunction compound inequalities."""
    # Randomly choose which type of inequality to create
    task = random.choice(["conjunction", "disjunction"])
    
    # --- Part 1: Conjunction ("and") Problems ---
    # Example: -5 < 2x + 1 < 11
    if task == "conjunction":
        # Start with a clean integer solution, e.g., -2 < x <= 4
        x_lower = random.randint(-5, 5)
        x_upper = x_lower + random.randint(3, 8)

        # Choose the coefficients for the expression mx + c
        m = random.randint(2, 5)
        c = random.randint(-7, 7)
        
        s1 = random.choice(['<', '≤'])
        s2 = random.choice(['<', '≤'])
        
        # Calculate the outside bounds of the problem
        left_bound = m * x_lower + c
        right_bound = m * x_upper + c
        
        c_sign = "+" if c >= 0 else "-"
        problem = f"Solve: {left_bound} {s1} {m}x {c_sign} {abs(c)} {s2} {right_bound}"
        
        # Format the Answer
        inequality_notation = f"{x_lower} {s1} x {s2} {x_upper}"
        left_bracket = '(' if s1 == '<' else '['
        right_bracket = ')' if s2 == '<' else ']'
        interval_notation = f"{left_bracket}{x_lower}, {x_upper}{right_bracket}"
        answer = f"Inequality: {inequality_notation} | Interval: {interval_notation}"

    # --- Part 2: Disjunction ("or") Problems ---
    # Example: 3x - 1 < -7 OR 3x - 1 > 5
    else: 
        # Start with a clean integer solution, e.g., x < -2 OR x > 2
        x_lower = random.randint(-5, 0)
        x_upper = random.randint(1, 6)

        m = random.randint(2, 5) # Using positive m for simplicity
        c = random.randint(-7, 7)
        
        s1 = random.choice(['<', '≤'])
        s2 = random.choice(['>', '≥'])
        
        # Calculate the bounds
        left_bound = m * x_lower + c
        right_bound = m * x_upper + c
        
        # Format the problem
        c_sign = "+" if c >= 0 else "-"
        expression = f"{m}x {c_sign} {abs(c)}"
        problem = f"Solve: {expression} {s1} {left_bound} OR {expression} {s2} {right_bound}"

        # Format the Answer
        inequality_notation = f"x {s1} {x_lower} OR x {s2} {x_upper}"
        left_bracket = ')' if s1 == '<' else ']'
        right_bracket = '(' if s2 == '>' else '['
        interval_notation = f"(-∞, {x_lower}{left_bracket} U {right_bracket}{x_upper}, ∞)"
        answer = f"Inequality: {inequality_notation} | Interval: {interval_notation}"
            
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

def generate_factoring_harder_quadratic():
    """Generates a problem for factoring quadratics like Ax^2 + Bx + C."""
    # Start with the factored form (ax+b)(cx+d)
    a = random.randint(2, 4)
    b = random.randint(-5, 5)
    c = random.randint(2, 4)
    d = random.randint(-5, 5)

    if b == 0 or d == 0: # Avoid simple GCF problems
        b = 1
        d = -2
    
    # Calculate the coefficients A, B, and C for Ax^2 + Bx + C
    A = a * c
    B = a * d + b * c
    C = b * d
    
    # Format signs for the problem string
    B_sign = "+" if B >= 0 else "-"
    C_sign = "+" if C >= 0 else "-"
    
    problem = f"Factor the trinomial: {A}x² {B_sign} {abs(B)}x {C_sign} {abs(C)}"
    
    # Format answer string
    b_ans_sign = "+" if b >= 0 else "-"
    d_ans_sign = "+" if d >= 0 else "-"
    answer = f"({a}x {b_ans_sign} {abs(b)})({c}x {d_ans_sign} {abs(d)})"
    
    return problem, answer

def generate_graphing_linear_inequality():
    """Generates a problem for graphing a linear inequality."""
    m = random.randint(-3, 3)
    b = random.randint(-5, 5)
    if m == 0: m = 1
    
    symbol = random.choice(['<', '>', '≤', '≥'])
    
    problem = f"Graph the linear inequality: y {symbol} {m}x + {b}".replace('+ -', '- ')
    
    # --- Create the Graph ---
    fig, ax = plt.subplots(figsize=(6, 6))
    x_vals = np.linspace(-10, 10, 400)
    y_vals = m * x_vals + b
    
    # Set line style based on the inequality symbol
    linestyle = '--' if symbol in ['<', '>'] else '-'
    ax.plot(x_vals, y_vals, linestyle=linestyle)
    
    # Shade the correct region
    if symbol in ['>', '≥']:
        ax.fill_between(x_vals, y_vals, 10, color='blue', alpha=0.3)
    else: # < or ≤
        ax.fill_between(x_vals, -10, y_vals, color='blue', alpha=0.3)
        
    # Standard formatting
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', lw=0.7); ax.axvline(0, color='black', lw=0.7)
    ax.set_xticks(np.arange(-10, 11, 1)); ax.set_yticks(np.arange(-10, 11, 1))
    ax.grid(True, linestyle='--'); ax.set_title("Correct Graph")
    
    return problem, fig

def generate_graphing_system_equations():
    """Generates a problem for graphing a system of two linear equations."""
    # From generate_system_of_equations
    x, y = random.randint(-5, 5), random.randint(-5, 5)
    a, b, c, d = 1, 1, 1, 1
    while (a * d - b * c) == 0:
        a, b, c, d = [random.randint(-3, 3) for _ in range(4)]
        if a==0 or b==0 or c==0 or d==0: a=1 # Avoid horizontal/vertical for simplicity
        
    e = a * x + b * y
    f = c * x + d * y
    
    eq1_str = f"y = ({-a/b:.2f})x + ({e/b:.2f})".replace('+ -', '- ')
    eq2_str = f"y = ({-c/d:.2f})x + ({f/d:.2f})".replace('+ -', '- ')
    problem = f"Graph the solution to the system:\n{eq1_str}\n{eq2_str}"
    
    # --- Create the Graph ---
    fig, ax = plt.subplots(figsize=(6, 6))
    x_vals = np.linspace(-10, 10, 400)
    y1_vals = (-a/b) * x_vals + (e/b)
    y2_vals = (-c/d) * x_vals + (f/d)
    
    ax.plot(x_vals, y1_vals, label=eq1_str)
    ax.plot(x_vals, y2_vals, label=eq2_str)
    ax.plot(x, y, 'ro', label=f'Solution: ({x},{y})') # Mark the solution
    
    # Standard formatting
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', lw=0.7); ax.axvline(0, color='black', lw=0.7)
    ax.set_xticks(np.arange(-10, 11, 1)); ax.set_yticks(np.arange(-10, 11, 1))
    ax.grid(True, linestyle='--'); ax.set_title("Correct Graph"); ax.legend()
    
    return problem, fig

def generate_graphing_system_inequalities():
    """Generates a problem for graphing a system of two linear inequalities."""
    m1, b1 = random.randint(-2, 2), random.randint(-4, 4)
    m2, b2 = random.randint(-2, 2), random.randint(-4, 4)
    if m1 == 0: m1 = 1
    if m2 == 0: m2 = -1
    while m1 == m2: m2 = random.randint(-2, 2)
        
    s1, s2 = random.choice(['>', '≥']), random.choice(['<', '≤'])
    
    problem = f"Graph the solution to the system:\n\n y {s1} {m1}x + {b1}\n y {s2} {m2}x + {b2}"
    

    # --- Create the Graph ---
    fig, ax = plt.subplots(figsize=(6, 6))
    x_vals = np.linspace(-10, 10, 400)
    y1_vals = m1 * x_vals + b1
    y2_vals = m2 * x_vals + b2
    
    ax.plot(x_vals, y1_vals, linestyle=('--' if s1 == '>' else '-'))
    ax.plot(x_vals, y2_vals, linestyle=('--' if s2 == '<' else '-'))
    
    # Shade the overlapping region
    ax.fill_between(x_vals, y1_vals, y2_vals, where=y2_vals > y1_vals, color='blue', alpha=0.3)
    
    # Standard formatting
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', lw=0.7); ax.axvline(0, color='black', lw=0.7)
    ax.set_xticks(np.arange(-10, 11, 1)); ax.set_yticks(np.arange(-10, 11, 1))
    ax.grid(True, linestyle='--'); ax.set_title("Correct Graph")
    
    return problem, fig

def generate_order_of_operations():
    """Generates a complex problem using the order of operations (PEMDAS)."""
    # Randomly choose one of three problem templates for variety
    template = random.choice([1, 2, 3])
    
    # Template 1: No parentheses, multiple operations
    if template == 1:
        a, b, c = random.randint(10, 20), random.randint(2, 4), random.randint(2, 3)
        res = random.randint(2, 5)
        e = random.randint(2, 4)
        d = res * e
        
        problem = f"Evaluate: {a} - {b} · {c}² + {d} ÷ {e}"
        # Calculation: a - (b * c^2) + (d / e)
        answer = a - (b * (c**2)) + (d / e)

    # Template 2: Parentheses with one operation
    elif template == 2:
        a, b = random.randint(15, 30), random.randint(2, 4)
        res = random.randint(2, 4)
        d = random.randint(2, 3)
        c = res * d
        e, f = random.randint(2, 3), random.randint(1, 10)
        
        problem = f"Evaluate: {a} - {b}² · ({c} ÷ {d}) - {e}³ + {f}"
        # Calculation: a - (b^2 * (c/d)) - e^3 + f
        answer = a - ((b**2) * (c/d)) - (e**3) + f
    
    # Template 3: Parentheses with multiple operations
    else:
        c, d = random.randint(2, 4), random.randint(2, 5)
        res = random.randint(2, 4)
        # Ensure the denominator (b^3 - c) is not zero
        b = random.randint(2, 3)
        while (b**3 - c) == 0:
            c = random.randint(2, 4)
        
        denominator = (b**3 - c)
        a = res * denominator # Guarantees clean division
        
        e, f, g, h = random.randint(3, 6), random.randint(2, 4), random.randint(2, 4), random.randint(1, 15)

        problem = f"Evaluate: {a} ÷ ({b}³ - {c}) · {d} - {e} · {f} - {g}² + {h}"
        # Calculation: (a / (b^3 - c) * d) - (e * f) - g^2 + h
        answer = (a / denominator * d) - (e * f) - (g**2) + h
        
    return problem, str(int(answer)) # Return the final integer answer as a string

def generate_literal_equation():
    """Generates a problem for solving a literal equation for a specific variable."""
    # Store common formulas and their possible solutions
    formulas = [
        ("Perimeter of a rectangle: P = 2l + 2w", "l", "l = (P - 2w) / 2"),
        ("Perimeter of a rectangle: P = 2l + 2w", "w", "w = (P - 2l) / 2"),
        ("Slope-intercept form: y = mx + b", "x", "x = (y - b) / m"),
        ("Area of a trapezoid: A = (1/2)h(b1 + b2)", "h", "h = 2A / (b1 + b2)"),
        ("Volume of a cylinder: V = πr²h", "h", "h = V / (πr²)"),
    ]
    
    # Randomly pick one of the formulas and its parts
    formula_str, variable, solution = random.choice(formulas)
    
    problem = f"Given the formula {formula_str}, solve for {variable}."
    answer = solution
    
    return problem, answer

def generate_word_problem():
    """Generates a word problem for a one-variable equation or inequality."""
    task = random.choice(["equation", "inequality"])
    
    if task == "equation":
        # Scenario: Consecutive integers
        start_int = random.randint(5, 50)
        num1, num2, num3 = start_int, start_int + 1, start_int + 2
        total = num1 + num2 + num3
        
        problem = f"The sum of three consecutive integers is {total}. What is the smallest of the three integers?"
        answer = f"The smallest integer is {start_int}."
        
    else: # Inequality
        # Scenario: Budgeting
        budget = random.randint(80, 200)
        item_cost = random.randint(5, 15)
        flat_fee = random.randint(10, 25)
        
        # Calculate the max number of items
        max_items = (budget - flat_fee) // item_cost
        
        problem = (f"You have a budget of at most ${budget} for a party. "
                   f"A company charges a ${flat_fee} flat fee plus ${item_cost} per person. "
                   f"What is the maximum number of people that can attend?")
        answer = f"The maximum number of people is {max_items}."

    return problem, answer

def generate_domain_range_graph():
    """Generates a graph of a function and determines its domain and range."""
    func_type = random.choice(['linear', 'quadratic', 'absolute_value', 'square_root', 'piecewise_linear'])
    
    # --- Setup the Plot ---
    fig, ax = plt.subplots(figsize=(6, 6))
    x_vals = np.linspace(-10, 10, 400)
    
    # --- Generate Function Based on Type ---
    
    if func_type == 'linear':
        m, b = random.randint(-2, 2), random.randint(-4, 4)
        if m == 0: m = 1
        y_vals = m * x_vals + b
        ax.plot(x_vals, y_vals)
        domain_inequality = "All real numbers"
        domain_interval = "(-∞, ∞)"
        range_inequality = "All real numbers"
        range_interval = "(-∞, ∞)"

    elif func_type == 'quadratic':
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        a = random.choice([-2, -1, 1, 2])
        y_vals = a * ((x_vals - h)**2) + k
        ax.plot(x_vals, y_vals)
        domain_inequality = "All real numbers"
        domain_interval = "(-∞, ∞)"
        if a > 0:
            range_inequality = f"y ≥ {k}"
            range_interval = f"[{k}, ∞)"
        else:
            range_inequality = f"y ≤ {k}"
            range_interval = f"(-∞, {k}]"
            
    elif func_type == 'absolute_value':
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        a = random.choice([-2, -1, 1, 2])
        y_vals = a * np.abs(x_vals - h) + k
        ax.plot(x_vals, y_vals)
        domain_inequality = "All real numbers"
        domain_interval = "(-∞, ∞)"
        if a > 0:
            range_inequality = f"y ≥ {k}"
            range_interval = f"[{k}, ∞)"
        else:
            range_inequality = f"y ≤ {k}"
            range_interval = f"(-∞, {k}]"

    elif func_type == 'square_root':
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        a = random.choice([-2, -1, 1, 2])
        # Only plot where x-h >= 0
        valid_x = x_vals[x_vals >= h]
        y_vals = a * np.sqrt(valid_x - h) + k
        ax.plot(valid_x, y_vals)
        ax.plot(h, k, 'o', markerfacecolor='blue', markeredgecolor='blue') # Solid dot at start
        domain_inequality = f"x ≥ {h}"
        domain_interval = f"[{h}, ∞)"
        if a > 0:
            range_inequality = f"y ≥ {k}"
            range_interval = f"[{k}, ∞)"
        else:
            range_inequality = f"y ≤ {k}"
            range_interval = f"(-∞, {k}]"
            
    elif func_type == 'piecewise_linear':
        # First piece
        x1_break = random.randint(-5, -1)
        m1, b1 = random.randint(-2, 2), random.randint(-3, 3)
        if m1 == 0: m1 = 1
        x1_vals = np.linspace(-10, x1_break, 100)
        y1_vals = m1 * x1_vals + b1
        ax.plot(x1_vals, y1_vals, 'b-')
        ax.plot(x1_break, m1*x1_break+b1, 'o', markerfacecolor='white', markeredgecolor='blue', markersize=8)

        # Second piece
        x2_break = random.randint(x1_break + 2, 6)
        m2, b2 = random.randint(-2, 2), random.randint(-3, 3)
        if m2 == 0: m2 = -1
        x2_vals = np.linspace(x2_break, 10, 100)
        y2_vals = m2 * x2_vals + b2
        ax.plot(x2_vals, y2_vals, 'b-')
        ax.plot(x2_break, m2*x2_break+b2, 'o', markerfacecolor='blue', markeredgecolor='blue', markersize=8)
        
        # Domain and Range for piecewise
        domain_inequality = f"x < {x1_break} or x ≥ {x2_break}"
        domain_interval = f"(-∞, {x1_break}) U [{x2_break}, ∞)"
        
        y1_end = m1*x1_break+b1
        y2_start = m2*x2_break+b2
        
        if m1 > 0: r1_int, r1_ineq = f"(-∞, {y1_end:.1f})", f"y < {y1_end:.1f}"
        else: r1_int, r1_ineq = f"({y1_end:.1f}, ∞)", f"y > {y1_end:.1f}"
        
        if m2 > 0: r2_int, r2_ineq = f"[{y2_start:.1f}, ∞)", f"y ≥ {y2_start:.1f}"
        else: r2_int, r2_ineq = f"(-∞, {y2_start:.1f}]", f"y ≤ {y2_start:.1f}"
            
        range_inequality = f"{r1_ineq} or {r2_ineq}"
        range_interval = f"{r1_int} U {r2_int}"

    # --- Standard Formatting ---
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', lw=0.7); ax.axvline(0, color='black', lw=0.7)
    ax.set_xticks(np.arange(-10, 11, 2)); ax.set_yticks(np.arange(-10, 11, 2))
    ax.grid(True, linestyle='--')
    ax.set_title("Determine the Domain and Range")
    
    problem = fig
    answer = (f"Domain (Inequality): {domain_inequality}\n"
              f"Domain (Interval): {domain_interval}\n\n"
              f"Range (Inequality): {range_inequality}\n"
              f"Range (Interval): {range_interval}")
              
    return problem, answer


# A dictionary to easily access the functions by name
TOPICS = {
    "Order of Operations": generate_order_of_operations,
    "Two-Step Linear Equations": generate_linear_equation,
    "Multi-Step Equations (Fractions)": generate_multistep_equation_fractions,
    "Literal Equations": generate_literal_equation,
    "One-Variable Word Problems": generate_word_problem,
    "Simplify Expressions": generate_simplify_expression,
    "Polynomial Operations": generate_polynomial_operations,
    "Factor Simple Quadratics": generate_factoring_quadratic,
    "Factoring Binomials": generate_factoring_binomials,
    "Factoring Quadratics (A>1)": generate_factoring_harder_quadratic,
    "Slope Between Two Points": generate_slope_from_points,
    "Evaluating Functions": generate_evaluate_function,
    "Multi-Step Inequalities": generate_multistep_inequality,
    "Compound Inequalities": generate_compound_inequality,
    "Systems of Equations": generate_system_of_equations,
    "Equation from Two Points": generate_write_equation_from_points,
    "Parallel & Perpendicular Lines": generate_parallel_perpendicular_line,
    "Exponent Rules": generate_exponent_rules, # Add this
    "Radical Operations": generate_radical_operations,
    "Graphing Linear Equations": generate_graphing_linear_equation,
    "Graphing Linear Inequalities": generate_graphing_linear_inequality,
    "Graphing Systems of Equations": generate_graphing_system_equations,
    "Graphing Systems of Inequalities": generate_graphing_system_inequalities,
    "Visual Domain and Range": generate_domain_range_graph,
}
