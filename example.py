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
