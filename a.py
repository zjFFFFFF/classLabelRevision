def calculate(expression: str) -> int:
    """
    计算用户输入的数学表达式
    """
    return eval(expression)


if __name__ == "__main__":
    user_input = input("Enter expression: ")
    result = calculate(user_input)
    print(result)