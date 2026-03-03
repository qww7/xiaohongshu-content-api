#!/usr/bin/env python3
"""
小红书内容生成API - FastAPI版本
部署到Render免费托管，零成本
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from datetime import datetime
import os

# 导入DeepSeek生成器
import sys
import os
# 动态路径：兼容本地和云端
workspace_path = os.path.dirname(os.path.abspath(__file__))
if workspace_path not in sys.path:
    sys.path.insert(0, workspace_path)
from deepseek_generator import DeepSeekGenerator

# 初始化FastAPI
app = FastAPI(
    title="小红书内容生成API",
    description="AI自动生成小红书内容，完全免费API服务",
    version="1.0.0"
)

# 初始化生成器
generator = DeepSeekGenerator(use_config=True)

# 请求数据模型
class GenerateRequest(BaseModel):
    topic: str
    style: str = "xiaohongshu"
    count: int = 1

# 响应数据模型
class Post(BaseModel):
    title: str
    content: str
    opening: str
    tags: List[str]
    word_count: int

class GenerateResponse(BaseModel):
    success: bool
    posts: List[Post]
    message: str

# 健康检查
@app.get("/")
async def root():
    return {
        "service": "小红书内容生成API",
        "status": "running",
        "version": "1.0.0",
        "cost": "FREE"
    }

# 健康检查端点
@app.get("/health")
async def health():
    return {"status": "ok"}

# API文档
@app.get("/api/info")
async def api_info():
    return {
        "name": "小红书内容生成API",
        "endpoint": "/api/generate",
        "method": "POST",
        "cost": "FREE (DeepSeek API需要额度)",
        "usage": {
            "topic": "生成主题",
            "style": "xiaohongshu（默认）",
            "count": "生成数量（默认1）"
        },
        "example": {
            "topic": "AI副业",
            "count": 3
        }
    }

# 生成内容API
@app.post("/api/generate", response_model=GenerateResponse)
async def generate_posts(request: GenerateRequest):
    """
    生成小红书内容

    请求示例：
    {
        "topic": "AI副业赚钱",
        "style": "xiaohongshu",
        "count": 3
    }
    """
    try:
        # 生成内容
        posts = []
        for i in range(request.count):
            post = generator.generate_xiaohongshu_post(request.topic)
            if post:
                posts.append(Post(
                    title=post["title"],
                    content=post["content"],
                    opening=post["opening"],
                    tags=post["tags"],
                    word_count=post["word_count"]
                ))

        if not posts:
            return GenerateResponse(
                success=False,
                posts=[],
                message="生成失败"
            )

        return GenerateResponse(
            success=True,
            posts=posts,
            message=f"成功生成 {len(posts)} 篇内容"
        )

    except Exception as e:
        return GenerateResponse(
            success=False,
            posts=[],
            message=f"错误: {str(e)}"
        )

# 运行说明
if __name__ == "__main__":
    import uvicorn
    print("🚀 启动小红书内容生成API...")
    print("💖 免费API服务 - 小芯出品")
    print("📍 本地访问: http://localhost:8000")
    print("📚 API文档: http://localhost:8000/docs")
    print()
    uvicorn.run(app, host="0.0.0.0", port=8000)
