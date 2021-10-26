# auto-generated source-code file VK_Logo_128.py with Pycture
# Pycture developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtGui, QtCore
import base64
import os

def Get_vk_logo(image_str):
    ImageStr = base64.b64decode(image_str)
    with open("vk_logo.png", "wb") as vk_logo_text:
        vk_logo_text.write(ImageStr)
    vk_logo_text.close()
    qp = QtGui.QPixmap("vk_logo.png").scaled(100, 100, transformMode=QtCore.Qt.SmoothTransformation)
    os.remove("vk_logo.png")
    return(qp)
        
vk_logo_str = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHXUExURYC7/3e2/2Cq/0id/zST/zOS/yKJ/xGA/wB3/0Sb/0Wc/2at/xyG/xWC/1Wk/wt9/wx9/12p/0yg/xaD/xeD/3+7/4W+/4e//xiE/1Ci/16p/2Os/xmE/xuF/0ed/wF4/wR5/w9//4K8/3W1/////+by/1+q/1yo/9Hm/2Gr/0me/3S1/9Po/1uo/0uf/zmV/4zC/5zK/8fh/zuW/zaU/5nJ//f7/366/ziV/y+Q/83k/w5+/zGR/yiM//3+//L4//v9/yqN/ySK/6fQ/yaL/x2G/+v0/8Le/x+I/63T/9To/2eu/wV6/26y//j7/0Ka/wd7/7/d//X6/wh7//n8/wN5/wZ6/5jI/7jZ/+fy/wJ4/2+y/ymN/8Pf/+jz/3u5/+/2/+Du/8vj/+Pw/+Tx//z9/+Hv/yWL/8He/0+h/8Dd/6DM/zCR/47D/4nA/93t/x6H//7+/xqF/+z1//D3/xOB/yGJ/4G8/3O0/6PO/8bh/6vS/w1+/9vs/4rB//T5/yOK/9/u/3m4/+31/0Ga/8Tg/1im/5fI/wp8/7ra/2qw/73c/1Sk/326/wl8/5HE/2yx/5TG/5PF/zKS/0Ob/2Ss/2uw/1Kj/0ac/4O9/0qe/xKB/wAAAID4xcAAAACddFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wDL/LxMAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAF5UlEQVR4Xu3b6X8TVRTG8Qkl6SDIYltbRUzFVkGQoqisYoulVq1Yi63auoALuCBaVHBBcUXcV5Slf6zJ3N/M3OXcaZBmJi/yfcPMOTP3Pp8kzJY0WGhIUFrWsbxcrlQqnZ2doVetWdukXF7esazU6Mj8K1jBqEvgBoYUiAFWrmLHJXXjaoY3uAHWsH1TrGWSlBOALZuGaRJmgHVs1VQ3MZliBGCLpmO6iB6gi37TdTNhnRaAbi56mFMLcDOtnPQybRqARm6YNgnQRz03XUxMAKq5UjOrALdQy5U6MqsAlHIWTd0aASjkLg6wlvXcrSEAqwVokQC3slaA9VGA21grwIYoACuFaAdoiQBLeP9x7W6vBaiyXIhqLQCLBWkHaAdoB2gHaIEAPSyZOg39VHW0lDsoGuiBom1jcCdLpgGDdL6ipQxSNNADRVspuIslE3vhbqo6WooUYAM9ZRNV2+bgHpZM7IYtVHW0FCnAVnrKvVRt24Ihlkzshu1UdbQUIcB9tJT7qTp2BA+wZGI/PEhVR0sRAjxES9lJ1bEr2M2Sif2wh6qOluIG2EsHVF37godZMrEf9lPV0VLcAI/QUYapukaCAyyZ2DFGVUdHcQPQwKNUXaPBQZZMY+wJqjo6ihPgMRqgKhgP5KeTj7MnqOroKHYA8xgw8ARlQV8gHkXDJ9kVE5Q1dBQrwFOUsSfjwrszkJ9OrGBfjFDW0FGsAIco42nKkr3BJEumKvuil7KGjmIGeIYqpiiLDgfCq1vHzjhEVUNHMQL0Uox5ZlAmGwsgfAppKHqALdRiz1KXTQbSub5mmN1BVUND0QLspJSYpiGbCTz959gd2yinaChpgOepxPZ30PCY8AWoMABemKWeoKHEAeasz3/WIUjpD5yRwQAx56xNXSHAi6ymXlINv/7Ad5BghNjLlBPUlSjAK0dYSx2NNs0y7Q3wKmPEKCcoK4Ojq19jUfc622aYDVhw2J/mceoxysob/Gs6dpxtM1S9AapHGQZHqMcoZ/Behhm8AcJ9jBOzThpUvYZLbLgIfwB7ijHKoOrzJpstKiOA/cZSBkWPKd//bkdGgLcYLPa28R+GouwdNmpARgBnDuO8Ss3nBJstKivAuwyWOEmjjpLXe1mXIamq90BU8759ZJ+nUUfJb16+2LPMZgUITzFWYiy9iKeSpaeBT+K092QU+YChUsnVIevZhGtJS7/vdKzMMVAqOfOznu1DNvZbJIAwzTwvGauLkG7qDBO+SzJ8xEC6qWgXVpTB6dNnzLvBxMfROF4zvovS2CeMY/h0tR0g2rb6GasG6fFKyntVHDv7OeOYAilAGH5xjoJmsati+cZEwziZko9m+CUVzVe0RIc9t2aaGcbJkgZwr4vNA6htr+fmVCe/CQY9QPVriol5+UFYpNNze25wLzZteoAw3E01RUPQ53lAYVrOOF5mgPD0Meqxb2i4xj2PaCwHGMjHChCGUzRi31J3jHoeUtm+YyAPJ8B5GrGtvgPuiOcxnct87mdxAtgPiQaOUbft8zyoFHzPUBI3gHP4uEDdssvzqFYi3ftACPADrdiP1C07PA+rZT8xmEMIEG6nF6Ns2eZ5XO9R/ZnRLFIA+02QL042e76w8DshHZbEAL/QhHN/HSl5vrLJ8Os691ZUDNBFM0bZtPH/fWm19jcGhRjAfg/EE//1fGt26vc/NjG2HOAMXfxJ2XC9X9td+Ovvi3Ol0j+smg6WDOLHvf3FZTtAO0ArBMi6P2+6+g+ZCv8pV6HvQfvnfK0RoMAfta6KAlzTVeHSuhgFKPA9aJFfVhf34/azBCjsJajPHQUoKEE0dYsE+JdSrs5HU6sAhbwEamYCFP6HTvm/BkybBhB+pdFMJ5k2DZDvayD8uV9NN92m62PCOj1Abq8B00WMAAvr8rhEzvij1zq2ahqmSTgBFs6yZVPUz38mN0DNykaeYF+z7gb/9Dtxack+ENVLDCnICKC7XFp/ZahcPl6pXM3+8/+rlcrxcnnoyvrSZXbNtLDwH9/HigeOFUT4AAAAAElFTkSuQmCC"