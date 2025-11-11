# 星期列表，0表示星期一，6表示星期日
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 各个月份天数（不考虑闰年）
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 用户输入今天的日期
year = int(input("请输入今年年份（例如2025）："))
month = int(input("请输入今天月份（1-12）："))
day = int(input("请输入今天日期（1-31）："))

# 用户输入今天是星期几
print("星期输入方式：星期一=0, 星期二=1, ... 星期日=6")
today_week_index = int(input("请输入今天星期的索引（0-6）："))

# 用户输入过几天
days_to_add = int(input("请输入要过几天："))

# 保存原始天数，用于计算星期几
original_days_to_add = days_to_add

# 计算过几天天后的日期
while days_to_add > 0:
    remaining_days_in_month = month_days[month - 1] - day
    if days_to_add > remaining_days_in_month:
        days_to_add -= (remaining_days_in_month + 1)
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    else:
        day += days_to_add
        days_to_add = 0

# 计算未来星期几
future_week_index = (today_week_index + original_days_to_add) % 7

# 输出结果
print(f"{original_days_to_add}天后的日期是：{year}年{month}月{day}日")
print(f"{original_days_to_add}天后的星期是：{weekdays[future_week_index]}")
