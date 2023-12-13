# booFuzz example


## booFuzz 설치:

```
pip install boofuzz
```

## 예제 다운로드 받기:
```
git clone https://github.com/YongyoonLee/boofuzz_example.git
```

## 예제 사용해 보기
### simple ftp 서버 실행
```
./simple_ftp/ftp &
```
* 새 터미널을 띄워서 실행하면, ftp 서버의 입력/응답을 볼 수 있음.
### booFuzz 예제 실행하기 
```
python3 ./boofuzz_ftp/fuzz_ftp.py
```
### 웹 브라우저에서, 퍼즈 테스팅 상황 확인하기
```
http://127.0.0.1:26000
```
