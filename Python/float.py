def almost_equal(x, y, places=7):
    return round(abs(x-y), places) == 0

print almost_equal(sum([0.1 for i in range(10)]), 1.0)


# {
#     // See https://go.microsoft.com/fwlink/?LinkId=733558
#     // for the documentation about the tasks.json format
#     "version": "2.0.0",
#     "tasks": [
#         {
#             "taskName": "echo",
#             "type": "shell",
#             "command": "echo Hello"
#         },
#         {
#             "version": "0.1.0",
#             "taskName": "py2",
#             "type": "shell",
#             // The command is tsc. Assumes that tsc has been installed using npm install -g typescript
#             "command": "/usr/bin/python",
        
#             // The command is a shell script
#             "isShellCommand": true,
        
#             // Show the output window only if unrecognized errors occur.
#             "showOutput": "always",
        
#             // args is the HelloWorld program to compile.
#             "args": ["${file}"]
#         }
#     ]

# }