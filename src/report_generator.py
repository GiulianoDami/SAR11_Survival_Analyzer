import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class ReportGenerator:
    def __init__(self, simulation_data):
        """
        Initialize the ReportGenerator with simulation data
        
        Args:
            simulation_data (dict): Dictionary containing simulation results
        """
        self.simulation_data = simulation_data
    
    def generate_detailed_report(self, output_path=None):
        """
        Generate a detailed report from simulation data
        
        Args:
            output_path (str, optional): Path to save the report
            
        Returns:
            str: Formatted report string
        """
        report = []
        report.append("SAR11 Survival Analysis Report")
        report.append("=" * 40)
        report.append("")
        
        # Basic statistics
        report.append("Simulation Summary:")
        report.append(f"  - Time period: {self.simulation_data.get('time_period', 'N/A')}")
        report.append(f"  - Initial population: {self.simulation_data.get('initial_population', 'N/A')}")
        report.append(f"  - Final population: {self.simulation_data.get('final_population', 'N/A')}")
        report.append("")
        
        # Environmental conditions
        env_conditions = self.simulation_data.get('environmental_conditions', {})
        report.append("Environmental Conditions:")
        for condition, value in env_conditions.items():
            report.append(f"  - {condition}: {value}")
        report.append("")
        
        # Key metrics
        metrics = self.simulation_data.get('key_metrics', {})
        report.append("Key Metrics:")
        for metric, value in metrics.items():
            report.append(f"  - {metric}: {value}")
        report.append("")
        
        # Stress analysis
        stress_analysis = self.simulation_data.get('stress_analysis', {})
        report.append("Stress Analysis:")
        for stress_type, impact in stress_analysis.items():
            report.append(f"  - {stress_type}: {impact}")
        report.append("")
        
        report_str = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(report_str)
        
        return report_str

def generate_summary_report(simulation_data, output_path=None):
    """
    Generate a summary report from simulation data
    
    Args:
        simulation_data (dict): Dictionary containing simulation results
        output_path (str, optional): Path to save the report
        
    Returns:
        str: Formatted summary report string
    """
    report = []
    report.append("SAR11 Survival Analyzer - Summary Report")
    report.append("=" * 50)
    report.append("")
    
    # Population trends
    population_data = simulation_data.get('population_data', [])
    if population_data:
        initial_pop = population_data[0] if len(population_data) > 0 else 0
        final_pop = population_data[-1] if len(population_data) > 0 else 0
        pop_change = ((final_pop - initial_pop) / initial_pop * 100) if initial_pop != 0 else 0
        
        report.append("Population Dynamics:")
        report.append(f"  - Initial population: {initial_pop:,}")
        report.append(f"  - Final population: {final_pop:,}")
        report.append(f"  - Population change: {pop_change:.2f}%")
        report.append("")
    
    # Critical thresholds
    thresholds = simulation_data.get('critical_thresholds', {})
    if thresholds:
        report.append("Critical Thresholds:")
        for threshold_name, threshold_value in thresholds.items():
            report.append(f"  - {threshold_name}: {threshold_value}")
        report.append("")
    
    # Risk assessment
    risk_assessment = simulation_data.get('risk_assessment', {})
    if risk_assessment:
        report.append("Risk Assessment:")
        for risk_factor, risk_level in risk_assessment.items():
            report.append(f"  - {risk_factor}: {risk_level}")
        report.append("")
    
    # Recommendations
    recommendations = simulation_data.get('recommendations', [])
    if recommendations:
        report.append("Recommendations:")
        for rec in recommendations:
            report.append(f"  - {rec}")
        report.append("")
    
    report_str = "\n".join(report)
    
    if output_path:
        with open(output_path, 'w') as f:
            f.write(report_str)
    
    return report_str