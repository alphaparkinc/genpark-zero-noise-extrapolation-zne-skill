from client import ZeroNoiseExtrapolation

def main():
    print("=== Testing Zero-Noise Extrapolation (ZNE) ===")
    zne = ZeroNoiseExtrapolation()
    scales = [1.0, 3.0]
    values = [0.90, 0.80]

    mitigated = zne.extrapolate_richardson(scales, values)
    print(f"Measured values at scales {scales}: {values}")
    print(f"Mitigated zero-noise value E(0): {mitigated}")
    assert abs(mitigated - 0.95) < 1e-5
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
