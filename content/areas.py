# 지역별 안내 — 대표 동 33개 + 동 디렉터리 허브 1개.
# 숫자 행정동(정자1·2·3동, 매탄1~4동 등)은 개별 페이지를 만들지 않고 대표 동으로 통합한다.
# 각 동의 고유 본문(생활권/이용 상황/방문/확인/FAQ)은 content/_data_dong_*.py 에서 가져온다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from ._data_dong_a import DATA as _DONG_A
from ._data_dong_b import DATA as _DONG_B

DONG = {**_DONG_A, **_DONG_B}

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다. 전화예약이 가장 빠릅니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

# 동 → 소속 구 메타
DISTRICT_NAME = {
    "jangan-gu": "장안구",
    "gwonseon-gu": "권선구",
    "paldal-gu": "팔달구",
    "yeongtong-gu": "영통구",
}


def _links(pairs, prefix):
    """[(라벨, 경로조각)] → 본문 인라인 링크 묶음."""
    return ", ".join(f'<a href="{prefix}{slug}/">{label}</a>' for label, slug in pairs)


def _station_links(stations):
    return ", ".join(
        f'<a href="/gyeonggi/suwon/station/{slug}/">{label}</a>'
        for label, slug in stations
    )


def _neighbor_links(neighbors):
    out = []
    for label, slug, gu in neighbors:
        out.append(f'<a href="/gyeonggi/suwon/{gu}/{slug}/">{label}</a>')
    return ", ".join(out)


def _dong_page(slug, d):
    gu_slug = d["district_slug"]
    gu = d["district"]
    name = d["name"]
    path = f"gyeonggi/suwon/{gu_slug}/{slug}/"

    station_html = _station_links(d["stations"]) if d.get("stations") else ""
    neighbor_html = _neighbor_links(d["neighbors"]) if d.get("neighbors") else ""
    zone_label, zone_slug = d["zone"]

    faq_html = "".join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in d["faqs"]
    )

    body = f"""
<p class="lead">{d['lead']}</p>

<section>
<h2>{name} 생활권 특징</h2>
<p>{d['character']}</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>{d['stations_note']} 역 인근에서 위치를 설명하실 때는 {station_html} 안내를 함께 참고해 주세요. 다만 실제 방문은 역 이름이 아니라 정확한 도로명 주소를 기준으로 진행됩니다.</p>
</section>

<section>
<h2>이런 상황에 많이 이용하십니다</h2>
<p>{d['scenario']}</p>
</section>

<section>
<h2>방문 가능 형태와 시간</h2>
<p>{d['visit']}</p>
</section>

<section>
<h2>방문 전 확인사항</h2>
<p>{d['check']}</p>
</section>

<section>
<h2>{name} 주변 함께 보기</h2>
<p>{name}과 생활권이 이어지는 인접 지역으로는 {neighbor_html} 안내가 있습니다. 두 곳 이상에 걸친 위치라면 <a href="/gyeonggi/suwon/area/{zone_slug}/">{zone_label}</a> 안내에서 생활권 단위로 확인하시는 편이 빠릅니다. {gu} 전체 구성은 <a href="/gyeonggi/suwon/{gu_slug}/">{gu} 출장마사지 안내</a>에서, 예약 절차는 <a href="/gyeonggi/suwon/reservation/">예약 안내</a>, 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
{faq_html}
</section>
"""
    return {
        "path": path,
        "title": d["title"],
        "desc": d["desc"],
        "h1": f"{name} 출장마사지·홈타이 방문 관리 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [
            ("구별 안내", "/gyeonggi/suwon/"),
            (gu, f"/gyeonggi/suwon/{gu_slug}/"),
            (name, None),
        ],
    }


# ── 동 디렉터리 허브 ──────────────────────────
def _dir_group(gu_slug):
    items = [
        (d["name"], f"/gyeonggi/suwon/{gu_slug}/{s}/")
        for s, d in DONG.items() if d["district_slug"] == gu_slug
    ]
    lis = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)
    return f'<ul class="card-grid">{lis}</ul>'


_DIR_BODY = f"""
<p class="lead">수원시 출장마사지·홈타이 지역별 안내는 장안구·권선구·팔달구·영통구 네 개 구의 대표 동 기준으로 구성됩니다. 거주하시거나 머무시는 동을 선택하면 생활권 특징과 방문 조건을 확인하실 수 있습니다.</p>

<section>
<h2>지역별 안내를 대표 동으로 묶은 이유</h2>
<p>수원시는 4개 구, 행정동만 40여 개에 이르는 큰 도시입니다. 하지만 정자1·2·3동, 매탄1~4동, 영통1~3동, 광교1·2동처럼 숫자로 나뉜 행정동을 페이지마다 따로 만들면 같은 생활권을 두고 비슷한 설명이 반복될 수밖에 없습니다. 그래서 이 사이트는 검색 수요가 분명한 대표 동을 기준으로 33개 지역 페이지를 운영하고, 숫자 동은 각 대표 동 페이지 안에서 통합해 안내합니다. 방문 가능 여부는 행정동 경계가 아니라 실제 주소와 예약 시간으로 판단하므로, 대표 동 기준 안내가 실제 이용 흐름과도 일치합니다.</p>
</section>

<section>
<h2>장안구 지역</h2>
<p>북수원 주거 생활권입니다. 정자동·천천동 같은 대표 주거지와 성균관대역·화서역 인접권을 중심으로 구성됩니다.</p>
{_dir_group("jangan-gu")}
</section>

<section>
<h2>권선구 지역</h2>
<p>서남부 생활권입니다. 권선동·호매실동·금곡동·고색동·오목천동 등 서수원 주거·산업 혼합 생활권을 다룹니다.</p>
{_dir_group("gwonseon-gu")}
</section>

<section>
<h2>팔달구 지역</h2>
<p>수원 원도심과 중심 상권입니다. 인계동·매산동·행궁동 등 수원역과 수원시청, 수원화성 인접 생활권을 다룹니다.</p>
{_dir_group("paldal-gu")}
</section>

<section>
<h2>영통구 지역</h2>
<p>동수원·광교 생활권입니다. 영통동·망포동·매탄동·원천동·광교동 등 신도시와 역세권 주거 생활권을 다룹니다.</p>
{_dir_group("yeongtong-gu")}
</section>

<section>
<h2>역세권·생활권으로도 확인하세요</h2>
<p>역 기준이 익숙하시면 <a href="/gyeonggi/suwon/station/">역세권 안내</a>를, 두 지역에 걸친 위치라면 <a href="/gyeonggi/suwon/area/">생활권 안내</a>를 참고하시면 됩니다. 구 단위로 먼저 보시려면 <a href="/gyeonggi/suwon/">구별 안내</a>에서 시작하실 수 있습니다.</p>
</section>

<section>
<h2>동 페이지에서 확인할 수 있는 것</h2>
<p>각 동 페이지에는 그 동만의 생활권 특징, 가까운 역세권, 자주 이용하시는 상황, 방문 가능한 형태와 시간대, 방문 전 확인사항, 자주 묻는 질문이 동마다 고유한 내용으로 정리되어 있습니다. 예를 들어 정자동은 북수원 대단지 주거지, 인계동은 수원시청역 중심상권과 오피스텔·숙소, 광교동은 광교호수공원 신도시 생활권처럼 성격이 분명히 다르므로 본문도 서로 겹치지 않게 작성했습니다. 거주하시거나 머무시는 동을 고르신 뒤, 예약 전화에서 도로명 주소만 알려주시면 가장 빠르게 안내받으실 수 있습니다. 찾으시는 동이 숫자로 나뉜 행정동(예: 정자1동, 매탄2동)이라면 해당 대표 동 페이지 안에 통합되어 있으니 그 페이지를 보시면 됩니다.</p>
</section>
""" + PRICING + _CTA

DIRECTORY = {
    "path": "gyeonggi/suwon/areas/",
    "title": "수원시 지역별 출장마사지·홈타이 안내｜대표 동 33곳",
    "desc": "수원시 장안·권선·팔달·영통 4개 구 대표 동별 출장마사지·홈타이 방문 안내 디렉터리입니다.",
    "h1": "수원시 지역별 출장마사지·홈타이 안내",
    "body": _DIR_BODY,
    "breadcrumb": [("지역별 안내", None)],
}


def _build_pages():
    pages = [DIRECTORY]
    # 메뉴/구 페이지 순서를 따르도록 구별로 정렬
    order = ["jangan-gu", "gwonseon-gu", "paldal-gu", "yeongtong-gu"]
    for gu in order:
        for slug, d in DONG.items():
            if d["district_slug"] == gu:
                pages.append(_dong_page(slug, d))
    return pages


PAGES = _build_pages()
