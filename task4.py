import numpy as np
from scipy.optimize import minimize

# Function to compute log-likelihood given bucket boundaries and data
def compute_log_likelihood(boundaries, scores, defaults):
    boundaries = np.sort(boundaries)
    boundaries = np.insert(boundaries, [0, len(boundaries)], [-np.inf, np.inf])  # Add -inf and inf as boundaries
    bucket_indices = np.digitize(scores, boundaries)
    n_buckets = len(boundaries) - 1
    n_records = np.bincount(bucket_indices)
    n_defaults = np.bincount(bucket_indices, weights=defaults)
    p_defaults = np.divide(n_defaults, n_records, out=np.zeros_like(n_defaults), where=n_records!=0)
    log_likelihood = np.sum(n_defaults * np.log(p_defaults))
    return -log_likelihood  # Minimize negative log-likelihood

# Function to find optimal bucket boundaries
def find_optimal_boundaries(scores, defaults, n_buckets):
    # Initial guess for bucket boundaries (evenly spaced)
    initial_guess = np.linspace(np.min(scores), np.max(scores), num=n_buckets + 1)[1:-1]
    # Minimize negative log-likelihood to find optimal boundaries
    result = minimize(compute_log_likelihood, initial_guess, args=(scores, defaults), method='Nelder-Mead')
    return np.sort(result.x)

# Example usage
fico_scores = np.random.randint(300, 850, size=1000)
defaults = np.random.choice([0, 1], size=1000, p=[0.9, 0.1])  # Example defaults (randomly generated)
n_buckets = 5

optimal_boundaries = find_optimal_boundaries(fico_scores, defaults, n_buckets)
print("Optimal bucket boundaries:", optimal_boundaries)
