from constant_model import ConstantDeceleration
from linear_model import LinearDeceleration
from quadratic_model import QuadraticDeceleration
import matplotlib.pyplot as plt
import numpy as np

def compute_all_constants(v1, x1, v2, x2):
    c_const = ConstantDeceleration.compute_constant(v1, x1, v2, x2)
    c_lin = LinearDeceleration.compute_constant(v1, x1, v2, x2)
    c_quad = QuadraticDeceleration.compute_constant(v1, x1, v2, x2)
    return c_const, c_lin, c_quad

def print_results(c_const, c_lin, c_quad):
    print("\n--- Results ---")
    print(f"Constant Model (c): {c_const:.2f} m/s^2")
    print(f"Linear Model (c): {c_lin:.2f} 1/s")
    print(f"Quadratic Model (c): {c_quad:.2f} 1/m")

def plot_graphs_separate(c_const, c_lin, c_quad, title_suffix=""):
    velocities = np.linspace(0, 500, 100)
    acc_constant = [ConstantDeceleration.acceleration(c_const, v) for v in velocities]
    acc_linear = [LinearDeceleration.acceleration(c_lin, v) for v in velocities]
    acc_quadratic = [QuadraticDeceleration.acceleration(c_quad, v) for v in velocities]

    # Constant Deceleration
    plt.figure(figsize=(8, 5))
    plt.plot(velocities, acc_constant, color="blue", linewidth=2, label="Constant Deceleration")
    plt.xlabel("Velocity [m/s]")
    plt.ylabel("Deceleration [m/s²]")
    plt.title(f"Constant Deceleration Model {title_suffix}")
    plt.grid(True)
    plt.legend()

    # Linear Deceleration
    plt.figure(figsize=(8, 5))
    plt.plot(velocities, acc_linear, color="orange", linewidth=2, label="Linear Deceleration")
    plt.xlabel("Velocity [m/s]")
    plt.ylabel("Deceleration [m/s²]")
    plt.title(f"Linear Deceleration Model {title_suffix}")
    plt.grid(True)
    plt.legend()

    # Quadratic Deceleration
    plt.figure(figsize=(8, 5))
    plt.plot(velocities, acc_quadratic, color="green", linewidth=2, label="Quadratic Deceleration")
    plt.xlabel("Velocity [m/s]")
    plt.ylabel("Deceleration [m/s²]")
    plt.title(f"Quadratic Deceleration Model {title_suffix}")
    plt.grid(True)
    plt.legend()

    plt.show()

def get_user_input():
    while True:
        try:
            v1 = float(input("Enter V1 [m/s]: "))
            x1 = float(input("Enter X1 [m]: "))
            v2 = float(input("Enter V2 [m/s]: "))
            x2 = float(input("Enter X2 [m]: "))
            return v1, x1, v2, x2
        except ValueError:
            print("❌ Invalid input, please enter numbers only. Try again.")

if __name__ == "__main__":
    # Built-in example
    print("Showing results for the example from the assignment:")
    v1, x1, v2, x2 = 200, 2, 450, 4
    c_const, c_lin, c_quad = compute_all_constants(v1, x1, v2, x2)
    print_results(c_const, c_lin, c_quad)
    plot_graphs_separate(c_const, c_lin, c_quad, title_suffix="(Example)")

    # User input loop
    while True:
        answer = input("Do you want to enter your own experiment data? (y/n): ").strip().lower()
        if answer == "y":
            v1, x1, v2, x2 = get_user_input()
            c_const, c_lin, c_quad = compute_all_constants(v1, x1, v2, x2)
            print_results(c_const, c_lin, c_quad)
            plot_graphs_separate(c_const, c_lin, c_quad, title_suffix="(User Input)")
        elif answer == "n":
            print("Exiting.")
            break
        else:
            print("❌ Please enter 'y' or 'n' only.")

