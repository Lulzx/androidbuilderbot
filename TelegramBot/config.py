#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import telebot
from telebot import types
import pymongo
import datetime


token = '410552084:AAETG-SNNAPM6JPOrmGP7mEN2e-rdn9kbTQ'

bot = telebot.TeleBot(token)

client = pymongo.MongoClient()
db = client.hackabase
users = db.users

hideBoard = telebot.types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

pattern = "(https?\:\/\/)?github\.com[\w\/]+"

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
main_menu.add('Мои репозитории')
main_menu.row('Добавить репозиторий')
