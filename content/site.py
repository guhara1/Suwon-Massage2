# 사이트 공통 설정 — 수원시 출장마사지·홈타이 안내
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.suwon-massage.example.com"

BRAND = "바로 GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 외부 문의 채널 (텔레그램)
TELEGRAM_BUILD = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"  # 제휴문의

# 지역 기준 경로 — 경기도 수원시
SUWON = "/gyeonggi/suwon/"

# 상단 메뉴 — 하위 메뉴에는 키워드("출장마사지")를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("구별 안내", "/gyeonggi/suwon/", [
        ("수원시 전체", "/gyeonggi/suwon/"),
        ("장안구", "/gyeonggi/suwon/jangan-gu/"),
        ("권선구", "/gyeonggi/suwon/gwonseon-gu/"),
        ("팔달구", "/gyeonggi/suwon/paldal-gu/"),
        ("영통구", "/gyeonggi/suwon/yeongtong-gu/"),
    ]),
    ("지역별 안내", "/gyeonggi/suwon/areas/", [
        ("지역 전체", "/gyeonggi/suwon/areas/"),
        ("정자동", "/gyeonggi/suwon/jangan-gu/jeongja-dong/"),
        ("천천동", "/gyeonggi/suwon/jangan-gu/cheoncheon-dong/"),
        ("율천동", "/gyeonggi/suwon/jangan-gu/yulcheon-dong/"),
        ("조원동", "/gyeonggi/suwon/jangan-gu/jowon-dong/"),
        ("권선동", "/gyeonggi/suwon/gwonseon-gu/gwonseon-dong/"),
        ("호매실동", "/gyeonggi/suwon/gwonseon-gu/homaesil-dong/"),
        ("금곡동", "/gyeonggi/suwon/gwonseon-gu/geumgok-dong/"),
        ("고색동", "/gyeonggi/suwon/gwonseon-gu/gosaek-dong/"),
        ("세류동", "/gyeonggi/suwon/gwonseon-gu/seryu-dong/"),
        ("인계동", "/gyeonggi/suwon/paldal-gu/ingye-dong/"),
        ("매산동", "/gyeonggi/suwon/paldal-gu/maesan-dong/"),
        ("행궁동", "/gyeonggi/suwon/paldal-gu/haenggung-dong/"),
        ("매교동", "/gyeonggi/suwon/paldal-gu/maegyo-dong/"),
        ("영통동", "/gyeonggi/suwon/yeongtong-gu/yeongtong-dong/"),
        ("망포동", "/gyeonggi/suwon/yeongtong-gu/mangpo-dong/"),
        ("매탄동", "/gyeonggi/suwon/yeongtong-gu/maetan-dong/"),
        ("원천동", "/gyeonggi/suwon/yeongtong-gu/woncheon-dong/"),
        ("광교동", "/gyeonggi/suwon/yeongtong-gu/gwanggyo-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/suwon/station/", [
        ("역 전체", "/gyeonggi/suwon/station/"),
        ("수원역", "/gyeonggi/suwon/station/suwon-station/"),
        ("화서역", "/gyeonggi/suwon/station/hwaseo-station/"),
        ("성균관대역", "/gyeonggi/suwon/station/sungkyunkwan-univ-station/"),
        ("매교역", "/gyeonggi/suwon/station/maegyo-station/"),
        ("수원시청역", "/gyeonggi/suwon/station/suwon-cityhall-station/"),
        ("매탄권선역", "/gyeonggi/suwon/station/maetan-gwonseon-station/"),
        ("망포역", "/gyeonggi/suwon/station/mangpo-station/"),
        ("영통역", "/gyeonggi/suwon/station/yeongtong-station/"),
        ("청명역", "/gyeonggi/suwon/station/cheongmyeong-station/"),
        ("광교중앙역", "/gyeonggi/suwon/station/gwanggyo-jungang-station/"),
        ("광교역", "/gyeonggi/suwon/station/gwanggyo-station/"),
        ("세류역", "/gyeonggi/suwon/station/seryu-station/"),
        ("고색역", "/gyeonggi/suwon/station/gosaek-station/"),
        ("오목천역", "/gyeonggi/suwon/station/omokcheon-station/"),
    ]),
    ("생활권 안내", "/gyeonggi/suwon/area/", [
        ("생활권 전체", "/gyeonggi/suwon/area/"),
        ("수원역·매산동", "/gyeonggi/suwon/area/suwon-station-maesan/"),
        ("인계동·수원시청", "/gyeonggi/suwon/area/ingye-cityhall/"),
        ("권선·매탄", "/gyeonggi/suwon/area/gwonseon-maetan/"),
        ("영통·망포", "/gyeonggi/suwon/area/yeongtong-mangpo/"),
        ("광교중앙·광교", "/gyeonggi/suwon/area/gwanggyo-jungang/"),
        ("정자·천천", "/gyeonggi/suwon/area/jeongja-cheoncheon/"),
        ("성균관대·율천", "/gyeonggi/suwon/area/sungkyunkwan-yulcheon/"),
        ("화서·고등", "/gyeonggi/suwon/area/hwaseo-godeung/"),
        ("호매실·금곡", "/gyeonggi/suwon/area/homaesil-geumgok/"),
        ("고색·오목천", "/gyeonggi/suwon/area/gosaek-omokcheon/"),
        ("팔달문·행궁동", "/gyeonggi/suwon/area/paldalmun-haenggung/"),
        ("원천·아주대", "/gyeonggi/suwon/area/woncheon-ajou-univ/"),
        ("광교호수공원", "/gyeonggi/suwon/area/gwanggyo-lake-park/"),
    ]),
    ("예약 안내", "/gyeonggi/suwon/reservation/", [
        ("예약 방법", "/gyeonggi/suwon/reservation/#how"),
        ("예약 가능 시간", "/gyeonggi/suwon/reservation/#hours"),
        ("방문 가능 장소", "/gyeonggi/suwon/reservation/#place"),
        ("추가 이동비 안내", "/gyeonggi/suwon/reservation/#fee"),
        ("결제·변경·취소", "/gyeonggi/suwon/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/gyeonggi/suwon/check/", [
        ("방문 가능 주소 확인", "/gyeonggi/suwon/check/#address"),
        ("자택 이용 전 확인", "/gyeonggi/suwon/check/#home"),
        ("숙소·오피스텔 확인", "/gyeonggi/suwon/check/#hotel"),
        ("개인정보 처리 기준", "/gyeonggi/suwon/check/#privacy"),
        ("고객 안전 안내", "/gyeonggi/suwon/check/#safety"),
    ]),
    ("홈타이 이용 가이드", "/gyeonggi/suwon/hometai-guide/", [
        ("홈타이란?", "/gyeonggi/suwon/hometai-guide/#what"),
        ("출장마사지와 차이", "/gyeonggi/suwon/hometai-guide/#diff"),
        ("이용 전 기준", "/gyeonggi/suwon/hometai-guide/#standard"),
        ("처음 이용 안내", "/gyeonggi/suwon/hometai-guide/#first"),
    ]),
    ("고객센터", "/gyeonggi/suwon/support/", [
        ("자주 묻는 질문", "/gyeonggi/suwon/support/#faq"),
        ("문의하기", "/gyeonggi/suwon/support/#contact"),
        ("운영 기준", "/gyeonggi/suwon/support/#policy"),
        ("사이트 소개", "/gyeonggi/suwon/about/"),
        ("개인정보 처리방침", "/gyeonggi/suwon/privacy/"),
        ("이용약관", "/gyeonggi/suwon/terms/"),
    ]),
]
