import validator

data = {
    "name" : 'xinpow',
    "age"  : 30,
    "email": "sub@xinpow.com",
    "website": "https://www.xinpow.com",
    "phone": "12312312312"
}

rules = {
    "name"   : "required|string|max:32|rule:^[a-zA-Z]+$",
    "age"    : "required|int|between:18,28",
    "phone"  : "required|rule:^\d{11}$",
    "email"  : ["required", "email", "max:64"],
    "website": ["url", "max:255"],
}

errMessage = {
    "name.required"   : "#label# is required",
    "name.string"     : "#label# must be a string",
    "name.max"        : "#label# must be less than 32 characters",
    "name.rule"       : "#label# must only contain letters",
    "age.required"    : "Age is required",
    "age.int"         : "Age must be an integer",
    "age.between"     : "Age must be between 18 and 28. (input: #value#)",
    "phone.required"  : "Phone number is required",
    "phone.rule"      : "Phone number must be 11 digits",
    "email.required"  : "Email is required",
    "email.email"     : "Email is invalid",
    "email.max"       : "Email must be less than 64 characters",
    "website.url"     : "Website is invalid",
    "website.max"     : "Website must be less than 255 characters",
}

status, errors = validator.validate(data, rules, errMessage)

print(status, errors)
