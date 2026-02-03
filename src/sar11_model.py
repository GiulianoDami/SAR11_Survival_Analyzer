import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class SAR11Model:
    def __init__(self, initial_population=1000, stress_threshold=0.5):
        """
        Initialize the SAR11 population model
        
        Args:
            initial_population (int): Starting population size
            stress_threshold (float): Threshold for stress-induced cell division
        """
        self.population = initial_population
        self.stress_threshold = stress_threshold
        self.history = []
        
    def update_population(self, stress_level, time_step):
        """
        Update population based on stress level and time step
        
        Args:
            stress_level (float): Current environmental stress level (0-1)
            time_step (float): Time increment
            
        Returns:
            int: Updated population count
        """
        # Base growth rate
        growth_rate = 0.1
        
        # Stress effect on growth
        if stress_level > self.stress_threshold:
            # Under stress, growth slows and some cells divide without dividing
            effective_growth = growth_rate * (1 - stress_level)
            # Some cells undergo DNA replication without cell division
            replication_factor = 0.3 * stress_level
        else:
            effective_growth = growth_rate
            replication_factor = 0
        
        # Calculate population change
        population_change = self.population * effective_growth * time_step
        population_change += self.population * replication_factor * time_step
        
        # Ensure non-negative population
        self.population = max(0, self.population + int(population_change))
        
        # Record history
        self.history.append({
            'time': time_step,
            'population': self.population,
            'stress_level': stress_level
        })
        
        return self.population

def simulate_population(initial_pop=1000, stress_levels=None, time_steps=100):
    """
    Simulate SAR11 population dynamics over time
    
    Args:
        initial_pop (int): Initial population size
        stress_levels (list): List of stress levels over time
        time_steps (int): Number of time steps to simulate
        
    Returns:
        pandas.DataFrame: Simulation results
    """
    if stress_levels is None:
        # Default stress pattern: increasing then decreasing
        stress_levels = [0.2] * 20 + [0.6] * 40 + [0.3] * 40
    
    model = SAR11Model(initial_pop)
    results = []
    
    for i in range(time_steps):
        stress_level = stress_levels[i] if i < len(stress_levels) else stress_levels[-1]
        population = model.update_population(stress_level, 1.0)
        results.append({
            'time': i,
            'population': population,
            'stress_level': stress_level
        })
    
    return pd.DataFrame(results)

def analyze_cell_behavior(df):
    """
    Analyze cellular behavior patterns from simulation data
    
    Args:
        df (pandas.DataFrame): Simulation results dataframe
        
    Returns:
        dict: Analysis results including stress thresholds and behavior patterns
    """
    # Identify stress periods
    high_stress_periods = df[df['stress_level'] > 0.5]
    low_stress_periods = df[df['stress_level'] < 0.3]
    
    # Calculate population changes during different stress conditions
    if len(high_stress_periods) > 0:
        high_stress_growth = (high_stress_periods['population'].iloc[-1] - 
                            high_stress_periods['population'].iloc[0]) / len(high_stress_periods)
    else:
        high_stress_growth = 0
        
    if len(low_stress_periods) > 0:
        low_stress_growth = (low_stress_periods['population'].iloc[-1] - 
                           low_stress_periods['population'].iloc[0]) / len(low_stress_periods)
    else:
        low_stress_growth = 0
    
    # Identify critical stress threshold crossings
    stress_crossings = df[(df['stress_level'] > 0.5) & 
                         (df['stress_level'].shift(1) <= 0.5)]
    
    return {
        'high_stress_growth_rate': high_stress_growth,
        'low_stress_growth_rate': low_stress_growth,
        'critical_stress_events': len(stress_crossings),
        'max_population': df['population'].max(),
        'min_population': df['population'].min()
    }