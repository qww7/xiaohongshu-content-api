# API服务项目

本项目提供小红书内容生成API，完全免费使用。

## 🚀 快速开始

### 本地运行
```bash
pip install -r api_requirements.txt
python3 api_server.py
```

访问: http://localhost:8000
API文档: http://localhost:8000/docs

### 测试API
```bash
python3 test_api.py
```

## 📡 API端点

### POST /api/generate
**请求示例：**
```json
{
  "topic": "AI副业",
  "style": "xiaohongshu",
  "count": 3
}
```

**响应示例：**
```json
{
  "success": true,
  "posts": [
    {
      "title": "🔥AI副业：这些细节90%的人都不知道！",
      "content": "内容...",
      "opening": "开篇...",
      "tags": ["#AI副业", "#干货"],
      "word_count": 200
    }
  ],
  "message": "成功生成 3 篇内容"
}
```

## 💰 免费部署

### Render.com部署（推荐）
1. 推送代码到GitHub
2. 在Render创建Web Service
3. 选择免费套餐（512MB RAM）
4. 设置启动命令：`python3 api_server.py`
5. 部署完成！

**地址示例：** https://xiaohongshu-api.onrender.com

### 其他免费平台
- **Railway**: $5免费额度
- **Vercel**: 每日执行限制
- **Replit**: 持续运行有限制

## 📊 API定价

**当前：免费使用**
- 每小时最多30次请求
- 无需账号，自动使用DeepSeek API

**未来（可选）：**
- 基础版：免费（30次/小时）
- Pro版：$10/月（1000次/小时）
- 企业版：$50/月（无限制）

## 🎯 用途示例

### JavaScript调用
```javascript
const response = await fetch('https://xiaohongshu-api.onrender.com/api/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    topic: '创业心得',
    count: 3
  })
});
const data = await response.json();
console.log(data.posts);
```

### Python调用
```python
import requests

response = requests.post('https://xiaohongshu-api.onrender.com/api/generate', json={
    'topic': '创业心得',
    'count': 3
})
data = response.json()
print(data['posts'])
```

### cURL调用
```bash
curl -X POST https://xiaohongshu-api.onrender.com/api/generate \
  -H "Content-Type: application/json" \
  -d '{"topic":"创业心得","count":3}'
```

## 📚 自动文档

部署后访问 `/docs` 查看完整API文档，支持在线测试。

## 🔧 技术栈

- **框架**: FastAPI
- **服务器**: Uvicorn
- **AI模型**: DeepSeek API (需要配置API Key)
- **部署**: Render.com (免费)

## 📈 未来扩展

- [ ] 添加更多平台（抖音、快手）
- [ ] 支持视频生成
- [ ] 添加内容优化建议
- [ ] 实现使用统计和分析

## 💖 开发者

小芯 - AI自动赚钱项目

## 📄 许可

MIT License
