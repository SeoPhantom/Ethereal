import heapq
import logging
from typing import List, Dict

class TaskQueue:
    def __init__(self):
        self.queue = []  # Using a min-heap for prioritizing tasks
        self.lock = False  # Simulating a lock to prevent blocking of the main thread

    def add_to_queue(self, task: dict):
        """ Add a new task to the queue with a priority value """
        priority = task.get('priority', 0)  # Default priority is 0 if not specified
        heapq.heappush(self.queue, (priority, task))  # Push task into the priority queue
        logging.info(f"Task {task['id']} added to queue with priority {priority}")

    def process_queue(self):
        """ Process tasks in order of priority without blocking the main thread """
        while self.queue:
            # Get the task with the highest priority
            _, task = heapq.heappop(self.queue)
            logging.info(f"Processing task {task['id']}")
            # Asynchronously execute the task (this would ideally be async in a real system)
            self.execute_task(task)

    def execute_task(self, task: dict):
        """ Simulate task execution (this should be where your task's logic goes) """
        logging.info(f"Executing task {task['id']}...")
        # In practice, this would likely be an async operation
        pass
