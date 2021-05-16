from auto_test.version_apk import *

app_ids = [
    [74, "remote-C-A7-master"],
    [78, "remote-C-H7-master"],
    [73, "方舟VCI数据库"],
    [75, "云穿越"],
    [85, '诊断能手7.0手机版'],
    [86, "诊断能手7.0PC版"],
    [38, "诊断能手工程师版"],
    [72, "方舟主控"],
    [71, "方舟脚本"],
    [6, "诊断能手"]
]


def test(app_info):
    hd = MyDb()
    sql = "SELECT * from tool_app_version WHERE App_Id = {} AND Delete_Flag = 0  ORDER BY id desc ;".format(app_info[0])
    engineer_version = hd.get_one(sql)
    return '{}----最新版本号+语义版本号--[{}，{}]'.format(app_info[1], engineer_version["App_Version_Code"],
                                               engineer_version["Inner_Version_Code"])


print(test(app_ids[0]))


