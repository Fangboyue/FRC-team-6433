# 使用方法：先安装 qrcode[pil]，然后运行：
# python make_web_qr.py "https://你的用户名.github.io/frc6433-recruitment/"
import sys
import qrcode

if len(sys.argv) != 2:
    print('用法: python make_web_qr.py "https://你的公开网页网址/"')
    raise SystemExit(1)
url=sys.argv[1]
img=qrcode.make(url)
img.save('FRC6433_网页二维码_海报版.png')
print('已生成 FRC6433_网页二维码_海报版.png')
