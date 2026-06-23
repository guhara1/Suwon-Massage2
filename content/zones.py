# 생활권 안내 — 허브 1개 + 생활권 13개. 두 지역에 걸친 위치를 묶어 안내한다.
# 각 생활권의 고유 본문은 content/_data_zone.py 에서 가져온다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from ._data_zone import DATA as ZONE

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>생활권 안에서 정확한 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""


def _member_link(label, slug, kind):
    if kind == "station":
        return f'<a href="/gyeonggi/suwon/station/{slug}/">{label}</a>'
    # kind == 구 슬러그 (예: paldal-gu)
    return f'<a href="/gyeonggi/suwon/{kind}/{slug}/">{label}</a>'


def _members_html(members):
    return ", ".join(_member_link(l, s, k) for l, s, k in members)


def _zone_page(slug, z):
    name = z["name"]
    members_html = _members_html(z["members"]) if z.get("members") else ""
    faq_html = "".join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in z["faqs"]
    )

    body = f"""
<p class="lead">{z['lead']}</p>

<section>
<h2>{name} 구성</h2>
<p>{z['character']}</p>
</section>

<section>
<h2>이 생활권에서 함께 보는 안내</h2>
<p>{name}은 {members_html} 안내와 이어집니다. 위치가 두 지역 경계에 걸쳐 있어도 같은 기준으로 방문하므로, 가까운 동이나 역 페이지 중 편하신 쪽을 보시면 됩니다.</p>
</section>

<section>
<h2>이런 상황에 많이 이용하십니다</h2>
<p>{z['scenario']}</p>
</section>

<section>
<h2>방문 가능 형태와 시간</h2>
<p>{z['visit']}</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>생활권 단위 안내는 위치를 찾기 쉽게 돕는 보조 페이지입니다. 실제 예약은 도로명 주소 기준으로 진행되며, 절차는 <a href="/gyeonggi/suwon/reservation/">예약 안내</a>, 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>에서 확인하실 수 있습니다. 다른 생활권은 <a href="/gyeonggi/suwon/area/">생활권 전체 안내</a>에서 살펴보세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
{faq_html}
</section>
"""
    return {
        "path": f"gyeonggi/suwon/area/{slug}/",
        "title": z["title"],
        "desc": z["desc"],
        "h1": f"{name} 출장마사지·홈타이 안내",
        "body": body + PRICING + _CTA,
        "breadcrumb": [("생활권 안내", "/gyeonggi/suwon/area/"), (name, None)],
    }


def _hub_list():
    lis = "".join(
        f'<li><a href="/gyeonggi/suwon/area/{slug}/">{z["name"]}</a></li>'
        for slug, z in ZONE.items()
    )
    return f'<ul class="card-grid">{lis}</ul>'


_HUB_BODY = f"""
<p class="lead">행정동이나 역 하나로 위치를 설명하기 애매할 때를 위해, 수원시를 13개 생활권으로 묶어 안내합니다. 두 지역에 걸친 위치라도 한 페이지에서 확인하실 수 있습니다.</p>

<section>
<h2>생활권 안내란</h2>
<p>수원시는 같은 구 안에서도 동과 역이 촘촘하게 겹쳐, 사는 분들조차 "여기는 무슨 동"이라고 딱 잘라 말하기 어려운 경계 구역이 많습니다. 생활권 안내는 그런 위치를 위해 가까운 동과 역, 랜드마크를 하나로 묶은 보조 페이지입니다. 예를 들어 수원역과 매산동 사이, 인계동과 수원시청역 사이처럼 실제 생활 반경이 이어지는 구간을 묶어 설명합니다. 검색 의도를 넓게 잡으면서도 같은 내용을 동·역마다 반복하지 않도록 분리한 구조입니다.</p>
</section>

<section>
<h2>수원시 13개 생활권</h2>
{_hub_list()}
</section>

<section>
<h2>어느 페이지를 봐야 할까요</h2>
<p>거주지나 숙소가 특정 동에 분명히 속하면 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>가, 역 인근이면 <a href="/gyeonggi/suwon/station/">역세권 안내</a>가 더 정확합니다. 두 기준 사이에서 애매하다면 이 생활권 안내를 보시면 됩니다. 어느 쪽을 보셔도 예약 절차와 비용 기준은 같습니다.</p>
</section>

<section>
<h2>생활권별 성격 한눈에 보기</h2>
<p>13개 생활권은 성격이 뚜렷하게 갈립니다. 수원역·매산동과 인계동·수원시청은 상권·오피스텔·숙소 방문이 많은 도심형 생활권이고, 영통·망포와 권선·매탄은 동수원 주거 역세권 생활권입니다. 광교중앙·광교와 광교호수공원은 신도시 생활권, 정자·천천과 성균관대·율천, 화서·고등은 북수원 주거·대학가 생활권입니다. 호매실·금곡과 고색·오목천은 서수원 주거·산업 혼합 생활권, 팔달문·행궁동은 수원화성 원도심 생활권, 원천·아주대는 대학·병원 인접 생활권입니다. 본인 생활 반경과 가장 비슷한 생활권을 골라 보시면 필요한 정보가 더 빨리 보일 것입니다.</p>
</section>

<section>
<h2>경계 지역도 방문됩니다</h2>
<p>생활권은 행정 경계가 아니라 실제 생활 반경을 기준으로 묶은 것이라, 두 동이나 두 역 사이에 끼인 위치도 포함합니다. 수원과 화성·용인이 맞닿은 망포·광교 일대처럼 시 경계에 가까운 곳도 수원시 주소라면 방문 범위입니다. 위치 설명이 어려우시면 가까운 큰 건물이나 사거리, 도로명 주소를 알려주시면 됩니다.</p>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "gyeonggi/suwon/area/",
    "title": "수원시 생활권별 출장마사지·홈타이 안내｜13개 생활권",
    "desc": "수원역·인계동·영통·광교 등 수원시 13개 생활권 단위 출장마사지·홈타이 안내입니다.",
    "h1": "수원시 생활권별 출장마사지·홈타이 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("생활권 안내", None)],
}


def _build_pages():
    pages = [HUB]
    for slug, z in ZONE.items():
        pages.append(_zone_page(slug, z))
    return pages


PAGES = _build_pages()
