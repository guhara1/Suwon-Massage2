# 색인 통보 도구 (tools/)

새 글을 올리거나 페이지를 수정한 뒤, 검색엔진에 가장 빠르게 알리는 도구 모음입니다.

## 0. 먼저 빌드

```bash
python build.py
```

빌드하면 다음이 생성됩니다.

- `sitemap.xml` — 색인 허용 페이지 + `lastmod`(신선도 신호)
- `rss.xml` — 동일 페이지 RSS 피드 (발견 보조)
- `robots.txt` — 모든 봇 허용 + sitemap 위치
- `<INDEXNOW_KEY>.txt` — IndexNow 소유 확인 키 파일 (루트)

## 1. IndexNow — 빙·네이버·얀덱스 즉시 통보 (권장, 무료, 키만 있으면 됨)

```bash
python tools/indexnow.py            # sitemap.xml 의 모든 URL 통보
python tools/indexnow.py https://suwon-massage2.pages.dev/gyeonggi/suwon/paldal-gu/ingye-dong/
python tools/indexnow.py --dry-run  # 전송 없이 대상만 확인
```

- 외부 패키지 불필요(표준 라이브러리만 사용).
- `api.indexnow.org` 한 곳에 보내면 참여 엔진 전체로 공유되며, 빙·네이버·얀덱스 직접 엔드포인트로도 함께 통보합니다.
- **네이버**는 IndexNow 파트너이므로 이 한 번으로 네이버에도 통보됩니다.
- 키 파일(`https://도메인/<KEY>.txt`)이 실제 접근 가능해야 통보가 수락됩니다. 배포 후 한 번 브라우저로 열어 확인하세요.

### 첫 일괄 통보
배포가 끝난 뒤 로컬에서 한 번만:

```bash
python tools/indexnow.py
```

이후에는 글을 올릴 때마다 바뀐 URL만 인자로 넘기면 됩니다.

## 2. 검색엔진 등록 (최초 1회)

- **네이버 서치어드바이저** — 사이트 등록 → 소유 확인(메인페이지에 `naver-site-verification` 메타 삽입됨) → `sitemap.xml`, `rss.xml` 제출.
- **Google Search Console** — 속성 등록 → `sitemap.xml` 제출. (구글은 IndexNow 미참여이므로 sitemap 제출이 정식 경로)
- **Bing Webmaster Tools** — 사이트 추가 후 IndexNow 키 확인.

## 3. (선택) Google Indexing API

```bash
pip install google-auth
export GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json
python tools/google_indexing.py
```

⚠️ Google Indexing API 는 **공식적으로 JobPosting·BroadcastEvent 페이지만** 처리합니다.
일반 페이지 색인 보장 용도가 아니며, 일반 색인은 Search Console + sitemap 제출이 정식 경로입니다.

## 참고: sitemap ping 자동화

Google(2023년 6월)·Bing 모두 sitemap **ping 엔드포인트를 폐지**했습니다.
지금은 ping 대신 **IndexNow(빙·네이버)** + **Search Console sitemap 제출(구글)** 조합이 가장 빠릅니다.
그래서 별도 ping 스크립트는 두지 않았습니다.
