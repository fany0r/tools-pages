#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import sys, os
from datetime import datetime, timedelta, date
from typing import Union, Optional
from pyscript import document

VERSION_DATE: dict[str, date] = {
    '10.x': date(2019, 12, 8),
    '11.x': date(2020, 10, 1),
    '12.x': date(2021, 9, 18),
    '13.x': date(2022, 9, 8),
    '14.x': date(2023, 7, 31),
    '15.x': date(2024, 8, 1)
}
CHECK_DATE = datetime(2019, 12, 7)

TABLE = [0x39cb44b8, 0x23754f67, 0x5f017211, 0x3ebb24da, 0x351707c6, 0x63f9774b, 0x17827288, 0x0fe74821,
         0x5b5f670f, 0x48315ae8, 0x785b7769, 0x2b7a1547, 0x38d11292, 0x42a11b32, 0x35332244, 0x77437b60,
         0x1eab3b10, 0x53810000, 0x1d0212ae, 0x6f0377a8, 0x43c03092, 0x2d3c0a8e, 0x62950cbf, 0x30f06ffa,
         0x34f710e0, 0x28f417fb, 0x350d2f95, 0x5a361d5a, 0x15cc060b, 0x0afd13cc, 0x28603bcf, 0x3371066b,
         0x30cd14e4, 0x175d3a67, 0x6dd66a13, 0x2d3409f9, 0x581e7b82, 0x76526b99, 0x5c8d5188, 0x2c857971,
         0x15f51fc0, 0x68cc0d11, 0x49f55e5c, 0x275e4364, 0x2d1e0dbc, 0x4cee7ce3, 0x32555840, 0x112e2e08,
         0x6978065a, 0x72921406, 0x314578e7, 0x175621b7, 0x40771dbf, 0x3fc238d6, 0x4a31128a, 0x2dad036e,
         0x41a069d6, 0x25400192, 0x00dd4667, 0x6afc1f4f, 0x571040ce, 0x62fe66df, 0x41db4b3e, 0x3582231f,
         0x55f6079a, 0x1ca70644, 0x1b1643d2, 0x3f7228c9, 0x5f141070, 0x3e1474ab, 0x444b256e, 0x537050d9,
         0x0f42094b, 0x2fd820e6, 0x778b2e5e, 0x71176d02, 0x7fea7a69, 0x5bb54628, 0x19ba6c71, 0x39763a99,
         0x178d54cd, 0x01246e88, 0x3313537e, 0x2b8e2d17, 0x2a3d10be, 0x59d10582, 0x37a163db, 0x30d6489a,
         0x6a215c46, 0x0e1c7a76, 0x1fc760e7, 0x79b80c65, 0x27f459b4, 0x799a7326, 0x50ba1782, 0x2a116d5c,
         0x63866e1b, 0x3f920e3c, 0x55023490, 0x55b56089, 0x2c391fd1, 0x2f8035c2, 0x64fd2b7a, 0x4ce8759a,
         0x518504f0, 0x799501a8, 0x3f5b2cad, 0x38e60160, 0x637641d8, 0x33352a42, 0x51a22c19, 0x085c5851,
         0x032917ab, 0x2b770ac7, 0x30ac77b3, 0x2bec1907, 0x035202d0, 0x0fa933d3, 0x61255df3, 0x22ad06bf,
         0x58b86971, 0x5fca0de5, 0x700d6456, 0x56a973db, 0x5ab759fd, 0x330e0be2, 0x5b3c0ddd, 0x495d3c60,
         0x53bd59a6, 0x4c5e6d91, 0x49d9318d, 0x103d5079, 0x61ce42e3, 0x7ed5121d, 0x14e160ed, 0x212d4ef2,
         0x270133f0, 0x62435a96, 0x1fa75e8b, 0x6f092fbe, 0x4a000d49, 0x57ae1c70, 0x004e2477, 0x561e7e72,
         0x468c0033, 0x5dcc2402, 0x78507ac6, 0x58af24c7, 0x0df62d34, 0x358a4708, 0x3cfb1e11, 0x2b71451c,
         0x77a75295, 0x56890721, 0x0fef75f3, 0x120f24f1, 0x01990ae7, 0x339c4452, 0x27a15b8e, 0x0ba7276d,
         0x60dc1b7b, 0x4f4b7f82, 0x67db7007, 0x4f4a57d9, 0x621252e8, 0x20532cfc, 0x6a390306, 0x18800423,
         0x19f3778a, 0x462316f0, 0x56ae0937, 0x43c2675c, 0x65ca45fd, 0x0d604ff2, 0x0bfd22cb, 0x3afe643b,
         0x3bf67fa6, 0x44623579, 0x184031f8, 0x32174f97, 0x4c6a092a, 0x5fb50261, 0x01650174, 0x33634af1,
         0x712d18f4, 0x6e997169, 0x5dab7afe, 0x7c2b2ee8, 0x6edb75b4, 0x5f836fb6, 0x3c2a6dd6, 0x292d05c2,
         0x052244db, 0x149a5f4f, 0x5d486540, 0x331d15ea, 0x4f456920, 0x483a699f, 0x3b450f05, 0x3b207c6c,
         0x749d70fe, 0x417461f6, 0x62b031f1, 0x2750577b, 0x29131533, 0x588c3808, 0x1aef3456, 0x0f3c00ec,
         0x7da74742, 0x4b797a6c, 0x5ebb3287, 0x786558b8, 0x00ed4ff2, 0x6269691e, 0x24a2255f, 0x62c11f7e,
         0x2f8a7dcd, 0x643b17fe, 0x778318b8, 0x253b60fe, 0x34bb63a3, 0x5b03214f, 0x5f1571f4, 0x1a316e9f,
         0x7acf2704, 0x28896838, 0x18614677, 0x1bf569eb, 0x0ba85ec9, 0x6aca6b46, 0x1e43422a, 0x514d5f0e,
         0x413e018c, 0x307626e9, 0x01ed1dfa, 0x49f46f5a, 0x461b642b, 0x7d7007f2, 0x13652657, 0x6b160bc5,
         0x65e04849, 0x1f526e1c, 0x5a0251b6, 0x2bd73f69, 0x2dbf7acd, 0x51e63e80, 0x5cf2670f, 0x21cd0a03,
         0x5cff0261, 0x33ae061e, 0x3bb6345f, 0x5d814a75, 0x257b5df4, 0x0a5c2c5b, 0x16a45527, 0x16f23945
         ]


# Keygen functions from keygen.py
TIME_VAL = []
COUNT_VAL = []

def diff_date(cur_date, date_format="%Y-%m-%d") -> int:
    cur_date_obj = datetime.strptime(cur_date, date_format)
    date_diff = cur_date_obj - CHECK_DATE
    return date_diff.days


def get_random_expire_time(days_num: int, is_max=False) -> (int, int):
    if len(TIME_VAL) == 0:
        for i in range(0x473C * 0x11, 0x00FFFFFF, 0x11):
            if i % 0x11 == 0:
                TIME_VAL.append(i)

    if days_num == 0:
        if is_max:
            val_0 = TIME_VAL[-1]
        else:
            days_num = 5 * 365 + int(random.random() * 30)
            val_0 = TIME_VAL[days_num]
    else:
        days_num = len(TIME_VAL) if days_num > len(TIME_VAL) else days_num
        val_0 = TIME_VAL[days_num]
    val_1 = (((val_0 ^ 0xffe53167) + 180597) ^ 0x22c078 ^ 0x5b8c27) & 0xffffff
    return val_0, val_1


def get_random_user_count(user_num=0, is_max=False) -> (int, int):
    if len(COUNT_VAL) == 0:
        for i in range(0xB, 0x3E8 * 0xB, 0xB):
            if i % 0xB == 0:
                COUNT_VAL.append(i)

    if user_num == 0:
        if is_max:
            val_0 = 0x3E8 * 0xB
        else:
            val_0 = random.choices(population=COUNT_VAL, k=1)[0]
    else:
        user_num = 0x3E8 if user_num > 0x3E8 else user_num
        val_0 = user_num * 0xB
    val_1 = ((val_0 ^ 0x3421) - 19760) ^ 0x7892
    return val_0, val_1


def get_calc_value(username: str, days_idx: int, user_idx: int) -> int:
    ret = 0
    cnt_idx = (15 * user_idx) & 0xff
    time_idx = (17 * days_idx) & 0xff
    cal_idx = 0
    for ch in username:
        val = ord(ch.upper())
        ret = TABLE[cnt_idx] + TABLE[time_idx] + TABLE[cal_idx] + TABLE[val + 47] * (
                (ret + TABLE[val]) ^ TABLE[val + 13])
        cnt_idx = (cnt_idx + 13) & 0xff
        time_idx = (time_idx + 9) & 0xff
        cal_idx = (cal_idx + 19) & 0xff
    return ret


def get_password_from_username(username: str, user_cnt=0, max_user=False, days_cnt=0, max_days=False) -> str:
    buff: list[Union[int, str]] = [0] * 10
    days_val0, days_val1 = get_random_expire_time(days_num=days_cnt, is_max=max_days)
    user_val0, user_val1 = get_random_user_count(user_num=user_cnt, is_max=max_user)

    val = get_calc_value(username, days_val0 // 0x11, user_val0 // 0xB)
    for idx in range(4):
        buff[4 + idx] = (val >> (idx * 8)) & 0xff
    buff[3] = 0xac
    buff[2] = (user_val1 & 0xff) ^ buff[5]
    buff[1] = ((user_val1 >> 8) & 0xff) ^ buff[7]
    buff[0] = (days_val1 & 0xff) ^ buff[6]
    buff[8] = ((days_val1 >> 8) & 0xff) ^ buff[4]
    buff[9] = ((days_val1 >> 16) & 0xff) ^ buff[5]

    for idx in range(10):
        if buff[idx] < 0:
            buff[idx] &= 0xff
        buff[idx] = hex(buff[idx])[2:].zfill(2)
    password = "%s%s-%s%s-%s%s-%s%s-%s%s" % (buff[0], buff[1], buff[2], buff[3], buff[4], buff[5], buff[6], buff[7], buff[8], buff[9])
    expire_date = CHECK_DATE + timedelta(days=TIME_VAL.index(days_val0))

    info = (
        f"用户名: {username}\n"
        f"激活码: {password}\n"
        f"可激活用户数: {user_val0 // 0xB}\n"
        f"到期时间为: {expire_date.strftime('%Y-%m-%d')}\n"
        f"剩余天数为: {(expire_date - datetime.now()).days} 天\n"
        "\nTips：激活前需要禁止 010Editor 访问网络，可通过防火墙或 hosts 实现。\n"
    )
    # print(info)
    return [password, info]

def generate(event):
    sys.stderr = open(os.devnull, 'w')

    input_text = document.querySelector("#username")
    username = input_text.value
    prefer_user = 996
    preferDaysInput = document.querySelector("#prefer_days")
    date_text = preferDaysInput.value

    try:
        prefer_days = diff_date(date_text)
    except Exception as e:
        prefer_days = diff_date("2029-12-31")
    finally:
        sys.stderr = sys.__stderr__

    # display key on web page
    result = get_password_from_username(username=username, user_cnt=prefer_user, days_cnt=prefer_days)
    serial_div = document.querySelector("#show-serial")
    serial_div.value = result[0]
    info_div = document.querySelector("#info")
    info_div.innerText = result[1]

