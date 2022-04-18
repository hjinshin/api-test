# api-test

github-api-test.py(Python 3.8)
1. requests로 github에 있는 user의 정보를 가져온다
2. 만약 requests가 성공하면(status_code == 200) json_data에 저장
3. pprint(예쁜 데이터 인쇄기)로 데이터 출력

pip freeze로 python virtual enviroment에 설치되어있는 패키지 리스트를 requirements.txt에 저장

.ignore은 가상환경 폴더가 업로드되지 않도록 함(venv/)
