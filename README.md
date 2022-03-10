# 필링 (필리 클론코딩)
<img width="1166" alt="스크린샷 2021-10-03 오후 12 42 43" src="https://user-images.githubusercontent.com/79790476/135738706-67514425-3f53-4427-8a0b-4d13d9531b4c.png">

### <a href="https://www.youtube.com/watch?v=n1NpDX8b3RY&ab_channel=%EA%B9%80%EC%98%81%ED%98%B8">필링 시연영상 보러가기</a>
## 오버도즈 팀원

- F.E<br>
  김영호<br>
  김태수<br>
  정행운<br>
  <br>
- B.E<br>
  고영수<br>
  최현수<br>
  <br>

### 개발 인원 및 기간

- 개발기간 : 2021/9/13 ~ 2021/10/1
- 개발 인원 : 프론트엔드 3명, 백엔드 2명

<br>

### 프로젝트 선정이유

- 디지털 헬스케어 분야에서 영양제 구독 이라는 독특한 서비스를 제공하는 필리 사이트를 모티브로 하였습니다. 
- 설문조사를 통해 추천성분을 제공하는 서비스의 차별화를 매력적인 포인트로 생각하였습니다.

<br>

## 적용 기술 및 구현 기능

### 적용 기술

> -Front-End : JSX, React, Hooks, Styled Component<br>
> -Back-End : Python 3.8, Django 3.2.7, MySQL 8.0.23, Unittest<br>
> -Common : Postman, Slack, Trello, AWS

<br>

구현 기능

1. 회원가입 / 로그인 페이지<br>
✔️ 토큰을 이용한 회원가입, 로그인, 로그아웃 기능<br>
✔️ 카카오소셜 로그인 기능<br>
✔️ 유효성 검사 로직에 따른 레이아웃 구현<br>
✔️ 모두 동의하기 기능 구현<br>

2. 내비게이션 바<br>
✔️ 메뉴 클릭시 동적 라우팅 적용<br>
✔️ 로그인, 로그아웃 시 내비게이션 바 레이아웃 변경<br>

3. 메인 페이지<br>
✔️ React-slick 라이브러리 이용 및 CSS 커스터마이즈 슬라이더 구현<br>
✔️ React-Spring 라이브러리를 이용한 숫자 애니메이션 추가<br>

4. 설문조사 결과<br>
✔️ 로그인한 유저의 설문조사 결과 상세페이지 렌더<br>

5. 설문조사<br>
✔️ query string을 활용한 동적 라우팅 구현<br>
✔️ state로 상태 관리 후 URL 변경 없이 설문 페이지 이동, 답변 선택 시 fetch API 활용하여 서버에 전송 기능<br>
✔️ 유효성 검증 로직 추가하여 FE/BE 양측에서 유효성 확인하도록 구현<br>


6. 카트<br>
✔️ <br>
✔️<br>
✔️<br>

7. Footer <br>
✔️ map을 통한 레이아웃 구현 <br>

8. 리뷰<br>
✔️ Mock data를 활용한 레이아웃 구현 <br>

9. 제품 리스트<br>
✔ 컴포넌트를 활용한 제품 카드 구현 <br>
✔ fetch API를 활용한 데이터 렌더링 <br>

10. 상세 페이지<br>
✔️ 장바구니 추가 기능 구현 <br>
✔️ 장바구니 추가 여부 팝업창 구현 <br>

11. 프로필<br>
✔️ 프로필 내 설문조사 결과 메뉴에서 로그인한 회원의 설문 결과 렌더 <br>
✔️ enum 패턴을 활용한 코드 간결화 <br>

<br>
- 이 프로젝트는 필리 사이트를 참조하여 만들었습니다.
<br>
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

<hr />
<br>
필리 프로젝트는 필리 클론 프로젝트이지만, 백지 상태에서 구현되었습니다. 개발자의 역할은 기획이 아닌, 기획 의도를 현실로 바꾸는, 기획의 ‘구현’이라 생각합니다. 따라서, 기획 과정을 건너 뛰고 구현에 집중하기 위해 필리 라는 서비스를 참고한 것일 뿐, 프로젝트의 모든 기능은, 실제 서비스 개발과정과 마찬가지로, 백지 상태에서 구현되었음을 밝힙니다.
