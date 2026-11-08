# 🛰️ lazyradar: Global AI Tech Radar & 5-Nation Top 20

> **레이지 시리즈 공식 글로벌 AI 기술 레이더 (Lazy Series Official Tech Radar)**
> 미국·중국·대한민국·유럽·일본 5대 주요국 Top 20 랭킹 분과 및 전 세계 100선 큐레이션 랭킹
> 매주 월요일 09:00 KST, GitHub Actions가 큐레이션된 100개 레포지토리의 Stars/Forks/최근 커밋 지표를 갱신해 순위를 다시 계산하고, Search API로 신규 후보를 제안합니다.

[![Weekly lazyradar Sync & Leaderboard](https://github.com/daeryundf2-prog/lazyradar/actions/workflows/weekly-sync.yml/badge.svg)](https://github.com/daeryundf2-prog/lazyradar/actions/workflows/weekly-sync.yml) 
![Last Synced](https://img.shields.io/badge/Last%20Synced-2026-11-02%2005:21%20UTC-blue) 
![Tracked Repos](https://img.shields.io/badge/Tracked%20Repositories-100-success) 
![5 Nations](https://img.shields.io/badge/Major%20Nations-US%20|%20CN%20|%20KR%20|%20EU%20|%20JP-purple) 
![Lazy Series](https://img.shields.io/badge/Lazy%20Series-Official%20Radar-orange) 
![Weekly Cron](https://img.shields.io/badge/Sync%20Schedule-Every%20Monday%2009:00%20KST-green)

---

## 🌍 5대 주요국별 바로가기

1. [🇺🇸 미국 (United States) Top 20](#cntry-us)
2. [🇨🇳 중국 (China) Top 20](#cntry-cn)
3. [🇰🇷 대한민국 (South Korea) Top 20](#cntry-kr)
4. [🇪🇺 유럽 (Europe) Top 20](#cntry-eu)
5. [🇯🇵 일본 (Japan) Top 20](#cntry-jp)
6. [🏆 전 세계 100선 통합 랭킹 (Global Top 100)](#global-top-100)

---

## 🗺️ 1. 주요 5대국별 Top 20 랭킹 분과

<a id="cntry-us"></a>
### 🇺🇸 미국 (United States) Top 20

| 국가순위 | 통합순위 | 상태 | 도구/프로젝트명 | 개발/조직 | 호환 모델 | Stars | Forks | 활동 점수 | 핵심 설명 및 실무 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `#01` | 🔥 Hot | **openclaw** | openclaw | `Llama 3.3 / Multi-LLM` | ⭐ `393,667` | 🍴 `82,734` | **80.79** | **2026년 급부상한 범용 제너럴리스트 에이전트. 랍스터(Lobster) 아키텍처 기반 자율 태스크 분기**<br>👉 *복잡한 웹 탐색, 코드 수정, 파일 시스템 조작을 단일 목표 지시로 자율 완결할 때* | [GitHub](https://github.com/openclaw/openclaw) |
| **#02** | `#02` | 🔥 Hot | **hermes-agent** | NousResearch | `Hermes 3 / Claude Code / Codex` | ⭐ `259,574` | 🍴 `57,129` | **78.66** | **자율적인 스킬 학습 및 영구 누적을 특징으로 하는 적응형 에이전트 하네스**<br>👉 *세션을 거듭할수록 팀의 특정 도메인 워크플로우에 맞춰 스스로 스킬을 학습하게 할 때* | [GitHub](https://github.com/nousresearch/hermes-agent) |
| **#03** | `#05` | 🔥 Hot | **AutoGPT** | Significant-Gravitas | `Multi-LLM` | ⭐ `187,861` | 🍴 `45,901` | **77.06** | **자율 에이전트의 시초이자 현재는 에이전트 빌더, 블록 기반 워크플로우, 벤치마킹을 아우르는 오픈 플랫폼**<br>👉 *다양한 모델의 자율 문제 해결 성공률을 표준 벤치마크로 측정할 때* | [GitHub](https://github.com/Significant-Gravitas/AutoGPT) |
| **#04** | `#07` | 🔥 Hot | **ollama** | Ollama Official | `Llama, Qwen, DeepSeek, Mistral` | ⭐ `185,620` | 🍴 `18,857` | **76.24** | **Mac, Linux, Windows에서 Llama, Qwen, DeepSeek 오픈 모델을 한 줄 명령으로 다운로드 및 실행하는 사실상 글로벌 표준**<br>👉 *로컬 개발 환경에서 GPU 가속을 활용해 오프라인 LLM 서빙 및 로컬 에이전트 백엔드 구축* | [GitHub](https://github.com/ollama/ollama) |
| **#05** | `#09` | 🔥 Hot | **ComfyUI** | comfyanonymous | `Flux, SDXL, Video Diffusion` | ⭐ `144,523` | 🍴 `17,222` | **75.07** | **가장 강력하고 모듈화된 노드 기반 생성형 이미지/비디오 워크플로우 런타임. 에이전트 API 연동 표준**<br>👉 *AI 이미지/영상 생성 파이프라인을 완전 자동화된 백엔드 API로 래핑하여 에이전트와 결합할 때* | [GitHub](https://github.com/comfyanonymous/ComfyUI) |
| **#06** | `#10` | 🔥 Hot | **llama.cpp** | Georgi Gerganov | `GGUF Quantized Models` | ⭐ `133,101` | 🍴 `25,042` | **75.04** | **GGUF 양자화 포맷의 원조. 일반 CPU와 통합 메모리 GPU에서 대규모 모델을 돌릴 수 있게 만든 오픈 인프라**<br>👉 *Ollama, Jan, LM Studio 등 전 세계 모든 로컬 AI 앱의 핵심 구동 엔진* | [GitHub](https://github.com/ggerganov/llama.cpp) |
| **#07** | `#11` | 🔥 Hot | **browser-use** | browser-use | `Claude 3.7 / Multi-LLM` | ⭐ `119,788` | 🍴 `13,348` | **74.03** | **AI가 사람처럼 브라우저를 띄워 클릭, 스크롤, 양식 제출, 로그인, 데이터 수집을 완결하는 웹 에이전트**<br>👉 *API가 없는 웹사이트 예약, 티켓팅, 경쟁사 가격 모니터링, 웹 기반 SaaS 자동 조작* | [GitHub](https://github.com/browser-use/browser-use) |
| **#08** | `#12` | 🔥 Hot | **vllm** | UC Berkeley LMSYS | `All Open-weight LLMs` | ⭐ `96,096` | 🍴 `24,280` | **73.6** | **PagedAttention 기반으로 메모리 낭비를 없애고 처리량을 최대 24배 끌어올린 오픈소스 프로덕션 서빙 엔진**<br>👉 *대규모 사내 서빙 클러스터에서 수백 명의 동시 에이전트 요청을 고속 처리할 때* | [GitHub](https://github.com/vllm-project/vllm) |
| **#09** | `#17` | 🔥 Hot | **mem0** | Mem0 Official | `Multi-LLM / Graph + Vector` | ⭐ `68,258` | 🍴 `8,099` | **71.16** | **사용자의 과거 대화, 선호도, 사실 관계를 지속적으로 갱신하고 인덱싱하는 개인화 메모리 레이어**<br>👉 *모든 에이전트 애플리케이션에 '사용자를 기억하는 영구 기억 장치'를 1줄 코드로 추가할 때* | [GitHub](https://github.com/mem0ai/mem0) |
| **#10** | `#19` | 🔥 Hot | **crewAI** | CrewAI Official | `Multi-LLM / Claude / OpenAI` | ⭐ `60,398` | 🍴 `8,998` | **70.72** | **기획자, 리서처, 작가 등 명확한 직책(Role)과 목표(Goal)를 부여해 가상의 팀을 조직하는 에이전트 프레임워크**<br>👉 *시장 조사 보고서 작성, 뉴스레터 발행 파이프라인을 3~4명의 전문 가상 직원 팀으로 실행* | [GitHub](https://github.com/crewAIInc/crewAI) |
| **#11** | `#20` | 🔥 Hot | **llama_index** | LlamaIndex Official | `Multi-LLM` | ⭐ `52,776` | 🍴 `8,495` | **70.08** | **PDF, 노션, DB 등 방대한 비정형 데이터를 에이전트가 탐색 가능한 인덱스로 연결하는 RAG 표준**<br>👉 *사내 위키, 고객지원 문서, API 문서를 에이전트의 지식 베이스로 공급할 때* | [GitHub](https://github.com/run-llama/llama_index) |
| **#12** | `#21` | 🔥 Hot | **whisper.cpp** | Georgi Gerganov | `OpenAI Whisper` | ⭐ `54,850` | 🍴 `6,264` | **69.99** | **C/C++로 밑바닥부터 재작성된 Whisper 추론 엔진. Apple Silicon Metal 가속으로 실시간 자막 전사 지원**<br>👉 *맥북이나 경량 엣지 디바이스에서 100% 오프라인 고속 음성 인식* | [GitHub](https://github.com/ggerganov/whisper.cpp) |
| **#13** | `#23` | 🔥 Hot | **langgraph** | LangChain Official | `Multi-LLM` | ⭐ `44,303` | 🍴 `7,620` | **69.23** | **상태(State)를 기반으로 순환 루프, 분기 조건, 인간 개입(Human-in-the-loop)을 정의하는 엔터프라이즈 에이전트 표준**<br>👉 *승인 단계가 필요한 결재 시스템, 실패 시 재시도하는 복합 에이전트 워크플로우 개발* | [GitHub](https://github.com/langchain-ai/langgraph) |
| **#14** | `#24` | 🔥 Hot | **sglang** | LMSYS Org | `DeepSeek / Llama / Qwen` | ⭐ `38,358` | 🍴 `10,069` | **68.84** | **복잡한 에이전트 툴 호출과 다단계 추론에서 반복되는 KV 캐시를 Radix 트리로 공유해 레이턴시를 5배 단축**<br>👉 *다단계 검색 및 CoT 추론을 반복하는 복잡한 에이전트의 응답 지연 극소화* | [GitHub](https://github.com/sgl-project/sglang) |
| **#15** | `#25` | 🔥 Hot | **CopilotKit** | CopilotKit Official | `Multi-LLM` | ⭐ `38,457` | 🍴 `4,800` | **68.21** | **기존 웹앱에 사이드바 코파일럿, 텍스트 인라인 편집, 프론트엔드 작업 제어 액션을 5분 만에 붙여주는 툴킷**<br>👉 *사내 대시보드나 SaaS 앱에 사용자의 클릭/입력을 대신하는 인앱 AI 비서를 붙일 때* | [GitHub](https://github.com/CopilotKit/CopilotKit) |
| **#16** | `#26` | 🔥 Hot | **diffusers** | Hugging Face | `PyTorch / Latent Diffusion` | ⭐ `34,848` | 🍴 `7,447` | **68.17** | **Stable Diffusion, Flux, ControlNet 등 최신 확산 모델을 통일된 파이썬 API로 다루는 표준 라이브러리**<br>👉 *에이전트가 백엔드에서 이미지 인페인팅, 스타일 변환, 뎁스 기반 생성을 프로그래밍할 때* | [GitHub](https://github.com/huggingface/diffusers) |
| **#17** | `#27` | 🔥 Hot | **dspy** | Stanford NLP | `Multi-LLM / Open Models` | ⭐ `38,880` | 🍴 `3,473` | **67.98** | **휴리스틱 프롬프트 대신 알고리즘으로 모델 가중치와 프롬프트를 자동 컴파일/최적화하는 스탠퍼드 프레임워크**<br>👉 *RAG 파이프라인의 검색 정밀도와 답변 일관성을 수학적 평가 지표에 맞춰 자동 튜닝할 때* | [GitHub](https://github.com/stanfordnlp/dspy) |
| **#18** | `#34` | 🔥 Hot | **fastmcp** | jlowin (Prefect) | `Claude Desktop / Claude Code / MCP` | ⭐ `28,269` | 🍴 `2,551` | **66.33** | **FastAPI 스타일의 데코레이터 문법으로 고성능 Model Context Protocol(MCP) 서버를 10줄 만에 빌드**<br>👉 *사내 파이썬 함수와 데이터베이스를 Claude의 외부 도구로 즉시 등록할 때* | [GitHub](https://github.com/jlowin/fastmcp) |
| **#19** | `#46` | 💤 Stable | **aider** | Paul Gauthier (Aider) | `Multi-LLM` | ⭐ `49,888` | 🍴 `5,125` | **54.4** | **터미널에서 Git과 완벽 연동되어 자동 커밋 메시지, diff 패치, 파일 맵을 관리하는 1위 코딩 도구**<br>👉 *로컬 터미널에서 기존 Git 레포지토리를 직접 보며 페어 프로그래밍으로 기능 추가 및 디버깅* | [GitHub](https://github.com/Aider-AI/aider) |
| **#20** | `#53` | ✨ Fresh | **seamless-m4t** | Meta (Facebook Research) | `SeamlessM4T v2` | ⭐ `11,901` | 🍴 `1,188` | **49.91** | **아시아-태평양 수십 개 언어 간의 실시간 음성-음성, 음성-텍스트 다자간 통번역을 지원하는 유니버설 모델**<br>👉 *한-중-일-동남아 크로스보더 비즈니스 미팅 실시간 통역* | [GitHub](https://github.com/facebookresearch/seamless_communication) |

<a id="cntry-cn"></a>
### 🇨🇳 중국 (China) Top 20

| 국가순위 | 통합순위 | 상태 | 도구/프로젝트명 | 개발/조직 | 호환 모델 | Stars | Forks | 활동 점수 | 핵심 설명 및 실무 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `#03` | 🔥 Hot | **deepseek-harness** | deepseek-ai | `DeepSeek` | ⭐ `268,633` | 🍴 `32,609` | **78.32** | **Cordis 설계를 도입하여 모델, 툴, 세션, 루프 전부를 플러그인으로 갈아끼우는 프레임워크 독립형 하네스**<br>👉 *DeepSeek 기반의 경량·모듈형 자율 코딩 에이전트 환경 구축* | [GitHub](https://github.com/deepseek-ai/deepseek-harness) |
| **#02** | `#08` | 🔥 Hot | **dify** | LangGenius | `Multi-LLM / Plugin Architecture` | ⭐ `160,186` | 🍴 `25,329` | **75.85** | **비주얼 오케스트레이션, RAG 파이프라인, 에이전트 워크플로우를 완성형 웹 앱으로 즉시 배포하는 글로벌 리딩 플랫폼**<br>👉 *개발팀과 비개발팀이 협업하여 실서비스용 엔터프라이즈 AI 앱을 노코드로 운영할 때* | [GitHub](https://github.com/langgenius/dify) |
| **#03** | `#13` | 🔥 Hot | **ragflow** | Infiniflow | `Deep Document Understanding` | ⭐ `93,320` | 🍴 `11,203` | **72.8** | **문서의 템플릿과 레이아웃을 깊이 이해하여 표와 단락이 엉키지 않도록 청킹하는 차세대 오픈소스 RAG**<br>👉 *복잡한 서식의 매뉴얼과 정관에서 단 하나의 오류도 없이 정확한 조항을 검색할 때* | [GitHub](https://github.com/infiniflow/ragflow) |
| **#04** | `#15` | 🔥 Hot | **MinerU** | OpenDataLab | `All LLMs / RAG Platforms` | ⭐ `82,961` | 🍴 `6,867` | **71.86** | **복잡한 비정형 PDF, 오피스 문서, 학술 논문을 마크다운/JSON으로 완벽 추출하여 RAG 병목을 해결한 1위 도구**<br>👉 *다단 레이아웃, 복합 표, 수식이 엉킨 논문/보고서를 LLM이 읽기 완벽한 포맷으로 변환* | [GitHub](https://github.com/opendatalab/MinerU) |
| **#05** | `#28` | 🔥 Hot | **FastGPT** | labring | `Multi-LLM` | ⭐ `29,970` | 🍴 `7,361` | **67.5** | **데이터 전처리, 벡터 검색, 재순위화(Reranking)에 특화된 완성형 지식 베이스 질의응답 플랫폼**<br>👉 *사내 CS 문의 응대 및 방대한 제품 매뉴얼 기반 고정밀 자동 답변봇* | [GitHub](https://github.com/labring/FastGPT) |
| **#06** | `#30` | 🔥 Hot | **fish-speech** | Fish Audio | `Zero-shot TTS` | ⭐ `33,537` | 🍴 `2,918` | **67.19** | **영어, 중국어, 일본어, 한국어를 완벽 지원하는 고품질 제로샷 텍스트-음성 변환 오픈 엔진**<br>👉 *글로벌 타깃 버추얼 휴먼 및 게임 캐릭터의 고화질 음성 더빙* | [GitHub](https://github.com/fishaudio/fish-speech) |
| **#07** | `#32` | 🔥 Hot | **Qwen-Code** | Alibaba Cloud QwenLM | `Qwen 2.5 Coder` | ⭐ `28,871` | 🍴 `3,295` | **66.64** | **터미널에서 직접 실행되는 오픈소스 코딩 에이전트. Qwen-2.5-Coder의 최적화된 토크나이저와 도구 연동**<br>👉 *오픈 모델 기반의 독립된 사내 전용 코딩 비서 환경 배포* | [GitHub](https://github.com/QwenLM/Qwen-Code) |
| **#08** | `#35` | 🔥 Hot | **DB-GPT** | eosphoros-ai | `Multi-agent DB` | ⭐ `20,237` | 🍴 `3,000` | **65.02** | **데이터와 메타데이터의 외부 유출 없이 로컬 DB에 직접 쿼리를 날리고 시각화하는 프라이빗 데이터 에이전트**<br>👉 *사내 RDBMS, NoSQL, 웨어하우스에 대한 안전한 자연어 데이터 분석 및 보고서 작성* | [GitHub](https://github.com/eosphoros-ai/DB-GPT) |
| **#09** | `#36` | 🔥 Hot | **ktransformers** | Tsinghua & KVCache AI | `DeepSeek MoE` | ⭐ `19,649` | 🍴 `1,600` | **64.34** | **일반 데스크톱 GPU(예: RTX 4090) 1장으로 DeepSeek 671B MoE 모델을 실행시키는 혁신적인 CPU-GPU 오프로딩**<br>👉 *수천만 원대 H100 서버 없이 일반 데스크톱에서 최고 스펙의 DeepSeek 모델을 로컬 구동* | [GitHub](https://github.com/kvcache-ai/ktransformers) |
| **#10** | `#40` | ✨ Fresh | **PaddleOCR** | Baidu Official | `PaddlePaddle Engine` | ⭐ `92,093` | 🍴 `11,606` | **60.77** | **80개 이상 언어를 지원하는 초경량, 고정밀 산업용 OCR. 다단 표 및 영수증 텍스트 추출의 글로벌 최강자**<br>👉 *스캔 공문서, 영수증, 송장 자동 입력 파이프라인의 핵심 전처리 엔진* | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| **#11** | `#41` | 💤 Stable | **DeepSeek-V3** | deepseek-ai | `MoE Architecture` | ⭐ `104,710` | 🍴 `16,746` | **58.65** | **671B 총 파라미터 중 37B만 활성화하는 초고효율 MoE 아키텍처. 상용 최상위 모델과 대등한 벤치마크 기록**<br>👉 *사내 프라이빗 대규모 LLM 클러스터의 메인 범용 추론 백본* | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3) |
| **#12** | `#44` | 💤 Stable | **DeepSeek-R1** | deepseek-ai | `DeepSeek / Open-weight Frontier` | ⭐ `91,994` | 🍴 `11,669` | **57.77** | **글로벌 AI 씬을 뒤흔든 오픈 가중치 최고봉 추론 모델. 강화학습을 통해 OpenAI o1 수준의 수학/코딩 추론 달성**<br>👉 *복잡한 알고리즘 설계, 정밀 코드 디버깅 및 고난도 수학적 논리 전개* | [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) |
| **#13** | `#47` | 💤 Stable | **ChatTTS** | 2noise | `Speech Generation` | ⭐ `39,963` | 🍴 `4,245` | **53.27** | **인터랙티브 대화에 특화된 혁신적 음성 합성 모델. 말하는 도중 자연스러운 웃음, 호흡, 억양 표현**<br>👉 *대화형 AI 보이스 에이전트 및 오디오북, 팟캐스트 내레이션 제작* | [GitHub](https://github.com/2noise/ChatTTS) |
| **#14** | `#50` | 💤 Stable | **CosyVoice** | Alibaba NLP | `Multi-lingual Speech` | ⭐ `24,234` | 🍴 `2,767` | **50.73** | **3초 오디오만으로 화자의 음색, 감정, 어투를 그대로 복제하고 다국어로 교차 발화하는 음성 모델**<br>👉 *유튜브 영상의 다국어 더빙 시 원작자 본인의 목소리로 외국어 대사 생성* | [GitHub](https://github.com/FunAudioLLM/CosyVoice) |
| **#15** | `#56` | 💤 Stable | **Qwen-Agent** | Alibaba Cloud QwenLM | `Qwen 2.5 / Qwen 3` | ⭐ `17,241` | 🍴 `1,758` | **48.86** | **8k부터 1M 컨텍스트까지 처리하는 알리바바 공식 에이전트. 펑션 콜링, 코드 인터프리터, 다중 툴 플래닝**<br>👉 *대규모 책 한 권이나 초대형 소스코드 레포를 읽고 분석하는 문서 에이전트* | [GitHub](https://github.com/QwenLM/Qwen-Agent) |
| **#16** | `#57` | ✨ Fresh | **SenseVoice** | Alibaba FunAudioLLM | `Multi-lingual Speech` | ⭐ `9,667` | 🍴 `845` | **48.71** | **Whisper 대비 5배 빠르고 감정, 음악, 웃음소리까지 감지하는 음성 인식 및 오디오 이해 모델**<br>👉 *고객센터 통화 감정 분석 및 고속 실시간 회의록 전사* | [GitHub](https://github.com/FunAudioLLM/SenseVoice) |
| **#17** | `#59` | ✨ Fresh | **GLM-4** | Zhipu AI (THUDM) | `1M Context / All-Tools` | ⭐ `7,074` | 🍴 `622` | **47.08** | **칭화대 계열 Zhipu AI의 플래그십. 1M 장문 처리, 복합 도구 호출, 고정밀 웹 브라우징 능력 제공**<br>👉 *긴 계약서 검토 및 대규모 데이터셋 크로스체크 에이전트* | [GitHub](https://github.com/THUDM/GLM-4) |
| **#18** | `#60` | 💤 Stable | **InternVL** | OpenGVLab | `Vision-Language Model` | ⭐ `10,174` | 🍴 `792` | **45.87** | **GPT-4V 수준의 시각 이해 벤치마크를 기록한 오픈소스 멀티모달. 고해상도 이미지 및 복합 도표 판독 특화**<br>👉 *공학 도면 판독, 차트 분석, 스마트폰 UI 스크린샷 이해 에이전트* | [GitHub](https://github.com/OpenGVLab/InternVL) |
| **#19** | `#61` | 💤 Stable | **XAgent** | OpenBMB | `Autonomous LLM` | ⭐ `8,550` | 🍴 `900` | **45.23** | **인간의 개입 없이 복잡한 목표를 하위 과제로 쪼개고 외부 도구를 탐색하며 실행하는 자율 문제 해결 시스템**<br>👉 *복잡한 데이터 분석, 코드 작성, 인터넷 조사를 사람 없이 밤새 자율 실행시킬 때* | [GitHub](https://github.com/OpenBMB/XAgent) |
| **#20** | `#62` | 💤 Stable | **MindSearch** | Shanghai AI Laboratory | `InternLM 2.5 / Multi-Agent` | ⭐ `6,944` | 🍴 `688` | **44.09** | **인간 인지 과정을 모방해 다단계 병렬 검색과 지식 그래프를 구성하는 심층 연구 엔진 (Perplexity 대안)**<br>👉 *복잡한 학술, 산업 리서치 주제에 대해 100개 이상의 웹페이지를 교차 검증해 레포트 작성* | [GitHub](https://github.com/InternLM/MindSearch) |

<a id="cntry-kr"></a>
### 🇰🇷 대한민국 (South Korea) Top 20

| 국가순위 | 통합순위 | 상태 | 도구/프로젝트명 | 개발/조직 | 호환 모델 | Stars | Forks | 활동 점수 | 핵심 설명 및 실무 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `#48` | ⚡ Active | **im-not-ai** | epoko77-ai | `Claude Skill / Prompt Engine` | ⭐ `6,360` | 🍴 `707` | **51.73** | **AI가 쓴 한글 텍스트의 번역투, 기계적 병렬, 71대 AI 티를 탐지해 자연스러운 한국어로 정밀 재작성**<br>👉 *생성형 AI로 작성한 보고서, 블로그, 제안서의 번역투와 기계적인 문체를 인간 문체로 탈바꿈* | [GitHub](https://github.com/epoko77-ai/im-not-ai) |
| **#02** | `#58` | 🔥 Hot | **Kiwi** | bab2min (이민철) | `C++ Kiwi Engine` | ⭐ `804` | 🍴 `83` | **47.89** | **C++로 작성된 초고속 고정밀 한국어 형태소 분석기. 띄어쓰기 오류가 있는 텍스트도 강력하게 교정 분석**<br>👉 *초당 수만 건의 비정형 텍스트 색인 전처리, 한국어 검색엔진 형태소 인덱싱* | [GitHub](https://github.com/bab2min/Kiwi) |
| **#03** | `#63` | 💤 Stable | **donut** | clovaai (Naver Clova) | `Donut Architecture` | ⭐ `6,927` | 🍴 `562` | **43.9** | **네이버 클로바가 공개한 OCR 엔진 없는 혁신적 엔드투엔드 문서 이해 모델. 이미지에서 JSON으로 직결 변환**<br>👉 *영수증, 송장, 명함, 양식 문서를 OCR 단계 없이 단번에 정형 데이터로 추출* | [GitHub](https://github.com/clovaai/donut) |
| **#04** | `#64` | ⚡ Active | **soynlp** | lovit (김현중) | `Unsupervised Korean NLP` | ⭐ `996` | 🍴 `182` | **42.5** | **사전 없이도 텍스트 데이터의 응집도(Cohesion)와 분기군(Branching Entropy)으로 단어를 자동 추출하는 비지도 토크나이저**<br>👉 *신조어나 전문 용어가 가득한 고객 리뷰, 포럼 데이터에서 미등록 어휘를 자동 추출할 때* | [GitHub](https://github.com/lovit/soynlp) |
| **#05** | `#65` | 💤 Stable | **deep-text-recognition** | clovaai (Naver Clova) | `PyTorch / Clova OCR` | ⭐ `3,937` | 🍴 `1,128` | **42.06** | **네이버 클로바 연구팀이 구축한 텍스트 인식 벤치마크 및 4단계 모듈형 고정밀 OCR 프레임워크**<br>👉 *간판, 스캔 문서, 번호판 등 다양한 환경의 비정형 문자 추출 모델 훈련 및 배포* | [GitHub](https://github.com/clovaai/deep-text-recognition-benchmark) |
| **#06** | `#70` | 💤 Stable | **langchain-kr** | teddylee777 (테디노트) | `LangChain / Multi-LLM` | ⭐ `2,058` | 🍴 `733` | **38.86** | **한국 AI 커뮤니티 최대 규모의 LangChain 실무 쿡북. 실무 RAG, 프롬프트 엔지니어링, 에이전트 튜토리얼 총망라**<br>👉 *기업 내 한국어 RAG 파이프라인 및 멀티 에이전트 워크플로우를 신속하게 프로토타이핑할 때* | [GitHub](https://github.com/teddylee777/langchain-kr) |
| **#07** | `#72` | ✨ Fresh | **fluent-korean** | snflkd | `Claude Code / Cursor / Codex` | ⭐ `1,471` | 🍴 `97` | **38.65** | **Claude Code 등 글로벌 CLI 코딩 에이전트가 번역투 없이 명확하고 유창한 한국어를 구사하도록 제어하는 플러그인**<br>👉 *코딩 에이전트 작업 시 영한 혼용이나 어색한 번역투 답변을 근절하고 자연스러운 개발 피드백 획득* | [GitHub](https://github.com/snflkd/fluent-korean) |
| **#08** | `#73` | 💤 Stable | **KoBERT** | SKTBrain (SK Telecom) | `BERT Architecture` | ⭐ `1,423` | 🍴 `375` | **36.68** | **SK텔레콤이 5400만 개 이상의 한국어 문장으로 학습해 공개한 한국어 대표 사전학습 언어모델**<br>👉 *고객 상담 분류, 감성 분석, 질문 유사도 판정 등 전통적 NLP 태스크 백본* | [GitHub](https://github.com/SKTBrain/KoBERT) |
| **#09** | `#75` | 💤 Stable | **KoAlpaca** | Beomi (이준범) | `Llama / Polyglot-Ko` | ⭐ `1,572` | 🍴 `221` | **36.65** | **한국어 인스트럭션 데이터셋 구축 및 라마/폴리글롯 파인튜닝의 시초가 된 대표 오픈소스**<br>👉 *사내 한국어 비즈니스 지시 수행 모델 파인튜닝 데이터셋 및 학습 파이프라인 구축* | [GitHub](https://github.com/Beomi/KoAlpaca) |
| **#10** | `#80` | 💤 Stable | **kogpt** | kakaobrain (Kakao Brain) | `GPT-3 Architecture (6B)` | ⭐ `1,012` | 🍴 `132` | **34.29** | **카카오브레인이 2000억 토큰 한국어 데이터를 학습해 오픈소스로 공개한 60억 파라미터 한국어 LLM**<br>👉 *한국어 대화 생성, 질의응답 및 프라이빗 로컬 생성 모델 구축* | [GitHub](https://github.com/kakaobrain/kogpt) |
| **#11** | `#81` | 💤 Stable | **Korpora** | ko-nlp (박은정 등) | `All Korean NLP Stacks` | ⭐ `759` | 🍴 `78` | **32.59** | **네이버 영화 리뷰, 국립국어원 등 대표적인 오픈 한국어 말뭉치를 한 줄 파이썬 코드로 다운로드/정제하는 툴킷**<br>👉 *사내 한국어 NLP 모델 훈련을 위한 벤치마크 및 공개 말뭉치 신속 파이프라인 구성* | [GitHub](https://github.com/ko-nlp/Korpora) |
| **#12** | `#82` | 💤 Stable | **KoELECTRA** | monologg (박장원) | `ELECTRA Architecture` | ⭐ `640` | 🍴 `136` | **32.33** | **대규모 한국어 텍스트로 사전학습된 고성능 ELECTRA 모델. 한국어 감정분석, 문서분류, 질의응답 최고 벤치마크**<br>👉 *사내 고객 상담 텍스트 분류, 악성 리뷰 필터링, RAG 리랭커로 활용* | [GitHub](https://github.com/monologg/KoELECTRA) |
| **#13** | `#83` | 💤 Stable | **KoGPT2** | SKT-AI (SK Telecom) | `GPT-2 Architecture` | ⭐ `559` | 🍴 `101` | **31.48** | **SK텔레콤이 공개한 한국어 범용 문장 생성 모델. 소설 이어쓰기, 챗봇 대화 생성용 기초 모델**<br>👉 *챗봇 프로토타입 제작 및 한국어 텍스트 자동 완성* | [GitHub](https://github.com/SKT-AI/KoGPT2) |
| **#14** | `#84` | 💤 Stable | **KULLM** | nlpai-lab (고려대학교 NLP연구실) | `GPT-4 Distillation / Polyglot` | ⭐ `586` | 🍴 `69` | **31.36** | **고려대학교 NLP 연구실과 HICA가 공동 제작한 한국어 인스트럭션 파인튜닝 모델 시리즈 (구름)**<br>👉 *학술 연구 및 한국어 상식 추론, 대화형 도메인 모델 프로토타이핑* | [GitHub](https://github.com/nlpai-lab/KULLM) |
| **#15** | `#86` | 💤 Stable | **KoBART** | SKT-AI | `BART Architecture` | ⭐ `471` | 🍴 `94` | **30.68** | **SK텔레콤이 공개한 한국어 사전학습 BART 모델. 한국어 장문 기사 요약 및 문장 생성 표준**<br>👉 *뉴스 기사 자동 3줄 요약, 사내 회의록 요약, 한국어 챗봇 생성 백본* | [GitHub](https://github.com/SKT-AI/KoBART) |
| **#16** | `#87` | 💤 Stable | **PyKoSpacing** | haven-jeon (전희원) | `Deep Learning / Python` | ⭐ `439` | 🍴 `115` | **30.55** | **대규모 말뭉치 기반 딥러닝으로 띄어쓰기가 누락되거나 잘못된 문장을 정확하게 교정하는 도구**<br>👉 *음성인식(STT) 텍스트 전처리 및 모바일 메신저 대화 띄어쓰기 자동 보정* | [GitHub](https://github.com/haven-jeon/PyKoSpacing) |
| **#17** | `#88` | 💤 Stable | **KcBERT** | Beomi (이준범) | `BERT Architecture` | ⭐ `497` | 🍴 `46` | **30.29** | **정제되지 않은 포털 뉴스 댓글 수천만 건으로 사전학습된 모델. 구어체, 오탈자, 비속어 필터링에 탁월**<br>👉 *SNS 댓글 모니터링, 악플 및 혐오 표현 자동 탐지 필터* | [GitHub](https://github.com/Beomi/KcBERT) |
| **#18** | `#89` | 💤 Stable | **cord** | clovaai (Naver Clova) | `Document AI` | ⭐ `495` | 🍴 `44` | **30.23** | **네이버 클로바가 공개한 영수증/송장 문서 정보 추출을 위한 통합 벤치마크 데이터셋**<br>👉 *경비 지출 관리 자동화 및 영수증 품목/금액 자동 파싱 엔진 개발* | [GitHub](https://github.com/clovaai/cord) |
| **#19** | `#90` | 💤 Stable | **polyglot** | EleutherAI & 튜닙 | `Polyglot-Ko 1.3B ~ 12.8B` | ⭐ `489` | 🍴 `42` | **30.14** | **한국어 씬에서 가장 널리 쓰이는 비영어권 오픈 파운데이션 모델. 한국어 토크나이저 최적화**<br>👉 *로컬 프라이빗 한국어 AI 비서 및 온프레미스 도메인 특화 모델 기반* | [GitHub](https://github.com/EleutherAI/polyglot) |
| **-** | `-` | 📦 Archived | **pororo** | kakaobrain (Kakao Brain) | `PyTorch / Transformer` | ⭐ `1,303` | 🍴 `216` | **35.82** | **카카오브레인이 공개한 30가지 이상의 한국어 NLP 태스크(개체명인식, 질의응답, 요약 등) 통합 프레임워크**<br>👉 *단 3줄의 코드로 기사 요약, 문맥 유사도, 기계 독해 파이프라인 즉시 구성* | [GitHub](https://github.com/kakaobrain/pororo) |

<a id="cntry-eu"></a>
### 🇪🇺 유럽 (Europe - 영국/프랑스/독일 등) Top 20

| 국가순위 | 통합순위 | 상태 | 도구/프로젝트명 | 개발/조직 | 호환 모델 | Stars | Forks | 활동 점수 | 핵심 설명 및 실무 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `#04` | 🔥 Hot | **n8n** | n8n.io | `Multi-LLM / LangChain 연동` | ⭐ `209,318` | 🍴 `61,352` | **77.78** | **수백 개의 SaaS와 데이터베이스를 AI 에이전트 노드로 연결하는 오픈소스 비주얼 워크플로우 플랫폼**<br>👉 *슬랙, 노션, 세일즈포스, 이메일 간 복잡한 비즈니스 로직에 AI 판단 노드를 얹어 자동화할 때* | [GitHub](https://github.com/n8n-io/n8n) |
| **#02** | `#06` | 🔥 Hot | **transformers** | Hugging Face (France/US) | `Every Open Model` | ⭐ `168,432` | 🍴 `35,080` | **76.35** | **현대 AI 오픈소스 생태계의 기틀. 전 세계 수십만 개의 사전학습 모델을 다운로드하고 추론하는 표준 라이브러리**<br>👉 *새로 발표된 전 세계 최신 모델을 단 몇 줄의 파이썬 코드로 불러와 테스트할 때* | [GitHub](https://github.com/huggingface/transformers) |
| **#03** | `#14` | 🔥 Hot | **ai-job-search** | Mads Lorentzen (Denmark) | `Claude Code / Codex / Gemini CLI` | ⭐ `68,793` | 🍴 `21,946` | **72.06** | **덴마크 개발자가 제작한 오픈소스. 채용공고 스크랩부터 이력서 맞춤 작성, 모의면접까지 자율 완결**<br>👉 *구직자가 수십 개 타깃 기업에 맞춘 고품질 영문 커버레터와 CV를 자동 생성할 때* | [GitHub](https://github.com/MadsLorentzen/ai-job-search) |
| **#04** | `#16` | 🔥 Hot | **unsloth** | Unsloth AI (UK - Daniel Han) | `Llama, Qwen, DeepSeek, Mistral` | ⭐ `78,936` | 🍴 `7,354` | **71.71** | **파이토치 연산을 수작업으로 최적화하여 LLM 파인튜닝 속도를 5배 빠르게, VRAM 사용량을 80% 줄인 영국 명품 툴**<br>👉 *일반 단일 GPU에서 70B 모델을 수 시간 만에 LoRA 파인튜닝할 때* | [GitHub](https://github.com/unslothai/unsloth) |
| **#05** | `#18` | 🔥 Hot | **AnythingLLM** | Mintplex Labs | `Multi-LLM / Multi-Vector` | ⭐ `67,837` | 🍴 `7,652` | **71.08** | **GDPR 및 완전 프라이버시를 보장하는 데스크톱/서버 AI 앱. 문서 드래그 앤 드롭 RAG, 다중 사용자 권한 관리**<br>👉 *외부 클라우드 전송이 엄격히 금지된 법무법인, 회계법인의 사내 폐쇄망 AI 포털* | [GitHub](https://github.com/Mintplex-Labs/anything-llm) |
| **#06** | `#22` | 🔥 Hot | **LocalAI** | mudler (Italy) | `Drop-in OpenAI Replacement` | ⭐ `50,122` | 🍴 `4,568` | **69.32** | **인터넷 없이 로컬 하드웨어에서 구동되는 오픈AI 규격 완벽 호환 REST API 서버 (텍스트, 음성, 이미지)**<br>👉 *기존 상용 OpenAI API 코드를 단 한 줄도 수정하지 않고 사내 로컬 환경으로 교체할 때* | [GitHub](https://github.com/mudler/LocalAI) |
| **#07** | `#29` | 🔥 Hot | **qdrant** | Qdrant (Germany - Berlin) | `Rust High Performance` | ⭐ `35,376` | 🍴 `2,792` | **67.38** | **Rust로 작성된 초고성능 벡터 검색 엔진. 풍부한 페이로드 필터링과 지연 없는 시맨틱 검색 지원**<br>👉 *수백만 건의 문서에서 태그, 날짜, 카테고리 필터와 벡터 유사도 검색을 동시 초고속 처리할 때* | [GitHub](https://github.com/qdrant/qdrant) |
| **#08** | `#31` | 🔥 Hot | **smolagents** | Hugging Face (France/US) | `Any LLM / Open Weights` | ⭐ `30,180` | 🍴 `3,185` | **66.8** | **복잡한 프레임워크 대신 에이전트의 모든 판단과 도구 호출을 파이썬 코드로 표현하는 미니멀리즘 에이전트**<br>👉 *수천 줄의 복잡한 추상화 없이 몇 줄의 순수 파이썬 코드로 가볍고 강력한 에이전트를 조립할 때* | [GitHub](https://github.com/huggingface/smolagents) |
| **#09** | `#33` | 🔥 Hot | **haystack** | deepset (Germany - Berlin) | `Multi-LLM` | ⭐ `26,904` | 🍴 `3,384` | **66.36** | **독일 특유의 견고한 엔지니어링으로 모듈화된 엔터프라이즈 RAG 및 에이전트 파이프라인 프레임워크**<br>👉 *기업 보안과 유지보수성이 핵심인 엔터프라이즈 시맨틱 검색 및 문서 질의응답 시스템 구축* | [GitHub](https://github.com/deepset-ai/haystack) |
| **#10** | `#37` | 🔥 Hot | **weaviate** | Weaviate (Netherlands - Amsterdam) | `Go / Cloud Native` | ⭐ `16,934` | 🍴 `1,433` | **63.6** | **네덜란드 암스테르담에서 탄생한 클라우드 네이티브 벡터 데이터베이스. 멀티모달 검색 및 하이브리드 검색 특화**<br>👉 *이미지와 텍스트가 섞인 멀티모달 이커머스 상품 시맨틱 검색 엔진* | [GitHub](https://github.com/weaviate/weaviate) |
| **#11** | `#38` | 🔥 Hot | **SubtitleEdit** | Nikolaj Lynge Olsson (Denmark) | `Local Whisper Integration` | ⭐ `14,815` | 🍴 `1,358` | **62.97** | **덴마크에서 개발되어 전 세계 영상 전문가들이 사용하는 오픈소스 자막 편집기. 로컬 AI 모델 내장으로 오프라인 전사**<br>👉 *방송국, 영상 제작사의 대용량 영상 로컬 자막 제작 및 다국어 싱크 수정* | [GitHub](https://github.com/SubtitleEdit/subtitleedit) |
| **#12** | `#39` | ⚡ Active | **mindsdb** | MindsDB (UK/US) | `SQL-to-Model` | ⭐ `39,837` | 🍴 `6,234` | **61.59** | **SQL 쿼리문 안에서 직접 AI 모델을 호출하고 실시간 예측 및 텍스트 분석을 수행하는 미들웨어**<br>👉 *기존 DB 엔지니어가 파이썬 코드 없이 익숙한 SQL만으로 사내 데이터에 AI를 적용할 때* | [GitHub](https://github.com/mindsdb/mindsdb) |
| **#13** | `#43` | 🔥 Hot | **maka** | Apache Maka Project (EU) | `Auditable Local Runs` | ⭐ `5,932` | 🍴 `572` | **58.25** | **에이전트가 내린 모든 툴 호출과 로컬 bash 명령어를 불변(Immutable) 원장에 기록해 법적 책임을 증명하는 엔진**<br>👉 *자율 에이전트의 오작동 및 보안 사고 발생 시 원인 규명과 법적 감사 증빙* | [GitHub](https://github.com/apache/maka) |
| **#14** | `#54` | ✨ Fresh | **moshi** | Kyutai Labs (France - Paris) | `Helium 7B / Mimi Audio` | ⭐ `11,361` | 🍴 `1,051` | **49.6** | **파리 비영리 연구소 Kyutai가 공개한 오픈소스 음성 대화 AI. STT/TTS 없이 200ms 지연으로 사람과 실시간 수다**<br>👉 *중간 텍스트 변환 병목 없이 사람과 즉각 호흡을 주고받는 차세대 실시간 대화봇* | [GitHub](https://github.com/kyutai-labs/moshi) |
| **#15** | `#55` | 🔥 Hot | **Mistral-Large** | Mistral AI (France) | `Mistral Architecture` | ⭐ `958` | 🍴 `195` | **49.39** | **프랑스 AI 대표주자 Mistral의 플래그십. 다국어(불어, 독어, 스페인어, 영어)와 복잡한 추론에서 최고 수준 성능**<br>👉 *EU AI Act 및 데이터 주권(Sovereign AI) 규제를 준수하는 기업용 대규모 언어 모델* | [GitHub](https://github.com/mistralai/mistral-common) |
| **#16** | `#68` | ✨ Fresh | **hibiki** | Kyutai Labs (France - Paris) | `Moshi Lineage` | ⭐ `1,534` | 🍴 `118` | **39.0** | **말하는 도중 실시간으로 다른 언어로 음성을 바꿔서 뱉어내는 엔드투엔드 동시통역 음성 모델**<br>👉 *국제 컨퍼런스 실시간 음성 통역 및 다국어 실시간 화상 회의* | [GitHub](https://github.com/kyutai-labs/hibiki) |
| **#17** | `#91` | 💤 Stable | **mistral-eval** | Mistral AI (France) | `Mistral Models` | ⭐ `93` | 🍴 `16` | **22.09** | **유럽 각국 언어(프랑스어, 독일어, 이탈리아어 등)에서의 논리적 일관성과 규제 준수성을 측정하는 벤치마크**<br>👉 *유럽 다국어 비즈니스 서비스 런칭 시 각 언어별 모델 응답 품질 보증* | [GitHub](https://github.com/mistralai/mistral-evals) |
| **-** | `-` | 📦 Archived | **text-generation-inference** | Hugging Face (TGI) | `Tensor Parallelism` | ⭐ `10,882` | 🍴 `1,288` | **46.59** | **Hugging Face의 엔터프라이즈급 LLM 서빙 엔진. 텐서 병렬화, 토큰 스트리밍, 플래시 어텐션 지원**<br>👉 *Kubernetes 환경에서 오픈 모델을 대규모 서비스 엔드포인트로 운영할 때* | [GitHub](https://github.com/huggingface/text-generation-inference) |
| **-** | `-` | 📦 Archived | **rhasspy** | Michael Hansen (EU Open Source) | `Offline Voice Stack` | ⭐ `2,754` | 🍴 `207` | **39.03** | **클라우드 전송 없는 완전 오프라인 프라이빗 음성 비서 툴킷. 홈 오토메이션(Home Assistant) 완벽 연동**<br>👉 *스마트홈 기기를 외부 서버 도청 걱정 없이 음성으로 제어할 때* | [GitHub](https://github.com/rhasspy/rhasspy) |
| **-** | `-` | 📦 Archived | **FARM** | deepset (Germany) | `Transformer Transfer Learning` | ⭐ `1,755` | 🍴 `242` | **37.21** | **독일 deepset이 개발한 산업용 트랜스포머 전이학습 및 도메인 모델 파인튜닝 프레임워크**<br>👉 *사내 도메인 특화 질문응답 및 텍스트 분류 모델 최적화 배포* | [GitHub](https://github.com/deepset-ai/FARM) |

<a id="cntry-jp"></a>
### 🇯🇵 일본 (Japan) Top 20

| 국가순위 | 통합순위 | 상태 | 도구/프로젝트명 | 개발/조직 | 호환 모델 | Stars | Forks | 활동 점수 | 핵심 설명 및 실무 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `#42` | 🔥 Hot | **koharu** | koharu-rs | `Rust / Multimodal Vision` | ⭐ `6,569` | 🍴 `486` | **58.55** | **Rust로 작성된 초고속 오픈소스 AI 만화 번역기. 텍스트 버블 탐지, OCR, 문맥 번역 및 인페인팅**<br>👉 *일본 만화 이미지의 일본어 대사를 인식하고 자연스러운 번역 텍스트로 자동 대치* | [GitHub](https://github.com/koharu-rs/koharu) |
| **#02** | `#45` | 🔥 Hot | **voicevox** | Hiroshiba (Japan) | `Japanese Neural TTS` | ⭐ `3,288` | 🍴 `380` | **55.33** | **일본 버추얼 유튜버 및 크리에이터 생태계의 절대적 1위 무료 음성 합성 소프트웨어 (즌다몬 등)**<br>👉 *일본어 해설 영상, 서브컬처 게임, 버추얼 캐릭터 대사 자동 생성* | [GitHub](https://github.com/VOICEVOX/voicevox) |
| **#03** | `#49` | 🔥 Hot | **natural-japanese** | coji | `Claude Code / Agent Skill` | ⭐ `2,003` | 🍴 `57` | **51.53** | **AI가 생성한 일본어 텍스트를 읽기 쉽고 격식 있는 비즈니스 일본어로 다듬는 전용 에이전트 스킬**<br>👉 *일본 현지 파트너사 비즈니스 이메일, 기술 문서의 정밀 경어체 교정* | [GitHub](https://github.com/coji/natural-japanese) |
| **#04** | `#51` | 🔥 Hot | **voicevox_core** | VOICEVOX Project | `C++ / Python / Rust Binding` | ⭐ `1,149` | 🍴 `168` | **50.05** | **VOICEVOX의 고속 음성 합성 백엔드 C++ 코어. 파이썬과 러스트에서 경량 임베디드로 음성 출력**<br>👉 *코딩 에이전트가 작업 완료 시 귀여운 일본어 보이스로 알림을 주도록 연동* | [GitHub](https://github.com/VOICEVOX/voicevox_core) |
| **#05** | `#52` | 🔥 Hot | **awesome-japanese-llm** | llm-jp (National Institute of Informatics) | `Japanese Academic LLMs` | ⭐ `1,442` | 🍴 `49` | **49.97** | **일본 국립정보학연구소(NII) 주도로 일본 내 공개된 모든 파운데이션 모델, 데이터셋을 집대성한 공식 허브**<br>👉 *일본 오픈소스 언어모델 현황 및 벤치마크 점수 일괄 비교* | [GitHub](https://github.com/llm-jp/awesome-japanese-llm) |
| **#06** | `#66` | 🔥 Hot | **llm-jp-eval** | llm-jp (National Institute of Informatics) | `Japanese LLMs` | ⭐ `173` | 🍴 `50` | **40.78** | **일본어 독해, 번역, 수학, 추론 등 다양한 과제를 통일된 파이프라인으로 측정하는 공식 평가 도구**<br>👉 *일본어 오픈소스 모델의 영역별 벤치마크 점수 자동 측정 및 리더보드 등재* | [GitHub](https://github.com/llm-jp/llm-jp-eval) |
| **#07** | `#67` | 💤 Stable | **mecab-ipadic-neologd** | neologd | `MeCab Dictionary` | ⭐ `2,798` | 🍴 `285` | **39.38** | **웹 문서와 SNS에서 매주 새로 등장하는 일본어 고유명사와 신조어를 자동 갱신하는 사실상 표준 사전**<br>👉 *일본 서브컬처, 애니메이션, 최신 IT 유행어가 포함된 텍스트의 정확한 형태소 분리* | [GitHub](https://github.com/neologd/mecab-ipadic-neologd) |
| **#08** | `#69` | ⚡ Active | **cmaes** | CyberAgentAILab | `CMA-ES Algorithm` | ⭐ `516` | 🍴 `80` | **38.93** | **Optuna 등 하이퍼파라미터 튜닝 프레임워크에 널리 쓰이는 초고속 경량 공분산 행렬 적응 진화 전략(CMA-ES)**<br>👉 *LLM 프롬프트 파라미터 및 하이퍼파라미터 자동 튜닝* | [GitHub](https://github.com/CyberAgentAILab/cmaes) |
| **#09** | `#71` | 💤 Stable | **manga-ocr** | kha-white | `Vision Transformer` | ⭐ `2,824` | 🍴 `143` | **38.82** | **일반 OCR이 판독하지 못하는 일본어 세로쓰기, 특수 폰트, 손글씨를 정확하게 판독하는 비전 모델**<br>👉 *일본 원서, 코믹스 이미지 내 텍스트 자동 판독* | [GitHub](https://github.com/kha-white/manga-ocr) |
| **#10** | `#74` | 💤 Stable | **mokuro** | kha-white | `manga-ocr integration` | ⭐ `1,772` | 🍴 `121` | **36.65** | **일본어 만화 이미지 위에 복사 가능한 텍스트 오버레이 레이어를 생성하여 사전 팝업 지원**<br>👉 *일본어 학습자가 원서를 읽으며 클릭 한 번으로 단어 뜻을 실시간 조회* | [GitHub](https://github.com/kha-white/mokuro) |
| **#11** | `#76` | 💤 Stable | **evolutionary-model-merge** | Sakana AI (Tokyo) | `Evolutionary Search / LLMs` | ⭐ `1,441` | 🍴 `123` | **35.77** | **도쿄 사카나 AI가 개발한 진화 알고리즘 기반 자동 모델 병합 도구. 교차 훈련 없이 고성능 하이브리드 LLM 탄생**<br>👉 *수학 특화 모델과 일본어 특화 모델을 유전 알고리즘으로 자동 병합하여 새로운 모델 생성* | [GitHub](https://github.com/SakanaAI/evolutionary-model-merge) |
| **#12** | `#77` | 💤 Stable | **TANGO** | CyberAgentAILab (CyberAgent) | `AudioLDM / Latent Diffusion` | ⭐ `1,165` | 🍴 `150` | **35.02** | **일본 대형 IT 기업 사이버에이전트가 개발한 텍스트 프롬프트로부터 현실적인 효과음과 음악을 생성하는 모델**<br>👉 *게임, 애니메이션 효과음(Sound Effects) 자동 제작 및 오디오 프로토타이핑* | [GitHub](https://github.com/CyberAgentAILab/TANGO) |
| **#13** | `#78` | 💤 Stable | **kuromoji** | atilika | `Java / Lucene Engine` | ⭐ `1,064` | 🍴 `140` | **34.56** | **Apache Lucene, Solr, Elasticsearch에 공식 내장된 가장 표준적인 자바 일본어 형태소 분석기**<br>👉 *대용량 엔터프라이즈 검색엔진의 일본어 문서 인덱싱 전처리* | [GitHub](https://github.com/atilika/kuromoji) |
| **#14** | `#79` | 💤 Stable | **kuromoji.js** | takuyaa | `JavaScript / Node.js` | ⭐ `1,009` | 🍴 `154` | **34.41** | **순수 자바스크립트로 브라우저나 Node.js 환경에서 C/바이너리 설치 없이 돌아가는 일본어 형태소 분석기**<br>👉 *웹 브라우저 클라이언트 사이드에서 즉시 일본어 단어 분리 및 한자 읽기(후리가나) 생성* | [GitHub](https://github.com/takuyaa/kuromoji.js) |
| **#15** | `#85` | 💤 Stable | **mecab-python3** | SamuraiT | `Python 3 / C++` | ⭐ `580` | 🍴 `53` | **31.08** | **일본어 자연어처리의 전설적인 MeCab 엔진을 현대 파이썬 3 환경에서 고속으로 호출하는 바인딩**<br>👉 *일본어 대규모 말뭉치 전처리 및 검색엔진 토크나이저 구축* | [GitHub](https://github.com/SamuraiT/mecab-python3) |
| **#16** | `#92` | 💤 Stable | **line-distilbert-jp** | line (LINE Corporation) | `DistilBERT` | ⭐ `47` | 🍴 `1` | **16.72** | **라인이 131GB 대규모 일본어 텍스트로 사전학습한 초경량 고속 언어모델**<br>👉 *모바일 기기 및 엣지 디바이스에서의 고속 일본어 의도 분석* | [GitHub](https://github.com/line/LINE-DistilBERT-Japanese) |
| **-** | `-` | 📦 Archived | **SudachiPy** | Works Applications | `Sudachi Engine` | ⭐ `443` | 🍴 `52` | **29.9** | **단어 분할 단위를 A(짧게), B(중간), C(길게) 3단계로 조절 가능한 엔터프라이즈 일본어 형태소 분석기**<br>👉 *일본 대기업 사내 검색엔진 및 계약서 문서 색인 전처리* | [GitHub](https://github.com/WorksApplications/SudachiPy) |

---

<a id="global-top-100"></a>
## 🏆 2. Global AI Weekly Top 100 Leaderboard (글로벌 100선 종합 랭킹)

GitHub 주간 갱신 메트릭(Stars, Forks)과 최근 커밋 활동성(Recency Bonus)을 종합 반영한 전 세계 100선 통합 랭킹입니다.

| 순위 | 변동 | 상태 | 프로젝트명 | 국가 | 카테고리 | Stars | Forks | 활동 점수 | 핵심 특징 및 활용처 | 링크 |
|:---:|:---:|:---:|---|---|---|:---:|:---:|:---:|---|:---:|
| **#01** | `−` | 🔥 Hot | **openclaw** | 미국 | 에이전트 하네스 & 자율 실행 | ⭐ `393,667` | 🍴 `82,734` | **80.79** | 2026년 급부상한 범용 제너럴리스트 에이전트. 랍스터(Lobster) 아키텍처 기반 자율 태스크 분기 | [GitHub](https://github.com/openclaw/openclaw) |
| **#02** | `−` | 🔥 Hot | **hermes-agent** | 미국 | 에이전트 하네스 & 자율 실행 | ⭐ `259,574` | 🍴 `57,129` | **78.66** | 자율적인 스킬 학습 및 영구 누적을 특징으로 하는 적응형 에이전트 하네스 | [GitHub](https://github.com/nousresearch/hermes-agent) |
| **#03** | `−` | 🔥 Hot | **deepseek-harness** | 중국 | 에이전트 하네스 & 자율 실행 | ⭐ `268,633` | 🍴 `32,609` | **78.32** | Cordis 설계를 도입하여 모델, 툴, 세션, 루프 전부를 플러그인으로 갈아끼우는 프레임워크 독립형 하네스 | [GitHub](https://github.com/deepseek-ai/deepseek-harness) |
| **#04** | `−` | 🔥 Hot | **n8n** | 유럽 | 워크플로우 & 파이프라인 오케스트레이션 | ⭐ `209,318` | 🍴 `61,352` | **77.78** | 수백 개의 SaaS와 데이터베이스를 AI 에이전트 노드로 연결하는 오픈소스 비주얼 워크플로우 플랫폼 | [GitHub](https://github.com/n8n-io/n8n) |
| **#05** | `−` | 🔥 Hot | **AutoGPT** | 미국 | 에이전트 벤치마크 & 하네스 | ⭐ `187,861` | 🍴 `45,901` | **77.06** | 자율 에이전트의 시초이자 현재는 에이전트 빌더, 블록 기반 워크플로우, 벤치마킹을 아우르는 오픈 플랫폼 | [GitHub](https://github.com/Significant-Gravitas/AutoGPT) |
| **#06** | `−` | 🔥 Hot | **transformers** | 유럽 | 모델 허브 & 표준 라이브러리 | ⭐ `168,432` | 🍴 `35,080` | **76.35** | 현대 AI 오픈소스 생태계의 기틀. 전 세계 수십만 개의 사전학습 모델을 다운로드하고 추론하는 표준 라이브러리 | [GitHub](https://github.com/huggingface/transformers) |
| **#07** | `−` | 🔥 Hot | **ollama** | 미국 | 로컬 인퍼런스 & 서빙 인프라 | ⭐ `185,620` | 🍴 `18,857` | **76.24** | Mac, Linux, Windows에서 Llama, Qwen, DeepSeek 오픈 모델을 한 줄 명령으로 다운로드 및 실행하는 사실상 글로벌 표준 | [GitHub](https://github.com/ollama/ollama) |
| **#08** | `−` | 🔥 Hot | **dify** | 중국 | 워크플로우 & 에이전트 플랫폼 | ⭐ `160,186` | 🍴 `25,329` | **75.85** | 비주얼 오케스트레이션, RAG 파이프라인, 에이전트 워크플로우를 완성형 웹 앱으로 즉시 배포하는 글로벌 리딩 플랫폼 | [GitHub](https://github.com/langgenius/dify) |
| **#09** | `▲1` | 🔥 Hot | **ComfyUI** | 미국 | 생성형 미디어 & 노드 UI | ⭐ `144,523` | 🍴 `17,222` | **75.07** | 가장 강력하고 모듈화된 노드 기반 생성형 이미지/비디오 워크플로우 런타임. 에이전트 API 연동 표준 | [GitHub](https://github.com/comfyanonymous/ComfyUI) |
| **#10** | `▼1` | 🔥 Hot | **llama.cpp** | 미국 | 로컬 인퍼런스 & 서빙 인프라 | ⭐ `133,101` | 🍴 `25,042` | **75.04** | GGUF 양자화 포맷의 원조. 일반 CPU와 통합 메모리 GPU에서 대규모 모델을 돌릴 수 있게 만든 오픈 인프라 | [GitHub](https://github.com/ggerganov/llama.cpp) |
| **#11** | `−` | 🔥 Hot | **browser-use** | 미국 | 브라우저 조작 & 웹 자동화 | ⭐ `119,788` | 🍴 `13,348` | **74.03** | AI가 사람처럼 브라우저를 띄워 클릭, 스크롤, 양식 제출, 로그인, 데이터 수집을 완결하는 웹 에이전트 | [GitHub](https://github.com/browser-use/browser-use) |
| **#12** | `−` | 🔥 Hot | **vllm** | 미국 | 로컬 인퍼런스 & 서빙 인프라 | ⭐ `96,096` | 🍴 `24,280` | **73.6** | PagedAttention 기반으로 메모리 낭비를 없애고 처리량을 최대 24배 끌어올린 오픈소스 프로덕션 서빙 엔진 | [GitHub](https://github.com/vllm-project/vllm) |
| **#13** | `−` | 🔥 Hot | **ragflow** | 중국 | 엔터프라이즈 RAG 엔진 | ⭐ `93,320` | 🍴 `11,203` | **72.8** | 문서의 템플릿과 레이아웃을 깊이 이해하여 표와 단락이 엉키지 않도록 청킹하는 차세대 오픈소스 RAG | [GitHub](https://github.com/infiniflow/ragflow) |
| **#14** | `▲1` | 🔥 Hot | **ai-job-search** | 유럽 | 자율 채용 지원 에이전트 | ⭐ `68,793` | 🍴 `21,946` | **72.06** | 덴마크 개발자가 제작한 오픈소스. 채용공고 스크랩부터 이력서 맞춤 작성, 모의면접까지 자율 완결 | [GitHub](https://github.com/MadsLorentzen/ai-job-search) |
| **#15** | `▼1` | 🔥 Hot | **MinerU** | 중국 | 문서 변환 & 구조화 | ⭐ `82,961` | 🍴 `6,867` | **71.86** | 복잡한 비정형 PDF, 오피스 문서, 학술 논문을 마크다운/JSON으로 완벽 추출하여 RAG 병목을 해결한 1위 도구 | [GitHub](https://github.com/opendatalab/MinerU) |
| **#16** | `−` | 🔥 Hot | **unsloth** | 유럽 | 초고속 모델 파인튜닝 | ⭐ `78,936` | 🍴 `7,354` | **71.71** | 파이토치 연산을 수작업으로 최적화하여 LLM 파인튜닝 속도를 5배 빠르게, VRAM 사용량을 80% 줄인 영국 명품 툴 | [GitHub](https://github.com/unslothai/unsloth) |
| **#17** | `−` | 🔥 Hot | **mem0** | 미국 | 에이전트 메모리 & 상태 관리 | ⭐ `68,258` | 🍴 `8,099` | **71.16** | 사용자의 과거 대화, 선호도, 사실 관계를 지속적으로 갱신하고 인덱싱하는 개인화 메모리 레이어 | [GitHub](https://github.com/mem0ai/mem0) |
| **#18** | `−` | 🔥 Hot | **AnythingLLM** | 유럽 | 프라이버시 중심 올인원 AI | ⭐ `67,837` | 🍴 `7,652` | **71.08** | GDPR 및 완전 프라이버시를 보장하는 데스크톱/서버 AI 앱. 문서 드래그 앤 드롭 RAG, 다중 사용자 권한 관리 | [GitHub](https://github.com/Mintplex-Labs/anything-llm) |
| **#19** | `−` | 🔥 Hot | **crewAI** | 미국 | 워크플로우 & 파이프라인 오케스트레이션 | ⭐ `60,398` | 🍴 `8,998` | **70.72** | 기획자, 리서처, 작가 등 명확한 직책(Role)과 목표(Goal)를 부여해 가상의 팀을 조직하는 에이전트 프레임워크 | [GitHub](https://github.com/crewAIInc/crewAI) |
| **#20** | `−` | 🔥 Hot | **llama_index** | 미국 | 데이터 인제스천 & RAG | ⭐ `52,776` | 🍴 `8,495` | **70.08** | PDF, 노션, DB 등 방대한 비정형 데이터를 에이전트가 탐색 가능한 인덱스로 연결하는 RAG 표준 | [GitHub](https://github.com/run-llama/llama_index) |
| **#21** | `−` | 🔥 Hot | **whisper.cpp** | 미국 | 로컬 인퍼런스 & 서빙 인프라 | ⭐ `54,850` | 🍴 `6,264` | **69.99** | C/C++로 밑바닥부터 재작성된 Whisper 추론 엔진. Apple Silicon Metal 가속으로 실시간 자막 전사 지원 | [GitHub](https://github.com/ggerganov/whisper.cpp) |
| **#22** | `−` | 🔥 Hot | **LocalAI** | 유럽 | 로컬 인퍼런스 서버 | ⭐ `50,122` | 🍴 `4,568` | **69.32** | 인터넷 없이 로컬 하드웨어에서 구동되는 오픈AI 규격 완벽 호환 REST API 서버 (텍스트, 음성, 이미지) | [GitHub](https://github.com/mudler/LocalAI) |
| **#23** | `−` | 🔥 Hot | **langgraph** | 미국 | 에이전트 하네스 & 상태 머신 | ⭐ `44,303` | 🍴 `7,620` | **69.23** | 상태(State)를 기반으로 순환 루프, 분기 조건, 인간 개입(Human-in-the-loop)을 정의하는 엔터프라이즈 에이전트 표준 | [GitHub](https://github.com/langchain-ai/langgraph) |
| **#24** | `−` | 🔥 Hot | **sglang** | 미국 | 로컬 인퍼런스 & 서빙 인프라 | ⭐ `38,358` | 🍴 `10,069` | **68.84** | 복잡한 에이전트 툴 호출과 다단계 추론에서 반복되는 KV 캐시를 Radix 트리로 공유해 레이턴시를 5배 단축 | [GitHub](https://github.com/sgl-project/sglang) |
| **#25** | `▲1` | 🔥 Hot | **CopilotKit** | 미국 | 인앱 코파일럿 & UI 연동 | ⭐ `38,457` | 🍴 `4,800` | **68.21** | 기존 웹앱에 사이드바 코파일럿, 텍스트 인라인 편집, 프론트엔드 작업 제어 액션을 5분 만에 붙여주는 툴킷 | [GitHub](https://github.com/CopilotKit/CopilotKit) |
| **#26** | `▲1` | 🔥 Hot | **diffusers** | 미국 | 생성형 미디어 & 노드 UI | ⭐ `34,848` | 🍴 `7,447` | **68.17** | Stable Diffusion, Flux, ControlNet 등 최신 확산 모델을 통일된 파이썬 API로 다루는 표준 라이브러리 | [GitHub](https://github.com/huggingface/diffusers) |
| **#27** | `▲1` | 🔥 Hot | **dspy** | 미국 | 프롬프트 최적화 & 컴파일러 | ⭐ `38,880` | 🍴 `3,473` | **67.98** | 휴리스틱 프롬프트 대신 알고리즘으로 모델 가중치와 프롬프트를 자동 컴파일/최적화하는 스탠퍼드 프레임워크 | [GitHub](https://github.com/stanfordnlp/dspy) |
| **#28** | `▲1` | 🔥 Hot | **FastGPT** | 중국 | 엔터프라이즈 RAG 플랫폼 | ⭐ `29,970` | 🍴 `7,361` | **67.5** | 데이터 전처리, 벡터 검색, 재순위화(Reranking)에 특화된 완성형 지식 베이스 질의응답 플랫폼 | [GitHub](https://github.com/labring/FastGPT) |
| **#29** | `▲1` | 🔥 Hot | **qdrant** | 유럽 | Rust 기반 고성능 벡터 DB | ⭐ `35,376` | 🍴 `2,792` | **67.38** | Rust로 작성된 초고성능 벡터 검색 엔진. 풍부한 페이로드 필터링과 지연 없는 시맨틱 검색 지원 | [GitHub](https://github.com/qdrant/qdrant) |
| **#30** | `▲10` | 🔥 Hot | **fish-speech** | 중국 | 자연스러운 음성 합성 | ⭐ `33,537` | 🍴 `2,918` | **67.19** | 영어, 중국어, 일본어, 한국어를 완벽 지원하는 고품질 제로샷 텍스트-음성 변환 오픈 엔진 | [GitHub](https://github.com/fishaudio/fish-speech) |
| **#31** | `−` | 🔥 Hot | **smolagents** | 유럽 | 코드 기반 경량 에이전트 | ⭐ `30,180` | 🍴 `3,185` | **66.8** | 복잡한 프레임워크 대신 에이전트의 모든 판단과 도구 호출을 파이썬 코드로 표현하는 미니멀리즘 에이전트 | [GitHub](https://github.com/huggingface/smolagents) |
| **#32** | `−` | 🔥 Hot | **Qwen-Code** | 중국 | 코딩 에이전트 CLI | ⭐ `28,871` | 🍴 `3,295` | **66.64** | 터미널에서 직접 실행되는 오픈소스 코딩 에이전트. Qwen-2.5-Coder의 최적화된 토크나이저와 도구 연동 | [GitHub](https://github.com/QwenLM/Qwen-Code) |
| **#33** | `−` | 🔥 Hot | **haystack** | 유럽 | 엔터프라이즈 RAG 오케스트레이터 | ⭐ `26,904` | 🍴 `3,384` | **66.36** | 독일 특유의 견고한 엔지니어링으로 모듈화된 엔터프라이즈 RAG 및 에이전트 파이프라인 프레임워크 | [GitHub](https://github.com/deepset-ai/haystack) |
| **#34** | `−` | 🔥 Hot | **fastmcp** | 미국 | MCP & 도구 생태계 | ⭐ `28,269` | 🍴 `2,551` | **66.33** | FastAPI 스타일의 데코레이터 문법으로 고성능 Model Context Protocol(MCP) 서버를 10줄 만에 빌드 | [GitHub](https://github.com/jlowin/fastmcp) |
| **#35** | `−` | 🔥 Hot | **DB-GPT** | 중국 | 프라이빗 DB 에이전트 | ⭐ `20,237` | 🍴 `3,000` | **65.02** | 데이터와 메타데이터의 외부 유출 없이 로컬 DB에 직접 쿼리를 날리고 시각화하는 프라이빗 데이터 에이전트 | [GitHub](https://github.com/eosphoros-ai/DB-GPT) |
| **#36** | `−` | 🔥 Hot | **ktransformers** | 중국 | 로컬 인퍼런스 가속 | ⭐ `19,649` | 🍴 `1,600` | **64.34** | 일반 데스크톱 GPU(예: RTX 4090) 1장으로 DeepSeek 671B MoE 모델을 실행시키는 혁신적인 CPU-GPU 오프로딩 | [GitHub](https://github.com/kvcache-ai/ktransformers) |
| **#37** | `−` | 🔥 Hot | **weaviate** | 유럽 | 클라우드 네이티브 벡터 DB | ⭐ `16,934` | 🍴 `1,433` | **63.6** | 네덜란드 암스테르담에서 탄생한 클라우드 네이티브 벡터 데이터베이스. 멀티모달 검색 및 하이브리드 검색 특화 | [GitHub](https://github.com/weaviate/weaviate) |
| **#38** | `−` | 🔥 Hot | **SubtitleEdit** | 유럽 | 로컬 음성 전사 & 자막 도구 | ⭐ `14,815` | 🍴 `1,358` | **62.97** | 덴마크에서 개발되어 전 세계 영상 전문가들이 사용하는 오픈소스 자막 편집기. 로컬 AI 모델 내장으로 오프라인 전사 | [GitHub](https://github.com/SubtitleEdit/subtitleedit) |
| **#39** | `▼14` | ⚡ Active | **mindsdb** | 유럽 | 데이터베이스 AI 미들웨어 | ⭐ `39,837` | 🍴 `6,234` | **61.59** | SQL 쿼리문 안에서 직접 AI 모델을 호출하고 실시간 예측 및 텍스트 분석을 수행하는 미들웨어 | [GitHub](https://github.com/mindsdb/mindsdb) |
| **#40** | `▼1` | ✨ Fresh | **PaddleOCR** | 중국 | 광학 문자 인식 (OCR) | ⭐ `92,093` | 🍴 `11,606` | **60.77** | 80개 이상 언어를 지원하는 초경량, 고정밀 산업용 OCR. 다단 표 및 영수증 텍스트 추출의 글로벌 최강자 | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| **#41** | `−` | 💤 Stable | **DeepSeek-V3** | 중국 | 최상위 추론 & 오픈 모델 | ⭐ `104,710` | 🍴 `16,746` | **58.65** | 671B 총 파라미터 중 37B만 활성화하는 초고효율 MoE 아키텍처. 상용 최상위 모델과 대등한 벤치마크 기록 | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3) |
| **#42** | `−` | 🔥 Hot | **koharu** | 일본 | Rust 기반 AI 만화 번역기 | ⭐ `6,569` | 🍴 `486` | **58.55** | Rust로 작성된 초고속 오픈소스 AI 만화 번역기. 텍스트 버블 탐지, OCR, 문맥 번역 및 인페인팅 | [GitHub](https://github.com/koharu-rs/koharu) |
| **#43** | `−` | 🔥 Hot | **maka** | 유럽 | 감사 가능한 로컬 실행 원장 | ⭐ `5,932` | 🍴 `572` | **58.25** | 에이전트가 내린 모든 툴 호출과 로컬 bash 명령어를 불변(Immutable) 원장에 기록해 법적 책임을 증명하는 엔진 | [GitHub](https://github.com/apache/maka) |
| **#44** | `−` | 💤 Stable | **DeepSeek-R1** | 중국 | 최상위 추론 & 오픈 모델 | ⭐ `91,994` | 🍴 `11,669` | **57.77** | 글로벌 AI 씬을 뒤흔든 오픈 가중치 최고봉 추론 모델. 강화학습을 통해 OpenAI o1 수준의 수학/코딩 추론 달성 | [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) |
| **#45** | `−` | 🔥 Hot | **voicevox** | 일본 | 서브컬처 신경망 음성 합성 | ⭐ `3,288` | 🍴 `380` | **55.33** | 일본 버추얼 유튜버 및 크리에이터 생태계의 절대적 1위 무료 음성 합성 소프트웨어 (즌다몬 등) | [GitHub](https://github.com/VOICEVOX/voicevox) |
| **#46** | `−` | 💤 Stable | **aider** | 미국 | 에이전트 코딩 & 터미널 | ⭐ `49,888` | 🍴 `5,125` | **54.4** | 터미널에서 Git과 완벽 연동되어 자동 커밋 메시지, diff 패치, 파일 맵을 관리하는 1위 코딩 도구 | [GitHub](https://github.com/Aider-AI/aider) |
| **#47** | `▲1` | 💤 Stable | **ChatTTS** | 중국 | 자연스러운 음성 합성 | ⭐ `39,963` | 🍴 `4,245` | **53.27** | 인터랙티브 대화에 특화된 혁신적 음성 합성 모델. 말하는 도중 자연스러운 웃음, 호흡, 억양 표현 | [GitHub](https://github.com/2noise/ChatTTS) |
| **#48** | `▲1` | ⚡ Active | **im-not-ai** | 대한민국 | 한국어 AI 글쓰기 윤문 & 휴머나이저 | ⭐ `6,360` | 🍴 `707` | **51.73** | AI가 쓴 한글 텍스트의 번역투, 기계적 병렬, 71대 AI 티를 탐지해 자연스러운 한국어로 정밀 재작성 | [GitHub](https://github.com/epoko77-ai/im-not-ai) |
| **#49** | `▲1` | 🔥 Hot | **natural-japanese** | 일본 | 일본어 비즈니스 문체 교정 에이전트 스킬 | ⭐ `2,003` | 🍴 `57` | **51.53** | AI가 생성한 일본어 텍스트를 읽기 쉽고 격식 있는 비즈니스 일본어로 다듬는 전용 에이전트 스킬 | [GitHub](https://github.com/coji/natural-japanese) |
| **#50** | `▲1` | 💤 Stable | **CosyVoice** | 중국 | 제로샷 음성 복제 | ⭐ `24,234` | 🍴 `2,767` | **50.73** | 3초 오디오만으로 화자의 음색, 감정, 어투를 그대로 복제하고 다국어로 교차 발화하는 음성 모델 | [GitHub](https://github.com/FunAudioLLM/CosyVoice) |
| **#51** | `▲1` | 🔥 Hot | **voicevox_core** | 일본 | 음성 합성 코어 엔진 | ⭐ `1,149` | 🍴 `168` | **50.05** | VOICEVOX의 고속 음성 합성 백엔드 C++ 코어. 파이썬과 러스트에서 경량 임베디드로 음성 출력 | [GitHub](https://github.com/VOICEVOX/voicevox_core) |
| **#52** | `▲1` | 🔥 Hot | **awesome-japanese-llm** | 일본 | 일본어 LLM 생태계 종합 인덱스 | ⭐ `1,442` | 🍴 `49` | **49.97** | 일본 국립정보학연구소(NII) 주도로 일본 내 공개된 모든 파운데이션 모델, 데이터셋을 집대성한 공식 허브 | [GitHub](https://github.com/llm-jp/awesome-japanese-llm) |
| **#53** | `▲1` | ✨ Fresh | **seamless-m4t** | 미국 | 다국어 음성 번역 하네스 | ⭐ `11,901` | 🍴 `1,188` | **49.91** | 아시아-태평양 수십 개 언어 간의 실시간 음성-음성, 음성-텍스트 다자간 통번역을 지원하는 유니버설 모델 | [GitHub](https://github.com/facebookresearch/seamless_communication) |
| **#54** | `▲1` | ✨ Fresh | **moshi** | 유럽 | 실시간 음성 대화 파운데이션 | ⭐ `11,361` | 🍴 `1,051` | **49.6** | 파리 비영리 연구소 Kyutai가 공개한 오픈소스 음성 대화 AI. STT/TTS 없이 200ms 지연으로 사람과 실시간 수다 | [GitHub](https://github.com/kyutai-labs/moshi) |
| **#55** | `▲1` | 🔥 Hot | **Mistral-Large** | 유럽 | 유럽 플래그십 파운데이션 모델 | ⭐ `958` | 🍴 `195` | **49.39** | 프랑스 AI 대표주자 Mistral의 플래그십. 다국어(불어, 독어, 스페인어, 영어)와 복잡한 추론에서 최고 수준 성능 | [GitHub](https://github.com/mistralai/mistral-common) |
| **#56** | `▲1` | 💤 Stable | **Qwen-Agent** | 중국 | 다국어 & 코딩 에이전트 | ⭐ `17,241` | 🍴 `1,758` | **48.86** | 8k부터 1M 컨텍스트까지 처리하는 알리바바 공식 에이전트. 펑션 콜링, 코드 인터프리터, 다중 툴 플래닝 | [GitHub](https://github.com/QwenLM/Qwen-Agent) |
| **#57** | `▼10` | ✨ Fresh | **SenseVoice** | 중국 | 초고속 음성 인식 & 감정 분석 | ⭐ `9,667` | 🍴 `845` | **48.71** | Whisper 대비 5배 빠르고 감정, 음악, 웃음소리까지 감지하는 음성 인식 및 오디오 이해 모델 | [GitHub](https://github.com/FunAudioLLM/SenseVoice) |
| **#58** | `▲1` | 🔥 Hot | **Kiwi** | 대한민국 | 초고속 C++ 지능형 한국어 형태소 분석기 | ⭐ `804` | 🍴 `83` | **47.89** | C++로 작성된 초고속 고정밀 한국어 형태소 분석기. 띄어쓰기 오류가 있는 텍스트도 강력하게 교정 분석 | [GitHub](https://github.com/bab2min/Kiwi) |
| **#59** | `▲1` | ✨ Fresh | **GLM-4** | 중국 | 엔터프라이즈 멀티모달 | ⭐ `7,074` | 🍴 `622` | **47.08** | 칭화대 계열 Zhipu AI의 플래그십. 1M 장문 처리, 복합 도구 호출, 고정밀 웹 브라우징 능력 제공 | [GitHub](https://github.com/THUDM/GLM-4) |
| **#60** | `▲2` | 💤 Stable | **InternVL** | 중국 | 멀티모달 시각 언어 모델 | ⭐ `10,174` | 🍴 `792` | **45.87** | GPT-4V 수준의 시각 이해 벤치마크를 기록한 오픈소스 멀티모달. 고해상도 이미지 및 복합 도표 판독 특화 | [GitHub](https://github.com/OpenGVLab/InternVL) |
| **#61** | `▼3` | 💤 Stable | **XAgent** | 중국 | 복합 자율 에이전트 | ⭐ `8,550` | 🍴 `900` | **45.23** | 인간의 개입 없이 복잡한 목표를 하위 과제로 쪼개고 외부 도구를 탐색하며 실행하는 자율 문제 해결 시스템 | [GitHub](https://github.com/OpenBMB/XAgent) |
| **#62** | `▲1` | 💤 Stable | **MindSearch** | 중국 | 심층 웹 리서치 에이전트 | ⭐ `6,944` | 🍴 `688` | **44.09** | 인간 인지 과정을 모방해 다단계 병렬 검색과 지식 그래프를 구성하는 심층 연구 엔진 (Perplexity 대안) | [GitHub](https://github.com/InternLM/MindSearch) |
| **#63** | `▲1` | 💤 Stable | **donut** | 대한민국 | OCR-free 비정형 문서 이해 트랜스포머 | ⭐ `6,927` | 🍴 `562` | **43.9** | 네이버 클로바가 공개한 OCR 엔진 없는 혁신적 엔드투엔드 문서 이해 모델. 이미지에서 JSON으로 직결 변환 | [GitHub](https://github.com/clovaai/donut) |
| **#64** | `▲1` | ⚡ Active | **soynlp** | 대한민국 | 비지도학습 한국어 자연어처리 | ⭐ `996` | 🍴 `182` | **42.5** | 사전 없이도 텍스트 데이터의 응집도(Cohesion)와 분기군(Branching Entropy)으로 단어를 자동 추출하는 비지도 토크나이저 | [GitHub](https://github.com/lovit/soynlp) |
| **#65** | `▲1` | 💤 Stable | **deep-text-recognition** | 대한민국 | 고정밀 문자 인식 (OCR) 프레임워크 | ⭐ `3,937` | 🍴 `1,128` | **42.06** | 네이버 클로바 연구팀이 구축한 텍스트 인식 벤치마크 및 4단계 모듈형 고정밀 OCR 프레임워크 | [GitHub](https://github.com/clovaai/deep-text-recognition-benchmark) |
| **#66** | `▲24` | 🔥 Hot | **llm-jp-eval** | 일본 | 일본어 자동 평가 하네스 | ⭐ `173` | 🍴 `50` | **40.78** | 일본어 독해, 번역, 수학, 추론 등 다양한 과제를 통일된 파이프라인으로 측정하는 공식 평가 도구 | [GitHub](https://github.com/llm-jp/llm-jp-eval) |
| **#67** | `−` | 💤 Stable | **mecab-ipadic-neologd** | 일본 | 일본어 신조어 & 맞춤형 사전 | ⭐ `2,798` | 🍴 `285` | **39.38** | 웹 문서와 SNS에서 매주 새로 등장하는 일본어 고유명사와 신조어를 자동 갱신하는 사실상 표준 사전 | [GitHub](https://github.com/neologd/mecab-ipadic-neologd) |
| **#68** | `−` | ✨ Fresh | **hibiki** | 유럽 | 실시간 다국어 음성 번역 | ⭐ `1,534` | 🍴 `118` | **39.0** | 말하는 도중 실시간으로 다른 언어로 음성을 바꿔서 뱉어내는 엔드투엔드 동시통역 음성 모델 | [GitHub](https://github.com/kyutai-labs/hibiki) |
| **#69** | `▼8` | ⚡ Active | **cmaes** | 일본 | 경량 블랙박스 최적화 라이브러리 | ⭐ `516` | 🍴 `80` | **38.93** | Optuna 등 하이퍼파라미터 튜닝 프레임워크에 널리 쓰이는 초고속 경량 공분산 행렬 적응 진화 전략(CMA-ES) | [GitHub](https://github.com/CyberAgentAILab/cmaes) |
| **#70** | `▼1` | 💤 Stable | **langchain-kr** | 대한민국 | LangChain & RAG 한국어 공식 쿡북 | ⭐ `2,058` | 🍴 `733` | **38.86** | 한국 AI 커뮤니티 최대 규모의 LangChain 실무 쿡북. 실무 RAG, 프롬프트 엔지니어링, 에이전트 튜토리얼 총망라 | [GitHub](https://github.com/teddylee777/langchain-kr) |
| **#71** | `▼1` | 💤 Stable | **manga-ocr** | 일본 | 일본어 만화/세로쓰기 특화 OCR | ⭐ `2,824` | 🍴 `143` | **38.82** | 일반 OCR이 판독하지 못하는 일본어 세로쓰기, 특수 폰트, 손글씨를 정확하게 판독하는 비전 모델 | [GitHub](https://github.com/kha-white/manga-ocr) |
| **#72** | `▼1` | ✨ Fresh | **fluent-korean** | 대한민국 | 코딩 에이전트 한국어 출력 스타일 | ⭐ `1,471` | 🍴 `97` | **38.65** | Claude Code 등 글로벌 CLI 코딩 에이전트가 번역투 없이 명확하고 유창한 한국어를 구사하도록 제어하는 플러그인 | [GitHub](https://github.com/snflkd/fluent-korean) |
| **#73** | `▼1` | 💤 Stable | **KoBERT** | 대한민국 | 한국어 사전학습 BERT 모델 | ⭐ `1,423` | 🍴 `375` | **36.68** | SK텔레콤이 5400만 개 이상의 한국어 문장으로 학습해 공개한 한국어 대표 사전학습 언어모델 | [GitHub](https://github.com/SKTBrain/KoBERT) |
| **#74** | `−` | 💤 Stable | **mokuro** | 일본 | 일본어 웹 만화 텍스트 레이어화 | ⭐ `1,772` | 🍴 `121` | **36.65** | 일본어 만화 이미지 위에 복사 가능한 텍스트 오버레이 레이어를 생성하여 사전 팝업 지원 | [GitHub](https://github.com/kha-white/mokuro) |
| **#75** | `▼2` | 💤 Stable | **KoAlpaca** | 대한민국 | 한국어 파운데이션 모델 & 파인튜닝 | ⭐ `1,572` | 🍴 `221` | **36.65** | 한국어 인스트럭션 데이터셋 구축 및 라마/폴리글롯 파인튜닝의 시초가 된 대표 오픈소스 | [GitHub](https://github.com/Beomi/KoAlpaca) |
| **#76** | `▼1` | 💤 Stable | **evolutionary-model-merge** | 일본 | 진화 알고리즘 기반 모델 병합 | ⭐ `1,441` | 🍴 `123` | **35.77** | 도쿄 사카나 AI가 개발한 진화 알고리즘 기반 자동 모델 병합 도구. 교차 훈련 없이 고성능 하이브리드 LLM 탄생 | [GitHub](https://github.com/SakanaAI/evolutionary-model-merge) |
| **#77** | `▼1` | 💤 Stable | **TANGO** | 일본 | 텍스트-오디오 디퓨전 생성 모델 | ⭐ `1,165` | 🍴 `150` | **35.02** | 일본 대형 IT 기업 사이버에이전트가 개발한 텍스트 프롬프트로부터 현실적인 효과음과 음악을 생성하는 모델 | [GitHub](https://github.com/CyberAgentAILab/TANGO) |
| **#78** | `▼1` | 💤 Stable | **kuromoji** | 일본 | 자바 기반 일본어 형태소 분석기 | ⭐ `1,064` | 🍴 `140` | **34.56** | Apache Lucene, Solr, Elasticsearch에 공식 내장된 가장 표준적인 자바 일본어 형태소 분석기 | [GitHub](https://github.com/atilika/kuromoji) |
| **#79** | `▼1` | 💤 Stable | **kuromoji.js** | 일본 | 자바스크립트 일본어 형태소 분석기 | ⭐ `1,009` | 🍴 `154` | **34.41** | 순수 자바스크립트로 브라우저나 Node.js 환경에서 C/바이너리 설치 없이 돌아가는 일본어 형태소 분석기 | [GitHub](https://github.com/takuyaa/kuromoji.js) |
| **#80** | `▼1` | 💤 Stable | **kogpt** | 대한민국 | 한국어 사전학습 대형 언어모델 | ⭐ `1,012` | 🍴 `132` | **34.29** | 카카오브레인이 2000억 토큰 한국어 데이터를 학습해 오픈소스로 공개한 60억 파라미터 한국어 LLM | [GitHub](https://github.com/kakaobrain/kogpt) |
| **#81** | `▼1` | 💤 Stable | **Korpora** | 대한민국 | 한국어 코퍼스 & 데이터셋 툴킷 | ⭐ `759` | 🍴 `78` | **32.59** | 네이버 영화 리뷰, 국립국어원 등 대표적인 오픈 한국어 말뭉치를 한 줄 파이썬 코드로 다운로드/정제하는 툴킷 | [GitHub](https://github.com/ko-nlp/Korpora) |
| **#82** | `▼1` | 💤 Stable | **KoELECTRA** | 대한민국 | 한국어 임베딩 & 사전학습 모델 | ⭐ `640` | 🍴 `136` | **32.33** | 대규모 한국어 텍스트로 사전학습된 고성능 ELECTRA 모델. 한국어 감정분석, 문서분류, 질의응답 최고 벤치마크 | [GitHub](https://github.com/monologg/KoELECTRA) |
| **#83** | `▼1` | 💤 Stable | **KoGPT2** | 대한민국 | 한국어 문장 생성 모델 | ⭐ `559` | 🍴 `101` | **31.48** | SK텔레콤이 공개한 한국어 범용 문장 생성 모델. 소설 이어쓰기, 챗봇 대화 생성용 기초 모델 | [GitHub](https://github.com/SKT-AI/KoGPT2) |
| **#84** | `▼1` | 💤 Stable | **KULLM** | 대한민국 | 한국어 특화 구름 LLM | ⭐ `586` | 🍴 `69` | **31.36** | 고려대학교 NLP 연구실과 HICA가 공동 제작한 한국어 인스트럭션 파인튜닝 모델 시리즈 (구름) | [GitHub](https://github.com/nlpai-lab/KULLM) |
| **#85** | `▼1` | 💤 Stable | **mecab-python3** | 일본 | 파이썬 MeCab 바인딩 | ⭐ `580` | 🍴 `53` | **31.08** | 일본어 자연어처리의 전설적인 MeCab 엔진을 현대 파이썬 3 환경에서 고속으로 호출하는 바인딩 | [GitHub](https://github.com/SamuraiT/mecab-python3) |
| **#86** | `▼1` | 💤 Stable | **KoBART** | 대한민국 | 한국어 생성 & 요약 모델 | ⭐ `471` | 🍴 `94` | **30.68** | SK텔레콤이 공개한 한국어 사전학습 BART 모델. 한국어 장문 기사 요약 및 문장 생성 표준 | [GitHub](https://github.com/SKT-AI/KoBART) |
| **#87** | `▼1` | 💤 Stable | **PyKoSpacing** | 대한민국 | 딥러닝 한국어 띄어쓰기 자동 교정기 | ⭐ `439` | 🍴 `115` | **30.55** | 대규모 말뭉치 기반 딥러닝으로 띄어쓰기가 누락되거나 잘못된 문장을 정확하게 교정하는 도구 | [GitHub](https://github.com/haven-jeon/PyKoSpacing) |
| **#88** | `▼1` | 💤 Stable | **KcBERT** | 대한민국 | 한국어 댓글/비정형 특화 BERT | ⭐ `497` | 🍴 `46` | **30.29** | 정제되지 않은 포털 뉴스 댓글 수천만 건으로 사전학습된 모델. 구어체, 오탈자, 비속어 필터링에 탁월 | [GitHub](https://github.com/Beomi/KcBERT) |
| **#89** | `▼1` | 💤 Stable | **cord** | 대한민국 | 영수증 문서 이해 데이터셋 & 모델 | ⭐ `495` | 🍴 `44` | **30.23** | 네이버 클로바가 공개한 영수증/송장 문서 정보 추출을 위한 통합 벤치마크 데이터셋 | [GitHub](https://github.com/clovaai/cord) |
| **#90** | `▼1` | 💤 Stable | **polyglot** | 대한민국 | 다국어 & 한국어 대형 언어 모델 | ⭐ `489` | 🍴 `42` | **30.14** | 한국어 씬에서 가장 널리 쓰이는 비영어권 오픈 파운데이션 모델. 한국어 토크나이저 최적화 | [GitHub](https://github.com/EleutherAI/polyglot) |
| **#91** | `−` | 💤 Stable | **mistral-eval** | 유럽 | 유럽 환경 적응형 프롬프트 평가 | ⭐ `93` | 🍴 `16` | **22.09** | 유럽 각국 언어(프랑스어, 독일어, 이탈리아어 등)에서의 논리적 일관성과 규제 준수성을 측정하는 벤치마크 | [GitHub](https://github.com/mistralai/mistral-evals) |
| **#92** | `−` | 💤 Stable | **line-distilbert-jp** | 일본 | 경량 일본어 사전학습 모델 | ⭐ `47` | 🍴 `1` | **16.72** | 라인이 131GB 대규모 일본어 텍스트로 사전학습한 초경량 고속 언어모델 | [GitHub](https://github.com/line/LINE-DistilBERT-Japanese) |

---

## 🛰️ 3. Weekly Radar Emerging Candidates (새롭게 포착된 유망 신규 AI)

GitHub Search API 고정 토픽 쿼리로 포착된, 아직 추적 목록에 없는 AI 오픈소스 후보입니다:

| 프로젝트명 | 언어 | Stars | Forks | 소개 | 저장소 링크 |
|---|:---:|:---:|:---:|---|:---:|
| **rea** | `TypeScript` | ⭐ `419,592` | 🍴 `104,797` | Reverse engineer anything with agents, from app behavior down to native binaries. | [GitHub](https://github.com/morluto/rea) |
| **ECC** | `JavaScript` | ⭐ `294,934` | 🍴 `43,653` | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. | [GitHub](https://github.com/affaan-m/ECC) |
| **firecrawl** | `TypeScript` | ⭐ `197,733` | 🍴 `10,448` | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥 | [GitHub](https://github.com/firecrawl/firecrawl) |
| **open-webui** | `Python` | ⭐ `157,499` | 🍴 `22,901` | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) | [GitHub](https://github.com/open-webui/open-webui) |
| **cc-switch** | `Rust` | ⭐ `150,992` | 🍴 `9,926` | A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io | [GitHub](https://github.com/farion1231/cc-switch) |
| **ming-voice** | `Python` | ⭐ `420` | 🍴 `24` | Low-latency local speech-to-speech voice assistant with Ming-3.0-audio-tiny on AMD and Nvidia GPUs. Easy setup on Windows and Linux | [GitHub](https://github.com/JMS1717/ming-voice) |
| **crisperwhisper-turkce-kelime-zamani** | `Python` | ⭐ `103` | 🍴 `11` | Verbatim speech-to-text with word timestamps on a 4 GB GPU: CrisperWhisper 2.0 Turbo (CT2 int8) + wav2vec2 CTC alignment. Turkish-first, Linux/WSL2. | [GitHub](https://github.com/alexturkey/crisperwhisper-turkce-kelime-zamani) |

---

## 🔎 4. 로컬 CLI 검색기 사용법 (`scripts/search.py`)

저장소 내 `scripts/search.py`를 통해 터미널에서 국가별, 순위별, 모델별로 즉시 조회할 수 있습니다:

```bash
# 1. 국가별 Top 20 조회 (us, cn, kr, eu, jp)
python scripts/search.py --country "kr"    # 🇰🇷 대한민국 Top 20 조회
python scripts/search.py --country "us"    # 🇺🇸 미국 Top 20 조회
python scripts/search.py --country "cn"    # 🇨🇳 중국 Top 20 조회
python scripts/search.py --country "eu"    # 🇪🇺 유럽 Top 20 조회
python scripts/search.py --country "jp"    # 🇯🇵 일본 Top 20 조회

# 2. 글로벌 통합 랭킹 상위 Top 10 또는 전수(Top 100) 조회
python scripts/search.py --top 10
python scripts/search.py --top

# 3. 특정 모델 호환 도구 검색 (deepseek, qwen, mistral, opus, astra 등)
python scripts/search.py --model "deepseek"

# 4. 기능 키워드 검색 (agent, ocr, voice, memory, pdf 등)
python scripts/search.py --query "agent"

# 5. 등록된 국가 및 카테고리 통계 보기
python scripts/search.py --list-countries
python scripts/search.py --list-categories
```

---

## ⚙️ 5. 자동화 아키텍처 및 파이프라인

```mermaid
flowchart LR
    A[GitHub Actions Cron<br>매주 월요일 09:00 KST] --> B[scripts/update_metrics.py]
    B -->|GitHub REST API| C[(100개 레포 주간<br>Stars / Forks / Commits)]
    C --> D[국가별 Top 20 &<br>글로벌 Top 100 랭킹 산정]
    A --> E[scripts/discover_trending.py]
    E -->|GitHub Search API| F[(신규 후보 레포 탐색)]
    D --> G[scripts/generate_global_readme.py]
    F --> G
    G --> H[README.md & Data 최신화]
    H --> I[Auto Git Commit & Push<br>skip-ci]
```

- **동적 가중치 산정 공식**:
  $$\text{Activity Score} = \log_{10}(\text{Stars}) \times 10 + \text{Recency Bonus} + \log_{10}(\text{Forks}) \times 2$$
  - 7일 이내 커밋: 가산점 +15 (🔥 Hot)
  - 30일 이내 커밋: 가산점 +8 (⚡ Active)
  - 90일 이내 커밋: 가산점 +3 (✨ Fresh)
  - 90일 초과: 가산점 0 (💤 Stable)

- **방법론**:
  - **목록 선정 기준**: 추적 대상 100개는 관리자가 수동 선정한 큐레이션 목록입니다. 국가 분류는 조직/저자의 공개 정보에 따릅니다. 신규 항목은 자동으로 목록에 합류하지 않고 Emerging 후보에만 표시됩니다.
  - **Emerging 후보의 한계**: `discover_trending.py`는 고정 토픽/키워드 쿼리(`topic:llm`, `topic:ai-agent`, `topic:mcp`, `deepseek`, `speech-to-speech`)에 최근 생성(14일 이내) 또는 최근 푸시(7일 이내) 필터를 적용해 신규·활발 레포를 포착합니다. 다만 주간 스타 증가분 지표는 없으므로 '급부상 순위'가 아니라 '최근 활동 중인 미등록 후보'로 해석해야 합니다.

---

## 📰 airadar (AI 뉴스 레이더, 실험)

[`airadar/`](airadar/) 디렉터리에는 AI 뉴스 RSS/HN 수집 → SQLite 중복 제거 → 이메일 다이제스트 → X/Threads 등 자동 포스팅 파이프라인이 들어 있습니다. 별도 비공개 저장소였던 `airadar`를 이 저장소로 옮긴 것입니다.

- 자동 포스팅은 기본 꺼짐입니다 (`config.yaml`의 `dry_run: true`, `post_to_*: false`). 이 저장소의 GitHub Actions에는 airadar 스케줄 실행이 없으며, push/PR 시 테스트만 돕니다.
- 시크릿은 저장소에 없습니다. `airadar/.env.example`을 `.env`로 복사해 로컬에서만 채우세요.
- 설치·사용법은 [airadar/README.md](airadar/README.md) 참고.

## 🤝 기여 및 건의
- 새로운 글로벌 오픈소스 AI 프로젝트나 획기적인 에이전트 도구가 발표되면 언제든 이슈(Issue)나 풀 리퀘스트(PR)를 남겨주세요.
- 관리 주체: [daeryundf2-prog](https://github.com/daeryundf2-prog)
