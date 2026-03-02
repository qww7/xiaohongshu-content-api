#!/usr/bin/env python3
"""
测试API服务器
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """测试健康检查"""
    print("=" * 70)
    print("🧪 测试1: 健康检查")
    print("=" * 70)
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        print(f"✅ 状态码: {response.status_code}")
        print(f"📊 响应: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def test_api_info():
    """测试API信息"""
    print("\n" + "=" * 70)
    print("🧪 测试2: API信息")
    print("=" * 70)
    try:
        response = requests.get(f"{BASE_URL}/api/info", timeout=5)
        data = response.json()
        print(f"✅ 服务名称: {data['name']}")
        print(f"✅ 端点: {data['endpoint']}")
        print(f"✅ 成本: {data['cost']}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def test_generate():
    """测试内容生成"""
    print("\n" + "=" * 70)
    print("🧪 测试3: 内容生成")
    print("=" * 70)
    try:
        payload = {
            "topic": "AI副业赚钱",
            "style": "xiaohongshu",
            "count": 2
        }
        print(f"📝 请求: {json.dumps(payload, ensure_ascii=False)}")

        response = requests.post(f"{BASE_URL}/api/generate", json=payload, timeout=30)
        data = response.json()

        print(f"\n✅ 生成成功: {data['success']}")
        print(f"📊 消息: {data['message']}")
        print(f"📄 生成篇数: {len(data['posts'])}")

        for i, post in enumerate(data['posts'], 1):
            print(f"\n📝 第{i}篇:")
            print(f"   标题: {post['title']}")
            print(f"   字数: {post['word_count']}")
            print(f"   内容: {post['content'][:100]}...")
            print(f"   标签: {' '.join(post['tags'])}")

        return response.status_code == 200 and len(data['posts']) > 0
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    """运行所有测试"""
    print("🚀 开始API测试...")
    print(f"📍 API地址: {BASE_URL}\n")

    tests = [
        test_health,
        test_api_info,
        test_generate
    ]

    results = []
    for test in tests:
        result = test()
        results.append(result)

    print("\n" + "=" * 70)
    print("📊 测试总结")
    print("=" * 70)
    print(f"✅ 通过: {sum(results)}/{len(results)}")

    if all(results):
        print("\n🎉 所有测试通过！API可以正常使用！")
        print(f"\n📚 API文档: {BASE_URL}/docs")
        print(f"🧹 健康检查: {BASE_URL}/health")
    else:
        print("\n⚠️ 部分测试失败，请检查服务器状态")

if __name__ == "__main__":
    main()
