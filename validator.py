import importlib, re

def validate(datas, rules, errMessage = {}):
    ret = []
    for i in datas:
        if i in rules:
            if type(rules[i]) == str:
                rules[i] = rules[i].split('|')
            if 'required' not in rules[i] and not datas[i].strip():
                break
            for rule in rules[i]:
                status, message = check(i, datas, rule, errMessage[f"{i}.{rule.split(':')[0]}"] if f"{i}.{rule.split(':')[0]}" in errMessage else None)
                if status == False:
                    ret.append(message_label(message, i, datas[i]))
    return (not len(ret) > 0), ret
            
def check(key, data, rules, rules_msg = None):
    rules_opt = rules.split(':')
    if rules_opt[0].lower() == 'required':
        if data[key] is None or (type(data[key]) == str and data[key].split() == ''):
            return False, message_label(rules_msg or '#label# must be required', key, data[key])
        return True, ''
    elif rules_opt[0].lower() == 'rule' and len(rules_opt) == 2:
        status = re.search(r'' + rules[len(rules_opt[0])+1:], data[key])
        return True if status else False, message_label(rules_msg or '#label# it does not match the rule', key, data[key])
    else:
        module = importlib.import_module('rules.' + rules_opt[0].lower())
        return module.handle(data[key], rules_msg) if len(rules_opt) == 1 else module.handle(data[key], rules_msg, *[i.strip() for i in rules[len(rules_opt[0])+1:].split(',')])

def message_label(message, key, value):
    return message.replace('#label#', str(key)).replace('#value#', str(value))
