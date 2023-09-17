import os

# 1. 设置你的GitHub仓库URL
repo_url = 'https://github.com/ERerGB/mAIketing.git'

# 2. 设置本地仓库路径
local_repo_path = '.'

# 3. 设置HTML代码
html_code = """
<!DOCTYPE html>
<html>
<head>
<title>Your HTML Title</title>
</head>
<body>
Hello, world!
</body>
</html>
"""

# 4. 将HTML代码保存到一个文件
with open(os.path.join(local_repo_path, 'index.html'), 'w') as file:
    file.write(html_code)

# 5. 使用os.system或subprocess模块执行Git命令
os.chdir(local_repo_path)
os.system('git add .')
os.system('git commit -m "Add index.html"')
os.system(f'git remote add origin {repo_url}')
os.system('git push -u origin master')

# 注意：
# 1. 你应该先在本地仓库路径初始化一个Git仓库（git init）
# 2. 你需要替换'repo_url'和'local_repo_path'为你的实际GitHub仓库URL和本地路径
# 3. 你的GitHub账户需要有推送权限到指定的仓库
# 4. 你可能需要先配置Git的用户名和邮箱（git config user.name "Your Name", git config user.email "you@example.com"）
