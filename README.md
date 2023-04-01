# Super Simple AI Functions

An easy-to-use implementation of AI functions using OpenAI's GPT-4 (or any other model version) to perform various tasks. This project is heavily inspired by [Ask Marvin](https://www.askmarvin.ai/).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/SuperSimpleAIFunctions.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Obtain an [OpenAI API key](https://beta.openai.com/signup/) and store it in a `keys.py` file in the same directory as the scripts or set it as an environment variable.

## Usage

### ai_functions.py

`ai_functions.py` contains the following function:

```python
def ai_function(function, args, description, model="gpt-4"):
```

The `ai_function` takes the following parameters:
- `function`: A string describing the function signature.
- `args`: A list of arguments for the function.
- `description`: A string describing the purpose of the function.
- `model`: (Optional) A string specifying the GPT model to use. Default is 'gpt-4'.

Example usage:

```python
import ai_functions

function = "def add(a: int, b: int) -> int:"
args = ["5", "7"]
description = "Adds two integers."

result = ai_functions.ai_function(function, args, description)
print(result)  # Output: 12
```

## Limitations

The table below shows the success rate of the AI functions with different GPT models:

| Description               | GPT-4 Result | GPT-3.5-turbo Result | Reason |
|---------------------------|--------------|----------------------|--------|
| Generate fake people      | PASSED       | FAILED               | Insufficient information for generating fake data |
| Generate Random Password  | PASSED       | FAILED               | Incorrect response format |
| Calculate area of triangle| FAILED       | FAILED               | Incorrect float value (GPT-4), Response parsing issue (GPT-3.5-turbo) |
| Calculate the nth prime number | PASSED  | FAILED               | Incorrect integer format in the response |
| Encrypt text              | PASSED       | PASSED               | N/A    |
| Find missing numbers      | PASSED       | PASSED               | N/A    |

It's important to note that AI Functions are not suited for certain tasks, particularly those involving mathematical calculations and precision. As observed in the case of calculating the area of a triangle and finding the nth prime number, GPT models can struggle with providing accurate results. The limitations of GPT models in such cases are mainly due to their inherent inability to perform precise arithmetic and the ambiguity in understanding user inputs.

In conclusion, while AI Functions can be helpful in various scenarios, they may not be the optimal choice for tasks requiring mathematical accuracy or specific domain knowledge. For such use-cases, utilizing traditional algorithms and libraries would yield better results.



### test_ai_functions.py

`test_ai_functions.py` contains test cases for the `ai_function`. To run the tests, execute the script with Python:

```bash
python test_ai_functions.py
```

The test script will output the results of each test case and provide a success rate.

## Contributing

Contributions are welcome! If you would like to add more test cases or improve the existing code, please feel free to submit a pull request.

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
