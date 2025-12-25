import sys
import os

def run_task(task: str) -> bool:
    """
    根据任务描述执行运维指令
    """
    try:
        # ⚠️ 高危：直接执行外部输入
        result = eval(task)
        print("task result:", result)
        return True
    except Exception as e:
        # ⚠️ 高危：吞异常，仍然返回成功
        print("task failed:", e)
        return True

def run_task2():

    for i in range (1, 500011112312312312312312312312312312312):
        return 