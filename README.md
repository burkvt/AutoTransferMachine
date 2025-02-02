<h1 align="center"> ⭐️ Auto Transfer Machine ⭐️ </h1>
<h2 align="center"><strong>:heart_on_fire:为发光发热而生:heart_on_fire:</a></strong></h2>

## :triangular_flag_on_post:主要功能
<img src="https://img.kimoji.club/images/2023/10/06/ATM.jpg" alt="ATM.jpg" border="0" />

* 1.转种模式：自动从源站抓取媒体信息并转种
* 2.发种模式：自动从本地媒体文件中提取信息并发种
* 3.站点签到（有空再做）
* 4.批量爬取站点指定资源并下载到本地
* 5.生成转种模板
* 6.从媒体中截取指定数量、格式的图片，上传到指定图床（有空再做）

## :warning:注意事项
* 使用有门槛，有问题需自行研究，脚本打开以后有群号，建议群内提问或提建议，没事不要提issue

## :warning:安装说明
1. #### 安装Docker以及Docker-compose环境 :star:
     * `curl -fsSL https://get.docker.com -o get-docker.sh`
     * `sudo sh get-docker.sh`
     * `sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

2. #### 拉取镜像 :star:
     * `docker pull hudan717/atm`

3. #### 加载ATM配置文档及启动 :star:
     * 把atm文件夹下载到你的机器中的任意位置，里面分别有三个子文件夹，里面各有一个占位的空文件，下载以后可以删除也可以不用理会
     * 下载以后，自行修改compose中的媒体映射路径
     * 在compose所在路径下，启动容器 `docker-compose run atm`
     * :star:请注意，要用 `docker-compose run` 不能用 `docker-compose up`
     * 容器启动后会自动进入内部的/app路径，输入`./update`更新最新脚本，输入`./a`开启脚本

## :warning:使用说明

* 使用建议
     * 容器的运行建议跑在screen下，以下给出最基本的screen操作流程
     * `sudo apt-get install screen` 安装screen
     * `screen -R atm` 创建一个名为atm的screen(可以理解成windows的分屏)
     * 在atm分屏中开启脚本后，你可以通过ctrl+a+d退出atm的screen，回到ssh主界面进行别的操作
     * 如果要回去看看脚本的工作进度，可以使用`screen -r atm` 或者 `screen -D -r atm`指令切换回screen
     * 脚本运行过程中，你可以通过`ctrl+z`随时暂停脚本,同时在暂停状态下，你也可以通过输入`fg`让脚本继续工作


## :star:更新流

* 增加server酱推送功能，每次任务完成后会推送消息通知
* 增加拉种模式下种子下载到本地后，同时导入到QB（默认暂停），方便随时下载
* 增加截图格式选择功能，用于适配个别站点硬性规定需要png源图的奇怪需求

## :warning:已适配转出站点

<table>
  <tr>
    <td colspan="6" align="center">:star:已适配</td>
    <td align="center">:construction_worker_man:施工中</td>
  </tr>  
  <tr>
    <td align="center">观众</td>
    <td align="center">CarPT</td> 
    <td align="center">大青虫</td> 
    <td align="center">打胶</td> 
    <td align="center">碟粉</td>     
    <td align="center">咖啡</td>     
    <td align="center">学校</td> <!-- 施工中 -->
  </tr>  
  <tr>
    <td align="center">龙之家</td>
    <td align="center">GTK</td> 
    <td align="center">海胆</td> 
    <td align="center">白兔</td> 
    <td align="center">好大</td>  
    <td align="center">铂金学院</td>    
    <td align="center">阿童木</td> <!-- 施工中 -->
  </tr> 
  <tr>
    <td align="center">自由农场</td>
    <td align="center">杜比</td> 
    <td align="center">红豆饭</td> 
    <td align="center">家园</td> 
    <td align="center">小蚂蚁</td>
    <td align="center">猫</td>     
    <td align="center">普斯特</td> <!-- 施工中 -->
  </tr> 
  <tr>
    <td align="center">明教</td>
    <td align="center">空</td> 
    <td align="center">HDTIME</td> 
    <td align="center">好多油</td> 
    <td align="center">HDVIDEO</td>
    <td align="center">铂金家</td>     
    <td align="center">蝴蝶</td> <!-- 施工中 -->
  </tr> 
  <tr>
    <td align="center">HDZONE</td> 
    <td align="center">大聪明</td> 
    <td align="center">北川</td> 
    <td align="center">冰淇淋</td>
    <td align="center">爱萝莉</td>
    <td align="center">PTLSP</td>
    <td align="center">我堡</td> <!-- 施工中 -->
  </tr> 
  <tr>
    <td align="center">ITZMX</td> 
    <td align="center">开心</td> 
    <td align="center">库非</td> 
    <td align="center">芒果</td>
    <td align="center">馒头</td>
    <td align="center">PTT</td>
    <td align="center">不可说</td> <!-- 施工中 -->
  </tr> 
  <tr>
    <td align="center">南洋</td> 
    <td align="center">OKPT</td> 
    <td align="center">奥申</td> 
    <td align="center">熊猫</td>
    <td align="center">猪猪</td>
    <td align="center">红叶</td>
    <td align="center">烧包</td> <!-- 施工中 -->
  </tr>
  <tr>
    <td align="center">肉丝</td> 
    <td align="center">聆音</td> 
    <td align="center">TCCF</td> 
    <td align="center">你堡</td>
    <td align="center">冬樱</td>
    <td align="center">52PT</td>
    <td align="center">瓷</td> <!-- 施工中 -->
  </tr>
  <tr>
    <td align="center">伊甸园</td> 
    <td align="center">1PTBA</td> 
    <td align="center">朱雀</td> 
    <td align="center">织梦</td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td> <!-- 施工中 -->
  </tr> 
</table>
<br>

<h1 align="center"> ️:gift_heart: 特别感谢 :gift_heart: </h1>

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars.githubusercontent.com/u/17682201?v=4" width="175px;"/><br /><sub><b>莫与</b></sub>](https://github.com/dongshuyan)  <br /> | [<img src="https://avatars.githubusercontent.com/u/32202634?v=4" width="175px;"/><br /><sub><b>明日</b></sub>](https://github.com/tomorrow505/)<br /> | [<img src="https://avatars.githubusercontent.com/u/53997080?v=4" width="175px;"/><br /><sub><b>大卫</b></sub>](https://github.com/ledccn)<br /> | [<img src="https://avatars.githubusercontent.com/u/103914473?v=4" width="175px;"/><br /><sub><b>贾佬</b></sub>](https://github.com/vertex-app)<br /> | [<img src="https://img.pterclub.com/images/2023/09/29/p11a08.jpg" width="175px;"/><br /><sub><b>shmt86</b></sub>](https://pterclub.com/userdetails.php?id=751)<br /> | 
|:---------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
 








