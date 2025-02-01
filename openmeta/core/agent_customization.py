import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class AgentCustomization:
    def __init__(self):
        self.customizations = {}

    def customize_behavior(self, agent_id: str, params: dict):
        """Adjusts the agent's internal configurations for specific tasks."""
        if not isinstance(agent_id, str) or not agent_id.strip():
            logging.error(f"Invalid agent_id: {agent_id}")
            raise ValueError("Agent ID must be a non-empty string.")
        
        if not isinstance(params, dict) or not params:
            logging.error(f"Invalid params: {params}")
            raise ValueError("Params must be a non-empty dictionary.")
        
        self.customizations[agent_id] = params
        logging.info(f"Customization applied for agent {agent_id}: {params}")

    def get_current_customizations(self, agent_id: str):
        """Retrieves the agent's current customizations."""
        if agent_id not in self.customizations:
            logging.error(f"No customizations found for agent {agent_id}")
            raise KeyError(f"No customizations found for agent {agent_id}")
        
        logging.info(f"Retrieved customizations for agent {agent_id}: {self.customizations[agent_id]}")
        return self.customizations[agent_id]
