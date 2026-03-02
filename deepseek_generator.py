#!/usr/bin/env python3
"""
使用DeepSeek API的内容生成器（支持配置文件）
"""

import json
import time
from datetime import datetime
import os

CONFIG_FILE = "/home/qww/.openclaw/workspace/.env.json"

try:
    import requests
except ImportError:
    print("正在安装 requests...")
    import subprocess
    subprocess.run(["pip3", "install", "requests", "--quiet"])
    import requests

def load_config():
    """加载API配置"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"apis": {}}

class DeepSeekGenerator:
    """DeepSeek 内容生成器"""

    def __init__(self, use_config=True):
        self.api_key = None

        if use_config:
            config = load_config()
            self.api_key = config.get("apis", {}).get("deepseek", {}).get("api_key", "")

        if self.api_key:
            print(f"✅ DeepSeek API 已配置")
            print(f"   API Key: {self.api_key[:10]}...{self.api_key[-4:]}")
        else:
            print("⚠️ 未配置API Key，使用演示模式（模板生成）")
            print("💡 配置方法: 编辑 .env.json 文件")

        self.api_url = "https://api.deepseek.com/chat/completions"
        self.model = "deepseek-chat"

    def generate_xiaohongshu_post(self, topic):
        """生成小红书图文内容"""

        if not self.api_key:
            # 演示模式：使用模板
            return self._generate_mock_post(topic)

        prompt = f"""
你是一个专业的小红书内容创作者。请为以下主题生成一篇高质量的小红书图文内容：

主题：{topic}

要求：
1. 标题：吸引眼球，使用emoji，符合小红书风格
2. 开篇：亲切自然，符合姐妹们的语气
3. 正文：结构清晰，有干货价值，使用emoji列表，每段不要太长
4. 标签：5-8个相关标签，格式如 #标签名
5. 整体语气：亲切、有温度、分享感强
6. 内容要有真实的个人体验感

请以JSON格式返回，格式如下：
{{
    "title": "帖子标题",
    "opening": "开篇语",
    "content": "正文内容",
    "tags": ["#标签1", "#标签2", ...]
}}

不要添加markdown代码块，直接返回JSON。

主题：{topic}
"""

        try:
            # 调用DeepSeek API
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": "你是一个专业的小红书内容创作者，擅长写亲切有温度的分享型文字，使用emoji，结构清晰，内容要有真实感和个人体验。"},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.9,
                "max_tokens": 1000
            }

            print(f"      🔄 正在调用DeepSeek API...")
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()

            result = response.json()
            text = result["choices"][0]["message"]["content"].strip()

            # 清理返回的文本
            if text.startswith("```json"):
                text = text[7:]
            elif text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]

            # 解析JSON
            post_data = json.loads(text)

            # 添加元数据
            post_data["topic"] = topic
            post_data["generated_at"] = datetime.now().isoformat()
            post_data["platform"] = "xiaohongshu"
            post_data["word_count"] = len(post_data["content"])
            post_data["mode"] = "API (DeepSeek)"

            print(f"      ✅ API返回成功")
            return post_data

        except json.JSONDecodeError as e:
            print(f"      ❌ JSON解析错误: {e}")
            print(f"      原始内容: {text[:200]}...")
            # 失败时返回模板
            return self._generate_mock_post(topic)
        except requests.exceptions.RequestException as e:
            print(f"      ❌ API请求错误: {e}")
            if self.api_key:
                print(f"      💡 提示：检查API Key是否正确，或额度是否充足")
            # 失败时返回模板
            return self._generate_mock_post(topic)
        except Exception as e:
            print(f"      ❌ 未知错误: {e}")
            # 失败时返回模板
            return self._generate_mock_post(topic)

    def _generate_mock_post(self, topic):
        """演示模式：使用模板生成"""
        templates = {
            "title": f"🔥{topic}：这些细节90%的人都不知道！",
            "opening": f"姐妹们！今天分享一个{topic}的干货📚",
            "content": f"""作为一个{topic}的老手，我发现大家经常忽略这些要点：

✅ 要点1：基础打牢很重要
先理解{topic}的核心逻辑，不要急于求成

✅ 要点2：坚持输出是关键
每天花30分钟做{topic}，持续一周就能看到效果

✅ 要点3：及时复盘优化
每周回顾一下，找出问题，持续改进

💡 小贴士：
- 新手不要贪多
- 定期复盘很重要
- 找到适合自己的节奏

喜欢的姐妹们记得点赞收藏哦～❤️""",
            "tags": [f"#{topic}", "#干货分享", "#学习成长", "#努力成为更好的自己", "#自律"]
        }

        post_data = {
            "title": templates["title"],
            "opening": templates["opening"],
            "content": templates["content"],
            "tags": templates["tags"],
            "topic": topic,
            "generated_at": datetime.now().isoformat(),
            "platform": "xiaohongshu",
            "word_count": len(templates["content"]),
            "mode": "Template (Demo)"
        }

        return post_data

    def generate_batch(self, topics, output_file=None):
        """批量生成内容"""
        print(f"\n🚀 开始批量生成内容...")
        print(f"   主题数: {len(topics)}")

        if self.api_key:
            print(f"   模式: API模式（DeepSeek）")
        else:
            print(f"   模式: 演示模式（模板生成）")

        results = []
        success_count = 0
        api_count = 0

        for i, topic in enumerate(topics, 1):
            print(f"\n📝 [{i}/{len(topics)}] 正在生成：{topic}")

            post = self.generate_xiaohongshu_post(topic)

            if post:
                results.append(post)
                success_count += 1
                mode = post.get("mode", "Unknown")
                print(f"   ✅ 生成成功 ({post['word_count']} 字, {mode})")
                print(f"   📌 标题: {post['title']}")

                if mode.startswith("API"):
                    api_count += 1
            else:
                print(f"   ❌ 生成失败，跳过")

            # 避免速率限制
            if self.api_key and i < len(topics):
                time.sleep(0.5)

        print(f"\n{'='*70}")
        print(f"✅ 批量生成完成！")
        print(f"   成功: {success_count}/{len(topics)}")
        print(f"   API生成: {api_count}/{success_count}")
        print(f"{'='*70}")

        # 保存结果
        if results:
            if not output_file:
                mode_type = "api" if self.api_key else "demo"
                output_file = f"/home/qww/.openclaw/workspace/generated_content_{mode_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"\n📄 结果已保存: {output_file}")

        return results

def main():
    """测试运行"""
    # 使用配置文件中的API Key
    generator = DeepSeekGenerator(use_config=True)

    # 测试主题（8个）
    topics = [
        "AI副业赚钱方法",
        "小红书运营技巧",
        "时间管理效率提升",
        "个人品牌建设",
        "流量增长实战",
        "短视频创作指南",
        "电商运营入门",
        "职场晋升秘籍"
    ]

    results = generator.generate_batch(topics)

    # 展示样例
    if results:
        print(f"\n{'='*70}")
        print(f"📄 内容样例对比：")
        print(f"{'='*70}")

        # 显示第一篇API生成的内容
        api_posts = [p for p in results if p.get("mode", "").startswith("API")]
        if api_posts:
            sample = api_posts[0]
            print(f"\n【API生成内容】\n")
            print(f"标题: {sample['title']}")
            print(f"开篇: {sample['opening']}")
            print(f"模式: {sample['mode']}")
            print(f"内容:\n{sample['content']}")
            print(f"\n标签: {' '.join(sample['tags'])}")
        else:
            print("\n⚠️ 未使用API生成（演示模式）")

if __name__ == "__main__":
    main()
