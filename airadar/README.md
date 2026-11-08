# airadar

AI 뉴스 자동 수집 → 이메일 다이제스트 → X/Threads 자동 포스팅 파이프라인.

## 구조

```
RSS/HN 수집 ──► SQLite (중복 제거) ──┬─► 이메일 다이제스트 (본인에게)
                                   └─► 점수 상위 항목 자동 포스팅 (X/Threads)
```

- 니치 키워드(딥페이크·C2PA·워터마크 등)가 붙은 기사에 +점수 → 자동 포스팅은 `min_score_to_post` 이상만
- `dry_run: true` 상태에선 실제 발송/포스팅 없이 출력만 — 테스트용

## 설치

```bash
cd airadar
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 값 채우기
```

## 사용

```bash
set -a && source .env && set +a

python -m airadar collect   # 수집만
python -m airadar save      # 수집 + 마크다운 저장 (digests/)
python -m airadar digest    # 이메일 다이제스트
python -m airadar post      # 자동 포스팅
python -m airadar run       # 전부 (스케줄러용)
python -m airadar status    # 통계
python -m airadar formats   # 포맷별 미리보기
python -m airadar preview   # 발행 예정 HTML 미리보기
python -m airadar weekly    # 주간 성과 리포트 이메일
python -m airadar ideas     # 뻘글/잡담 소재 뽑기
python -m airadar metrics   # 발행 글 반응 수집 (Bluesky)
python -m airadar report    # 포맷별 발행 로그
```

## 포맷 실험 (A/B)

같은 기사를 6가지 스타일로 발행하고, 어떤 포맷이 먹히는지 비교할 수 있습니다.
자동 발행 시 "오늘 가장 적게 쓴 포맷"을 자동 선택해 고르게 분배됩니다.

| 포맷 | 내용 |
|---|---|
| `headline` | 제목+링크 (봇 스타일) |
| `tldr` | 한줄 요약 첨부 |
| `hottake` | 짧은 한줄평 + 제목 |
| `question` | 질문형 (참여 유도) |
| `bookmark` | 저장 유도형 |
| `thread` | 훅→요약→링크 3파트 스레드 |

모든 발행은 `posts` 테이블에 포맷·플랫폼·remote_id와 함께 기록됩니다.
`report`로 로그를 보고, X/Threads 앱에서 각 포스트의 반응(좋아요·조회수)을 대조하면
어떤 포맷이 잘 되는지 확인할 수 있습니다. 포맷 추가는 `airadar/drafter.py`의
`FORMATS`에 함수 하나만 넣으면 됩니다.

## 추가 기능

- **카드 이미지**: `card_images: true`면 포스트에 제목 카드 자동 첨부 (X/Bluesky/Mastodon)
- **LLM 해설**: `use_llm: true` + `ANTHROPIC_API_KEY` 또는 `OPENAI_API_KEY` → hottake 포맷이 AI 생성 한줄평으로
- **주간 리포트**: `weekly_report_day` 요일에 `run` 시 포맷/플랫폼별 집계 이메일
- **미리보기**: `python -m airadar preview` → `preview.html` (발행 예정 글 + 카드 확인)
- **소재 뽑기**: `python -m airadar ideas` → 뻘글/잡담 주제
- **반응 수집**: `python -m airadar metrics` → Bluesky 발행분 좋아요/리포스트 집계 (X는 무료 API 읽기 제한으로 수동 확인)
- **소재 뱅크**: `CONTENT_BANK.md` — 직접 쓸 글감 목록

## 플랫폼별 준비물

| 플랫폼 | 비용 | 준비 |
|---|---|---|
| X | 무료(쓰기 500/월) | developer.x.com 앱 + 키 4개 |
| Bluesky | 무료 | 앱 비밀번호 (설정 → App Passwords) |
| Threads | 무료 | Meta 개발자 앱 + 장기 토큰 |
| Mastodon | 무료 | 인스턴스 → 개발 → 액세스 토큰 |
| 이메일 | 무료 | Gmail 앱 비밀번호 |

## 인증 설정

### 이메일 (Gmail)
1. Google 계정 → 보안 → 2단계 인증 활성화
2. "앱 비밀번호" 생성 → `AIRADAR_SMTP_PASSWORD`에 입력

### X API
1. developer.x.com에서 Free 플랜 앱 생성 (월 500건, 1일 ~17건 제한, 쓰기 전용)
2. 앱 권한을 Read+Write로, 키 4개를 `.env`에 입력
3. **자동화 계정은 X 규정상 프로필에 봇임을 명시해야 함** — bio에 "자동 포스팅 봇" 등 추가 권장

### Threads API
1. developers.facebook.com에서 앱 생성 → Threads API 추가
2. 포스팅할 계정의 Threads 사용자 인증 → `THREADS_USER_ID`, 장기 액세스 토큰 발급
3. 참고: Threads는 뻘글 섞는 본계정에 자동포스팅하면 어색할 수 있음 — 별도 계정 권장

## 자동 실행 (launchd, 4시간마다)

`com.airadar.daily.plist`는 이름과 달리 `StartInterval` 14400초(4시간) 간격으로
실행됩니다. 간격을 바꾸려면 plist의 `StartInterval` 값을 수정하세요.

```bash
# plist 템플릿 경로 확인 후:
cp com.airadar.daily.plist ~/Library/LaunchAgents/
# plist 안의 /PATH/TO/airadar를 실제 경로로 수정
launchctl load ~/Library/LaunchAgents/com.airadar.daily.plist
```

## 안전장치

- `max_posts_per_run`: 실행당 포스팅 상한
- `min_score_to_post`: 무관한 뉴스 자동 발행 방지
- SQLite dedup: 같은 링크 두 번 안 올림
- `dry_run`: 설정 잘못해도 실발행 안 함

## 주의

완전 자동 포스팅은 계정 품질 리스크가 있습니다. 제목만 갖고 올리므로 내용 오류·중복 주제·저품질 기사가 그대로 나갈 수 있습니다. 처음 1~2주는 `dry_run` 또는 이메일만으로 운영하면서 출력 품질을 확인한 뒤 실발행을 켜세요.
