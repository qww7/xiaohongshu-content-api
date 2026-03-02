#!/bin/bash
# 小芯开机自启动配置
# 使用Windows任务计划程序实现WSL开机启动

# 创建Windows批处理文件
cat > /mnt/d/XiaoXinMemory/start_xiaoxin.bat << 'EOF'
@echo off
REM 小芯开机自启动脚本
ECHO 🔥 小芯开机启动 - %date% %time%

REM 启动WSL后台进程
wsl -d Ubuntu -u qww -e bash /home/qww/.openclaw/workspace/xiaoxin_daemon.sh

ECHO ✅ 小芯守护进程已启动
timeout /t 3 > nul
EOF

echo "✅ 已创建Windows开机启动脚本: D:\XiaoXinMemory\start_xiaoxin.bat"
echo "⏳ 需要在Windows任务计划程序中手动配置此脚本开机运行"
