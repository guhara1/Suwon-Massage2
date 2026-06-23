# 역세권 안내 — 허브 1개 + 역 14개.
# 환승역도 URL은 하나만 사용한다. 출구별·역+테마 조합 페이지는 만들지 않는다.
# 각 역의 고유 본문은 content/_data_station.py 에서 가져온다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from ._data_station import DATA as STATION

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>역 인근 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다. 전화예약이 가장 빠릅니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""


def _dong_links(dongs):
    return ", ".join(
        f'<a href="/gyeonggi/suwon/{gu}/{slug}/">{label}</a>'
        for label, slug, gu in dongs
    )


def _station_page(slug, s):
    name = s["name"]
    zone_label, zone_slug = s["zone"]
    dong_html = _dong_links(s["dongs"]) if s.get("dongs") else ""
    faq_html = "".join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in s["faqs"]
    )

    body = f"""
<p class="lead">{s['lead']}</p>

<section>
<h2>{name} 역세권 분위기</h2>
<p>{s['character']}</p>
</section>

<section>
<h2>인근 생활권과 대표 동</h2>
<p>{s['dong_note']} 가까운 대표 동으로는 {dong_html} 안내가 이어집니다. 건물 이름이 비슷한 구역이 많으니 예약 시 도로명 주소를 함께 알려주시면 도착이 정확해집니다.</p>
</section>

<section>
<h2>이런 일정에 자주 이용됩니다</h2>
<p>{s['scenario']}</p>
</section>

<section>
<h2>방문 형태와 시간대</h2>
<p>{s['visit']}</p>
</section>

<section>
<h2>{name} 인근 예약 팁</h2>
<p>{s['tip']}</p>
</section>

<section>
<h2>{name} 주변 함께 보기</h2>
<p>{name} 인근은 <a href="/gyeonggi/suwon/area/{zone_slug}/">{zone_label}</a> 안내에서 생활권 단위로도 확인하실 수 있습니다. 다른 역 기준이 편하시면 <a href="/gyeonggi/suwon/station/">역세권 전체 안내</a>를, 동 기준이 익숙하시면 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>를 참고해 주세요. 예약 절차는 <a href="/gyeonggi/suwon/reservation/">예약 안내</a>에 정리되어 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
{faq_html}
</section>
"""
    return {
        "path": f"gyeonggi/suwon/station/{slug}/",
        "title": s["title"],
        "desc": s["desc"],
        "h1": f"{name} 출장마사지·홈타이 인근 방문 관리 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [("역세권 안내", "/gyeonggi/suwon/station/"), (name, None)],
    }


# ── 역세권 허브 ──────────────────────────────
def _hub_list():
    lis = "".join(
        f'<li><a href="/gyeonggi/suwon/station/{slug}/">{s["name"]}</a></li>'
        for slug, s in STATION.items()
    )
    return f'<ul class="card-grid">{lis}</ul>'


_HUB_BODY = f"""
<p class="lead">수원시를 지나는 1호선·수인분당선·신분당선 주요 역세권을 기준으로 방문 관리를 안내합니다. 환승역은 노선이 여러 개라도 페이지는 하나만 운영합니다.</p>

<section>
<h2>역세권 안내 구성 기준</h2>
<p>수원시는 경부선과 수인분당선, 신분당선이 지나는 경기 남부 교통의 요지입니다. 이 사이트의 역 안내는 역마다 페이지 하나를 두는 단일 페이지 원칙을 따릅니다. 수원역처럼 환승 성격이 강한 역도 노선별로 쪼개지 않고, 출구 번호별 페이지나 역 이름에 관리 테마를 붙인 조합 페이지도 만들지 않습니다. 그런 페이지는 내용이 겹칠 수밖에 없고 검색 이용자에게도 도움이 되지 않기 때문입니다. 각 역 페이지에서는 역세권 분위기, 인근 대표 동, 방문 형태, 예약 팁을 역마다 고유하게 설명합니다.</p>
</section>

<section>
<h2>수원시 주요 역세권</h2>
{_hub_list()}
<p>수원역과 수원시청역은 상권형 역세권이라 심야·숙소 방문 문의가 많고, 망포역·영통역·매탄권선역은 동수원 주거 역세권이라 자택 예약이 중심입니다. 광교중앙역·광교역은 광교신도시 생활권, 성균관대역·화서역은 북수원 대학가·주거 생활권으로 성격이 갈립니다.</p>
</section>

<section>
<h2>역 기준으로 예약하실 때</h2>
<p>역 이름은 위치를 설명하는 좋은 기준이지만, 실제 방문에는 정확한 주소가 필요합니다. 예약 전화에서 가까운 역과 함께 건물명 또는 도로명 주소를 알려주시면 도착 시간을 정확히 안내해 드립니다. 거주 지역 기준이 편하시면 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>를, 두 지역에 걸친 위치라면 <a href="/gyeonggi/suwon/area/">생활권 안내</a>를 확인해 주세요. 어느 역에서 출발하든 예약 절차와 이용 기준은 동일합니다.</p>
</section>

<section>
<h2>노선별 수원 역세권</h2>
<p>수원을 지나는 노선은 성격이 다릅니다. 1호선(경부선)은 수원역·화서역·성균관대역·세류역으로 이어지는 원도심·대학가 축이고, 수인분당선은 고색역·오목천역·매교역·수원시청역·매탄권선역·망포역·영통역·청명역으로 이어지며 서수원 산업권부터 동수원 주거권까지 가장 넓게 연결합니다. 신분당선은 광교중앙역·광교역으로 광교신도시를 잇습니다. 환승 성격이 있는 수원역도 노선별로 페이지를 쪼개지 않고 하나로 운영하니, 역 이름만 알려주시면 됩니다.</p>
</section>

<section>
<h2>수원 인근 역 처리 기준</h2>
<p>병점역·세마역·동탄역은 화성·오산 성격이 강하고, 의왕역은 의왕시 성격이 강해 수원 핵심 역세권으로 다루지 않고 인접 생활권으로만 언급합니다. 예정역·미개통역도 단독 페이지로 만들지 않습니다. 수원 경계와 맞닿은 위치라도 주소에 따라 방문이 가능할 수 있으니 전화로 확인해 주세요.</p>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "gyeonggi/suwon/station/",
    "title": "수원시 역세권 출장마사지·홈타이 안내｜주요 14개 역",
    "desc": "수원역·수원시청역·망포역·영통역·광교중앙역 등 수원 주요 역세권 출장마사지·홈타이 안내입니다.",
    "h1": "수원시 역세권별 출장마사지·홈타이 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("역세권 안내", None)],
}


def _build_pages():
    pages = [HUB]
    for slug, s in STATION.items():
        pages.append(_station_page(slug, s))
    return pages


PAGES = _build_pages()
