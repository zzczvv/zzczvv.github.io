import os
# 定义要检测和插入的字符串
target = '<script src="assets\js\鼠标吸附.js"></script>\n'
target_2 = '<script src="assets\js\鼠标爱心.js"></script>\n'
target_3 = '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>\n'
target_4 = '<script>function btn_click(){confetti();}</script>\n'
# 定义要遍历的文件夹路径
folder = r'D:\用户\Documents\GitHub\zzclovevv.github.io'
# 遍历文件夹下的所有html文件
for file in os.listdir(folder):

    # 只处理html文件
    if file.endswith('.html'):
        # 读取文件内容
        with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
            content = f.read()
        # 检测是否有目标字符串
        # if target not in content:
            # 如果没有，就在</body>后面加上
        content = content.replace('</body>', target + target_2 + target_3  + target_4 + '</body>')
        # 保存修改后的文件内容
        with open(os.path.join(folder, file), 'w', encoding='utf-8') as f:
            f.write(content)
