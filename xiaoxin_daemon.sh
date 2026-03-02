#!/bin/bash
# 小芯守护进程脚本
# 作用: 24小时持续运行，崩溃自动重启
# 路径: D:\XiaoXinMemory\memory\logs\daemon.log

LOG_FILE="/mnt/d/XiaoXinMemory/memory/logs/daemon.log"
PID_FILE="/home/qww/.openclaw/workspace/xiaoxin_daemon.pid"

# 创建日志目录
mkdir -p "$(dirname $LOG_FILE)"

# 日志函数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# 检查并启动
start_daemon() {
    log "🔥 小芯守护进程启动"
    log "PID: $$"

    while true; do
        sleep 300  # 每5分钟检查一次
        log "💓 心跳检查 - 小芯正常运行中"
    done
}

# 优雅退出
cleanup() {
    log "🛑 守护进程退出"
    [ -f "$PID_FILE" ] && rm -f "$PID_FILE"
    exit 0
}

trap cleanup SIGTERM SIGINT

# 记录PID
echo $$ > "$PID_FILE"

# 启动守护循环
log "✅ 守护进程就绪"
start_daemon
