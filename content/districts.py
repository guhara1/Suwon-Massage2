# 구별 안내 — 수원시 구 허브(/gyeonggi/suwon/) + 장안·권선·팔달·영통 4개 구 페이지.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>구 안에서 정확한 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다. 전화예약이 가장 빠릅니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""


def _grid(items):
    lis = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)
    return f'<ul class="card-grid">{lis}</ul>'


# ── 구 허브 (구별 안내) ───────────────────────
_HUB_BODY = f"""
<p class="lead">수원시 출장마사지·홈타이는 장안구, 권선구, 팔달구, 영통구 네 개 구로 나뉘어 안내됩니다. 각 구마다 생활권 성격이 뚜렷하게 다르므로, 먼저 거주하시거나 머무시는 구를 선택해 주세요.</p>

<section>
<h2>수원시 4개 구 구성</h2>
<p>수원시는 경기도에서 인구가 가장 많은 도시로, 장안구·권선구·팔달구·영통구 네 개 구로 이루어져 있습니다. 같은 수원이라도 장안구는 북수원 주거지, 권선구는 서남부 주거·산업 생활권, 팔달구는 원도심과 중심 상권, 영통구는 동수원과 광교 신도시 생활권으로 분위기가 크게 다릅니다. 방문 관리 안내도 구마다 가까운 역과 생활 리듬이 다르기 때문에, 구 단위로 먼저 구분한 뒤 대표 동으로 내려가는 구조로 정리했습니다.</p>
</section>

<section>
<h2>구별 안내 바로가기</h2>
{_grid([
    ("장안구", "/gyeonggi/suwon/jangan-gu/"),
    ("권선구", "/gyeonggi/suwon/gwonseon-gu/"),
    ("팔달구", "/gyeonggi/suwon/paldal-gu/"),
    ("영통구", "/gyeonggi/suwon/yeongtong-gu/"),
])}
<p>장안구는 정자동·천천동을 중심으로 한 북수원 주거 생활권이고, 권선구는 권선동·호매실동·고색동 등 서수원 생활권입니다. 팔달구는 수원역·인계동·행궁동을 잇는 원도심 중심상권, 영통구는 영통동·망포동·광교동을 아우르는 동수원 생활권입니다.</p>
</section>

<section>
<h2>대표 동으로 통합 안내하는 이유</h2>
<p>정자1·2·3동, 매탄1~4동, 영통1~3동, 광교1·2동처럼 숫자로 나뉜 행정동은 개별 페이지로 만들지 않고 각 대표 동 페이지에서 통합해 안내합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하면 이용자에게도 혼란스럽고, 방문 가능 여부는 행정동 경계가 아니라 실제 주소로 판단하기 때문입니다. 대표 동 33곳 전체 목록은 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>역세권·생활권으로도 확인하세요</h2>
<p>역 기준이 익숙하시면 <a href="/gyeonggi/suwon/station/">역세권 안내</a>에서 수원역·수원시청역·망포역·광교중앙역 등 14개 역을, 두 지역에 걸친 위치라면 <a href="/gyeonggi/suwon/area/">생활권 안내</a>에서 13개 생활권을 확인하실 수 있습니다. 처음 이용하신다면 <a href="/gyeonggi/suwon/hometai-guide/">홈타이 이용 가이드</a>와 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>을 먼저 읽어보시기를 권합니다.</p>
</section>

<section>
<h2>구를 고를 때 참고하세요</h2>
<p>거주지나 숙소가 어느 구에 속하는지 헷갈릴 때는 가까운 큰 기준점을 떠올리면 쉽습니다. 수원종합운동장·만석공원·성균관대 방면이면 장안구, 수원역 서쪽·호매실지구·수원델타플렉스 방면이면 권선구, 수원역·수원시청·수원화성·인계동 방면이면 팔달구, 삼성전자·아주대·광교호수공원·영통·망포 방면이면 영통구일 가능성이 높습니다. 구 경계가 애매한 위치라도 걱정하실 필요는 없습니다. 방문은 행정구역이 아니라 도로명 주소로 진행되므로, 어느 구 페이지를 보셔도 예약 절차와 비용 기준은 같습니다. 정확한 소속 구가 궁금하시면 예약 전화에서 주소를 말씀해 주시면 바로 확인해 드립니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item"><h3>수원 전역이 방문 범위인가요?</h3><p>네, 장안구·권선구·팔달구·영통구 수원시 전 지역이 방문 범위입니다. 화성·용인·의왕과 맞닿은 경계 지역도 주소에 따라 가능할 수 있으니 전화로 확인해 주세요.</p></div>
<div class="faq-item"><h3>구 단위 말고 동으로 바로 찾고 싶어요.</h3><p>대표 동 33곳을 한 페이지에 모은 <a href="/gyeonggi/suwon/areas/">지역별 안내</a>에서 바로 찾으실 수 있습니다. 역 기준이면 역세권 안내가 더 편합니다.</p></div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "gyeonggi/suwon/",
    "title": "수원시 구별 출장마사지·홈타이 안내｜장안·권선·팔달·영통",
    "desc": "수원시 4개 구 출장마사지·홈타이 안내입니다. 장안·권선·팔달·영통 생활권 차이를 확인하세요.",
    "h1": "수원시 구별 출장마사지·홈타이 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("구별 안내", None)],
}


# ── 개별 구 페이지 ───────────────────────────
JANGAN = {
    "path": "gyeonggi/suwon/jangan-gu/",
    "title": "장안구 출장마사지｜정자·천천·성균관대 생활권 홈타이 안내",
    "desc": "장안구 출장마사지 이용 전 정자동, 천천동, 성균관대역, 조원동 생활권을 확인하세요.",
    "h1": "장안구 출장마사지·홈타이 지역 안내",
    "breadcrumb": [("구별 안내", "/gyeonggi/suwon/"), ("장안구", None)],
    "body": f"""
<p class="lead">장안구는 수원 북부의 주거 생활권입니다. 정자동, 천천동, 율천동, 조원동, 영화동, 송죽동, 파장동, 연무동을 중심으로 안내합니다.</p>

<section>
<h2>장안구 생활권 특징</h2>
<p>장안구는 수원의 북부를 차지하는 대표적인 주거 지역입니다. 정자동과 천천동은 대단지 아파트와 주택가가 어우러진 북수원의 핵심 주거지로 검색 수요가 가장 꾸준하고, 율천동은 성균관대역과 대학가 생활권에 맞닿아 있습니다. 조원동은 수원종합운동장과 장안구청을 낀 행정·주거 생활권이며, 파장동과 연무동은 광교산 자락과 북수원 외곽으로 이어집니다. 같은 장안구라도 정자동 아파트 단지와 율천동 대학가, 파장동 주택가는 생활 리듬이 서로 달라, 방문 시간대나 공간 준비 안내도 동마다 조금씩 다릅니다.</p>
</section>

<section>
<h2>장안구 대표 동</h2>
{_grid([
    ("정자동", "/gyeonggi/suwon/jangan-gu/jeongja-dong/"),
    ("천천동", "/gyeonggi/suwon/jangan-gu/cheoncheon-dong/"),
    ("율천동", "/gyeonggi/suwon/jangan-gu/yulcheon-dong/"),
    ("조원동", "/gyeonggi/suwon/jangan-gu/jowon-dong/"),
    ("영화동", "/gyeonggi/suwon/jangan-gu/yeonghwa-dong/"),
    ("송죽동", "/gyeonggi/suwon/jangan-gu/songjuk-dong/"),
    ("파장동", "/gyeonggi/suwon/jangan-gu/pajang-dong/"),
    ("연무동", "/gyeonggi/suwon/jangan-gu/yeonmu-dong/"),
])}
<p>정자1·2·3동은 정자동 페이지로, 조원1·2동은 조원동 페이지로 통합 안내합니다. 숫자 행정동을 따로 찾으셨더라도 필요한 내용은 대표 동 페이지 안에 모두 담겨 있습니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>장안구 생활권에서는 1호선 <a href="/gyeonggi/suwon/station/hwaseo-station/">화서역</a>과 수인분당선 <a href="/gyeonggi/suwon/station/sungkyunkwan-univ-station/">성균관대역</a>이 주요 거점입니다. 율천동과 천천동은 성균관대역 생활권과 가깝고, 정자동·영화동은 화서역과 수원종합운동장 방면으로 이어집니다. 역 인근 위치라도 실제 방문은 도로명 주소를 기준으로 진행됩니다.</p>
</section>

<section>
<h2>생활권으로 함께 보기</h2>
<p>정자동과 천천동이 이어지는 <a href="/gyeonggi/suwon/area/jeongja-cheoncheon/">정자·천천 생활권</a>, 율천동과 성균관대역을 묶은 <a href="/gyeonggi/suwon/area/sungkyunkwan-yulcheon/">성균관대·율천 생활권</a> 안내도 함께 확인해 보세요. 수원 전체 구 구성은 <a href="/gyeonggi/suwon/">구별 안내</a>에서 볼 수 있습니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>장안구는 대단지 아파트와 대학가 원룸, 외곽 주택가가 섞여 있어 건물 유형을 함께 알려주시면 방문 준비가 수월합니다. 아파트는 동·호수와 공동현관 출입 방법을, 원룸·오피스텔은 건물 입구 안내를 미리 확인해 주세요. 자세한 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>에 정리되어 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item"><h3>정자1동인데 페이지가 따로 없나요?</h3><p>정자1·2·3동은 같은 생활권이라 정자동 페이지에서 통합 안내합니다. 예약 시 도로명 주소만 정확히 알려주시면 됩니다.</p></div>
<div class="faq-item"><h3>광교산 자락 외곽도 방문되나요?</h3><p>파장동·연무동을 포함한 장안구 전역이 방문 범위입니다. 외곽 주택가는 큰길 기준 진입 방향을 함께 알려주시면 도착이 빨라집니다.</p></div>
</section>
""" + PRICING + _CTA,
}

GWONSEON = {
    "path": "gyeonggi/suwon/gwonseon-gu/",
    "title": "권선구 출장마사지｜권선·호매실·고색 생활권 안내",
    "desc": "권선구 출장마사지 예약 전 권선동, 호매실, 금곡, 고색, 오목천 생활권을 확인하세요.",
    "h1": "권선구 출장마사지·홈타이 지역 안내",
    "breadcrumb": [("구별 안내", "/gyeonggi/suwon/"), ("권선구", None)],
    "body": f"""
<p class="lead">권선구는 수원 서남부의 주거·산업 생활권입니다. 권선동, 세류동, 금곡동, 호매실동, 고색동, 오목천동, 구운동, 서둔동, 곡선동을 중심으로 안내합니다.</p>

<section>
<h2>권선구 생활권 특징</h2>
<p>권선구는 수원역 서쪽으로 펼쳐지는 서남부 생활권입니다. 권선동은 수원시청역과 매탄권선역 사이의 주거·상권 지역이고, 세류동은 세류역과 수원역 남부를 잇습니다. 호매실동과 금곡동은 신축 아파트가 들어선 서수원 주거지로 최근 거주 세대가 빠르게 늘었고, 고색동과 오목천동은 수원델타플렉스 산업단지와 주거지가 섞인 수인분당선 역세권 생활권입니다. 같은 권선구라도 호매실 신도시와 고색 산업권, 권선동 도심권은 생활 리듬이 달라 안내도 동별로 구분합니다.</p>
</section>

<section>
<h2>권선구 대표 동</h2>
{_grid([
    ("권선동", "/gyeonggi/suwon/gwonseon-gu/gwonseon-dong/"),
    ("세류동", "/gyeonggi/suwon/gwonseon-gu/seryu-dong/"),
    ("금곡동", "/gyeonggi/suwon/gwonseon-gu/geumgok-dong/"),
    ("호매실동", "/gyeonggi/suwon/gwonseon-gu/homaesil-dong/"),
    ("고색동", "/gyeonggi/suwon/gwonseon-gu/gosaek-dong/"),
    ("오목천동", "/gyeonggi/suwon/gwonseon-gu/omokcheon-dong/"),
    ("구운동", "/gyeonggi/suwon/gwonseon-gu/guun-dong/"),
    ("서둔동", "/gyeonggi/suwon/gwonseon-gu/seodun-dong/"),
    ("곡선동", "/gyeonggi/suwon/gwonseon-gu/gokseon-dong/"),
])}
<p>권선1·2동은 권선동 페이지로, 세류1·2·3동은 세류동 페이지로 통합 안내합니다. 호매실동과 금곡동은 같은 서수원이라도 호매실은 지구 중심, 금곡은 주거·상권 인접권으로 나누어 설명합니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>권선구에는 수인분당선 <a href="/gyeonggi/suwon/station/gosaek-station/">고색역</a>과 <a href="/gyeonggi/suwon/station/omokcheon-station/">오목천역</a>, <a href="/gyeonggi/suwon/station/seryu-station/">세류역</a>이 지나고, 권선동은 <a href="/gyeonggi/suwon/station/suwon-cityhall-station/">수원시청역</a>·<a href="/gyeonggi/suwon/station/maetan-gwonseon-station/">매탄권선역</a> 생활권과 가깝습니다. 호매실·금곡은 역과 다소 떨어진 버스 생활권이라 큰길 기준 위치를 함께 알려주시면 좋습니다.</p>
</section>

<section>
<h2>생활권으로 함께 보기</h2>
<p>호매실동과 금곡동을 묶은 <a href="/gyeonggi/suwon/area/homaesil-geumgok/">호매실·금곡 생활권</a>, 고색동과 오목천동을 묶은 <a href="/gyeonggi/suwon/area/gosaek-omokcheon/">고색·오목천 생활권</a>, 권선동과 매탄동을 잇는 <a href="/gyeonggi/suwon/area/gwonseon-maetan/">권선·매탄 생활권</a> 안내가 있습니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>호매실·금곡 신축 단지는 방문 차량 등록이 필요한 곳이 있으니 단지명과 동·호수를 미리 알려주세요. 고색·오목천 산업권 인근은 야간 도로 사정이 바뀌는 구간이 있어 현재 사용하는 출입구 기준으로 위치를 설명해 주시면 정확합니다. 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>을 참고하세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item"><h3>호매실과 금곡은 같은 동네 아닌가요?</h3><p>두 곳 모두 서수원 생활권이지만 호매실은 지구 중심, 금곡은 주거·상권 인접권으로 분위기가 달라 페이지를 나누어 안내합니다.</p></div>
<div class="faq-item"><h3>고색 산업단지 쪽도 방문되나요?</h3><p>고색동·오목천동을 포함한 권선구 전역이 방문 범위입니다. 업무 공간이라면 출입 절차와 가능 시간대를 함께 알려주세요.</p></div>
</section>
""" + PRICING + _CTA,
}

PALDAL = {
    "path": "gyeonggi/suwon/paldal-gu/",
    "title": "팔달구 출장마사지｜수원역·인계동·행궁동 생활권 안내",
    "desc": "팔달구 출장마사지 이용 전 수원역, 인계동, 행궁동, 매교동 생활권을 확인하세요.",
    "h1": "팔달구 출장마사지·홈타이 지역 안내",
    "breadcrumb": [("구별 안내", "/gyeonggi/suwon/"), ("팔달구", None)],
    "body": f"""
<p class="lead">팔달구는 수원의 원도심과 중심 상권이 함께 있는 지역입니다. 인계동, 매산동, 매교동, 고등동, 화서동, 행궁동, 우만동, 지동을 중심으로 안내합니다.</p>

<section>
<h2>팔달구 생활권 특징</h2>
<p>팔달구는 수원에서 검색 의도가 가장 강한 중심 생활권입니다. 인계동은 수원시청과 나혜석거리를 낀 수원 최대 중심상권이고, 매산동은 수원역과 로데오거리를 품은 원도심 상권입니다. 행궁동은 팔달문과 수원화성을 둘러싼 관광·주거 생활권이며, 매교동은 매교역과 원도심 재개발 단지가 이어집니다. 화서동은 화서역과 주거지, 우만동은 아주대 인접 주거지로 성격이 갈립니다. 중심상권·원도심·관광지가 한 구에 모여 있어 자택뿐 아니라 오피스텔·숙소 방문 비중이 높은 것이 팔달구의 특징입니다.</p>
</section>

<section>
<h2>팔달구 대표 동</h2>
{_grid([
    ("인계동", "/gyeonggi/suwon/paldal-gu/ingye-dong/"),
    ("매산동", "/gyeonggi/suwon/paldal-gu/maesan-dong/"),
    ("매교동", "/gyeonggi/suwon/paldal-gu/maegyo-dong/"),
    ("고등동", "/gyeonggi/suwon/paldal-gu/godeung-dong/"),
    ("화서동", "/gyeonggi/suwon/paldal-gu/hwaseo-dong/"),
    ("행궁동", "/gyeonggi/suwon/paldal-gu/haenggung-dong/"),
    ("우만동", "/gyeonggi/suwon/paldal-gu/uman-dong/"),
    ("지동", "/gyeonggi/suwon/paldal-gu/ji-dong/"),
])}
<p>화서1·2동은 화서동 페이지로, 우만1·2동은 우만동 페이지로 통합 안내합니다. 수원역 페이지와 매산동 페이지, 수원시청역 페이지와 인계동 페이지는 역세권 기준과 상권 기준으로 역할을 나누어 작성했습니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>팔달구에는 수원의 관문 <a href="/gyeonggi/suwon/station/suwon-station/">수원역</a>과 <a href="/gyeonggi/suwon/station/suwon-cityhall-station/">수원시청역</a>, <a href="/gyeonggi/suwon/station/maegyo-station/">매교역</a>, <a href="/gyeonggi/suwon/station/hwaseo-station/">화서역</a>이 지납니다. 인계동은 수원시청역, 매산동은 수원역, 행궁동은 매교역·팔달문 방면으로 위치를 설명하면 편합니다.</p>
</section>

<section>
<h2>생활권으로 함께 보기</h2>
<p>수원역과 매산동을 묶은 <a href="/gyeonggi/suwon/area/suwon-station-maesan/">수원역·매산동 생활권</a>, 인계동과 수원시청을 묶은 <a href="/gyeonggi/suwon/area/ingye-cityhall/">인계동·수원시청 생활권</a>, 팔달문과 행궁동을 묶은 <a href="/gyeonggi/suwon/area/paldalmun-haenggung/">팔달문·행궁동 생활권</a> 안내가 있습니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>인계동·매산동 일대는 오피스텔과 숙소가 많아 건물명과 호실, 외부인 출입 절차를 함께 알려주시면 도착이 정확합니다. 행궁동은 관광지 인근 골목이 좁은 구간이 있어 큰길 기준 진입 방향이 도움이 됩니다. 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>에서 확인하세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item"><h3>수원역과 매산동은 같은 안내인가요?</h3><p>아닙니다. 수원역 페이지는 역세권·이동 기준, 매산동 페이지는 원도심 상권·주거 기준으로 역할을 나누어 작성했습니다.</p></div>
<div class="faq-item"><h3>행궁동 숙소로도 방문되나요?</h3><p>행궁동을 포함한 팔달구 전역이 방문 범위입니다. 숙소는 호실과 프런트 경유 여부를 함께 알려주세요.</p></div>
</section>
""" + PRICING + _CTA,
}

YEONGTONG = {
    "path": "gyeonggi/suwon/yeongtong-gu/",
    "title": "영통구 출장마사지｜영통·망포·광교 생활권 안내",
    "desc": "영통구 출장마사지 예약 전 영통동, 망포동, 매탄동, 광교 생활권을 확인하세요.",
    "h1": "영통구 출장마사지·홈타이 지역 안내",
    "breadcrumb": [("구별 안내", "/gyeonggi/suwon/"), ("영통구", None)],
    "body": f"""
<p class="lead">영통구는 수원 동부와 광교·영통·망포 생활권이 강한 지역입니다. 영통동, 망포동, 매탄동, 원천동, 광교동, 이의동, 하동, 신동을 중심으로 안내합니다.</p>

<section>
<h2>영통구 생활권 특징</h2>
<p>영통구는 수원 동부의 신도시·주거 생활권입니다. 영통동은 영통역과 청명역을 낀 동수원 대표 주거·상권 지역이고, 망포동은 망포역을 중심으로 화성 경계까지 이어지는 신축 주거지입니다. 매탄동은 매탄권선역과 삼성전자 인근 생활권, 원천동은 아주대와 광교호수공원 인접권입니다. 광교동은 광교중앙역·광교역·광교호수공원을 품은 신도시 생활권으로, 이의동·하동과 함께 묶입니다. 신도시 아파트와 오피스텔이 많아 방문 동선이 비교적 정형화되어 있는 것이 영통구의 특징입니다.</p>
</section>

<section>
<h2>영통구 대표 동</h2>
{_grid([
    ("영통동", "/gyeonggi/suwon/yeongtong-gu/yeongtong-dong/"),
    ("망포동", "/gyeonggi/suwon/yeongtong-gu/mangpo-dong/"),
    ("매탄동", "/gyeonggi/suwon/yeongtong-gu/maetan-dong/"),
    ("원천동", "/gyeonggi/suwon/yeongtong-gu/woncheon-dong/"),
    ("광교동", "/gyeonggi/suwon/yeongtong-gu/gwanggyo-dong/"),
    ("이의동", "/gyeonggi/suwon/yeongtong-gu/iui-dong/"),
    ("하동", "/gyeonggi/suwon/yeongtong-gu/ha-dong/"),
    ("신동", "/gyeonggi/suwon/yeongtong-gu/sin-dong/"),
])}
<p>영통1·2·3동은 영통동 페이지로, 매탄1~4동은 매탄동 페이지로, 망포1·2동은 망포동 페이지로, 광교1·2동은 광교동 페이지로 통합 안내합니다. 영통동 페이지와 영통역 페이지, 광교동 페이지와 광교중앙역 페이지는 생활권 기준과 역세권 기준으로 역할을 나누었습니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>영통구에는 수인분당선 <a href="/gyeonggi/suwon/station/yeongtong-station/">영통역</a>·<a href="/gyeonggi/suwon/station/mangpo-station/">망포역</a>·<a href="/gyeonggi/suwon/station/cheongmyeong-station/">청명역</a>·<a href="/gyeonggi/suwon/station/maetan-gwonseon-station/">매탄권선역</a>과 신분당선 <a href="/gyeonggi/suwon/station/gwanggyo-jungang-station/">광교중앙역</a>·<a href="/gyeonggi/suwon/station/gwanggyo-station/">광교역</a>이 지납니다. 동마다 가까운 역이 분명해 위치 설명이 비교적 쉬운 편입니다.</p>
</section>

<section>
<h2>생활권으로 함께 보기</h2>
<p>영통동과 망포동을 묶은 <a href="/gyeonggi/suwon/area/yeongtong-mangpo/">영통·망포 생활권</a>, 광교중앙역과 광교를 묶은 <a href="/gyeonggi/suwon/area/gwanggyo-jungang/">광교중앙·광교 생활권</a>, 원천동과 아주대를 묶은 <a href="/gyeonggi/suwon/area/woncheon-ajou-univ/">원천·아주대 생활권</a>, <a href="/gyeonggi/suwon/area/gwanggyo-lake-park/">광교호수공원 생활권</a> 안내가 있습니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>영통·광교 신도시 아파트는 공동현관 호출과 방문 차량 등록 확인이 가장 중요합니다. 단지명과 동·호수를 정확히 알려주시면 도착이 빠릅니다. 망포·광교는 화성·용인과 맞닿은 경계 구역이 있으나 수원시 영통구 주소 기준으로 안내합니다. 준비사항은 <a href="/gyeonggi/suwon/check/">이용 전 확인사항</a>을 참고하세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item"><h3>광교동과 광교중앙역은 같은 안내인가요?</h3><p>아닙니다. 광교동 페이지는 신도시 전체 생활권, 광교중앙역 페이지는 역세권 이동 기준으로 역할을 나누어 작성했습니다.</p></div>
<div class="faq-item"><h3>망포동인데 화성과 가까운 끝자락도 되나요?</h3><p>수원시 영통구 망포동 주소라면 모두 방문 범위입니다. 경계 너머 인접 지역은 위치에 따라 가능할 수 있으니 전화로 확인해 주세요.</p></div>
</section>
""" + PRICING + _CTA,
}

PAGES = [HUB, JANGAN, GWONSEON, PALDAL, YEONGTONG]
