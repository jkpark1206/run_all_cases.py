import hashlib
# from config.config import local_config
import os
# path = 'C:\\Users\\Administrator\\Desktop\\gujianhuizong\\test\\recovery(11.7M).img'


#通过传入固件路径，获取该固件的MD5值
def Get_file_md5(file_path):
    try:
        with open(file_path,'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            hash_value = md5obj.hexdigest()
            return hash_value
    except Exception as e:
        print('ERROR', f'获取文件{file_path}md5值出错,原因{e}')
        return False


# if __name__=='__main__':
#     print(Get_file_md5(path))
