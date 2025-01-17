import numpy as np
from typing import List, Dict, Any, Union
from .quantum_layer import QuantumLayer
from .agent_layer import Agent, AgentNetwork

class HybridIntegration:
    def __init__(self):
        self.quantum_layer = QuantumLayer()
        self.agent_network = AgentNetwork()
        self.integration_weights = {'quantum': 0.5, 'classical': 0.5}

    def integrate_results(self, 
                        classical_data: List[float], 
                        quantum_data: List[float],
                        weights: Dict[str, float] = None) -> np.ndarray:
        """
        Integrate classical and quantum results using weighted averaging
        """
        if weights:
            self.integration_weights = weights

        if len(classical_data) != len(quantum_data):
            raise ValueError("Classical and quantum data must have the same length")

        classical_weight = self.integration_weights['classical']
        quantum_weight = self.integration_weights['quantum']

        classical_array = np.array(classical_data)
        quantum_array = np.array(quantum_data)

        integrated_result = (classical_weight * classical_array + 
                           quantum_weight * quantum_array)
        
        return integrated_result

    def optimize_weights(self, 
                        performance_metrics: Dict[str, float]) -> Dict[str, float]:
        """
        Optimize integration weights based on performance metrics
        """
        quantum_performance = performance_metrics.get('quantum', 0.5)
        classical_performance = performance_metrics.get('classical', 0.5)

        total_performance = quantum_performance + classical_performance
        
        if total_performance == 0:
            return self.integration_weights

        self.integration_weights = {
            'quantum': quantum_performance / total_performance,
            'classical': classical_performance / total_performance
        }

        return self.integration_weights

    def process_hybrid_task(self, 
                          task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task using both quantum and classical components
        """
        # Process with quantum layer
        quantum_results = self.quantum_layer.simulate_superposition(
            task_data.get('input_data', [])
        )

        # Process with agent network
        agent = Agent("HybridAgent", "Integration")
        classical_results = agent.execute_task(task_data.get('task_description', ''))

        # Integrate results
        if isinstance(classical_results.get('success_rate'), (int, float)):
            classical_data = [classical_results['success_rate']]
            integrated_results = self.integrate_results(
                classical_data,
                quantum_results[:1] if len(quantum_results) > 0 else [0.5]
            )
        else:
            integrated_results = quantum_results

        return {
            'task_id': task_data.get('task_id'),
            'quantum_results': quantum_results.tolist(),
            'classical_results': classical_results,
            'integrated_results': integrated_results.tolist(),
            'weights_used': self.integration_weights
        }

if __name__ == "__main__":
    # Example usage
    hybrid_system = HybridIntegration()
    
    # Test data
    task_data = {
        'task_id': 'TASK001',
        'input_data': [1.0, 2.0, 3.0],
        'task_description': 'Optimize resource allocation'
    }
    
    # Process hybrid task
    result = hybrid_system.process_hybrid_task(task_data)
    print("Hybrid Processing Result:", result)
    
    # Test integration
    classical_data = [0.8, 0.9, 0.7]
    quantum_data = [0.75, 0.85, 0.95]
    integrated = hybrid_system.integrate_results(classical_data, quantum_data)
    print("Integration Result:", integrated)
