# autopr/log_config.py

import logging
import sys
import os
import structlog

def configure_logging():
    # --- 1. 定义日志文件路径 ---
    log_dir = ".autopr/logs"
    log_filepath = os.path.join(log_dir, "autopr_run.log")
    os.makedirs(log_dir, exist_ok=True)

    # --- 2. 配置 Python 内置的 logging，让它同时处理控制台和文件 ---
    logging.basicConfig(
        level=logging.INFO,  # 设置基础级别
        stream=sys.stdout,     # 默认输出到控制台
        format="%(message)s",  # 让 structlog 控制最终格式
    )
    # 添加一个 FileHandler 来将日志写入文件
    file_handler = logging.FileHandler(log_filepath, mode='w') # 'w' 模式表示每次运行都覆盖旧日志
    # 给文件日志设置一个简单的格式
    file_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"))
    # 将文件处理器添加到根记录器
    logging.getLogger().addHandler(file_handler)

    # --- 3. 配置 structlog，让它使用我们上面配置好的 logging ---
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.dict_tracebacks,
            # 这个处理器是关键，它会将日志记录交给标准 logging 系统处理
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


# Configure logging on module import
configure_logging()


def get_logger(*args, **kwargs):
    return structlog.get_logger(*args, **kwargs)