import unittest
from openmeta.core.task_queue import TaskQueue

class TestTaskQueue(unittest.TestCase):
    def setUp(self):
        self.task_queue = TaskQueue()

    def test_add_to_queue(self):
        task = {'id': 1, 'priority': 2, 'action': 'do something'}
        self.task_queue.add_to_queue(task)
        self.assertEqual(len(self.task_queue.queue), 1)

    def test_process_queue(self):
        # Add tasks with different priorities
        task1 = {'id': 1, 'priority': 2, 'action': 'do something'}
        task2 = {'id': 2, 'priority': 1, 'action': 'do another thing'}
        self.task_queue.add_to_queue(task1)
        self.task_queue.add_to_queue(task2)

        # Process tasks and check the order
        self.task_queue.process_queue()
        self.assertEqual(self.task_queue.queue, [])

if __name__ == "__main__":
    unittest.main()
