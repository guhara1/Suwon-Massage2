#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex·Seznam 등.

글을 새로 올리거나 수정할 때마다 실행하면 참여 검색엔진에 즉시 통보한다.
표준 라이브러리만 사용한다(외부 패키지 불필요).

사용법:
    python tools/indexnow.py                # sitemap.xml 의 모든 URL 통보
    python tools/indexnow.py <url> [<url>…]  # 지정한 URL만 통보
    python tools/indexnow.py --dry-run       # 전송 없이 대상 URL만 출력

먼저 `python build.py` 로 sitemap.xml 과 <KEY>.txt 가 생성/배포되어 있어야 한다.
키 파일(https://도메인/<KEY>.txt)이 실제로 접근 가능해야 통보가 수락된다.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

SITE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", SITE).split("/")[0]
KEY_LOCATION = f"{SITE}/{INDEXNOW_KEY}.txt"

# api.indexnow.org 한 곳에 보내면 참여 엔진 전체로 공유되지만,
# 빙·네이버에는 직접 엔드포인트로도 함께 통보해 확실히 한다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def sitemap_urls() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(urls: list) -> None:
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")

    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"  {resp.status} {resp.reason:18} {ep}")
        except urllib.error.HTTPError as e:
            # 200/202 외에도 일부 엔진은 본문에 사유를 담아 4xx 를 줄 수 있다.
            body = e.read().decode("utf-8", "replace")[:200]
            print(f"  {e.code} {e.reason:18} {ep}  {body}")
        except urllib.error.URLError as e:
            print(f"  ERR  {ep}  {e.reason}")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    urls = args if args else sitemap_urls()
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    print(f"host={HOST}  key={INDEXNOW_KEY}")
    print(f"keyLocation={KEY_LOCATION}")
    print(f"대상 URL {len(urls)}개:")
    for u in urls:
        print("  -", u)
    if dry:
        print("\n--dry-run: 전송하지 않았습니다.")
        return
    # IndexNow 는 요청당 최대 10,000 URL. 안전하게 청크 처리.
    print("\n전송 중…")
    for i in range(0, len(urls), 10000):
        submit(urls[i:i + 10000])
    print("\n완료. 빙 웹마스터도구 / 네이버 서치어드바이저에서 수집 현황을 확인하세요.")


if __name__ == "__main__":
    main()
