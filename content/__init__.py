# 전체 페이지 목록 집계 — 수원시 출장마사지·홈타이
from . import main, districts, areas, stations, zones, info, about

PAGES = (
    [main.PAGE]
    + districts.PAGES
    + areas.PAGES
    + stations.PAGES
    + zones.PAGES
    + info.PAGES
    + [about.PAGE]
)
