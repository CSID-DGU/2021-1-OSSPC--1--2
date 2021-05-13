import pymysql


class Database:
    def __init__(self):
        self.score_db = pymysql.connect(
            user='chin9510',
            password='tongsantris2021',
            host='tongsantris-db.cm8wqdx1uq7w.ap-northeast-2.rds.amazonaws.com',
            db='tongsantris',
            charset='utf8'
        )

        # def compare_id_data(self,id_text):
        #     #불러 오기
        #     curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        #     sql = "SELECT user_id FROM users"
        #     curs.execute(sql)
        #     data = curs.fetchall() #리스트 안에 딕셔너리가 있는 형태
        #     curs.close()
        #     #데이터가 튜플 형태라 파라미터로 받아온 id_text와 비교가 안됨 데이터의 value만 추출하는 방법 필요
        #     self.flag = False
        #     for datas in data:
        #         if datas['user_id']==id_text:
        #             self.flag=True
        #         else:
        #             self.flag=False
        #     return self.flag

    def compare_data(self, id_text, pw_text):
        # 불러 오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users "
        curs.execute(sql)
        data = curs.fetchall()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        self.flag = False
        for datas in data:
            # print(datas['user_id'],datas['user_password'])
            # print(id_text,pw_text)
            if datas['user_id'] == id_text:
                if datas['user_password'] == pw_text:
                    self.flag = True
        # print(self.flag)
        return self.flag


    def add_id_data(self,user_id):
        #추가하기
        curs = self.score_db.cursor()
        # 데이터베이스에 같은 id가 이미 존재하면 에러 메세지 띄우는 코드 필요.
        sql = "INSERT INTO users (user_id) VALUES (%s)"
        curs.execute(sql, user_id)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()


    def add_password_data(self,user_password,user_id):
        #추가하기
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password= %s WHERE user_id=%s"
        curs.execute(sql,(user_password,user_id))
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()
