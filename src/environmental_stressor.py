import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class EnvironmentalStressor:
    """
    Base class for environmental stressors that can be applied to the SAR11 model.
    """
    
    def __init__(self, name, severity=1.0):
        self.name = name
        self.severity = severity
    
    def apply(self, model_state):
        """
        Apply the stressor to the current model state.
        
        Parameters:
        model_state (dict): Current state of the SAR11 model
        
        Returns:
        dict: Updated model state after applying stressor
        """
        raise NotImplementedError("Subclasses must implement apply method")

def apply_phytoplankton_bloom(model_state, bloom_intensity=1.0):
    """
    Apply a phytoplankton bloom stressor to the SAR11 model.
    
    Parameters:
    model_state (dict): Current state of the SAR11 model
    bloom_intensity (float): Intensity of the bloom (0.0 to 1.0)
    
    Returns:
    dict: Updated model state with bloom effects applied
    """
    # Simulate increased competition for nutrients during bloom
    if 'nutrient_level' in model_state:
        model_state['nutrient_level'] *= (1 - 0.3 * bloom_intensity)
    
    # Simulate increased predation pressure
    if 'predation_rate' in model_state:
        model_state['predation_rate'] += 0.1 * bloom_intensity
    
    # Simulate potential for increased growth due to food availability
    if 'growth_rate' in model_state:
        model_state['growth_rate'] += 0.05 * bloom_intensity
    
    return model_state

def apply_nutrient_scarcity(model_state, scarcity_level=1.0):
    """
    Apply a nutrient scarcity stressor to the SAR11 model.
    
    Parameters:
    model_state (dict): Current state of the SAR11 model
    scarcity_level (float): Level of nutrient scarcity (0.0 to 1.0)
    
    Returns:
    dict: Updated model state with nutrient scarcity effects applied
    """
    # Reduce available nutrients
    if 'nutrient_level' in model_state:
        model_state['nutrient_level'] *= (1 - 0.4 * scarcity_level)
    
    # Decrease growth rate due to limited resources
    if 'growth_rate' in model_state:
        model_state['growth_rate'] *= (1 - 0.2 * scarcity_level)
    
    # Increase mortality rate due to starvation
    if 'mortality_rate' in model_state:
        model_state['mortality_rate'] += 0.1 * scarcity_level
    
    # Increase stress response factor
    if 'stress_response' in model_state:
        model_state['stress_response'] += 0.15 * scarcity_level
    
    return model_state