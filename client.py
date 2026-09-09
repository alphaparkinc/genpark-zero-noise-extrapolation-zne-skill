class ZeroNoiseExtrapolation:
    """
    Quantum Error Mitigation via Zero-Noise Extrapolation (ZNE).
    Scales noise by scale factors lambda via pulse folding.
    Uses polynomial / Richardson extrapolation to infer zero-noise expectation value.
    """
    def extrapolate_richardson(self, scales, values):
        s1, s2 = scales[0], scales[1]
        v1, v2 = values[0], values[1]
        slope = (v2 - v1) / (s2 - s1)
        intercept = v1 - slope * s1
        return intercept
