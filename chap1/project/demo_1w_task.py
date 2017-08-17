'''
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档
输入指令，退出程序的交互
在退出程序之前，打印查询过的所有城市。
'''

def weather_dict_change():
    with open("weather_info.txt") as f:
        weather_dict = {}
        for line in f:
            weather_dict[line.split(",")[0]] = line.strip('\n').split(",")[1]

    #print (weather_dict)

    return weather_dict

def main():
    weather_dict = weather_dict_change()
    record = {}
    cmd = input("请输入城市名或指令:")
    while cmd != "quit":
        if cmd in weather_dict:
            print("%s天气状况的天气状况为:%s"%(cmd,weather_dict[cmd]))
            record[cmd] = weather_dict[cmd]
        elif cmd == "history":
            for city,weather in record.items():
                print(city,weather)
        elif cmd == "help":
            print("\n输入城市名，查询该城市的天气；\n")
            print("输入help，获取帮助文档；\n")
            print("输入history，获取查询历史；\n")
            print("输入quit，退出天气查询系统。\n")
        else:
            print("输入命令无效")
    
        cmd = input("请输入城市名或指令:")

if __name__ == '__main__':
    main()


    






