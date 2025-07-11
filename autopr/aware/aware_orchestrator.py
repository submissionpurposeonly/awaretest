# autopr/aware/aware_orchestrator.py

from autopr.log_config import get_logger
from .agent_context_manager import context_manager

class AwareOrchestrator:
    def __init__(self):
        self.log = get_logger(service="aware_orchestrator")
        self.MAX_RETRIES = 3

    async def handle_exception(self, exception: Exception, agent_context: dict) -> bool:
        """处理异常的核心方法"""
        task_id = agent_context.get("task_id", "default_task")
        self.log.info(f"AWARE: Caught exception: {exception}", task_id=task_id)

        # --- 第1步：异常分类 ---
        # 我们只处理我们设计的 RuntimeError
        if isinstance(exception, RuntimeError) and "Tool" in str(exception):
            self.log.info("AWARE: Classified exception as 'Tool Invocation Error'.")

            # --- 第2步：检查重试次数并执行初步处理 ---
            retry_count = context_manager.get_retry_count(task_id)
            if retry_count < self.MAX_RETRIES:
                self.log.warning(f"AWARE: Attempting retry #{retry_count + 1}...")
                context_manager.increment_retry_count(task_id)
                agent_context['replan_needed'] = True # 指示 main 模块进行重试
                agent_context['last_action'] = f"AWARE: Retrying after Tool Invocation Error (Attempt {retry_count + 1})."
                return True # 返回 True 表示“我处理了，请重试”

            # --- 第3步：深度分析与重新规划 ---
            else:
                self.log.error(f"AWARE: Retries exhausted after {self.MAX_RETRIES} attempts. Escalating analysis.")
                self.log.info("AWARE: Simulating log trace... Found that the root cause is a 'Reasoning' error.")

                # 匹配到了“推理错误”这个更高阶的模式
                self.log.info("AWARE: Matched 'Reasoning Error' pattern. Triggering re-plan.")

                # 修改上下文，给 AutoPR 新的指令
                new_instructions = "The 'summary-service-v2' tool is not available. Generate a new plan using only standard tools."
                agent_context['replan_instructions'] = new_instructions
                agent_context['last_action'] = "AWARE: Initiating re-plan due to reasoning error."
                agent_context['replan_needed'] = True # 再次指示需要重新规划，但这次 main 模块可以根据 replan_instructions 做不同处理

                # 重置重试计数器，以便新计划可以有自己的重试机会
                context_manager.retry_counts.pop(task_id, None)
                return True # 返回 True 表示“我处理了，请按我的新指示重新规划”

        # --- 第4步：对于其他未知异常 ---
        else:
            self.log.error("AWARE: Unhandled exception type. Escalating to human.", exc_info=True)
            agent_context['replan_needed'] = False
            return False # 返回 False 表示“我处理不了，请中止任务”

# 创建一个全局实例供项目使用
aware_runtime = AwareOrchestrator()