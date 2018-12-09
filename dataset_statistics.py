# open database
# select semua kalimat
# tambahkan jumlah kata di database

# rata-rata adalah total jumlah kata dibagi jumlah kalimat

# longest sentence adalah ranking jumlah kata terbesar
# shortest sentence adalah ranking jumlah kata terkecil
# deviasi -> cari rumus standar deviasi
# perlu boxplot? plot statistik kata seperti di nltk ?


import sqlite3
import jieba
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

nama_tabel = 'gabungan.db'

def count_word_en():
    sql_tambah_kolom = 'alter table id_zhcn add column word_count_en INTEGER;'

    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    try:
        cur.execute(sql_tambah_kolom)
    except:
        pass

    sql_select = 'select id, text_en_id from id_zhcn where word_count_en is null ;'
    try:
        cur.execute(sql_select)
    except:
        pass

    hasils = cur.fetchall()

    sql_update = 'update id_zhcn set word_count_en = {} where id={} '

    for hasil in hasils:
        tokens = tokenizer.tokenize(hasil[1])
        cur.execute(sql_update.format(len(tokens),hasil[0]))

    conn.commit()


def count_word_id():
    sql_tambah_kolom = 'alter table id_zhcn add column word_count INTEGER;'

    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    try:
        cur.execute(sql_tambah_kolom)
    except:
        pass

    sql_select = 'select id, text_id from id_zhcn where word_count is null ;'
    try:
        cur.execute(sql_select)
    except:
        pass

    hasils = cur.fetchall()

    sql_update = 'update id_zhcn set word_count = {} where id={} '

    for hasil in hasils:
        tokens = tokenizer.tokenize(hasil[1])
        cur.execute(sql_update.format(len(tokens), hasil[0]))

    conn.commit()

def count_word_zhcn():
    sql_tambah_kolom = 'alter table id_zhcn add column word_count_zhcn INTEGER;'

    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    try:
        cur.execute(sql_tambah_kolom)
    except:
        pass

    sql_select = 'select id, text_zhcn from id_zhcn where word_count_zhcn is null ;'
    try:
        cur.execute(sql_select)
    except:
        pass

    hasils = cur.fetchall()

    sql_update = 'update id_zhcn set word_count_zhcn = {} where id={} '

    for hasil in hasils:
        tokens = list(jieba.cut(hasil[1]))
        cur.execute(sql_update.format(len(tokens), hasil[0]))
        # print(tokens)

    conn.commit()

def count_mean_id():
    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    sql_count_indo = 'select count(text_id), sum(word_count), max(word_count), min(word_count) from id_zhcn'
    try:
        cur.execute(sql_count_indo)
    except:
        pass

    hasils = cur.fetchone()
    rerata = hasils[1]/hasils[0]
    print('Indonesian sentences pair = {0}, Average of word count per sentences = {1:.2f}, longest sentences = {2} words, shortest sentences = {3} words'.format(hasils[0],rerata,hasils[2],hasils[3]))

def count_mean_en():
    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    sql_count_indo = 'select count(text_en_id), sum(word_count_en), max(word_count_en), min(word_count_en) from id_zhcn'
    try:
        cur.execute(sql_count_indo)
    except:
        pass

    hasils = cur.fetchone()
    rerata = hasils[1]/hasils[0]
    print('English sentences pair = {0}, Average of word count per sentences = {1:.2f}, longest sentences = {2} words, shortest sentences = {3} words'.format(hasils[0],rerata,hasils[2],hasils[3]))

def count_mean_zhcn():
    conn = sqlite3.connect(nama_tabel)
    cur = conn.cursor()
    sql_count_indo = 'select count(text_zhcn), sum(word_count_zhcn), max(word_count_zhcn), min(word_count_zhcn) from id_zhcn'
    try:
        cur.execute(sql_count_indo)
    except:
        pass

    hasils = cur.fetchone()
    rerata = hasils[1]/hasils[0]
    print('Mandarin sentences pair = {0}, Average of word count per sentences = {1:.2f}, longest sentences = {2} words, shortest sentences = {3} words'.format(hasils[0],rerata,hasils[2],hasils[3]))

if __name__ == '__main__':
    # count_word_zhcn()
    # count_word_en()
    # count_word_id()
    count_mean_id()
    count_mean_en()
    count_mean_zhcn()