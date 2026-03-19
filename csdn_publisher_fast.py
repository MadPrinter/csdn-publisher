# -*- coding: utf-8 -*-
"""
CSDN Publisher - Production Ready v3.1
基于调试结果完全修复的版本
"""

import sys
import os
import time
import re
from typing import Optional, Dict, List, Tuple

try:
    import pyperclip
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
except ImportError as e:
    print(f"[ERROR] 缺少依赖：{e}")
    sys.exit(1)


class Config:
    CSDN_EDITOR_URL = "https://editor.csdn.net/md/"
    TIMEOUT_LOGIN = 10
    TIMEOUT_MODAL = 15       # 等待弹窗时间
    TIMEOUT_PUBLISH = 30     # 等待发布完成时间
    DEFAULT_TAGS = ["AI", "OpenClaw", "自动化"]
    SUCCESS_KEYWORDS = ["发布成功", "正在审核", "发表成功"]


class CSDNPublisher:
    def __init__(self, driver):
        self.driver = driver
        self.start_time = None
    
    def publish(self, markdown_file: str) -> Tuple[bool, str]:
        self.start_time = time.time()
        
        try:
            # 1. 读取并解析文件
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
            fm = self._parse_front_matter(content)
            title = fm.get('title', 'Untitled')
            body = fm.get('body', content)
            tags = fm.get('tags', Config.DEFAULT_TAGS)[:3]
            
            print(f"[CSDN] 文章：{title}")
            print(f"[CSDN] 标签：{', '.join(tags)}")
            
            # 2. 打开编辑器
            self.driver.get(Config.CSDN_EDITOR_URL)
            time.sleep(3)
            
            # 3. 等待登录
            print("[CSDN] 检查登录...")
            try:
                WebDriverWait(self.driver, Config.TIMEOUT_LOGIN).until(
                    EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder,"请输入文章标题")]'))
                )
                print("[CSDN] 已登录")
            except TimeoutException:
                return False, "未登录 CSDN"
            
            # 4. 填写标题
            print("[CSDN] 填写标题...")
            title_input = self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"请输入文章标题")]')
            title_input.clear()
            title_input.send_keys(title)
            
            # 5. 粘贴内容
            print("[CSDN] 粘贴内容...")
            editor = self.driver.find_element(By.CLASS_NAME, 'cledit-section')
            editor.click()
            time.sleep(0.5)
            pyperclip.copy(body)
            cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
            editor.send_keys(cmd_ctrl, 'v')
            time.sleep(2)
            
            # 6. 关闭可能的初始弹窗
            try:
                close_btn = self.driver.find_element(By.XPATH, '//button[@title="关闭"]')
                close_btn.click()
                time.sleep(1)
            except:
                pass
            
            # 7. 滚动到底部并点击发布
            print("[CSDN] 点击发布...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            publish_btn = self.driver.find_element(By.XPATH, '//button[contains(text(),"发布文章")]')
            self.driver.execute_script("arguments[0].click();", publish_btn)
            
            # 8. 等待弹窗出现（关键修复：增加等待时间）
            print("[CSDN] 等待弹窗...")
            modal_found = False
            for i in range(Config.TIMEOUT_MODAL):
                time.sleep(1)
                modals = self.driver.find_elements(By.CSS_SELECTOR, '.modal')
                if modals:
                    print(f"[CSDN] {i+1}s 弹窗出现")
                    modal_found = True
                    break
            
            if not modal_found:
                # 检查是否有限制提示
                source = self.driver.page_source
                if '频繁' in source or '限制' in source:
                    return False, "发布频率过高，请稍后再试"
                return False, "弹窗未出现"
            
            # 9. 点击添加标签按钮
            print("[CSDN] 添加标签...")
            try:
                tag_btn = self.driver.find_element(By.CSS_SELECTOR, 'button.tag__btn-tag')
                self.driver.execute_script("arguments[0].click();", tag_btn)
                time.sleep(1.5)  # 等待输入框出现
            except:
                pass
            
            # 10. 填写标签
            try:
                tag_input = self.driver.find_element(By.CSS_SELECTOR, '.mark_selection_box input')
                for tag in tags:
                    tag_input.send_keys(tag)
                    time.sleep(0.3)
                    tag_input.send_keys(Keys.ENTER)
                    time.sleep(0.2)
                time.sleep(1)
            except Exception as e:
                print(f"[CSDN] 标签填写失败：{e}")
            
            # 11. 点击确认发布
            print("[CSDN] 确认发布...")
            confirm_btn = self.driver.find_element(By.CSS_SELECTOR, 'button.btn-b-red')
            self.driver.execute_script("arguments[0].click();", confirm_btn)
            
            # 12. 等待发布完成
            print("[CSDN] 等待发布完成...")
            for i in range(Config.TIMEOUT_PUBLISH):
                time.sleep(1)
                source = self.driver.page_source
                url = self.driver.current_url
                
                # 检查成功关键词
                for kw in Config.SUCCESS_KEYWORDS:
                    if kw in source:
                        article_id = self._extract_article_id(url, source)
                        return True, f"https://blog.csdn.net/article/details/{article_id}"
                
                # 检查 URL 变化
                if 'articleId=' in url:
                    article_id = url.split('articleId=')[1].split('&')[0]
                    return True, f"https://blog.csdn.net/article/details/{article_id}"
                
                # 检查页面标题变化
                if i > 10 and '写文章' not in self.driver.title:
                    article_id = self._extract_article_id(url, source)
                    return True, f"https://blog.csdn.net/article/details/{article_id}"
            
            # 超时检查
            article_id = self._extract_article_id(self.driver.current_url, self.driver.page_source)
            if article_id:
                return True, f"https://blog.csdn.net/article/details/{article_id}"
            
            return False, "发布超时"
            
        except Exception as e:
            return False, f"发布失败：{e}"
    
    def _extract_article_id(self, url: str, source: str) -> str:
        """从 URL 或源码提取文章 ID"""
        if 'articleId=' in url:
            return url.split('articleId=')[1].split('&')[0]
        match = re.search(r'articleId[=:](\d+)', source)
        if match:
            return match.group(1)
        return 'pending'
    
    def _parse_front_matter(self, content: str) -> Dict:
        """解析 markdown front matter"""
        result = {'title': 'Untitled', 'tags': [], 'body': content}
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
        if match:
            result['body'] = match.group(2)
            for line in match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    if key.strip() == 'title':
                        result['title'] = value.strip().strip('"\'')
                    elif key.strip() == 'tags':
                        result['tags'] = []
        if not result['tags']:
            result['tags'] = Config.DEFAULT_TAGS
        return result


def main():
    if len(sys.argv) < 2:
        print("用法：python csdn_publisher_fast.py <blog.md>")
        sys.exit(1)
    
    print("=" * 60)
    print("CSDN Publisher v3.1")
    print("=" * 60)
    
    chrome_options = Options()
    chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"[ERROR] Chrome 启动失败：{e}")
        sys.exit(1)
    
    try:
        publisher = CSDNPublisher(driver)
        success, message = publisher.publish(sys.argv[1])
        
        print("\n" + "=" * 60)
        if success:
            print(f"[SUCCESS] 发布成功!")
            print(f"[LINK] {message}")
        else:
            print(f"[FAILED] {message}")
        print("=" * 60)
        
        sys.exit(0 if success else 1)
    finally:
        try:
            driver.quit()
        except:
            pass


if __name__ == "__main__":
    main()
