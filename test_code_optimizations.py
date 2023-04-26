from ai_functions import optimize_function
import openai
import keys
import inspect


# Initialize the OpenAI API client
openai.api_key = keys.OPENAI_API_KEY


def test_optimized_function_returns_correct_result(model):
    def calculate_square(x):
        """
        This function returns the square of its input.
        """
        return x**2

    optimized_function = optimize_function(calculate_square, ["x"], model)
    assert optimized_function(2) == 4
    assert optimized_function(3) == 9
    assert optimized_function(4) == 16
    optimized_function_source = inspect.getsource(optimized_function)
    print(
        f"Here is the optimized function in terms of time and space complexity:\n{optimized_function_source}")


# test_optimized_function_returns_correct_result("gpt-3.5-turbo")
test_optimized_function_returns_correct_result("gpt-4")
