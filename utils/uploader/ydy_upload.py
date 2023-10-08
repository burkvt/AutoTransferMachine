from loguru import logger
import time
import os
from utils.uploader.upload_tools import *
import re
import cloudscraper

def ydy_upload(siteinfo,file1,record_path,qbinfo,basic,hashlist):
    url = siteinfo.url
    post_url = f"{url}takeupload.php"
    tags=[]
    time_out=40
    if (file1.pathinfo.type=='anime' or file1.pathinfo.type=='tv') and file1.pathinfo.collection==0:
        fileinfo=file1.chinesename+'在'+siteinfo.sitename+'第'+file1.episodename+'集'
    else:
        fileinfo=file1.chinesename+'在'+siteinfo.sitename


    #选择类型
    if 'anime' in file1.pathinfo.type.lower():
        select_type='422'
        logger.info('已成功填写类型为其他')
    elif 'show' in file1.pathinfo.type.lower():
        select_type='422'
        logger.info('已成功填写类型为其他')                
    elif 'tv' in file1.pathinfo.type.lower() and "BLU" in file1.type.upper():
        select_type='424'
        logger.info('已成功填写类型为剧集BLURAY')          
    elif 'tv' in file1.pathinfo.type.lower():
        select_type='421'
        logger.info('已成功填写类型为剧集HD')                   
    elif 'movie' in file1.pathinfo.type.lower() and "BLU" in file1.type.upper():
        select_type='420'
        logger.info('已成功填写类型为电影BLURAY')          
    elif 'tv' in file1.pathinfo.type.lower():
        select_type='423'
        logger.info('已成功填写类型为电影HD')                  
    else:
        select_type='422'
        logger.info('已成功填写类型为其它')    

    #选择来源
    if 'WEB' in file1.source.upper():
        source_sel='5'
        logger.info('已成功选择来源为WEB-DL')     
    elif 'UHD' in file1.source.upper():
        source_sel='1'
        logger.info('已成功选择来源为UHD-BLURAY')        
    elif 'BLU' in file1.source.upper():
        source_sel='2'
        logger.info('已成功选择来源为BLURAY')         
    elif 'ENCODE' in file1.source.upper():
        source_sel='7'
        logger.info('已成功选择来源为ENCODE')         
    elif 'HDTV' in file1.source.upper():
        source_sel='3'
        logger.info('已成功选择来源为HDTV')         
    elif 'DVD' in file1.source.upper():
        source_sel='4'
        logger.info('已成功选择来源为DVD')         
    else:
        source_sel='8'
        logger.info('已成功选择来源为其它') 
      
        





    #选择媒介
    if 'WEB' in file1.type.upper():
        medium_sel='0'
        logger.info('已成功选择媒介为WEB-DL')           
    elif 'UHD' in file1.type.upper():
        medium_sel='1'
        logger.info('已成功选择媒介为UHD-BLURAY')        
    elif 'BLU' in file1.type.upper():
        medium_sel='2'
        logger.info('已成功选择媒介为BLURAY')         
    elif 'ENCODE' in file1.type.upper():
        medium_sel='4'
        logger.info('已成功选择媒介为ENCODE')        
    elif 'HDTV' in file1.type.upper():
        medium_sel='5'
        logger.info('已成功选择媒介为HDTV')         
    else:
        medium_sel='0'
        logger.info('未识别到媒介信息，不选择媒介')


    #选择编码
    if 'H' in file1.Video_Format.upper() and '264' in file1.Video_Format:
        codec_sel='1'
        logger.info('已成功选择编码为H264/AVC')
    elif 'x' in file1.Video_Format.lower() and '264' in file1.Video_Format:
        codec_sel='1'
        logger.info('已成功选择编码为H264/AVC')     
    elif 'AVC' in file1.Video_Format:
        codec_sel='1'
        logger.info('已成功选择编码为H264/AVC')                
    elif 'H' in file1.Video_Format.upper() and '265' in file1.Video_Format:
        codec_sel='5'
        logger.info('已成功选择编码为H265/HEVC')
    elif 'x' in file1.Video_Format.lower() and '265' in file1.Video_Format:
        codec_sel='5'
        logger.info('已成功选择编码为H265/HEVC')    
    elif 'HEVC' in file1.Video_Format.upper():
        codec_sel='5'
        logger.info('已成功选择编码为H265/HEVC')                
    elif 'MPEG-2' in file1.Video_Format.upper():
        codec_sel='4'
        logger.info('已成功选择编码为MPEG-2') 
    elif 'MPEG-4' in file1.Video_Format.upper():
        codec_sel='4'
        logger.info('已成功选择编码为MPEG-4')               
    elif 'VC' in file1.Video_Format.upper():
        codec_sel='2'
        logger.info('已成功选择编码为VC1')  
    elif 'XVID' in file1.Video_Format.upper():
        codec_sel='3'
        logger.info('已成功选择编码为XVID')
    elif 'AV' in file1.Video_Format.upper():
        codec_sel='5'
        logger.info('已成功选择编码为AV1')                     
    else:
        codec_sel='5'
        logger.info('未识别到视频编码信息，不选择')  

#选择音频编码
    if file1.Audio_Format.upper()=='AAC':
        audiocodec_sel='6'
    elif 'DTS-HD' in file1.Audio_Format.upper() and 'MA' in file1.Audio_Format.upper():
        audiocodec_sel='9'
    elif 'DTS-HD' in file1.Audio_Format.upper() and 'HR' in file1.Audio_Format.upper():
        audiocodec_sel='1'
    elif 'DTS-HD' in file1.Audio_Format.upper() and 'X' in file1.Audio_Format.upper():
        audiocodec_sel='1'
    elif 'DTS' in file1.Audio_Format.upper():
        audiocodec_sel='1'
    elif 'AutoTransferMachineOS' in file1.Audio_Format.upper():
        audiocodec_sel='10'
    elif 'TRUE' in file1.Audio_Format.upper():
        audiocodec_sel='8'
    elif 'EAC3' in file1.Audio_Format.upper() or 'EAC-3' in file1.Audio_Format.upper() or 'DDP' in file1.Audio_Format.upper():
        audiocodec_sel='5'
    elif 'AC3' in file1.Audio_Format.upper() or 'AC-3' in file1.Audio_Format.upper():
        audiocodec_sel='5'
    elif 'DD' in file1.Audio_Format.upper():
        audiocodec_sel='5'
    elif 'PCM' in file1.Audio_Format.upper():
        audiocodec_sel='0'
    elif 'FLAC' in file1.Audio_Format.upper():
        audiocodec_sel='2'
    elif 'APE' in file1.Audio_Format.upper():
        audiocodec_sel='4'
    elif 'MP3' in file1.Audio_Format.upper():
        audiocodec_sel='0'
    elif 'WAV' in file1.Audio_Format.upper():
        audiocodec_sel='3'
    else:
        audiocodec_sel='0'
    logger.info('已成功选择音频编码为'+file1.Audio_Format.upper())

    #选择分辨率
    if '2160' in file1.standard_sel or '4K' in file1.standard_sel.upper():
        standard_sel='4'
    elif '1080p' in file1.standard_sel.lower():
        standard_sel='1'
    elif '1080i' in file1.standard_sel.lower():
        standard_sel='2'
    elif '2K' in file1.standard_sel.upper():
        standard_sel='3'
    else:
        standard_sel='1'
    logger.info('已成功选择分辨率为'+file1.standard_sel)





    #选择制作组
    team_sel='9'    
    logger.info('制作组已成功选择为Other')



    
    if siteinfo.uplver==1:
        uplver='yes'
    else:
        uplver='no'

    torrent_file = file1.torrentpath
    file_tup = ("file", (os.path.basename(torrent_file), open(torrent_file, 'rb'), 'application/x-bittorrent')),
            

    other_data = {
            "name": file1.uploadname,
            "small_descr": file1.small_descr+file1.pathinfo.exinfo,
            "url": file1.imdburl,
            "nfo": "",
            "color": "0",
            "font": "0",
            "size": "0",
            "descr": file1.content,
            "type": select_type,
            "medium_sel": medium_sel,
            "standard_sel": standard_sel,
            "codec_sel": codec_sel,
            "audiocodec_sel": audiocodec_sel,
            "team_sel": team_sel,
            "uplver": uplver,
            }

    scraper=cloudscraper.create_scraper()
    success_upload=0
    try_upload=0
    while success_upload==0:
        try_upload+=1
        if try_upload>5:
            return False,fileinfo+' 发布种子发生请求错误,请确认站点是否正常运行'
        logger.info('正在发布种子')
        try:
            r = scraper.post(post_url, cookies=cookies_raw2jar(siteinfo.cookie),data=other_data, files=file_tup,timeout=time_out)
            success_upload=1
        except Exception as r:
            logger.warning('发布种子发生错误: %s' %(r))
            success_upload=0
    
    return afterupload(r,fileinfo,record_path,siteinfo,file1,qbinfo,hashlist)