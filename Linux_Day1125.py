"""
리눅스 명령어 정리.

ctrl + c: 작업 중지

ls - al(la): 모든 내용 출력.

mkdir: dir생성
    -p: 중간 폴더까지 동시에 생성

chmod: 권한값변경
    chmod 755 ex.txt

rmdir: dir삭제
    -r: 하위내용 모두 삭제
    -f: 조건 무시

rm: dir삭제
    rmdir보다 자주쓰임
    -r, R: 하위내용 모두 삭제
    -f: 조건 무시

mv: 파일위치 이동
    mv log dir1: logdir을 dir1안으로 이동

cp: 파일복사(하위 내용 있으면 복사x)
    -f: 파일 있으면 지우고 강제 복사
    -R: 하위내용까지 모두 복사

cat
    -n: 줄 번호 표시
    -b: 빈 행은 제외 후 줄 번호 표시
    -E: 각 행의 끝에 $ 표시

more: 파일을 페이지 단위로 분할

less: more와 동일 기능이지만 기능이 더 많다.

head / tail: pandas와 동일
    head - 10, tail - 10
    -f: 실시간 로그를 출력
    탈출은 ctrl + c

find: 원하는 파일 찾기.
    *: 0개 이상의 문자,
    ?: 1개의 문자

find[시작파일위치][조건]
    -name: 문자열 찾기
    -user: 사용자 찾기
    -perm: 권한값으로 찾기
    -type x: type으로 찾기
    -size: 크기로 찾기
    2> / dev / null: error가 뜨면 null로 변환해라

-exec: find 등 작업 수행이 끝난 뒤 추가작업을 하고 싶을 때
    find / -size 0 - exec ls - la {} /;

grep: 특정 패턴을 찾고 싶을 때
    grep root /var/log/secure
    -v: 일치하지 않는 라인
    -c: 일치하는 행의 개수
    -n: 일치하는 행과 행의 번호

pipe( | ):
    grep root / var / log / secure | less(more, head, tail, cat)

리다이렉션:
    >: 파일이 없으면 생성 후 추가, 있으면 기존내용 삭제 후 추가
    >>: 파일 x면 생성, 있으면 기존 내용에 추가(append)
    <: 파일로부터 표준 입력을 받는다.(input)
    동시 사용도 가능하다.
    sort < / etc / passwd > sorted.txt
    passwd를 sort한 뒤에 sorted.txt로 입력해라.
"""