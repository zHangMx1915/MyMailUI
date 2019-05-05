import json
# 写入json

state = {'user': '5151561651621', 'pass': 'zx2579188'}
print(type(state))
with open("data_config.json", "w") as f:
    json.dump(state, f)
