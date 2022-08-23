## 2022.08.22
users 생성
* 회원가입 구현
    password 검증
    password 일치 확인
    email 중복 검증
    테스트 완료

## 2022.08.23
* 로그인 구현
    password write_only=ture
    토큰을 통한 유저 찾기
* profile 구현
    user 확장 필드
    닉네임, 직위, 주제, 이미지
    user feild OneToOne 결합, on_delete=models.CASCADE
    권한 부여를 통한 해당유저만 수정
* admin page user에 profile 같이 나오도록 구현
* 게시판 구현
    작성자, 프로파일, 제목, 카테고리, 내용, 이미지, 좋아요, 작성 및 수정일, 상단표시여부
    router로 경로 설정
    권한 여부
    게시판 필터 (작성자, 좋아요)
    게시판 조회 페이지 나누기 = 3
    좋아요 기능 추가 ( add, remove )

