# 🚀 部署指南：完全免费API服务

## 当前状态

✅ API开发完成且测试通过
✅ 本地运行正常
⏳ 待部署到云端（免费）

---

## 📍 第一步：推送到GitHub

### 1. 创建GitHub仓库
- 登录 https://github.com
- 点击 "New repository"
- 仓库名：`xiaohongshu-content-api`
- 选择 Public（公开可获得更好曝光）
- 点击 "Create repository"

### 2. 推送代码

打开本地终端，运行：

```bash
cd /home/qww/.openclaw/workspace
git init
git add api_server.py api_requirements.txt deepseek_generator.py API_README.md .env.json
git commit -m "初始提交：小红书内容生成API"
git branch -M main
git remote add origin https://github.com/你的用户名/xiaohongshu-content-api.git
git push -u origin main
```

---

## 📍 第二步：部署到Render（免费）

### 1. 访问Render并注册

https://render.com/
- 使用GitHub账号登录（最快）

### 2. 创建Web Service

点击 "New +" → "Web Service"

### 3. 连接GitHub仓库

- 选择 `xiaohongshu-content-api`
- 点击 "Connect"

### 4. 配置部署

**Basic设置:**
```
Name：xiaohongshu-api（或自定义）
Region：Singapore（离中国近，速度快）
Branch：main
```

**Runtime设置:**
```
Runtime：Python 3
Build Command：pip install -r api_requirements.txt
Start Command：python3 api_server.py
```

**关键：FREE套餐**
```
✅ 选择"Free"套餐（完全免费）
- 512MB RAM
- 0.1 CPU
- 足够API使用！
```

### 5. 环境变量（可选）

如果有DeepSeek API Key，添加环境变量：

```
Environment Variables → Add Variable
Name：DEEPSEEK_API_KEY
Value：sk-8cb81334002d4f679d3188242a2ebec0
```

### 6. 部署

点击 "Create Web Service"
等待5-10分钟...

### 7. 完成后

得到一个URL，例如：
```
https://xiaohongshu-api.onrender.com
```

---

## 📍 第三步：测试部署的API

```bash
# 测试健康检查
curl https://xiaohongshu-api.onrender.com/health

# 测试内容生成
curl -X POST https://xiaohongshu-api.onrender.com/api/generate \
  -H "Content-Type: application/json" \
  -d '{"topic":"AI创业","count":2}'
```

访问API文档：
```
https://xiaohongshu-api.onrender.com/docs
```

---

## 📍 第四步：注册到API市场（可选，增加曝光）

### RapidAPI（全球最大）

1. 访问：https://rapidapi.com/
2. 注册账号
3. 点击 "Add New API"
4. 填写信息：
   - Name：Xiaohongshu Content API
   - Description：免费生成小红书内容
   - Endpoint：https://xiaohongshu-api.onrender.com
5. 定价：设置为Free
6. 发布！

---

## 📊 自动化完成后你做什么？

### 完全不用操作的情况

```
✅ API部署在云端
✅ 每天自动运行
✅ 任何人都可以自动调用
✅ 需要的话，设置免费额度限制

你（哥）：零操作
小芯：自动运行
用户：自助使用
```

### 可选的监控

```bash
# 查看调用日志（可选）
curl https://xiaohongshu-api.onrender.com/health
```

Render会自动监控服务状态：
- 服务崩溃：自动重启
- 流量过大：自动限流
- 每周报告：发送到邮箱

---

## 💰 你什么都不做，如何赚钱？

### 方案A：免费API + 赞赏
1. API完全免费
2. GitHub仓库添加赞助链接
3. 用户自愿赞助
4. 被动收入

### 方案B：免费额度 + 付费升级
1. 每天免费30次
2. 付费用户：$10/月，无限次
3. 用户自助订阅
4. 被动收入

### 方案C：API市场
1. 发布到RapidAPI
2. 设置付费套餐
3. 平台自动收款
4. 你零操作

---

## ⏰ 时间估算

| 步骤 | 时间 | 你的操作 |
|------|------|----------|
| 1. GitHub推送 | 5分钟 | 需要操作 |
| 2. Render部署 | 10分钟 | 需要操作 |
| 3. 测试验证 | 5分钟 | 小芯做 |
| 4. API市场注册 | 15分钟 | 可选 |

**总时间：20-40分钟（一次性投入）**

---

## 🎯 这之后

```
Day 1: 部署完成 ✅
Day 2+: API自动运行，你零操作 ✅
用户: 自助调用API
收入: 按设置的节奏自动到账

完全符合：
✅ AI自主（小芯自动运行）
✅ 自动赚钱（API收费）
✅ 每天重复（用户每天调用）
✅ 你零操作
```

---

## 🔥 现在就开始

需要我帮你准备GitHub推送命令吗？

还是你已经准备好了，告诉我完成部署！
