"""
Constant Deceleration Model

Formula origin:
If deceleration is constant (a = -c), then from kinematics:
    v^2 = v0^2 + 2 a x
At stopping point (v=0):
    a = -v0^2 / (2x)
We take c = v0^2 / (2x) as the magnitude of deceleration.
"""
class ConstantDeceleration:
    """
    Model where the bullet decelerates with constant acceleration.
    a = -c (constant deceleration)
    """

    @staticmethod
    def compute_constant(v1, x1, v2, x2):
        """
        Compute the constant c using two experiments (average).
        Args:
            v1, x1: velocity and depth from experiment 1
            v2, x2: velocity and depth from experiment 2
        Returns:
            c (positive magnitude of constant deceleration)
        """
        c1 = (v1 ** 2) / (2 * x1)
        c2 = (v2 ** 2) / (2 * x2)
        return (c1 + c2) / 2

    @staticmethod
    def acceleration(c, v):
        """
        Returns the deceleration for velocity v (always constant, negative).
        """
        return -c
