import re
import sys
import os
from utils.para_ctrl.para_ctrl import *
from utils.site.site import makesites
from utils.pathinfo.pathinfo import findpathinfo
from utils.seed_machine.seed_machine import start_machine
from utils.seed_machine.seedupload_machine import startupload_machine
from utils.img_upload.imgupload import img_upload
from utils.mediafile.mediafile import *
from utils.mediafile.upload_mediafile import *
import utils.getinfo.torrent_download as td
from utils.getinfo.info_transfer import *
from doubaninfo.doubaninfo import getdoubaninfo

@logger.catch
def main():
    os.system('clear')
    logger.info(f'欢迎使用大胡开发的ATM自动转种机，如果你有意和我一起开发和测试本工具，欢迎你加入ATM研发群870081858')
    yamlinfo=read_para()
    os.chdir(yamlinfo['basic']['screenshot_path'])
    if 'basic' in yamlinfo and 'log' in yamlinfo['basic'] and yamlinfo['basic']['log']!=None:
        log = yamlinfo['basic']['log']
        if os.path.exists(log):
            os.remove(log)
        logger.add(log, level="TRACE", backtrace=True, diagnose=True)

    if yamlinfo['mod']=='img_upload':
        logger.info('正在使用上传图床模式')
        res=img_upload(imgdata=yamlinfo['image hosting'],imglist=yamlinfo['imgfilelist'],host=yamlinfo['img_host'],form=yamlinfo['img_form'])
        logger.info('成功上传图床')
        print(res)

    if yamlinfo['mod'] == 'upload':
        sites = makesites(yamlinfo['site info'])
        # for item in sites:
        #    sites[item].print()

        pathlist = findpathinfo(yamlinfo, sites)
        # for item in pathlist:
        #    item.print()

        startupload_machine(pathlist, sites, yamlinfo)
        write_yaml(yamlinfo)

    if yamlinfo['mod']=='transfer':
        torrentaddress = yamlinfo['basic']['torrent_path']
        sites=makesites(yamlinfo['site info'])
        #for item in sites:
        #    sites[item].print()
        
        pathlist=findpathinfo(yamlinfo,sites)
        #for item in pathlist:
        #    item.print()

        start_machine(pathlist,sites,yamlinfo)
        write_yaml(yamlinfo)

    if yamlinfo['mod']=='douban_info':
        #doubaninfo(yamlinfo['douban_url'])
        if 'doubancookie' in yamlinfo['basic'] and yamlinfo['basic']['doubancookie']:
            getdoubaninfo(url=yamlinfo['douban_url'],cookie=yamlinfo['basic']['doubancookie'])
        else:
            getdoubaninfo(url=yamlinfo['douban_url'])

    if yamlinfo['mod']=='media_img':
        screenshotnum=int(yamlinfo['basic']['picture_num'])
        screenshotaddress=yamlinfo['basic']['screenshot_path']
        takescreenshot(yamlinfo['media_file'],screenshotaddress,screenshotnum)
        imgpaths=[]
        for i in range (screenshotnum):
            imgpaths.append(os.path.join(screenshotaddress,str(i+1)+'.jpg'))
        res=img_upload(imgdata=yamlinfo['image hosting'],imglist=imgpaths,host=yamlinfo['img_host'],form=yamlinfo['img_form'])
        if res=='':
            print(self.chinesename+'上传图床失败')
        else:
            print('成功获得图片链接：\n'+res)

    if yamlinfo['mod']=='download':
        td.get_torrent(yamlinfo)


    if yamlinfo['mod']=='transinfo':
        if yamlinfo['basic']['torrent_list']:
            if "xlsx" in yamlinfo['basic']['torrent_list']:
                getmediainfo(yamlinfo)
            else:
                print('torrent_list的路径不是一个正确的xlsx文件路径，请检查配置文件')

        else:
            print('配置文件中无torrent_list项,请检查配置文件')



if __name__ == '__main__':
    main()