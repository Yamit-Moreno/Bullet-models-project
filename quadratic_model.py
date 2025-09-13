import math

class QuadraticDeceleration:
    """
    Deceleration proportional to v^2: a = -c v^2
    With cutoff velocity v_final so penetration is finite:
        x = (1/c) * ln(v0 / v_final)
    Units: [c] = 1/m
    """

    @staticmethod
    def compute_constant(v1, x1, v2, x2, v_final=1e-3):
        """
        Compute the quadratic constant c from TWO experiments (average).
        Args:
            v1, x1, v2, x2 : experiments
            v_final : small cutoff velocity [m/s]
        Returns:
            c (float): quadratic constant [1/m]
        """
        c1 = math.log(v1 / v_final) / x1
        c2 = math.log(v2 / v_final) / x2
        return (c1 + c2) / 2

    @staticmethod
    def acceleration(c, v):
        """Deceleration a(v) for plotting [m/s^2]."""
        return -c * (v ** 2)

