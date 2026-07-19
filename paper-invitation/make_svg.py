import base64
import os

img_path = '/Users/Seunghyun/.gemini/antigravity/scratch/kseh1029.github.io/paper-invitation/wedding_cover_illust.jpg'
b64_img = ""
if os.path.exists(img_path):
    with open(img_path, 'rb') as f:
        b64_img = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')

# ==========================================
# 1. OUTSIDE SVG (85x85mm Fold -> 170x85mm Trim Line -> 174x89mm Bleed Line)
# ==========================================
svg_outside = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="174mm" height="89mm" viewBox="0 0 174 89">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&amp;family=Noto+Serif+KR:wght@300;400;600;700&amp;family=Montserrat:wght@300;400;500;600&amp;display=swap');
      .font-serif {{ font-family: 'Noto Serif KR', 'KoPub Batang', serif; font-weight: 300; }}
      .font-serif-bold {{ font-family: 'Noto Serif KR', 'KoPub Batang', serif; font-weight: 600; }}
      .font-cinzel {{ font-family: 'Cinzel', serif; }}
      .font-montserrat {{ font-family: 'Montserrat', sans-serif; }}
      .guide-line {{ fill: none; stroke-width: 0.2; }}
    </style>
  </defs>

  <!-- Layer 1: Background -->
  <g id="Background">
    <rect x="0" y="0" width="174" height="89" fill="#FAF8F5" />
  </g>

  <!-- Layer 2: Content Outside -->
  <g id="Content">
    <!-- ==================== LEFT PANEL: Back Cover - Calendar & NFC (x: 2 to 87, center: 44.5) ==================== -->
    <g transform="translate(0, 0)">
      <!-- Month Title -->
      <text class="font-serif-bold" font-size="3.2" fill="#333333" text-anchor="middle" x="44.5" y="15" letter-spacing="0.8">2026년   10월</text>
      
      <!-- Weekdays Headers -->
      <text class="font-serif-bold" font-size="1.6" fill="#C85A5A" text-anchor="middle" x="23.5" y="24">일</text>
      <text class="font-serif" font-size="1.6" fill="#666666" text-anchor="middle" x="30.5" y="24">월</text>
      <text class="font-serif" font-size="1.6" fill="#666666" text-anchor="middle" x="37.5" y="24">화</text>
      <text class="font-serif" font-size="1.6" fill="#666666" text-anchor="middle" x="44.5" y="24">수</text>
      <text class="font-serif" font-size="1.6" fill="#666666" text-anchor="middle" x="51.5" y="24">목</text>
      <text class="font-serif" font-size="1.6" fill="#666666" text-anchor="middle" x="58.5" y="24">금</text>
      <text class="font-serif-bold" font-size="1.6" fill="#4A65B8" text-anchor="middle" x="65.5" y="24">토</text>

      <!-- Calendar Dates Grid -->
      <!-- Row 1: y=31 -->
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="51.5" y="31">1</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="58.5" y="31">2</text>
      <text class="font-serif-bold" font-size="1.6" fill="#4A65B8" text-anchor="middle" x="65.5" y="31">3</text>

      <!-- Row 2: y=37 -->
      <text class="font-serif-bold" font-size="1.6" fill="#C85A5A" text-anchor="middle" x="23.5" y="37">4</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="30.5" y="37">5</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="37.5" y="37">6</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="44.5" y="37">7</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="51.5" y="37">8</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="58.5" y="37">9</text>
      <text class="font-serif-bold" font-size="1.6" fill="#4A65B8" text-anchor="middle" x="65.5" y="37">10</text>

      <!-- Row 3: y=43 -->
      <text class="font-serif-bold" font-size="1.6" fill="#C85A5A" text-anchor="middle" x="23.5" y="43">11</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="30.5" y="43">12</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="37.5" y="43">13</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="44.5" y="43">14</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="51.5" y="43">15</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="58.5" y="43">16</text>
      <text class="font-serif-bold" font-size="1.6" fill="#4A65B8" text-anchor="middle" x="65.5" y="43">17</text>

      <!-- Row 4: y=49 -->
      <text class="font-serif-bold" font-size="1.6" fill="#C85A5A" text-anchor="middle" x="23.5" y="49">18</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="30.5" y="49">19</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="37.5" y="49">20</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="44.5" y="49">21</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="51.5" y="49">22</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="58.5" y="49">23</text>
      <text class="font-serif-bold" font-size="1.6" fill="#4A65B8" text-anchor="middle" x="65.5" y="49">24</text>

      <!-- Row 5: y=55 -->
      <text class="font-serif-bold" font-size="1.6" fill="#C85A5A" text-anchor="middle" x="23.5" y="55">25</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="30.5" y="55">26</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="37.5" y="55">27</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="44.5" y="55">28</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="51.5" y="55">29</text>
      <text class="font-serif" font-size="1.6" fill="#555555" text-anchor="middle" x="58.5" y="55">30</text>
      
      <!-- Highlighted 31st Circle -->
      <circle cx="65.5" cy="54.4" r="3.2" fill="#C2A784" />
      <text class="font-serif-bold" font-size="1.6" fill="#FFFFFF" text-anchor="middle" x="65.5" y="55">31</text>

      <!-- NFC Badge Container (Center cx=44.5, cy=72) -->
      <g transform="translate(44.5, 71)">
        <circle cx="0" cy="0" r="11" fill="none" stroke="#C2A784" stroke-width="0.5" />
        
        <!-- NFC Wave lines -->
        <path d="M-5,-4 C-3,-6.5 3,-6.5 5,-4" fill="none" stroke="#C2A784" stroke-width="0.4" stroke-linecap="round" />
        <path d="M-3,-2 C-1.5,-3.5 1.5,-3.5 3,-2" fill="none" stroke="#C2A784" stroke-width="0.4" stroke-linecap="round" />
        <path d="M-1,-0.3 C-0.5,-1 0.5,-1 1,-0.3" fill="none" stroke="#C2A784" stroke-width="0.4" stroke-linecap="round" />
        
        <!-- Phone Hand Icon -->
        <rect x="-2.5" y="0.5" width="5" height="7.5" rx="0.8" fill="none" stroke="#C2A784" stroke-width="0.4" />
        <path d="M 2.5,4.5 C 4,4.5 5,5.5 4.5,7 C 4,8.5 2.5,8.5 1,8" fill="none" stroke="#C2A784" stroke-width="0.4" stroke-linecap="round" />
        
        <!-- Text NFC -->
        <text class="font-montserrat" font-size="2.6" font-weight="700" fill="#C2A784" text-anchor="middle" x="0" y="5" letter-spacing="0.5">NFC</text>
      </g>
    </g>

    <!-- ==================== RIGHT PANEL: Front Cover - Illustration & Typography (x: 87 to 172, center: 129.5) ==================== -->
    <g transform="translate(87, 2)">
      <!-- Cover Illustration Image -->
      <image href="{b64_img if b64_img else 'wedding_cover_illust.jpg'}" x="0" y="0" width="85" height="64" preserveAspectRatio="xMidYMid slice" />
      
      <!-- Titles & Names below the illustration -->
      <text class="font-montserrat" font-size="1.6" font-weight="500" fill="#A1835D" text-anchor="middle" x="42.5" y="70" letter-spacing="1">OUR WEDDING DAY</text>
      <text class="font-montserrat" font-size="1.5" font-weight="500" fill="#666666" text-anchor="middle" x="42.5" y="74.5" letter-spacing="0.5">2026. 10. 31 SAT</text>
      <text class="font-montserrat" font-size="2.0" font-weight="600" fill="#3E2723" text-anchor="middle" x="42.5" y="79" letter-spacing="1">SEUNGHYUN &amp; DASOL</text>
    </g>
  </g>

  <!-- Layer 3: Print Guidelines & Folding Lines (Toggleable) -->
  <g id="Guidelines" opacity="0.8">
    <rect class="guide-line" x="0.1" y="0.1" width="173.8" height="88.8" stroke="#FFB3B3" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FFB3B3" x="3" y="87.8">작업사이즈 외곽선 (Bleed Line: 174 x 89 mm)</text>

    <rect class="guide-line" x="2" y="2" width="170" height="85" stroke="#FF4D4D" stroke-dasharray="1 1" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FF4D4D" x="3" y="1.5">재단선 (Trim Line: 170 x 85 mm - 접었을 때 85 x 85 mm)</text>

    <rect class="guide-line" x="5" y="5" width="79" height="79" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />
    <rect class="guide-line" x="90" y="5" width="79" height="79" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />

    <line class="guide-line" x1="87" y1="2" x2="87" y2="87" stroke="#A1835D" stroke-dasharray="2 1" stroke-width="0.3" />
    <text class="font-serif" font-size="1.2" fill="#A1835D" x="88" y="86.5">접는선 (중앙 폴딩)</text>
  </g>
</svg>'''

with open('/Users/Seunghyun/.gemini/antigravity/scratch/kseh1029.github.io/paper-invitation/wedding-invitation-outside-85x85.svg', 'w', encoding='utf-8') as f:
    f.write(svg_outside)

# ==========================================
# 2. INSIDE SVG (85x85mm Fold -> 170x85mm Trim Line -> 174x89mm Bleed Line)
# ==========================================
svg_inside = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="174mm" height="89mm" viewBox="0 0 174 89">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&amp;family=Noto+Serif+KR:wght@300;400;600;700&amp;family=Montserrat:wght@300;400;500;600&amp;display=swap');
      .font-serif { font-family: 'Noto Serif KR', 'KoPub Batang', serif; font-weight: 300; }
      .font-serif-medium { font-family: 'Noto Serif KR', 'KoPub Batang', serif; font-weight: 400; }
      .font-serif-bold { font-family: 'Noto Serif KR', 'KoPub Batang', serif; font-weight: 600; }
      .font-cinzel { font-family: 'Cinzel', serif; }
      .font-montserrat { font-family: 'Montserrat', sans-serif; }
      .guide-line { fill: none; stroke-width: 0.2; }
    </style>

    <!-- Map Warning Icon -->
    <g id="warning-icon">
      <polygon points="0,-3 3,2.5 -3,2.5" fill="#2E7D32" />
      <text font-family="sans-serif" font-size="3" font-weight="bold" fill="#FFFFFF" text-anchor="middle" x="0" y="1.5">!</text>
    </g>

    <!-- Bus Shuttle Icon -->
    <g id="bus-icon">
      <rect x="-2.5" y="-3" width="5" height="5.5" rx="0.8" fill="#2E7D32" />
      <rect x="-2" y="-2.3" width="4" height="2" fill="#FFFFFF" />
      <circle cx="-1.2" cy="1.2" r="0.6" fill="#FFFFFF" />
      <circle cx="1.2" cy="1.2" r="0.6" fill="#FFFFFF" />
    </g>

    <!-- Gas Station Icon -->
    <g id="gas-icon">
      <rect x="-2" y="-2.5" width="3" height="5" rx="0.5" fill="#2E7D32" />
      <path d="M 1,-1 L 2,-1 L 2,1.5 L 1.5,1.5" fill="none" stroke="#2E7D32" stroke-width="0.5" />
    </g>
  </defs>

  <!-- Layer 1: Background -->
  <g id="Background">
    <rect x="0" y="0" width="174" height="89" fill="#FAF8F5" />
  </g>

  <!-- Layer 2: Inside Content -->
  <g id="Content">
    <!-- ==================== LEFT PANEL: Invitation Greeting & Family (x: 2 to 87, center: 44.5) ==================== -->
    <g transform="translate(0, 0)">
      <!-- INVITATION Header -->
      <text class="font-cinzel" font-size="2.6" font-weight="600" fill="#A1835D" text-anchor="middle" x="44.5" y="14" letter-spacing="1.5">INVITATION</text>
      
      <!-- Upper Diamond Ornament -->
      <path d="M 24,18 L 41,18 M 48,18 L 65,18" stroke="#C2A784" stroke-width="0.3" />
      <polygon points="44.5,16.8 45.7,18 44.5,19.2 43.3,18" fill="#C2A784" />

      <!-- Greeting Body Text -->
      <g font-size="1.5" fill="#333333" text-anchor="middle" class="font-serif">
        <text x="44.5" y="24.5">가을이 깊어지는 계절에</text>
        <text x="44.5" y="29.0">소중한 분들께 좋은 소식을 전합니다.</text>
        <text x="44.5" y="33.5">함께하는 시간이 자연스럽고 편안한 사람과</text>
        <text x="44.5" y="38.0">새로운 시작을 준비하게 되었습니다.</text>

        <text x="44.5" y="46.0">앞으로의 날들도 이 계절처럼</text>
        <text x="44.5" y="50.5">차분하고 따뜻하게</text>
        <text x="44.5" y="55.0">두 사람이 함께 잘 채워가겠습니다.</text>
        <text x="44.5" y="59.5">기쁜 날에 오셔서 축복해 주시면</text>
        <text x="44.5" y="64.0">큰 기쁨이 되겠습니다.</text>
      </g>

      <!-- Lower Diamond Ornament -->
      <path d="M 24,67.5 L 41,67.5 M 48,67.5 L 65,67.5" stroke="#C2A784" stroke-width="0.3" />
      <polygon points="44.5,66.3 45.7,67.5 44.5,68.7 43.3,67.5" fill="#C2A784" />

      <!-- Groom & Bride Family Section -->
      <g transform="translate(0, 69)">
        <!-- Vertical Divider -->
        <line x1="44.5" y1="3" x2="44.5" y2="17" stroke="#D0C0A8" stroke-width="0.3" />

        <!-- Groom Side (Left, cx = 25) -->
        <text class="font-serif-medium" font-size="1.4" fill="#A1835D" text-anchor="middle" x="25" y="5.5" letter-spacing="1">신 랑 측</text>
        <text class="font-serif" font-size="1.15" fill="#555555" text-anchor="middle" x="25" y="10.2">(故) 김창득 · 이재숙<tspan font-size="1.0" fill="#777777">의 차남</tspan></text>
        <text class="font-serif-bold" font-size="2.4" fill="#222222" text-anchor="middle" x="25" y="16" letter-spacing="2">승 현</text>

        <!-- Bride Side (Right, cx = 64) -->
        <text class="font-serif-medium" font-size="1.4" fill="#A1835D" text-anchor="middle" x="64" y="5.5" letter-spacing="1">신 부 측</text>
        <text class="font-serif" font-size="1.15" fill="#555555" text-anchor="middle" x="64" y="10.2">김종문 · 김명임<tspan font-size="1.0" fill="#777777">의 차녀</tspan></text>
        <text class="font-serif-bold" font-size="2.4" fill="#222222" text-anchor="middle" x="64" y="16" letter-spacing="2">다 솔</text>
      </g>
    </g>

    <!-- ==================== RIGHT PANEL: Illustrated Map, Date & Location, QR Code (x: 87 to 172, center: 129.5) ==================== -->
    <g transform="translate(87, 0)">
      <!-- 1. ILLUSTRATED MAP SECTION (Top y: 4 to 48) -->
      <g transform="translate(0, 4)">
        <!-- Roads (Beige / Grey Paths) -->
        <path d="M 8,28 C 15,22 25,12 35,4" fill="none" stroke="#A89F91" stroke-width="3.5" stroke-linecap="round" />
        <path d="M 8,28 C 15,22 25,12 35,4" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" />
        
        <path d="M 12,24 C 20,24 35,26 48,24 C 60,22 70,16 80,12" fill="none" stroke="#D3CBBE" stroke-width="3" stroke-linecap="round" />
        <path d="M 40,25 C 48,30 60,35 78,28" fill="none" stroke="#D3CBBE" stroke-width="2.5" />

        <path d="M 62,5 L 62,38" fill="none" stroke="#D3CBBE" stroke-width="2" />
        <path d="M 48,24 L 48,40" fill="none" stroke="#D3CBBE" stroke-width="2" />

        <text class="font-serif" font-size="1.0" fill="#555555" transform="rotate(-32 18 20)" x="18" y="20">도시고속도로</text>
        <text class="font-serif" font-size="0.9" fill="#2E7D32" transform="rotate(-32 13 25)" x="13" y="25">황령터널 방면</text>

        <use href="#warning-icon" x="25" y="19" />
        <g transform="translate(25, 23)">
          <rect x="-17" y="0" width="34" height="6" rx="1" fill="#FFFFFF" opacity="0.9" stroke="#E0E0E0" stroke-width="0.2" />
          <text class="font-serif-bold" font-size="1.0" fill="#2E7D32" text-anchor="middle" x="0" y="2.5">직진 시</text>
          <text class="font-serif-bold" font-size="1.0" fill="#2E7D32" text-anchor="middle" x="0" y="4.5">도시고속도로로 진입하오니</text>
          <text class="font-serif-bold" font-size="1.0" fill="#C85A5A" text-anchor="middle" x="0" y="6.2">유의하시기 바랍니다.</text>
        </g>

        <!-- GS Caltex Gas Station -->
        <use href="#gas-icon" x="33" y="28" />
        <text class="font-serif" font-size="0.9" fill="#333333" x="31" y="32">GS칼텍스</text>
        <text class="font-serif" font-size="0.9" fill="#333333" x="31" y="34">주유소</text>

        <text class="font-serif" font-size="0.9" fill="#666666" x="48" y="19">남천 동원</text>
        <text class="font-serif" font-size="0.9" fill="#666666" x="48" y="21">로얄듀크</text>

        <text class="font-serif" font-size="0.9" fill="#666666" x="42" y="36">대연힐스테이트</text>
        <text class="font-serif" font-size="0.9" fill="#666666" x="42" y="38">푸르지오</text>

        <text class="font-serif" font-size="0.9" fill="#666666" x="65" y="34">대남</text>
        <text class="font-serif" font-size="0.9" fill="#666666" x="65" y="36">교차로</text>

        <!-- Namcheon Station Exits -->
        <g transform="translate(72, 22)">
          <line x1="-10" y1="8" x2="10" y2="-8" stroke="#2E7D32" stroke-width="0.8" />
          <circle cx="8" cy="-6" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="8" y="-5.7">1</text>
          <circle cx="4" cy="-3" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="4" y="-2.7">2</text>
          <circle cx="-3" cy="2" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="-3" y="2.3">3</text>
          <circle cx="-7" cy="5" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="-7" y="5.3">4</text>
          <text class="font-serif-bold" font-size="1.1" fill="#2E7D32" x="-2" y="-8">남천역</text>
        </g>

        <!-- Shuttle Bus Station -->
        <use href="#bus-icon" x="62" y="23" />
        <text class="font-serif" font-size="0.9" fill="#2E7D32" x="55" y="22">셔틀버스</text>
        <text class="font-serif" font-size="0.9" fill="#2E7D32" x="55" y="24">타는곳</text>

        <!-- Main Venue Banner -->
        <g transform="translate(36, 6)">
          <rect x="-1" y="-4.5" width="40" height="9" rx="1" fill="#FFFFFF" stroke="#2E7D32" stroke-width="0.4" />
          <text class="font-serif-bold" font-size="1.1" fill="#2E7D32" x="2" y="-2.5">1층 클래식홀</text>
          <text class="font-serif-bold" font-size="1.5" fill="#111111" x="2" y="0.5">그랜드 모먼트</text>
          <text class="font-serif" font-size="0.9" fill="#C85A5A" x="2" y="3.2">오후 5시</text>
          <text class="font-serif" font-size="0.85" fill="#555555" x="18" y="-2.5">부산광역시 남구 황령대로 401-9</text>
        </g>
      </g>

      <!-- 2. DATE & VENUE SUMMARY TEXT (Middle y: 50 to 65) -->
      <g text-anchor="middle" transform="translate(42.5, 52)">
        <text class="font-serif-bold" font-size="1.6" fill="#222222" x="0" y="0">2026년 10월 31일 토요일 오후 5시</text>
        <text class="font-serif-bold" font-size="1.6" fill="#222222" x="0" y="4.5">그랜드 모먼트 클래식홀</text>
        <text class="font-serif" font-size="1.3" fill="#555555" x="0" y="8.8">부산광역시 남구 황령대로 401-9</text>
      </g>

      <!-- 3. QR CODE & SMARTPHONE SECTION (Bottom y: 66 to 85) -->
      <g transform="translate(0, 65)">
        <path d="M 4,2 L 2,2 L 2,4 M 81,2 L 83,2 L 83,4" stroke="#CCCCCC" stroke-width="0.3" fill="none" />
        
        <g class="font-serif" font-size="1.3" fill="#333333" text-anchor="start" transform="translate(10, 5)">
          <text x="0" y="0">휴대폰 카메라</text>
          <text x="0" y="4.2">앱을 실행하고</text>
          <text x="0" y="8.4">QR코드를</text>
          <text x="0" y="12.6">눌러주세요</text>
        </g>

        <!-- Right Smartphone & QR Illustration -->
        <g transform="translate(58, 1)">
          <rect x="-10" y="0" width="16" height="21" rx="2.5" fill="#FFFFFF" stroke="#000000" stroke-width="0.8" />
          <rect x="-8.5" y="1.5" width="13" height="18" rx="1" fill="#FAF8F5" stroke="#000000" stroke-width="0.3" />
          <line x1="-3" y1="1" x2="1" y2="1" stroke="#000000" stroke-width="0.4" />

          <path d="M -10,12 C -13,10 -15,11 -15,14 C -15,16 -12,17 -10,18" fill="none" stroke="#000000" stroke-width="0.8" stroke-linecap="round" />
          <path d="M -10,16 C -14,15 -16,18 -14,21 C -12,23 -8,22 -6,21" fill="none" stroke="#000000" stroke-width="0.8" stroke-linecap="round" />
          <path d="M 6,14 C 10,14 14,16 16,19 C 17,21 15,23 12,22 L 6,20" fill="none" stroke="#000000" stroke-width="0.8" stroke-linecap="round" />

          <!-- QR Code Vector -->
          <g transform="translate(-6.5, 3.5)">
            <rect x="0" y="0" width="9" height="9" fill="#FFFFFF" />
            <rect x="0.5" y="0.5" width="2.5" height="2.5" fill="#000000" />
            <rect x="1" y="1" width="1.5" height="1.5" fill="#FFFFFF" />
            <rect x="1.25" y="1.25" width="1" height="1" fill="#000000" />
            
            <rect x="6" y="0.5" width="2.5" height="2.5" fill="#000000" />
            <rect x="6.5" y="1" width="1.5" height="1.5" fill="#FFFFFF" />
            <rect x="6.75" y="1.25" width="1" height="1" fill="#000000" />

            <rect x="0.5" y="6" width="2.5" height="2.5" fill="#000000" />
            <rect x="1" y="6.5" width="1.5" height="1.5" fill="#FFFFFF" />
            <rect x="1.25" y="6.75" width="1" height="1" fill="#000000" />

            <rect x="3.5" y="0.5" width="0.8" height="0.8" fill="#000" />
            <rect x="4.5" y="1.5" width="0.8" height="0.8" fill="#000" />
            <rect x="3.5" y="2.5" width="0.8" height="0.8" fill="#000" />
            <rect x="0.5" y="3.5" width="0.8" height="0.8" fill="#000" />
            <rect x="2.0" y="4.5" width="0.8" height="0.8" fill="#000" />
            <rect x="3.5" y="3.5" width="0.8" height="0.8" fill="#000" />
            <rect x="4.8" y="3.5" width="0.8" height="0.8" fill="#000" />
            <rect x="6.0" y="3.5" width="0.8" height="0.8" fill="#000" />
            <rect x="7.2" y="4.5" width="0.8" height="0.8" fill="#000" />
            <rect x="4.5" y="5.5" width="0.8" height="0.8" fill="#000" />
            <rect x="3.5" y="6.5" width="0.8" height="0.8" fill="#000" />
            <rect x="4.8" y="7.5" width="0.8" height="0.8" fill="#000" />
            <rect x="6.0" y="6.5" width="0.8" height="0.8" fill="#000" />
            <rect x="7.2" y="7.5" width="0.8" height="0.8" fill="#000" />
          </g>
        </g>
      </g>
    </g>
  </g>

  <!-- Layer 3: Guidelines -->
  <g id="Guidelines" opacity="0.8">
    <rect class="guide-line" x="0.1" y="0.1" width="173.8" height="88.8" stroke="#FFB3B3" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FFB3B3" x="3" y="87.8">작업사이즈 외곽선 (Bleed Line: 174 x 89 mm)</text>

    <rect class="guide-line" x="2" y="2" width="170" height="85" stroke="#FF4D4D" stroke-dasharray="1 1" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FF4D4D" x="3" y="1.5">재단선 (Trim Line: 170 x 85 mm - 접었을 때 85 x 85 mm)</text>

    <rect class="guide-line" x="5" y="5" width="79" height="79" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />
    <rect class="guide-line" x="90" y="5" width="79" height="79" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />

    <line class="guide-line" x1="87" y1="2" x2="87" y2="87" stroke="#A1835D" stroke-dasharray="2 1" stroke-width="0.3" />
    <text class="font-serif" font-size="1.2" fill="#A1835D" x="88" y="86.5">접는선 (중앙 폴딩)</text>
  </g>
</svg>'''

with open('/Users/Seunghyun/.gemini/antigravity/scratch/kseh1029.github.io/paper-invitation/wedding-invitation-inside-85x85.svg', 'w', encoding='utf-8') as f:
    f.write(svg_inside)

print("SVG files generated successfully!")
