# 바로 GO — 수원 출장마사지·홈타이 안내 사이트

경기도 수원시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로 GO** · 전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·schema·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·텔레그램·메뉴 구조
  main.py           # 메인 페이지 (+ FAQPage JSON-LD)
  districts.py      # 구별: 수원시 허브 + 장안·권선·팔달·영통 4개 구
  areas.py          # 지역별: 대표 동 33개 + 동 디렉터리
  stations.py       # 역세권별: 허브 + 14개 역
  zones.py          # 생활권별: 허브 + 13개 생활권
  info.py           # 예약·이용 전 확인사항·홈타이 가이드·고객센터·개인정보·약관
  about.py          # 사이트 소개 (E-E-A-T)
  _data_dong_a.py   # 장안·권선 동 본문 데이터
  _data_dong_b.py   # 팔달·영통 동 본문 데이터
  _data_station.py  # 역 본문 데이터
  _data_zone.py     # 생활권 본문 데이터
assets/             # CSS(프리미엄 팔레트), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다. 모든 페이지에 WebPage·BreadcrumbList·Organization 구조화 데이터가 자동 삽입됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 33개만 — 정자1·2·3동, 매탄1~4동 등 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 출구별 페이지 없음
- 메뉴·URL에 “출장마사지” 반복 없음 — 키워드는 Title·H1·첫 문단에만 자연스럽게
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 물리적 사업장 주소가 없는 방문형 서비스이므로 LocalBusiness 스키마 미사용

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
