# 메인 페이지 — 수원시 허브. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_FAQ = [
    ("수원시 전지역 방문이 가능한가요?",
     "예약 시간, 정확한 위치, 배정 상황에 따라 달라집니다. 장안구·권선구·팔달구·영통구 지역별 안내에서 대표 동 기준으로 확인할 수 있습니다."),
    ("수원역이나 인계동 근처도 가능한가요?",
     "수원역·수원시청역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."),
    ("정자1동, 매탄2동은 왜 따로 없나요?",
     "숫자로 나뉜 행정동은 정자동·매탄동 같은 대표 동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."),
    ("당일 예약도 가능한가요?",
     "가능할 수 있지만 저녁 시간대와 주말은 문의가 많아 사전 예약을 권장합니다."),
]

_FAQ_JSONLD = (
    '<script type="application/ld+json">\n{\n'
    '  "@context": "https://schema.org",\n'
    '  "@type": "FAQPage",\n'
    '  "mainEntity": [\n'
    + ",\n".join(
        '    {{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}'.format(q=q, a=a)
        for q, a in _FAQ
    )
    + "\n  ]\n}\n</script>\n"
)

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 수원시 전지역</p>
    <h1>수원 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/gyeonggi/suwon/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>4개 구</strong><span>장안·권선·팔달·영통</span></li>
      <li><strong>33곳</strong><span>대표 지역</span></li>
      <li><strong>14개</strong><span>역세권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_FAQ_HTML = "".join(
    f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in _FAQ
)

_BODY = f"""
<section id="intro">
<h2>수원시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>수원시 출장마사지를 찾는 분들은 보통 현재 위치가 수원역, 인계동, 영통동, 망포동, 광교, 권선동, 호매실 중 어디에 가까운지 먼저 확인합니다. 이 페이지는 수원시 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 구별·지역별·역세권·생활권 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내합니다. 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다.</p>
</section>

<section id="districts">
<h2>장안구·권선구·팔달구·영통구 생활권 차이</h2>
<p>수원시는 장안구, 권선구, 팔달구, 영통구 4개 구로 나뉘며 각 구마다 생활권이 다릅니다. 장안구는 정자동, 천천동, 조원동 같은 북수원 주거지 중심이고, 권선구는 권선동, 호매실동, 금곡동, 고색동 중심의 서수원 생활권입니다. 팔달구는 수원역, 인계동, 행궁동 같은 원도심과 중심상권이 강하고, 영통구는 영통동, 망포동, 매탄동, 광교동 중심의 동수원 생활권입니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/suwon/jangan-gu/">장안구</a></li>
<li><a href="/gyeonggi/suwon/gwonseon-gu/">권선구</a></li>
<li><a href="/gyeonggi/suwon/paldal-gu/">팔달구</a></li>
<li><a href="/gyeonggi/suwon/yeongtong-gu/">영통구</a></li>
</ul>
<p>수원 전체 구 구성은 <a href="/gyeonggi/suwon/">구별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="areas">
<h2>수원역·인계동·영통·광교 대표 지역 안내</h2>
<p>대표 지역 페이지는 인계동, 수원역, 영통동, 망포동, 광교동, 호매실동, 정자동 같은 세부 검색을 담당합니다. 인계동은 수원시청역과 나혜석거리 중심상권, 광교동은 광교중앙역과 광교호수공원 생활권, 망포동은 망포역과 화성 경계 인접권을 중심으로 작성되어 페이지마다 본문이 다릅니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/suwon/paldal-gu/ingye-dong/">인계동</a></li>
<li><a href="/gyeonggi/suwon/paldal-gu/maesan-dong/">매산동</a></li>
<li><a href="/gyeonggi/suwon/gwonseon-gu/gwonseon-dong/">권선동</a></li>
<li><a href="/gyeonggi/suwon/yeongtong-gu/yeongtong-dong/">영통동</a></li>
<li><a href="/gyeonggi/suwon/yeongtong-gu/mangpo-dong/">망포동</a></li>
<li><a href="/gyeonggi/suwon/yeongtong-gu/maetan-dong/">매탄동</a></li>
<li><a href="/gyeonggi/suwon/yeongtong-gu/gwanggyo-dong/">광교동</a></li>
<li><a href="/gyeonggi/suwon/gwonseon-gu/homaesil-dong/">호매실동</a></li>
<li><a href="/gyeonggi/suwon/jangan-gu/jeongja-dong/">정자동</a></li>
</ul>
<p>대표 동 33곳 전체 목록은 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>수원역·수원시청역·망포역·광교중앙역 역세권 안내</h2>
<p>역세권 페이지는 수원역, 수원시청역, 망포역, 영통역, 광교중앙역처럼 실제 검색 수요가 생길 수 있는 키워드를 담당합니다. 수원역 페이지는 역세권과 이동 기준을, 인접한 매산동 페이지는 원도심 상권 기준을 다루어 본문을 분리했습니다. 수원시청역과 인계동, 광교중앙역과 광교동도 같은 방식으로 역할을 나눕니다.</p>
<ul class="card-grid">
<li><a href="/gyeonggi/suwon/station/suwon-station/">수원역</a></li>
<li><a href="/gyeonggi/suwon/station/suwon-cityhall-station/">수원시청역</a></li>
<li><a href="/gyeonggi/suwon/station/maetan-gwonseon-station/">매탄권선역</a></li>
<li><a href="/gyeonggi/suwon/station/mangpo-station/">망포역</a></li>
<li><a href="/gyeonggi/suwon/station/yeongtong-station/">영통역</a></li>
<li><a href="/gyeonggi/suwon/station/gwanggyo-jungang-station/">광교중앙역</a></li>
<li><a href="/gyeonggi/suwon/station/sungkyunkwan-univ-station/">성균관대역</a></li>
<li><a href="/gyeonggi/suwon/station/hwaseo-station/">화서역</a></li>
</ul>
<p>수원 주요 14개 역세권 전체는 <a href="/gyeonggi/suwon/station/">역세권 안내</a>에서, 두 지역에 걸친 위치는 <a href="/gyeonggi/suwon/area/">생활권 안내</a>에서 확인하세요.</p>
</section>

<section id="check">
<h2>수원시 홈타이 예약 전 확인사항</h2>
<p>수원시 홈타이는 자택, 숙소, 오피스텔, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 수원역, 인계동, 영통동, 광교처럼 접근성이 좋은 지역도 있지만 호매실, 고색, 오목천, 파장동, 연무동 일부는 시간대와 주소에 따라 이동 기준이 달라질 수 있습니다. 예약 전 절차는 <a href="/gyeonggi/suwon/reservation/">예약 안내</a>에서, 방문 전 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>에서, 홈타이가 처음이라면 <a href="/gyeonggi/suwon/hometai-guide/">홈타이 이용 가이드</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="policy">
<h2>수원시 페이지 중복 방지 운영 기준</h2>
<p>수원시 홈타이 사이트에서 가장 중요한 부분은 번호 동을 무리하게 쪼개지 않는 것입니다. 정자1·2·3동, 매탄1~4동, 영통1~3동, 광교1·2동을 각각 개별 페이지로 만들면 본문이 비슷해질 수 있어, 대표 동 기준으로 통합하고 세부 번호 동은 본문 안에서 자연스럽게 설명합니다. 같은 본문에서 지역명만 바꾸는 방식은 쓰지 않으며, 팔달구 페이지와 수원역 페이지, 인계동 페이지와 수원시청역 페이지처럼 겹치기 쉬운 페이지는 지역 기준과 역세권 기준으로 본문을 분리했습니다. 운영 원칙은 <a href="/gyeonggi/suwon/about/">사이트 소개</a>에 정리되어 있습니다.</p>
</section>

<section id="how">
<h2>수원시 출장마사지 사이트 이용 방법</h2>
<p>먼저 수원 메인에서 큰 구조를 확인한 뒤, 거주하시거나 머무시는 위치에 맞는 페이지로 내려가시면 됩니다. 동을 아시면 지역별 안내, 역이 익숙하면 역세권 안내, 두 곳에 걸친 위치면 생활권 안내를 보시면 됩니다. 예약은 위치와 희망 시간을 확인하고 코스와 인원을 정한 뒤 방문 가능 여부를 안내받아 확정하는 순서로 진행됩니다. 저녁 시간대와 주말은 문의가 몰릴 수 있으니 한두 시간 여유를 두고 전화예약 주시기를 권장합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
{_FAQ_HTML}
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>수원시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "수원시 출장마사지｜수원역·인계동·영통·광교 홈타이 지역 안내",
    "desc": "수원시 출장마사지·홈타이 예약 전 수원역, 인계동, 영통동, 광교, 권선동 생활권을 확인하세요.",
    "h1": "수원시 출장마사지 · 수원시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _FAQ_JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
