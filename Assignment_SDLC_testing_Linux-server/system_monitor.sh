#!/bin/bash
# System Monitoring Script
DATE=$(date +'%Y-%m-%d_%H-%M-%S')
LOG_DIR="/var/log/system_monitor"
LOG_FILE="$LOG_DIR/system_metrics_$DATE.log"

mkdir -p "$LOG_DIR"

{
  echo "===== System Metrics on $DATE ====="
  echo
  echo "--- Top CPU Consuming Processes ---"
  ps aux --sort=-%cpu | head -10
  echo
  echo "--- Top Memory Consuming Processes ---"
  ps aux --sort=-%mem | head -10
  echo
  echo "--- Disk Usage ---"
  df -h
  echo
  echo "--- Largest Directories in /var/log ---"
  du -h /var/log | sort -rh | head -10
  echo
  echo "======================================="
} >> "$LOG_FILE"
