#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tencent_finance import query
from .feed import DataFeed
from .info import InfoPack
from .bundle import Bundle


class Share(object):
    '''
    Class that represents a share

    '''

    @classmethod
    def from_sec_code(cls, sec_code):
        '''
        Create a new Share instance.
        :param sec_code:
        :return: Share
        '''
        exchange = query.query_exchange(sec_code)
        return cls([Bundle(sec_code, exchange)])

    @classmethod
    def from_pinyin(cls, pinyin):
        '''

        :param pinyin: Full
        :return:
        '''
        result = query.query_all(pinyin)
        bundles = []
        for ch in result:
            if ch.pinyin == pinyin:
                bundles.append(Bundle(ch.sec_code, ch.exchange))
        return cls(bundles)

    def __init__(self, bundles):
        '''
        Initialize a new Share instance.
        :param sec_code:
        '''
        self.bundles = bundles
        self.data_feed = DataFeed(bundles)
        self.basic_info = InfoPack()
        self.extend_info = InfoPack()
        self.refresh()

    def refresh(self):
        self.data_feed.basic_info(self.basic_info)
        self.data_feed.extend_info(self.extend_info)

    # Common PART

    @property
    def sec_code(self):
        code = []
        for item in self.bundles:
            code.append(item.sec_code)
        return code

    @property
    def exchange(self):
        name = []
        for item in self.bundles:
            name.append(item.exchange)
        return name

    # SZ PART

    @property
    def sz_ssdq(self):
        '''
        所属地区
        '''
        return self.basic_info.sz.ssdq

    @property
    def sz_sssj(self):
        '''
        上市时间
        '''
        return self.basic_info.sz.sssj

    @property
    def sz_mgxjl(self):
        '''
        每股现金流(元)
        '''
        return self.basic_info.sz.mgxjl

    @property
    def sz_jlrzzl(self):
        '''
        净利润增长率(%)
        '''
        return self.basic_info.sz.jlrzzl

    @property
    def sz_zgb(self):
        '''
        总股本(亿)
        '''
        return self.basic_info.sz.zgb

    @property
    def sz_ltga(self):
        '''
        流通A股(亿)
        '''
        return self.basic_info.sz.ltga

    @property
    def sz_mggjj(self):
        '''
        每股公积金(元)
        '''
        return self.basic_info.sz.mggjj

    @property
    def sz_mgwfplr(self):
        '''
        每股未分配利润
        '''
        return self.basic_info.sz.mgwfplr

    @property
    def sz_mgsy(self):
        '''
        每股收益(元)
        '''
        return self.basic_info.sz.mgsy

    @property
    def sz_mgjzc(self):
        '''
        每股净资产(元)
        '''
        return self.basic_info.sz.mgjzc

    @property
    def sz_jzcsyl(self):
        '''
        净资产收益率(%)
        '''
        return self.basic_info.sz.jzcsyl

    @property
    def sz_zysrzzl(self):
        '''
        主营收入增长率(%)
        '''
        return self.basic_info.sz.zysrzzl


    # SH PART

    @property
    def sh_ssdq(self):
        '''
        所属地区
        '''
        return self.basic_info.sh.ssdq

    @property
    def sh_sssj(self):
        '''
        上市时间
        '''
        return self.basic_info.sh.sssj

    @property
    def sh_mgxjl(self):
        '''
        每股现金流(元)
        '''
        return self.basic_info.sh.mgxjl

    @property
    def sh_jlrzzl(self):
        '''
        净利润增长率(%)
        '''
        return self.basic_info.sh.jlrzzl

    @property
    def sh_zgb(self):
        '''
        总股本(亿)
        '''
        return self.basic_info.sh.zgb

    @property
    def sh_ltga(self):
        '''
        流通A股(亿)
        '''
        return self.basic_info.sh.ltga

    @property
    def sh_mggjj(self):
        '''
        每股公积金(元)
        '''
        return self.basic_info.sh.mggjj

    @property
    def sh_mgwfplr(self):
        '''
        每股未分配利润
        '''
        return self.basic_info.sh.mgwfplr

    @property
    def sh_mgsy(self):
        '''
        每股收益(元)
        '''
        return self.basic_info.sh.mgsy

    @property
    def sh_mgjzc(self):
        '''
        每股净资产(元)
        '''
        return self.basic_info.sh.mgjzc

    @property
    def sh_jzcsyl(self):
        '''
        净资产收益率(%)
        '''
        return self.basic_info.sh.jzcsyl

    @property
    def sh_zysrzzl(self):
        '''
        主营收入增长率(%)
        '''
        return self.basic_info.sh.zysrzzl

    # HK PART

    @property
    def cmp_name_cn(self):
        return self.basic_info.hk.CMP_NAME_CN

    @property
    def master_hareholder(self):
        return self.basic_info.hk.MASTER_HAREHOLDER

    @property
    def chairman(self):
        return self.basic_info.hk.CHAIRMAN

    @property
    def activities(self):
        return self.basic_info.hk.ACTIVITIES

    @property
    def website(self):
        return self.basic_info.hk.WEBSITE

    @property
    def listing_date(self):
        return self.basic_info.hk.LISTING_DATE

    @property
    def unit(self):
        return self.basic_info.hk.UNIT

    @property
    def stock_sum(self):
        return self.basic_info.hk.STOCK_SUM

    @property
    def hk_stock_sum(self):
        return self.basic_info.hk.HK_STOCK_SUM

    @property
    def directors(self):
        return self.basic_info.hk.DIRECTORS

    @property
    def secretary(self):
        return self.basic_info.hk.SECRETARY

    @property
    def reg_office(self):
        return self.basic_info.hk.REG_OFFICE

    @property
    def head_office(self):
        return self.basic_info.hk.HEAD_OFFICE

    @property
    def stk_cede_registry(self):
        return self.basic_info.hk.STK_CEDE_REGISTRY

    @property
    def auditors(self):
        return self.basic_info.hk.AUDITORS

    @property
    def bankers(self):
        return self.basic_info.hk.BANKERS

    @property
    def ladvisors(self):
        return self.basic_info.hk.LADVISORS

    @property
    def tel(self):
        return self.basic_info.hk.TEL

    @property
    def fax(self):
        return self.basic_info.hk.FAX

    @property
    def email(self):
        return self.basic_info.hk.EMAIL

    @property
    def sector_name(self):
        return self.basic_info.hk.SECTOR_NAME

    @property
    def tclose(self):
        return self.basic_info.hk.TCLOSE

    @property
    def zxbjdw(self):
        return self.basic_info.hk.ZXBJDW

    @property
    def website_url(self):
        return self.basic_info.hk.WEBSITE_URL
