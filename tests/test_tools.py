import logging
from openmeta.core.tools import Tool

logging.basicConfig(
    filename="ethereal_sdk_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def test_tool():
    try:
        tool_name = "MockTool"
        tool = Tool(tool_name)
        
        params = ("param1",)
        kwargs = {"key": "value"}
        logging.info(f"Executing tool: {tool_name} with params: {params} and kwargs: {kwargs}")
        
        result = tool.execute(*params, **kwargs)
        
        assert "MockTool executed" in result, f"Test failed. Expected 'MockTool executed' in the result."
        
        logging.info(f"Test passed. Tool '{tool_name}' executed successfully with result: {result}")
    
    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        print(f"AssertionError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_tool()
