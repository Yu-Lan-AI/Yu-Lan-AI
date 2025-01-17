from quantum_layer import QuantumLayer
from agent_layer import Agent, AgentNetwork
from hybrid_integration import HybridIntegration
import numpy as np
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class YuLanSystem:
    def __init__(self):
        self.quantum_layer = QuantumLayer()
        self.agent_network = AgentNetwork()
        self.hybrid_integration = HybridIntegration()
        logger.info("Yu Lan system initialized")

    def setup_agent_network(self):
        """Initialize and configure the agent network"""
        specializations = [
            ("Agent1", "Optimization"),
            ("Agent2", "Analytics"),
            ("Agent3", "Planning")
        ]
        
        for name, spec in specializations:
            agent = Agent(name, spec)
            self.agent_network.add_agent(agent)
            logger.info(f"Added agent: {name} with specialization: {spec}")

        # Connect agents
        self.agent_network.connect_agents("Agent1", "Agent2")
        self.agent_network.connect_agents("Agent2", "Agent3")
        self.agent_network.connect_agents("Agent1", "Agent3")
        logger.info("Agent network connections established")

    def process_task(self, task_data):
        """Process a task through the Yu Lan system"""
        try:
            logger.info(f"Processing task: {task_data.get('task_id', 'Unknown')}")
            
            # Quantum processing
            quantum_results = self.quantum_layer.simulate_superposition(
                task_data.get('input_data', [])
            )
            logger.info("Quantum processing completed")

            # Agent processing
            agent_results = []
            for agent in self.agent_network.agents:
                result = agent.execute_task(task_data.get('task_description', ''))
                agent_results.append(result)
            logger.info("Agent processing completed")

            # Hybrid integration
            final_results = self.hybrid_integration.process_hybrid_task(task_data)
            logger.info("Hybrid integration completed")

            return {
                'status': 'success',
                'quantum_results': quantum_results.tolist(),
                'agent_results': agent_results,
                'final_results': final_results
            }

        except Exception as e:
            logger.error(f"Error processing task: {str(e)}")
            return {
                'status': 'error',
                'error_message': str(e)
            }

def main():
    # Initialize Yu Lan system
    yulan = YuLanSystem()
    yulan.setup_agent_network()

    # Example task
    task_data = {
        'task_id': 'TASK001',
        'input_data': [1.0, 2.0, 3.0, 4.0],
        'task_description': 'Optimize resource allocation and predict outcomes'
    }

    # Process task
    results = yulan.process_task(task_data)
    
    # Display results
    if results['status'] == 'success':
        print("\nYu Lan Task Processing Results:")
        print("--------------------------------")
        print(f"Task ID: {task_data['task_id']}")
        print(f"Quantum Results: {results['quantum_results']}")
        print("\nAgent Results:")
        for result in results['agent_results']:
            print(f"- {result['agent']}: {result['status']} "
                  f"(Success Rate: {result['success_rate']:.2f})")
        print("\nFinal Integrated Results:")
        print(results['final_results'])
    else:
        print(f"Error: {results['error_message']}")

if __name__ == "__main__":
    main()
