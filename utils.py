from docx import Document
import datetime

#date_obj = datetime.date.today()
#date_str = date_obj.strftime('%#m月%#d日')  #加#号不补零，去掉#号自动补零
#weekday = date_obj.strftime('%w')

#print(date_str)
#print(weekday)

def get_week_day(date):
    week_day_dict = {
        6: '（周日）',
        0: '（周一）',
        1: '（周二）',
        2: '（周三）',
        3: '（周四）',
        4: '（周五）',
        5: '（周六）',
    }

    day = date.weekday()
    #print(day)
    return week_day_dict[day]

#print("today is " + date_str + get_week_day(date_obj))

def read_zhiban_from_word(file_path):
    zhiban = {}
    doc = Document(file_path)

    for i, table in enumerate(doc.tables):
        #print(f"Tables {i}:")
        
        for row in table.rows:
            if row.cells[0].text == "日 期":
                continue
            #for cell in row.cells:
            #    print(cell.text, end="  |")
           # print(type(row.cells[0].text))
            daliy = row.cells[0].text.strip() #去掉字符串中的空格
            #print("日（" in daliy)
            zhiban[daliy] = row.cells[1].text
            #print("")

        #print(zhiban)
        return zhiban

zb = read_zhiban_from_word("D:\\test.docx")

#获取当前日期+星期
def get_today():
    date_obj = datetime.date.today()
    date_str = date_obj.strftime('%#m月%#d日')  #加#号不补零，去掉#号自动补零 对于Linux 需要在字段类型前加上 -
    #weekday = date_obj.strftime('%w')
    today = date_str + get_week_day(date_obj)
    print(today)
    return today

#获取值班部门
def get_dp():
    zb = read_zhiban_from_word("D:\\test.docx")
    print(zb)
    dp = zb.get(get_today(), "综合办公室")  #若值班表里不存在就返回综合办公室
    return dp

print(get_dp())



