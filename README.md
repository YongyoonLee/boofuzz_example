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
### simple ftp 서버 컴파일 및 실행
```
cd simple_ftp
make
./ftp
```
### booFuzz 예제 실행하기 
```
cd ../boofuzz_ftp
python3 fuzz_ftp.py
```
### 웹 브라우저에서, 퍼즈 테스팅 상황 확인하기
```
http://127.0.0.1:26000
```