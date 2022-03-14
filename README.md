# qBittorrent_Serverchan_Push
qBittorrent_Serverchan_Push是一个基于**python3**编写的消息推送脚本，主要功能是在qBittorrent下载完成后调用**ServerChan**进行消息推送  
  
**注意：** 本项目依赖的在线推送服务Server酱Turbo已开启会员订阅制度，免费账户可能无法正常使用该项目！

## 文件清单
|  文件   | 说明  |
|  ----  | ----  |
| qBittorrent_Serverchan_Push.ipynb  | Google Colab项目，用于在线编写、调试和提交 |
| qBittorrent_Serverchan_Push.py  | py脚本文件，用于qBittorrent调用 |

## 调用库
|  库   | 说明  |
|  ----  | ----  |
| requests  | 用于向Server酱发起推送请求 |
| sys  | 用于从qBittorrent获取外部参数 |
| math  | 用于计算Torrent文件大小，并进行单位转换 |  
| urllib.parse  | 用于进行URL特殊字符编码 |   
  

## 部署说明

1. 将**qBittorrent_Serverchan_Push.py**下载至本地（群晖或其他Linux系统注意为qBittorrent账户赋予执行权限）。
2. 注册[Server酱Turbo](https://sct.ftqq.com/)账户，获取SendKey。
3. 在[消息通道](https://sct.ftqq.com/forward)中设置需要推送的途径，保存后进行发送测试，确认推送消息能够送达。
4. 编辑**qBittorrent_Serverchan_Push.py** ，填入获取的SendKey并保存。
5. 配置Python3，安装[调用库](https://github.com/Stalker-404/qBittorrent_Serverchan_Push/edit/main/README.md#%E8%B0%83%E7%94%A8%E5%BA%93)中涉及的依赖环境

## 使用说明

打开qBittorrent客户端或WebUI设置，勾选**Torrent 完成时运行外部程序**并在框内填入以下内容并保存：  
  
```python3 /<Your Path>/qbittorrent_serverchan_push.py "%N" "%D" "%Z" "%C"```  
  
其中： \<Your Path\>为qBittorrent_Serverchan_Push.py文件所在位置  
  
![qBittorrent Setting](images/qBittorrentSetting.png)

## 微信服务号推送效果
<img width="300" src="images/MsgPush.jpg"/> <img width="300" src="images/Content.jpg"/>

## 开源协议
本项目使用[Apache License 2.0](https://github.com/Stalker-404/qBittorrent_Serverchan_Push/blob/main/LICENSE)开源许可证
