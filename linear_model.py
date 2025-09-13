"""
Linear Deceleration Model

Formula origin:
If deceleration is proportional to velocity:
    dv/dt = -c v
Then:
    X = V / c  =>  c = V / X
"""
class LinearDeceleration:
    """
    Model where the bullet decelerates with acceleration proportional to velocity.
    a = -c v
    """

    @staticmethod
    def compute_constant(v1, x1, v2, x2):
        """
        Compute the linear constant c using two experiments (average).
        Args:
            v1, x1: velocity and depth from experiment 1
            v2, x2: velocity and depth from experiment 2
        Returns:
            c (linear constant)
        """
        c1 = v1 / x1
        c2 = v2 / x2
        return (c1 + c2) / 2

    @staticmethod
    def acceleration(c, v):
        """
        Returns the deceleration for velocity v.
        """
        return -c * v

