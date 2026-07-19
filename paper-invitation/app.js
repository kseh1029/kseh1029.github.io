/* ==========================================================================
   종이 청첩장 시안 시뮬레이터 로직 (Vanilla Javascript)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 상태 관리 객체 (State)
  const state = {
    // 레이아웃 & 용지
    layoutType: '3fold-vertical',
    paperSize: 'size-standard',
    showGuidelines: true,
    viewMode: 'flat-inside', // flat-inside, flat-outside, folding-3d
    zoom: 100,

    // 타이포그래피 & 데코레이션
    fontFamily: 'font-serif',
    letterSpacing: 0.5,
    lineHeight: 1.8,
    textAlign: 'center',
    borderStyle: 'border-none',
    dividerStyle: 'div-flower',
    paperColor: 'color-ivory',

    // 텍스트 컨텐츠
    coverTitle: 'The Wedding of',
    coverNames: '김승현 그리고 김다솔',
    coverDate: '2026. 10. 31 SATURDAY',
    showCoverIllust: true,
    
    greetingTitle: '초대합니다',
    greetingBody: `가을이 깊어지는 계절에\n소중한 분들께 좋은 소식을 전합니다.\n함께하는 시간이 자연스럽고 편안한 사람과\n새로운 시작을 준비하게 되었습니다.\n\n앞으로의 날들도 이 계절처럼\n차분하고 따뜻하게\n두 사람이 함께 잘 채워가겠습니다.\n기쁜 날에 오셔서 축복해 주시면\n큰 기쁨이 되겠습니다.`,
    
    groomFather: '(故) 김창득',
    groomMother: '이재숙',
    groomRelation: '의 차남',
    groomName: '승현',
    
    brideFather: '김종문',
    brideMother: '김명임',
    brideRelation: '의 차녀',
    brideName: '다솔',
    
    weddingDatetime: '2026년 10월 31일 토요일 오후 5시',
    weddingVenueName: '그랜드 모먼트 클래식홀 (지하 4층)',
    weddingVenueAddr: '부산광역시 남구 황령대로 401-9 (대연동)',
    showMap: true,
    
    transShuttle: `지하철 2호선 남천역 4번 출구 앞 (대남교차로 방면 탑승)\n결혼식 당일 셔틀버스가 상시 운행됩니다. (매시간 5분, 20분, 35분, 50분)`,
    transSubwayBus: `지하철: 2호선 남천역 4번 출구에서 셔틀버스 이용\n시내버스: 38번, 583번 버스 승차 후 '동원 보라아파트 정류장' 하차`,
    transCar: `네비게이션: '그랜드 모먼트' 검색\n주차: 예식장 주차장 3시간 무료 주차 지원`
  };

  // 꽃 SVG 디바이더 문자열
  const flowerSvg = `
    <svg viewBox="0 0 100 30" xmlns="http://www.w3.org/2000/svg">
      <path d="M50,5 C55,15 65,15 60,20 C55,25 50,15 50,15 C50,15 45,25 40,20 C35,15 45,15 50,5 Z" />
      <path d="M50,15 C52,18 55,20 62,20 C69,20 65,13 60,15 C55,17 50,15 50,15 Z" opacity="0.7" />
      <path d="M50,15 C48,18 45,20 38,20 C31,20 35,13 40,15 C45,17 50,15 50,15 Z" opacity="0.7" />
      <circle cx="50" cy="15" r="2" fill="#fff" />
      <path d="M15,15 L40,15" stroke="currentColor" stroke-width="0.5" stroke-dasharray="1 2" />
      <path d="M60,15 L85,15" stroke="currentColor" stroke-width="0.5" stroke-dasharray="1 2" />
    </svg>
  `;

  const blankOrnamentSvg = `
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="40" fill="none" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 3" />
      <path d="M50,20 L50,80 M20,50 L80,50" stroke="currentColor" stroke-width="0.5" opacity="0.3" />
      <path d="M45,45 L55,55 M45,55 L55,45" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    </svg>
  `;

  // DOM 요소 선택
  const DOM = {
    // 탭 버튼 및 컨텐츠
    tabBtns: document.querySelectorAll('.tab-btn'),
    tabDesign: document.getElementById('tab-design'),
    tabContent: document.getElementById('tab-content'),

    // 디자인 설정 입력 컨트롤들
    layoutType: document.getElementById('layout-type'),
    paperSize: document.getElementById('paper-size'),
    showGuidelines: document.getElementById('show-guidelines'),
    fontFamily: document.getElementById('font-family'),
    letterSpacing: document.getElementById('letter-spacing'),
    valLetterSpacing: document.getElementById('val-letter-spacing'),
    lineHeight: document.getElementById('line-height'),
    valLineHeight: document.getElementById('val-line-height'),
    alignBtns: document.querySelectorAll('[data-align]'),
    borderStyle: document.getElementById('border-style'),
    dividerStyle: document.getElementById('divider-style'),
    paperColor: document.getElementById('paper-color'),

    // 텍스트 설정 입력 컨트롤들
    coverTitle: document.getElementById('cover-title'),
    coverNames: document.getElementById('cover-names'),
    coverDate: document.getElementById('cover-date'),
    greetingTitle: document.getElementById('greeting-title'),
    greetingBody: document.getElementById('greeting-body'),
    groomFather: document.getElementById('groom-father'),
    groomMother: document.getElementById('groom-mother'),
    groomName: document.getElementById('groom-name'),
    brideFather: document.getElementById('bride-father'),
    brideMother: document.getElementById('bride-mother'),
    brideName: document.getElementById('bride-name'),
    weddingDatetime: document.getElementById('wedding-datetime'),
    weddingVenueName: document.getElementById('wedding-venue-name'),
    weddingVenueAddr: document.getElementById('wedding-venue-addr'),
    showMap: document.getElementById('show-map'),
    showCoverIllust: document.getElementById('show-cover-illust'),
    transShuttle: document.getElementById('trans-shuttle'),
    transSubwayBus: document.getElementById('trans-subway-bus'),
    transCar: document.getElementById('trans-car'),

    // 동작 버튼
    btnPrint: document.getElementById('btn-print'),
    btnZoomIn: document.getElementById('btn-zoom-in'),
    btnZoomOut: document.getElementById('btn-zoom-out'),
    zoomValue: document.getElementById('zoom-value'),
    viewBtns: document.querySelectorAll('.view-btn'),

    // 캔버스 엘리먼트
    canvasWrapper: document.getElementById('canvas-wrapper'),
    flatViewer: document.getElementById('flat-viewer'),
    panelsContainer: document.getElementById('panels-container'),
    folding3dViewer: document.getElementById('folding-3d-viewer'),
    card3dModel: document.getElementById('card-3d'),
    btnFoldOpen: document.getElementById('btn-fold-open'),
    btnFoldClose: document.getElementById('btn-fold-close'),
    scene3D: document.querySelector('.scene-3d')
  };

  // ==========================================================================
  // SIDEBAR TAB INTERACTION
  // ==========================================================================
  DOM.tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      DOM.tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const tabName = btn.getAttribute('data-sidebar-tab');

      if (tabName === 'design') {
        DOM.tabDesign.classList.add('active');
        DOM.tabContent.classList.remove('active');
      } else {
        DOM.tabDesign.classList.remove('active');
        DOM.tabContent.classList.add('active');
      }
    });
  });

  // ==========================================================================
  // 3D CARD DRAG TO ROTATE LOGIC
  // ==========================================================================
  let isDragging = false;
  let previousMousePosition = { x: 0, y: 0 };
  let currentRotation = { x: 20, y: -10 }; // 초기 회전 각도

  DOM.scene3D.addEventListener('mousedown', (e) => {
    isDragging = true;
    previousMousePosition = { x: e.clientX, y: e.clientY };
  });

  document.addEventListener('mouseup', () => {
    isDragging = false;
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDragging || state.viewMode !== 'folding-3d') return;

    const deltaMove = {
      x: e.clientX - previousMousePosition.x,
      y: e.clientY - previousMousePosition.y
    };

    // 마우스 이동 거리에 비례하여 회전각 업데이트 (적정 배율 곱함)
    currentRotation.y += deltaMove.x * 0.5;
    currentRotation.x -= deltaMove.y * 0.5;

    // 상하 회전각(X축) 한계 제한 (-60도 ~ 60도)
    currentRotation.x = Math.max(-60, Math.min(60, currentRotation.x));

    DOM.card3dModel.style.transform = `rotateX(${currentRotation.x}deg) rotateY(${currentRotation.y}deg)`;

    previousMousePosition = {
      x: e.clientX,
      y: e.clientY
    };
  });

  // 모바일 터치 대응 회전
  DOM.scene3D.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      isDragging = true;
      previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }
  });

  document.addEventListener('touchend', () => {
    isDragging = false;
  });

  document.addEventListener('touchmove', (e) => {
    if (!isDragging || state.viewMode !== 'folding-3d' || e.touches.length !== 1) return;

    const deltaMove = {
      x: e.touches[0].clientX - previousMousePosition.x,
      y: e.touches[0].clientY - previousMousePosition.y
    };

    currentRotation.y += deltaMove.x * 0.6;
    currentRotation.x -= deltaMove.y * 0.6;
    currentRotation.x = Math.max(-60, Math.min(60, currentRotation.x));

    DOM.card3dModel.style.transform = `rotateX(${currentRotation.x}deg) rotateY(${currentRotation.y}deg)`;

    previousMousePosition = {
      x: e.touches[0].clientX,
      y: e.touches[0].clientY
    };
  });

  // 3D 접고 펴기 제어 버튼 바인딩
  DOM.btnFoldOpen.addEventListener('click', () => {
    DOM.card3dModel.classList.remove('folded');
    DOM.btnFoldOpen.classList.add('active');
    DOM.btnFoldClose.classList.remove('active');
  });

  DOM.btnFoldClose.addEventListener('click', () => {
    DOM.card3dModel.classList.add('folded');
    DOM.btnFoldOpen.classList.remove('active');
    DOM.btnFoldClose.classList.add('active');
  });

  // ==========================================================================
  // RENDER DRAFT CANVASES (FLAT & 3D)
  // ==========================================================================

  // 공통 마크업 빌더 헬퍼
  const buildCoverMarkup = () => `
    ${state.showCoverIllust ? `
      <div class="cover-illust-wrapper">
        <img src="wedding_cover_illust.jpg" alt="Wedding Cover Illustration" class="cover-illust-img">
      </div>
    ` : ''}
    <div class="cover-english" contenteditable="true" data-key="coverTitle">${state.coverTitle}</div>
    <div class="cover-calligraphy">Wedding</div>
    <div class="cover-divider"></div>
    <div class="cover-names" contenteditable="true" data-key="coverNames">${state.coverNames}</div>
    <div class="cover-date" contenteditable="true" data-key="coverDate">${state.coverDate}</div>
  `;

  const buildGreetingMarkup = () => `
    <div class="panel-section-title" contenteditable="true" data-key="greetingTitle">${state.greetingTitle}</div>
    <div class="floral-divider">${state.dividerStyle === 'div-flower' ? flowerSvg : ''}</div>
    <div class="greeting-text-box" contenteditable="true" data-key="greetingBody">${state.greetingBody.replace(/\n/g, '<br>')}</div>
    <div class="floral-divider">${state.dividerStyle === 'div-flower' ? flowerSvg : ''}</div>
    <div class="relations-box">
      <div class="relation-row">
        <span class="relation-parents" contenteditable="true" data-key="groomFather">${state.groomFather}</span>
        <span class="relation-parents" opacity="0.5">·</span>
        <span class="relation-parents" contenteditable="true" data-key="groomMother">${state.groomMother}</span>
        <span class="relation-type">${state.groomRelation}</span>
        <span class="relation-name" contenteditable="true" data-key="groomName">${state.groomName}</span>
      </div>
      <div class="relation-row">
        <span class="relation-parents" contenteditable="true" data-key="brideFather">${state.brideFather}</span>
        <span class="relation-parents" opacity="0.5">·</span>
        <span class="relation-parents" contenteditable="true" data-key="brideMother">${state.brideMother}</span>
        <span class="relation-type">${state.brideRelation}</span>
        <span class="relation-name" contenteditable="true" data-key="brideName">${state.brideName}</span>
      </div>
    </div>
  `;

  const buildLocationMarkup = () => `
    <div class="panel-section-title">Wedding Day</div>
    <div class="wedding-time-summary" contenteditable="true" data-key="weddingDatetime">${state.weddingDatetime}</div>
    <div class="location-hall-name" contenteditable="true" data-key="weddingVenueName">${state.weddingVenueName}</div>
    <div class="location-hall-addr" contenteditable="true" data-key="weddingVenueAddr">${state.weddingVenueAddr}</div>
    
    ${state.showMap ? `
      <div class="location-map-wrapper">
        <img src="../wedding/map-illustrated.png" alt="illustrated wedding map" onerror="this.src='https://placehold.co/400x200?text=Map+Placeholder'">
      </div>
    ` : ''}

    <div class="transport-info-box">
      <div class="transport-section">
        <div class="transport-title">지하철 및 셔틀버스</div>
        <div class="transport-desc" contenteditable="true" data-key="transShuttle">${state.transShuttle.replace(/\n/g, '<br>')}</div>
      </div>
      <div class="transport-section">
        <div class="transport-title">시내버스 안내</div>
        <div class="transport-desc" contenteditable="true" data-key="transSubwayBus">${state.transSubwayBus.replace(/\n/g, '<br>')}</div>
      </div>
      <div class="transport-section">
        <div class="transport-title">자가용 및 주차</div>
        <div class="transport-desc" contenteditable="true" data-key="transCar">${state.transCar.replace(/\n/g, '<br>')}</div>
      </div>
    </div>
  `;

  const buildBackMarkup = () => `
    <div class="panel-blank-ornament">
      ${blankOrnamentSvg}
    </div>
    <div class="back-thankyou" contenteditable="true">
      소중한 발걸음 하셔서<br>
      저희의 앞날을 축복해 주시면<br>
      감사하겠습니다.
    </div>
  `;

  const buildBlankMarkup = () => `
    <div class="panel-blank-ornament">
      ${blankOrnamentSvg}
    </div>
    <div style="font-size: 11px; color: var(--accent-gold-dark); letter-spacing: 2px;">INVITATION</div>
  `;

  const buildDateOnlyMarkup = () => `
    <div class="mini-calendar-container">
      <div class="calendar-header">2026년 &nbsp; 10월</div>
      <table class="calendar-table">
        <thead>
          <tr>
            <th class="sun">일</th>
            <th>월</th>
            <th>화</th>
            <th>수</th>
            <th>목</th>
            <th>금</th>
            <th class="sat">토</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td></td><td></td><td></td><td></td>
            <td>1</td><td>2</td><td class="sat">3</td>
          </tr>
          <tr>
            <td class="sun">4</td><td>5</td><td>6</td><td>7</td>
            <td>8</td><td>9</td><td class="sat">10</td>
          </tr>
          <tr>
            <td class="sun">11</td><td>12</td><td>13</td><td>14</td>
            <td>15</td><td>16</td><td class="sat">17</td>
          </tr>
          <tr>
            <td class="sun">18</td><td>19</td><td>20</td><td>21</td>
            <td>22</td><td>23</td><td class="sat">24</td>
          </tr>
          <tr>
            <td class="sun">25</td><td>26</td><td>27</td><td>28</td>
            <td>29</td><td>30</td><td class="sat"><span class="wedding-day-highlight">31</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  `;

  // 1. 2D 평면 렌더링
  const renderFlatCard = () => {
    DOM.panelsContainer.innerHTML = '';
    const layout = state.layoutType;
    const isInside = state.viewMode === 'flat-inside';

    if (layout === '3fold-vertical') {
      // 3단 세로 접지
      if (isInside) {
        // 내지: 왼쪽(빈 문양) - 가운데(인사말) - 오른쪽(오시는길/약도)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-blank">${buildBlankMarkup()}</div>
          <div class="panel-fold-line" style="left: 33.333%"></div>
          <div class="card-panel panel-greeting">${buildGreetingMarkup()}</div>
          <div class="panel-fold-line" style="left: 66.666%"></div>
          <div class="card-panel panel-location">${buildLocationMarkup()}</div>
        `;
      } else {
        // 외지: 왼쪽(뒷표지) - 가운데(안쪽 날개/빈칸) - 오른쪽(앞표지)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-back">${buildBackMarkup()}</div>
          <div class="panel-fold-line" style="left: 33.333%"></div>
          <div class="card-panel panel-blank">${buildBlankMarkup()}</div>
          <div class="panel-fold-line" style="left: 66.666%"></div>
          <div class="card-panel panel-cover">${buildCoverMarkup()}</div>
        `;
      }
    } 
    else if (layout === '2fold-vertical') {
      // 2단 세로 접지
      if (isInside) {
        // 내지: 왼쪽(인사말) - 오른쪽(오시는길)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-greeting">${buildGreetingMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-location">${buildLocationMarkup()}</div>
        `;
      } else {
        // 외지: 왼쪽(뒷표지) - 오른쪽(앞표지)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-back">${buildBackMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-cover">${buildCoverMarkup()}</div>
        `;
      }
    }
    else if (layout === '2fold-mini') {
      // 명함 크기 2단 접지
      if (isInside) {
        // 내지: 왼쪽(인사말) - 오른쪽(오시는길)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-greeting" style="padding: 24px 16px;">${buildGreetingMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-location" style="padding: 24px 16px;">${buildLocationMarkup()}</div>
        `;
      } else {
        // 외지: 왼쪽(뒷면 날짜) - 오른쪽(앞면 표지)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-back" style="display: flex; align-items: center; justify-content: center; text-align: center; padding: 24px 16px;">${buildDateOnlyMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-cover" style="padding: 24px 16px;">${buildCoverMarkup()}</div>
        `;
      }
    }
    else if (layout === '2fold-horizontal') {
      // 2단 가로 접지 (위아래로 접히는 구조 혹은 가로형 책자 구조)
      // 여기서는 2단 가로로 배치 (인쇄 상 가로 사이드 바이 사이드 배치)
      if (isInside) {
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-greeting" style="padding: 30px 40px;">${buildGreetingMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-location" style="padding: 30px 40px;">${buildLocationMarkup()}</div>
        `;
      } else {
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-back">${buildBackMarkup()}</div>
          <div class="panel-fold-line" style="left: 50%"></div>
          <div class="card-panel panel-cover">${buildCoverMarkup()}</div>
        `;
      }
    } 
    else if (layout === 'postcard') {
      // 엽서형 (접지 없음, 앞뒷면만 존재)
      if (isInside) {
        // 엽서 뒷면 (내용)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-greeting" style="width: 100%; height: 100%;">${buildGreetingMarkup()}</div>
        `;
      } else {
        // 엽서 앞면 (표지)
        DOM.panelsContainer.innerHTML = `
          <div class="card-panel panel-cover" style="width: 100%; height: 100%;">${buildCoverMarkup()}</div>
        `;
      }
    }

    // 인라인 편집 이벤트 수신 대기 설정
    setupInlineEditingListeners();
  };

  // 2. 3D 시뮬레이터 렌더링
  const render3DCard = () => {
    DOM.card3dModel.innerHTML = '';
    
    // 3D 카드 모델의 클래스 초기화
    DOM.card3dModel.className = 'card-3d-model';
    DOM.card3dModel.classList.add(DOM.btnFoldClose.classList.contains('active') ? 'folded' : 'unfolded');

    const layout = state.layoutType;

    if (layout === '3fold-vertical') {
      // 3단 세로 3D
      // Center panel (Greeting / Inside, Blank / Outside)
      // Left panel (Blank / Inside, Back / Outside) - rotateY(180) when folded
      // Right panel (Location / Inside, Cover / Outside) - rotateY(-180) when folded
      DOM.card3dModel.innerHTML = `
        <!-- Left Panel -->
        <div class="panel-3d left-p">
          <div class="panel-3d-face front">
            ${buildBlankMarkup()}
          </div>
          <div class="panel-3d-face back">
            ${buildBackMarkup()}
          </div>
        </div>

        <!-- Center Panel -->
        <div class="panel-3d center-p">
          <div class="panel-3d-face front">
            <div class="panel-greeting" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center;">
              ${buildGreetingMarkup()}
            </div>
          </div>
          <div class="panel-3d-face back">
            <div class="panel-blank" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
              ${buildBlankMarkup()}
            </div>
          </div>
        </div>

        <!-- Right Panel -->
        <div class="panel-3d right-p">
          <div class="panel-3d-face front">
            <div class="panel-location" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center;">
              ${buildLocationMarkup()}
            </div>
          </div>
          <div class="panel-3d-face back">
            <div class="panel-cover" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
              ${buildCoverMarkup()}
            </div>
          </div>
        </div>
      `;
    } 
    else if (layout === '2fold-vertical' || layout === '2fold-horizontal' || layout === '2fold-mini') {
      // 2단 세로/가로/미니 3D
      DOM.card3dModel.classList.add('fold-2d-v');
      DOM.card3dModel.innerHTML = `
        <!-- Left Panel (접히는 면: 내지 왼쪽 / 바깥 뒷면) -->
        <div class="panel-3d left-p">
          <div class="panel-3d-face front">
            <div class="panel-greeting" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center;">
              ${buildGreetingMarkup()}
            </div>
          </div>
          <div class="panel-3d-face back">
            ${layout === '2fold-mini' ? `<div style="display: flex; align-items: center; justify-content: center; height: 100%; text-align: center; padding: 20px 10px;">${buildDateOnlyMarkup()}</div>` : buildBackMarkup()}
          </div>
        </div>

        <!-- Center/Right Panel (고정면: 내지 오른쪽 / 바깥 표지) -->
        <div class="panel-3d center-p">
          <div class="panel-3d-face front">
            <div class="panel-location" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center;">
              ${buildLocationMarkup()}
            </div>
          </div>
          <div class="panel-3d-face back">
            <div class="panel-cover" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
              ${buildCoverMarkup()}
            </div>
          </div>
        </div>
      `;
    } 
    else {
      // 엽서형 3D (회전만 가능한 양면 카드)
      DOM.card3dModel.innerHTML = `
        <div class="panel-3d center-p">
          <div class="panel-3d-face front">
            <div class="panel-greeting" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
              ${buildGreetingMarkup()}
            </div>
          </div>
          <div class="panel-3d-face back">
            <div class="panel-cover" style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
              ${buildCoverMarkup()}
            </div>
          </div>
        </div>
      `;
    }
  };

  // 패널의 가로/세로 비율 및 크기 조절 함수
  const adjustPanelDimensions = () => {
    if (state.layoutType === '2fold-mini') {
      document.documentElement.style.setProperty('--panel-w', '200px');
      document.documentElement.style.setProperty('--panel-h', '360px');
      return;
    }
    const isHorizontal = state.layoutType === '2fold-horizontal';
    if (state.paperSize === 'size-square') {
      document.documentElement.style.setProperty('--panel-w', '400px');
      document.documentElement.style.setProperty('--panel-h', '400px');
    } else if (state.paperSize === 'size-long') {
      if (isHorizontal) {
        document.documentElement.style.setProperty('--panel-w', '640px');
        document.documentElement.style.setProperty('--panel-h', '320px');
      } else {
        document.documentElement.style.setProperty('--panel-w', '320px');
        document.documentElement.style.setProperty('--panel-h', '640px');
      }
    } else { // size-standard
      if (isHorizontal) {
        document.documentElement.style.setProperty('--panel-w', '570px');
        document.documentElement.style.setProperty('--panel-h', '380px');
      } else {
        document.documentElement.style.setProperty('--panel-w', '380px');
        document.documentElement.style.setProperty('--panel-h', '570px');
      }
    }
  };

  // 시안 렌더 통합 함수
  const renderAll = () => {
    adjustPanelDimensions();
    if (state.viewMode === 'folding-3d') {
      DOM.flatViewer.classList.remove('active');
      DOM.folding3dViewer.classList.add('active');
      render3DCard();
    } else {
      DOM.flatViewer.classList.add('active');
      DOM.folding3dViewer.classList.remove('active');
      renderFlatCard();
    }
    updateCardStyles();
  };

  // ==========================================================================
  // UPDATE CARD STYLES (FONTS, ALIGNMENT, DECORS)
  // ==========================================================================
  const updateCardStyles = () => {
    const panels = document.querySelectorAll('.card-panel, .panel-3d-face');
    
    // 폰트 클래스 및 스타일 반영
    panels.forEach(panel => {
      // 폰트 클래스 리셋 및 재부여
      panel.classList.remove('font-serif', 'font-sans', 'font-classic', 'font-playfair');
      panel.classList.add(state.fontFamily);

      // 정렬 및 텍스트 디테일 스타일 적용
      panel.classList.remove('align-center', 'align-left', 'align-right');
      panel.classList.add(`align-${state.textAlign}`);
      
      panel.style.letterSpacing = `${state.letterSpacing}px`;
      panel.style.lineHeight = state.lineHeight;
    });

    // 종이 컬러, 테두리, 구분선 데코레이터 클래스 부여
    const canvasCardFlat = DOM.flatViewer;
    const model3d = DOM.card3dModel;

    // 초기화
    const resetClasses = (el) => {
      if (!el) return;
      el.className = el.className.split(' ').filter(c => 
        !c.startsWith('color-') && 
        !c.startsWith('border-') && 
        !c.startsWith('div-') &&
        !c.startsWith('layout-')
      ).join(' ');
    };

    resetClasses(canvasCardFlat);
    resetClasses(model3d);

    // 클래스 추가
    const styleClasses = [
      state.paperColor,
      state.borderStyle,
      state.dividerStyle,
      `layout-${state.layoutType}`
    ];

    styleClasses.forEach(c => {
      canvasCardFlat.classList.add(c);
      model3d.classList.add(c);
    });

    // 가이드라인 오버레이 토글
    if (state.showGuidelines) {
      DOM.canvasWrapper.classList.remove('hide-guides');
    } else {
      DOM.canvasWrapper.classList.add('hide-guides');
    }

    // 레이아웃 타입에 따라 캔버스 크기 제어
    const panelsContainer = DOM.panelsContainer;
    if (state.layoutType === '3fold-vertical') {
      panelsContainer.style.width = 'calc(var(--panel-w) * 3)';
      panelsContainer.style.height = 'var(--panel-h)';
    } else if (state.layoutType === '2fold-vertical' || state.layoutType === '2fold-horizontal' || state.layoutType === '2fold-mini') {
      panelsContainer.style.width = 'calc(var(--panel-w) * 2)';
      panelsContainer.style.height = 'var(--panel-h)';
    } else {
      // 엽서형
      panelsContainer.style.width = 'var(--panel-w)';
      panelsContainer.style.height = 'var(--panel-h)';
    }

    // 줌 레벨 스크린 캔버스에 적용
    applyZoom();
  };

  // ==========================================================================
  // INLINE EDITING LOGIC (SYNC CANVAS -> SIDEBAR FORM)
  // ==========================================================================
  const setupInlineEditingListeners = () => {
    const editableElements = DOM.panelsContainer.querySelectorAll('[contenteditable="true"]');
    
    editableElements.forEach(el => {
      el.addEventListener('input', () => {
        const key = el.getAttribute('data-key');
        if (!key) return;

        // 엔터로 인한 <br> 또는 \n 변환 처리
        let val = el.innerHTML;
        // HTML -> 텍스트 포맷 (줄바꿈 \n 처리)
        val = val.replace(/<br\s*\/?>/gi, '\n');
        val = val.replace(/&nbsp;/g, ' ');
        // 태그 제거
        const temp = document.createElement('div');
        temp.innerHTML = val;
        val = temp.textContent || temp.innerText || '';

        // 상태값 업데이트
        state[key] = val;

        // 사이드바 입력창에 동기화
        const inputEl = document.getElementById(
          key === 'coverTitle' ? 'cover-title' :
          key === 'coverNames' ? 'cover-names' :
          key === 'coverDate' ? 'cover-date' :
          key === 'greetingTitle' ? 'greeting-title' :
          key === 'greetingBody' ? 'greeting-body' :
          key === 'groomFather' ? 'groom-father' :
          key === 'groomMother' ? 'groom-mother' :
          key === 'groomName' ? 'groom-name' :
          key === 'brideFather' ? 'bride-father' :
          key === 'brideMother' ? 'bride-mother' :
          key === 'brideName' ? 'bride-name' :
          key === 'weddingDatetime' ? 'wedding-datetime' :
          key === 'weddingVenueName' ? 'wedding-venue-name' :
          key === 'weddingVenueAddr' ? 'wedding-venue-addr' :
          key === 'transShuttle' ? 'trans-shuttle' :
          key === 'transSubwayBus' ? 'trans-subway-bus' :
          key === 'transCar' ? 'trans-car' : ''
        );

        if (inputEl) {
          inputEl.value = val;
        }

        // 3D 뷰어 등 다른 곳에 텍스트 즉시 동기화하기 위해 (렌더링을 완전히 다시하면 커서가 튐으로, 선택적 업데이트)
        syncTo3DViewer(key, val);
      });
    });
  };

  // 3D 뷰어에 인라인 텍스트 즉시 동기화
  const syncTo3DViewer = (key, val) => {
    if (state.viewMode === 'folding-3d') return; // 이미 3D 모드면 이벤트가 2D 인라인에서 오지 않음
    
    const targets = DOM.card3dModel.querySelectorAll(`[data-key="${key}"]`);
    targets.forEach(t => {
      t.innerHTML = val.replace(/\n/g, '<br>');
    });
  };

  // ==========================================================================
  // SIDEBAR INPUT CHANGE -> CANVAS RE-RENDER
  // ==========================================================================
  const syncSidebarToState = (inputEl, stateKey, isHTML = false) => {
    inputEl.addEventListener('input', () => {
      state[stateKey] = inputEl.value;
      
      // 2D 캔버스의 대응 요소 업데이트 (전체 다시 렌더링하면 포커스가 튀지 않음)
      const targets2D = DOM.panelsContainer.querySelectorAll(`[data-key="${stateKey}"]`);
      targets2D.forEach(t => {
        t.innerHTML = isHTML ? inputEl.value.replace(/\n/g, '<br>') : inputEl.value;
      });

      // 3D 캔버스 동기화
      const targets3D = DOM.card3dModel.querySelectorAll(`[data-key="${stateKey}"]`);
      targets3D.forEach(t => {
        t.innerHTML = isHTML ? inputEl.value.replace(/\n/g, '<br>') : inputEl.value;
      });
    });
  };

  // 모든 인풋 요소에 양방향 바인딩 걸기
  syncSidebarToState(DOM.coverTitle, 'coverTitle');
  syncSidebarToState(DOM.coverNames, 'coverNames');
  syncSidebarToState(DOM.coverDate, 'coverDate');
  syncSidebarToState(DOM.greetingTitle, 'greetingTitle');
  syncSidebarToState(DOM.greetingBody, 'greetingBody', true);
  syncSidebarToState(DOM.groomFather, 'groomFather');
  syncSidebarToState(DOM.groomMother, 'groomMother');
  syncSidebarToState(DOM.groomName, 'groomName');
  syncSidebarToState(DOM.brideFather, 'brideFather');
  syncSidebarToState(DOM.brideMother, 'brideMother');
  syncSidebarToState(DOM.brideName, 'brideName');
  syncSidebarToState(DOM.weddingDatetime, 'weddingDatetime');
  syncSidebarToState(DOM.weddingVenueName, 'weddingVenueName');
  syncSidebarToState(DOM.weddingVenueAddr, 'weddingVenueAddr');
  syncSidebarToState(DOM.transShuttle, 'transShuttle', true);
  syncSidebarToState(DOM.transSubwayBus, 'transSubwayBus', true);
  syncSidebarToState(DOM.transCar, 'transCar', true);

  // 셀렉터 및 기타 UI 이벤트 감지
  DOM.layoutType.addEventListener('change', () => {
    state.layoutType = DOM.layoutType.value;
    renderAll();
  });

  DOM.paperSize.addEventListener('change', () => {
    state.paperSize = DOM.paperSize.value;
    renderAll();
  });

  DOM.showGuidelines.addEventListener('change', () => {
    state.showGuidelines = DOM.showGuidelines.checked;
    updateCardStyles();
  });

  DOM.showCoverIllust.addEventListener('change', () => {
    state.showCoverIllust = DOM.showCoverIllust.checked;
    renderAll();
  });

  DOM.fontFamily.addEventListener('change', () => {
    state.fontFamily = DOM.fontFamily.value;
    updateCardStyles();
  });

  DOM.letterSpacing.addEventListener('input', () => {
    state.letterSpacing = DOM.letterSpacing.value;
    DOM.valLetterSpacing.textContent = `${state.letterSpacing}px`;
    updateCardStyles();
  });

  DOM.lineHeight.addEventListener('input', () => {
    state.lineHeight = DOM.lineHeight.value;
    DOM.valLineHeight.textContent = state.lineHeight;
    updateCardStyles();
  });

  DOM.alignBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      DOM.alignBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.textAlign = btn.getAttribute('data-align');
      updateCardStyles();
    });
  });

  DOM.borderStyle.addEventListener('change', () => {
    state.borderStyle = DOM.borderStyle.value;
    updateCardStyles();
  });

  DOM.dividerStyle.addEventListener('change', () => {
    state.dividerStyle = DOM.dividerStyle.value;
    // 구분선이 바뀌면 레이아웃 마크업이 크게 변하므로 전면 재렌더링
    renderAll();
  });

  DOM.paperColor.addEventListener('change', () => {
    state.paperColor = DOM.paperColor.value;
    updateCardStyles();
  });

  DOM.showMap.addEventListener('change', () => {
    state.showMap = DOM.showMap.checked;
    renderAll();
  });

  // ==========================================================================
  // VIEW MODE TOGGLE & ZOOM LOGIC
  // ==========================================================================
  DOM.viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      DOM.viewBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      state.viewMode = btn.getAttribute('data-view');
      renderAll();
    });
  });

  // Zoom
  const applyZoom = () => {
    if (state.viewMode === 'folding-3d') {
      DOM.scene3D.style.transform = `scale(${state.zoom / 100})`;
    } else {
      DOM.flatViewer.style.transform = `scale(${state.zoom / 100})`;
    }
    DOM.zoomValue.textContent = `${state.zoom}%`;
  };

  DOM.btnZoomIn.addEventListener('click', () => {
    if (state.zoom < 200) {
      state.zoom += 10;
      applyZoom();
    }
  });

  DOM.btnZoomOut.addEventListener('click', () => {
    if (state.zoom > 50) {
      state.zoom -= 10;
      applyZoom();
    }
  });

  // Print Event
  DOM.btnPrint.addEventListener('click', () => {
    // 줌 배율을 100%로 리셋한 후 인쇄창을 띄워 인쇄 깨짐 방지
    const prevZoom = state.zoom;
    state.zoom = 100;
    applyZoom();

    // 인쇄 모드 실행
    window.print();

    // 인쇄 완료 후 기존 배율 복구
    setTimeout(() => {
      state.zoom = prevZoom;
      applyZoom();
    }, 500);
  });

  // ==========================================================================
  // INITIAL RUN
  // ==========================================================================
  renderAll();
});
