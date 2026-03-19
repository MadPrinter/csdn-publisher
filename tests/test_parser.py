# -*- coding: utf-8 -*-
"""
Markdown 解析器单元测试
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from csdn_publisher_fast import MarkdownParser


def test_parse_complete_front_matter():
    """测试完整的 front matter 解析"""
    content = """---
title: 测试文章
tags:
  - AI
  - OpenClaw
  - 自动化
categories:
  - 技术
summary: 这是测试摘要
---

这是正文内容。
"""
    _, result = MarkdownParser.load_file('tests/fixtures/sample_blog.md')
    
    # 模拟解析
    fm = MarkdownParser.parse_front_matter(content)
    
    assert fm['title'] == '测试文章', f"标题错误：{fm['title']}"
    assert 'AI' in fm['tags'], f"标签错误：{fm['tags']}"
    assert 'OpenClaw' in fm['tags'], f"标签错误：{fm['tags']}"
    print("✅ test_parse_complete_front_matter 通过")


def test_parse_minimal_front_matter():
    """测试最小 front matter 解析"""
    content = """---
title: 简单文章
---

正文。
"""
    fm = MarkdownParser.parse_front_matter(content)
    
    assert fm['title'] == '简单文章'
    assert fm['body'] == '正文。\n'
    print("✅ test_parse_minimal_front_matter 通过")


def test_parse_no_front_matter():
    """测试无 front matter 解析"""
    content = "# 标题\n\n正文"
    fm = MarkdownParser.parse_front_matter(content)
    
    assert fm['title'] == 'Untitled'
    assert 'body' in fm
    print("✅ test_parse_no_front_matter 通过")


def test_parse_default_tags():
    """测试默认标签"""
    content = """---
title: 无标签文章
---

正文。
"""
    fm = MarkdownParser.parse_front_matter(content)
    
    assert len(fm['tags']) > 0, "应该有默认标签"
    print("✅ test_parse_default_tags 通过")


if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Markdown 解析器测试")
    print("=" * 50)
    
    test_parse_complete_front_matter()
    test_parse_minimal_front_matter()
    test_parse_no_front_matter()
    test_parse_default_tags()
    
    print("=" * 50)
    print("✅ 所有测试通过")
    print("=" * 50)
