# -*- coding: utf-8 -*-
"""
捕获 CSDN 发布弹窗的完整页面结构
"""

import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

print("连接 Chrome...")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

# 打开编辑器
print("打开编辑器...")
driver.get('https://editor.csdn.net/md/')
time.sleep(3)

# 填写标题
print("填写标题...")
try:
    title_input = driver.find_element(By.XPATH, '//input[contains(@placeholder,"请输入文章标题")]')
    title_input.send_keys("测试" + str(time.time()))
    time.sleep(1)
    print("标题已填写")
except Exception as e:
    print(f"标题填写失败：{e}")

# 填写内容
print("填写内容...")
try:
    editor = driver.find_element(By.CLASS_NAME, 'cledit-section')
    editor.click()
    time.sleep(0.5)
    editor.send_keys("测试内容")
    time.sleep(2)
    print("内容已填写")
except Exception as e:
    print(f"内容填写失败：{e}")

# 滚动到底部
print("滚动到底部...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# 点击发布
print("点击发布按钮...")
try:
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for btn in buttons:
        if '发布' in btn.text:
            print(f"找到发布按钮：{btn.text}")
            driver.execute_script("arguments[0].click();", btn)
            break
    time.sleep(3)
    print("已点击发布")
except Exception as e:
    print(f"点击失败：{e}")

# 保存完整页面 HTML
print("保存页面 HTML...")
page_html = driver.page_source
output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'full_page.html')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(page_html)
print(f"页面 HTML 已保存到：{output_file}")

# 查找所有包含"发布"的元素
print("\n" + "=" * 50)
print("包含'发布'的元素：")
print("=" * 50)
publish_elements = driver.execute_script("""
    var result = [];
    var buttons = document.querySelectorAll('button');
    buttons.forEach(function(btn) {
        if (btn.textContent.includes('发布')) {
            result.push({
                tag: 'button',
                text: btn.textContent.trim(),
                className: btn.className,
                id: btn.id
            });
        }
    });
    var divs = document.querySelectorAll('div');
    divs.forEach(function(div) {
        if (div.textContent.includes('发布') && div.textContent.length < 50) {
            result.push({
                tag: 'div',
                text: div.textContent.trim(),
                className: div.className
            });
        }
    });
    return JSON.stringify(result, null, 2);
""")
print(publish_elements)

# 查找所有弹窗相关元素
print("\n" + "=" * 50)
print("弹窗相关元素：")
print("=" * 50)
modal_elements = driver.execute_script("""
    var result = [];
    var modals = document.querySelectorAll('[class*="modal"], [class*="Modal"], [class*="dialog"], [class*="Dialog"], [class*="popup"], [class*="mask"]');
    modals.forEach(function(el) {
        result.push({
            className: el.className,
            id: el.id,
            text: el.textContent.substring(0, 100)
        });
    });
    return JSON.stringify(result, null, 2);
""")
print(modal_elements)

driver.quit()
print("\n完成！")
