# autopr/aware/agent_context_manager.py

class AgentContextManager:
    """一个非常简单的上下文管理器，用于在内存中跟踪重试次数。"""
    def __init__(self):
        # 用一个字典来存储每个任务的重试次数
        self.retry_counts = {}

    def get_retry_count(self, task_id: str) -> int:
        return self.retry_counts.get(task_id, 0)

    def increment_retry_count(self, task_id: str):
        current_count = self.get_retry_count(task_id)
        self.retry_counts[task_id] = current_count + 1

# 创建一个全局实例供项目使用
context_manager = AgentContextManager()