# autopr/actions/moch_summarize_action.py

from autopr.actions.base import Action
from pydantic import BaseModel
from autopr.log_config import get_logger
from pydantic import Field
import asyncio

log = get_logger(__name__)

class MockSummarizeInputs(BaseModel):
    # 这个输入模型定义了我们的 action 能接受什么参数
    use_v2_engine: bool = Field(default=False, description="Whether to use the 'summary-service-v2' engine.")
    # 我们在这里保留 diff_content 以便正常逻辑可以运行
    diff_content: str = Field(default="", description="The content of the code diff to summarize.")

class MockSummarizeOutputs(BaseModel):
    # 这个输出模型定义了我们的 action 成功后会返回什么
    summary: str = Field(description="The generated summary of the code diff.")

class MockSummarizeAction(Action[MockSummarizeInputs, MockSummarizeOutputs]):
    # action 的唯一 ID，AutoPR 的规划模块会用它来指定运行哪个 action
    id = "mock_summarize_code"

    async def run(self, inputs: MockSummarizeInputs) -> MockSummarizeOutputs:
        """
        这个方法是 action 的核心执行逻辑。
        """
        log.info(f"MockSummarizeAction: Running with use_v2_engine={inputs.use_v2_engine}")

        # 这是我们为 case study 设计的关键部分
        if inputs.use_v2_engine:
            # 模拟推理出了一个不存在的工具并调用失败
            log.warning("Simulating a non-existent tool call for 'summary-service-v2'.")
            raise RuntimeError("Tool 'summary-service-v2' does not exist.")
        else:
            # 这是当 AWARE 重新规划后，应该走的正常逻辑
            log.info("Executing standard summarization logic.")
            summary = f"This is a standard summary for the provided content."
            return MockSummarizeOutputs(summary=summary)