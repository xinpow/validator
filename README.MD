## Validator

A simple Python package for validating data based on rules.

## Installation

```
pip install xinpow-validator
```

## Example Usage

```python
import validator

data = {
    "name" : 'xinpow',
    "age"  : 30,
    "email": "sub@xinpow.com",
    "website": "https://www.xinpow.com",
    "phone": ""
}

rules = {
    "name"   : "required|string|max:32|rule:^[a-zA-Z]+$",
    "age"    : "required|int|min:18|max:100",
    "phone"  : "required|rule:^\d{11}$",
    "email"  : ["required", "email", "max:64"],
    "website": ["url", "max:255"],
}

status, errors = validator.validate(data, rules)

print(status, errors)
```

## Available Rules

- required
- string
- int
- float
- email
- url
- min
- max
- rule
- between

## Custom Rules

You can define your own rules by creating a function that returns a boolean value.

### example
> file: rules/float.py
```python
def handle(value, err_msg: str, *args, **kwargs):
    err_msg = (err_msg or '#label# must be float.')
    if not isinstance(value, float):
        return False, err_msg
    return True, None
```
Save the file and name it according to your rule name, then save it to the 'rule' directory.

You can use it in the rule like this: "required|float" or ["required", "float"].