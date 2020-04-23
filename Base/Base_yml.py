import yaml,rootpath,os


# #只获取yml数据，但不作处理
# def get_data(filename):
#     file_path= filepath.path+os.sep+"Data"+os.sep+filename+".yml"
#     with open(file_path,'r') as f:
#        return yaml.load(f)

# 获取一个列表类型的yml数据
def get_yml_with_filename_key(filename, testname):
    #windows路径比较特别，在Jenkins上 只需要 ./Data...  而pychram需要为 ../Data
    filename= rootpath.path+os.sep+"Data"+os.sep+filename+".yml"
    with open(filename, 'r') as f:
        # 将字典第一层即 TestData2数据抽出，此时为 ｛login_test1：｛name1:xxxx,password1:xxx｝，login_test2：｛name1:xxxx,password1:xxx｝｝
        data = yaml.load(f)[testname]
    case_list = []
    # data.values()获取 login_test1,login_test2键对应的值 ｛name1:xxxx,password1:xxx｝ 和｛name1:xxxx,password1:xxx｝，
    # 再将这些类型为字典的键值转入列表，最后返回，在用例paratrimeze方法 直接使用这个列表
    for case_data in data.values():
        case_list.append(case_data)
    return case_list

#这种路径获取方式，pycharm和 命令窗都不一样，只能命令窗可以执行
# def get_yml_with_filename_key(filename, testname):
#     with open("./Data/"+filename+".yml", 'r') as f:
#         # 将字典第一层即 TestData2数据抽出，此时为 ｛login_test1：｛name1:xxxx,password1:xxx｝，login_test2：｛name1:xxxx,password1:xxx｝｝
#         data = yaml.load(f)[testname]
#     case_list = []
#     # data.values()获取 login_test1,login_test2键对应的值 ｛name1:xxxx,password1:xxx｝ 和｛name1:xxxx,password1:xxx｝，
#     # 再将这些类型为字典的键值转入列表，最后返回，在用例paratrimeze方法 直接使用这个列表
#     for case_data in data.values():
#         case_list.append(case_data)
#     return case_list

if __name__ == '__main__':
    print(get_yml_with_filename_key("trans_data", "TestData"))
