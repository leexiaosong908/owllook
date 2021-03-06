#!/usr/bin/env python
"""
 Created by howie.hu at 2018/8/13.
"""
import os
import subprocess

if __name__ == '__main__':
    # os.environ['MODE'] = 'PRO'
    servers = [
        ["pipenv", "run", "python", "owllook/server.py"],
        ["pipenv", "run", "python", "owllook/scheduled_task.py"]
    ]
    procs = []
    for server in servers:
        proc = subprocess.Popen(server)
        procs.append(proc)
    for proc in procs:
        proc.wait()
        if proc.poll():
            exit(0)
