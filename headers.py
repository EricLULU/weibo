import random

class Headers(object):
    def headers(self):  
        """
            随机的headers， 每个headers使用十分钟，使用的过程中，每次爬取间隔20秒
        """ 
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'DNT':'1',
            'Host':'weibo.com',
            'Cookie':'SINAGLOBAL=7546083704663.263.1533686587069; wb_view_log=1366*7681; wb_view_log_6675576190=1366*7681; un=18506218669; wb_view_log_6673953302=1366*7681; wvr=6; wb_view_log_5066651816=1366*7681; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; ALF=1567430043; SSOLoginState=1535894043; SCF=ApwoSBtKEZHC324-bFq03YPeveOxk1cmYQhIfB_0-EY69oGQGOObuMiE9pe4OUOOHYgRX2ylFS8_Vqv0f0bY3_8.; SUB=_2A252j5JMDeRhGeNO7VQX9S_EyjqIHXVV_ISErDV8PUNbmtBeLVLckW9NTvWs2kdOPukk46TWgO4rcUXcyMTTx4IR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh18_F-DxOVlVe_5lRnNJ-45JpX5KzhUgL.Fo-7SoqcSK2ReKq2dJLoIEXLxKqL122L122LxK.L1h-L1KzLxK-L1hqLB.zLxKqLBKzLBKnLxKBLBonL12zt; SUHB=0YhRte-ukssW68; YF-V5-G0=731b77772529a1f49eac82a9d2c2957f; _s_tentry=login.sina.com.cn; UOR=,,www.so.com; Apache=8712577896076.59.1535894083395; ULV=1535894083461:2:2:2:8712577896076.59.1535894083395:1535891238993; YF-Page-G0=e44a6a701dd9c412116754ca0e3c82c3',
            'Referer':'http://www.so.com/link?url=http%3A%2F%2Fweibo.com%2Fu%2F1537790411%3Fc%3Dspr_qdhz_bd_360ss_weibo_mr&q=%E5%BE%AE%E5%8D%9A%E9%B9%BF%E6%99%97&ts=1535791329&t=0b023c685d837dd001e2973b9f82e8a',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            }

        cookies = [
                   'SINAGLOBAL=7546083704663.263.1533686587069; un=13125822181; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; login_sid_t=30fb275fca9a1cf521a93a7aa763f7b0; cross_origin_proto=SSL; YF-V5-G0=4955da6a9f369238c2a1bc4f70789871; _s_tentry=passport.weibo.com; UOR=,,www.so.com; wb_view_log=1366*7681; Apache=3228720525188.3887.1535964982917; ULV=1535964982928:4:4:4:3228720525188.3887.1535964982917:1535894561586; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW33jPF.unkph-acaIUB1ZP5JpX5K2hUgL.FoqcS0-fS0qp1K52dJLoI0YLxK.LB.zL1K2LxK-LBo2LBo2LxKnL1h5L1h2LxK-LBKqL1KqLxKML1hnLBo2LxK.LB.zL1K2LxK-LBo2LBo2t; ALF=1567500957; SSOLoginState=1535964958; SCF=ApwoSBtKEZHC324-bFq03YPeveOxk1cmYQhIfB_0-EY67e02gO1-vorJSwMyFj_bJwnvo__G66xEAIl7xFufpsk.; SUB=_2A252iIdODeRhGeBI7FcU9yjNwjyIHXVV__-GrDV8PUNbmtBeLW39kW9NRmEzZULKhUXa_hR1XtmV7c8oqM1q_hd7; SUHB=0d4-a3FZ_brl7o; wvr=6; YF-Page-G0=19f6802eb103b391998cb31325aed3bc; wb_view_log_6675576190=1366*7681; WBtopGlobal_register_version=9744cb1b8d390b27',
                   #'SINAGLOBAL=7546083704663.263.1533686587069; wb_view_log=1366*7681; wb_view_log_6675576190=1366*7681; un=18506218669; wb_view_log_6673953302=1366*7681; wb_view_log_5066651816=1366*7681; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; YF-V5-G0=731b77772529a1f49eac82a9d2c2957f; _s_tentry=login.sina.com.cn; Apache=8712577896076.59.1535894083395; ULV=1535894083461:2:2:2:8712577896076.59.1535894083395:1535891238993; YF-Page-G0=e44a6a701dd9c412116754ca0e3c82c3; login_sid_t=c8064e334483c3e77a0e52eb089bb1f7; cross_origin_proto=SSL; WBStorage=e8781eb7dee3fd7f|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhH2Qi1_mo63.krwW7Q9-gH5JpX5K2hUgL.FoqcS0e4SKe0ehz2dJLoIEXLxKqLBoeLBo5LxK-LBo2LBo2LxKnLBoqL1h-LxK-L12eL1KMLxKqLBo-LBoMt; ALF=1567430151; SSOLoginState=1535894152; SCF=ApwoSBtKEZHC324-bFq03YPeveOxk1cmYQhIfB_0-EY6m59_6NlwNwmFu3qzYFOCr_EzVSkg0CfcXTAohM2xrFg.; SUB=_2A252j5LYDeRhGeBI7FEY9S3Pyz6IHXVV_IMQrDV8PUNbmtBeLWSnkW9NRmFsPA6HzKVZGuaYIFYjgqtS89rQYQtN; SUHB=0IIVLwO38hwSwM; wvr=6; WBtopGlobal_register_version=9744cb1b8d390b27',
                   #'SINAGLOBAL=7546083704663.263.1533686587069; wb_view_log=1366*7681; wb_view_log_6675576190=1366*7681; un=18506218669; wb_view_log_6673953302=1366*7681; wvr=6; wb_view_log_5066651816=1366*7681; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; ALF=1567430043; SSOLoginState=1535894043; SCF=ApwoSBtKEZHC324-bFq03YPeveOxk1cmYQhIfB_0-EY69oGQGOObuMiE9pe4OUOOHYgRX2ylFS8_Vqv0f0bY3_8.; SUB=_2A252j5JMDeRhGeNO7VQX9S_EyjqIHXVV_ISErDV8PUNbmtBeLVLckW9NTvWs2kdOPukk46TWgO4rcUXcyMTTx4IR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh18_F-DxOVlVe_5lRnNJ-45JpX5KzhUgL.Fo-7SoqcSK2ReKq2dJLoIEXLxKqL122L122LxK.L1h-L1KzLxK-L1hqLB.zLxKqLBKzLBKnLxKBLBonL12zt; SUHB=0YhRte-ukssW68; YF-V5-G0=731b77772529a1f49eac82a9d2c2957f; _s_tentry=login.sina.com.cn; UOR=,,www.so.com; Apache=8712577896076.59.1535894083395; ULV=1535894083461:2:2:2:8712577896076.59.1535894083395:1535891238993; YF-Page-G0=e44a6a701dd9c412116754ca0e3c82c3'
                   ]
                #qq
                #185
                #131
                #131_1
                #185_1
                #qq_1
        cookie = random.choice(cookies)
        headers['Cookie'] = cookie 
        #print(headers)
        return headers    #返回headers