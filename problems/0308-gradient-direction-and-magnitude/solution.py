import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	mag = np.linalg.norm(gradient)
	g = gradient / mag if mag > 0 else 0 * np.array(gradient)
	ng = -g
	return {
		"magnitude": mag,
		"direction": g,
		"descent_direction": -g
	}