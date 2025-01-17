from typing import Dict, List, Any
import numpy as np

class Agent:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.knowledge_base: Dict[str, Any] = {}
        self.performance_history: List[float] = []

    def execute_task(self, task: str) -> Dict[str, Any]:
        """Execute a given task and return results"""
        # Simulate task execution with some randomness for demonstration
        success_rate = np.random.uniform(0.7, 1.0)
        result = {
            'agent': self.name,
            'task': task,
            'success_rate': success_rate,
            'status': 'completed' if success_rate > 0.8 else 'partial'
        }
        self.performance_history.append(success_rate)
        return result

    def collaborate(self, other_agent: 'Agent', task: str) -> Dict[str, Any]:
        """Collaborate with another agent on a task"""
        combined_expertise = (len(self.performance_history) + 
                            len(other_agent.performance_history)) / 2
        synergy_factor = np.random.uniform(1.0, 1.5)
        
        result = {
            'agents': [self.name, other_agent.name],
            'task': task,
            'synergy_factor': synergy_factor,
            'combined_expertise': combined_expertise
        }
        return result

    def learn_from_experience(self) -> float:
        """Update agent's knowledge based on past performance"""
        if not self.performance_history:
            return 0.0
        learning_rate = np.mean(self.performance_history)
        self.knowledge_base['performance_trend'] = learning_rate
        return learning_rate

class AgentNetwork:
    def __init__(self):
        self.agents: List[Agent] = []
        self.connections: Dict[str, List[str]] = {}

    def add_agent(self, agent: Agent):
        """Add a new agent to the network"""
        self.agents.append(agent)
        self.connections[agent.name] = []

    def connect_agents(self, agent1_name: str, agent2_name: str):
        """Establish a connection between two agents"""
        if agent1_name in self.connections and agent2_name in self.connections:
            self.connections[agent1_name].append(agent2_name)
            self.connections[agent2_name].append(agent1_name)

    def get_agent_by_name(self, name: str) -> Agent:
        """Retrieve an agent by their name"""
        for agent in self.agents:
            if agent.name == name:
                return agent
        raise ValueError(f"Agent {name} not found in network")

if __name__ == "__main__":
    # Example usage
    network = AgentNetwork()
    
    # Create and add agents
    agent1 = Agent("Agent1", "Logistics")
    agent2 = Agent("Agent2", "Analytics")
    network.add_agent(agent1)
    network.add_agent(agent2)
    
    # Connect agents
    network.connect_agents("Agent1", "Agent2")
    
    # Execute tasks
    result1 = agent1.execute_task("Optimize delivery routes")
    result2 = agent2.execute_task("Analyze performance data")
    
    # Collaborate on a task
    collab_result = agent1.collaborate(agent2, "Joint optimization")
    
    print("Individual task results:", result1, result2)
    print("Collaboration result:", collab_result)
