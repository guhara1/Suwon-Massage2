#!/usr/bin/env python3
"""Google Indexing API 통보 (선택) — urlNotifications:publish.

주의(중요):
  Google Indexing API 는 공식적으로 JobPosting·BroadcastEvent 구조화 데이터
  페이지만 처리합니다. 일반 페이지 색인은 보장되지 않으며, 일반 색인은
  Search Console + sitemap.xml 제출이 정식 경로입니다. IndexNow(빙·네이버)와
  성격이 다릅니다.

준비:
  1) pip install google-auth
  2) Google Cloud 콘솔에서 서비스 계정 생성 → JSON 키 발급, Indexing API 사용 설정
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) 환경변수로 키 경로 지정: export GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json

사용법:
  python tools/google_indexing.py                 # sitemap.xml 의 모든 URL
  python tools/google_indexing.py <url> [<url>…]   # 지정 URL
  python tools/google_indexing.py --delete <url>   # URL_DELETED 통보
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def sitemap_urls() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def get_token() -> str:
    try:
        import google.auth
        import google.auth.transport.requests as gtr
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth")
    creds, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/indexing"]
    )
    creds.refresh(gtr.Request())
    return creds.token


def publish(url: str, token: str, deleted: bool = False) -> None:
    body = json.dumps({
        "url": url,
        "type": "URL_DELETED" if deleted else "URL_UPDATED",
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  {resp.status} {url}")
    except urllib.error.HTTPError as e:
        print(f"  {e.code} {url}  {e.read().decode('utf-8','replace')[:200]}")


def main() -> None:
    deleted = "--delete" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--delete"]
    urls = args if args else sitemap_urls()
    token = get_token()
    print(f"{'삭제' if deleted else '갱신'} 통보 {len(urls)}개")
    for u in urls:
        publish(u, token, deleted)
    print("완료.")


if __name__ == "__main__":
    main()
