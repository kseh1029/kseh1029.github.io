import base64
import os

img_path = '/Users/Seunghyun/.gemini/antigravity/scratch/kseh1029.github.io/paper-invitation/wedding_cover_illust.jpg'
b64_img = ""
if os.path.exists(img_path):
    with open(img_path, 'rb') as f:
        b64_img = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')

# ==========================================
# 1. OUTSIDE SVG (90x90mm Fold -> 180x90mm Trim Line -> 182x92mm Bleed Line [1mm Bleed])
# ==========================================
svg_outside_182 = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="182mm" height="92mm" viewBox="0 0 182 92">
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
    <!-- Full Bleed Background (182 x 92 mm) -->
    <rect x="0" y="0" width="182" height="92" fill="#FAF8F5" />
  </g>

  <!-- Layer 2: Content Outside -->
  <g id="Content">
    <!-- ==================== LEFT PANEL: Back Cover - Calendar & NFC (x: 0 to 91, center: 46) ==================== -->
    <g transform="translate(0, 0)">
      <!-- Month Title -->
      <text class="font-serif-bold" font-size="3.5" fill="#333333" text-anchor="middle" x="46" y="15" letter-spacing="0.8">2026년   10월</text>
      
      <!-- Weekdays Headers -->
      <!-- Cols x: 23.5, 31, 38.5, 46, 53.5, 61, 68.5 -->
      <text class="font-serif-bold" font-size="1.7" fill="#C85A5A" text-anchor="middle" x="23.5" y="25">일</text>
      <text class="font-serif" font-size="1.7" fill="#666666" text-anchor="middle" x="31" y="25">월</text>
      <text class="font-serif" font-size="1.7" fill="#666666" text-anchor="middle" x="38.5" y="25">화</text>
      <text class="font-serif" font-size="1.7" fill="#666666" text-anchor="middle" x="46" y="25">수</text>
      <text class="font-serif" font-size="1.7" fill="#666666" text-anchor="middle" x="53.5" y="25">목</text>
      <text class="font-serif" font-size="1.7" fill="#666666" text-anchor="middle" x="61" y="25">금</text>
      <text class="font-serif-bold" font-size="1.7" fill="#4A65B8" text-anchor="middle" x="68.5" y="25">토</text>

      <!-- Calendar Dates Grid -->
      <!-- Row 1: y=32.5 -->
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="53.5" y="32.5">1</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="61" y="32.5">2</text>
      <text class="font-serif-bold" font-size="1.7" fill="#4A65B8" text-anchor="middle" x="68.5" y="32.5">3</text>

      <!-- Row 2: y=39 -->
      <text class="font-serif-bold" font-size="1.7" fill="#C85A5A" text-anchor="middle" x="23.5" y="39">4</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="31" y="39">5</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="38.5" y="39">6</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="46" y="39">7</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="53.5" y="39">8</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="61" y="39">9</text>
      <text class="font-serif-bold" font-size="1.7" fill="#4A65B8" text-anchor="middle" x="68.5" y="39">10</text>

      <!-- Row 3: y=45.5 -->
      <text class="font-serif-bold" font-size="1.7" fill="#C85A5A" text-anchor="middle" x="23.5" y="45.5">11</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="31" y="45.5">12</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="38.5" y="45.5">13</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="46" y="45.5">14</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="53.5" y="45.5">15</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="61" y="45.5">16</text>
      <text class="font-serif-bold" font-size="1.7" fill="#4A65B8" text-anchor="middle" x="68.5" y="45.5">17</text>

      <!-- Row 4: y=52 -->
      <text class="font-serif-bold" font-size="1.7" fill="#C85A5A" text-anchor="middle" x="23.5" y="52">18</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="31" y="52">19</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="38.5" y="52">20</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="46" y="52">21</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="53.5" y="52">22</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="61" y="52">23</text>
      <text class="font-serif-bold" font-size="1.7" fill="#4A65B8" text-anchor="middle" x="68.5" y="52">24</text>

      <!-- Row 5: y=58.5 -->
      <text class="font-serif-bold" font-size="1.7" fill="#C85A5A" text-anchor="middle" x="23.5" y="58.5">25</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="31" y="58.5">26</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="38.5" y="58.5">27</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="46" y="58.5">28</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="53.5" y="58.5">29</text>
      <text class="font-serif" font-size="1.7" fill="#555555" text-anchor="middle" x="61" y="58.5">30</text>
      
      <!-- Highlighted 31st Circle -->
      <circle cx="68.5" cy="57.8" r="3.4" fill="#C2A784" />
      <text class="font-serif-bold" font-size="1.7" fill="#FFFFFF" text-anchor="middle" x="68.5" y="58.5">31</text>

      <!-- NFC Badge Container (Center cx=46, cy=75) -->
      <g transform="translate(46, 75)">
        <circle cx="0" cy="0" r="11.5" fill="none" stroke="#C2A784" stroke-width="0.5" />
        
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

    <!-- ==================== RIGHT PANEL: Front Cover - Illustration & Typography (x: 91 to 182, center: 136) ==================== -->
    <g transform="translate(0, 0)">
      <!-- Cover Illustration Image (Full Bleed to top and right edges: x=91 to 182, y=0 to 68) -->
      <image href="{b64_img if b64_img else 'wedding_cover_illust.jpg'}" x="91" y="0" width="91" height="68" preserveAspectRatio="xMidYMid slice" />
      
      <!-- Titles & Names below the illustration (Center x = 136) -->
      <text class="font-montserrat" font-size="1.8" font-weight="500" fill="#A1835D" text-anchor="middle" x="136" y="74.5" letter-spacing="1">OUR WEDDING DAY</text>
      <text class="font-montserrat" font-size="1.6" font-weight="500" fill="#666666" text-anchor="middle" x="136" y="79.5" letter-spacing="0.5">2026. 10. 31 SAT</text>
      <text class="font-montserrat" font-size="2.2" font-weight="600" fill="#3E2723" text-anchor="middle" x="136" y="85" letter-spacing="1">SEUNGHYUN &amp; DASOL</text>
    </g>
  </g>

  <!-- Layer 3: Print Guidelines & Folding Lines (Toggleable) -->
  <g id="Guidelines" opacity="0.8">
    <!-- Bleed Outer Boundary (182 x 92 mm) -->
    <rect class="guide-line" x="0.1" y="0.1" width="181.8" height="91.8" stroke="#FFB3B3" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FFB3B3" x="2" y="90.8">작업사이즈 외곽선 (Bleed Line: 182 x 92 mm - 도련 1mm)</text>

    <!-- Trim Line (180 x 90 mm) -->
    <rect class="guide-line" x="1" y="1" width="180" height="90" stroke="#FF4D4D" stroke-dasharray="1 1" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FF4D4D" x="2" y="1.5">재단선 (Trim Line: 180 x 90 mm - 접었을 때 90 x 90 mm)</text>

    <!-- Safe Margin Lines (3mm padding inside trim line: x=4 to 87, y=4 to 87) -->
    <rect class="guide-line" x="4" y="4" width="84" height="84" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />
    <rect class="guide-line" x="94" y="4" width="84" height="84" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />

    <!-- Center Fold Line (x = 91) -->
    <line class="guide-line" x1="91" y1="1" x2="91" y2="91" stroke="#A1835D" stroke-dasharray="2 1" stroke-width="0.3" />
    <text class="font-serif" font-size="1.2" fill="#A1835D" x="92" y="89.5">접는선 (중앙 폴딩)</text>
  </g>
</svg>'''

base_dir = '/Users/Seunghyun/.gemini/antigravity/scratch/kseh1029.github.io/paper-invitation'
with open(os.path.join(base_dir, 'wedding-invitation-outside-182x92.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_outside_182)

# ==========================================
# 2. INSIDE SVG (90x90mm Fold -> 180x90mm Trim Line -> 182x92mm Bleed Line [1mm Bleed])
# ==========================================
svg_inside_182 = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="182mm" height="92mm" viewBox="0 0 182 92">
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
    <rect x="0" y="0" width="182" height="92" fill="#FAF8F5" />
  </g>

  <!-- Layer 2: Inside Content -->
  <g id="Content">
    <!-- ==================== LEFT PANEL: Invitation Greeting & Family (x: 0 to 91, center: 46) ==================== -->
    <g transform="translate(0, 0)">
      <!-- INVITATION Header -->
      <text class="font-cinzel" font-size="2.8" font-weight="600" fill="#A1835D" text-anchor="middle" x="46" y="14" letter-spacing="1.5">INVITATION</text>
      
      <!-- Upper Diamond Ornament -->
      <path d="M 25,18.5 L 42.5,18.5 M 49.5,18.5 L 67,18.5" stroke="#C2A784" stroke-width="0.3" />
      <polygon points="46,17.3 47.2,18.5 46,19.7 44.8,18.5" fill="#C2A784" />

      <!-- Greeting Body Text -->
      <g font-size="1.55" fill="#333333" text-anchor="middle" class="font-serif">
        <text x="46" y="25.5">가을이 깊어지는 계절에</text>
        <text x="46" y="30.2">소중한 분들께 좋은 소식을 전합니다.</text>
        <text x="46" y="34.9">함께하는 시간이 자연스럽고 편안한 사람과</text>
        <text x="46" y="39.6">새로운 시작을 준비하게 되었습니다.</text>

        <text x="46" y="48.0">앞으로의 날들도 이 계절처럼</text>
        <text x="46" y="52.7">차분하고 따뜻하게</text>
        <text x="46" y="57.4">두 사람이 함께 잘 채워가겠습니다.</text>
        <text x="46" y="62.1">기쁜 날에 오셔서 축복해 주시면</text>
        <text x="46" y="66.8">큰 기쁨이 되겠습니다.</text>
      </g>

      <!-- Lower Diamond Ornament -->
      <path d="M 25,70.5 L 42.5,70.5 M 49.5,70.5 L 67,70.5" stroke="#C2A784" stroke-width="0.3" />
      <polygon points="46,69.3 47.2,70.5 46,71.7 44.8,70.5" fill="#C2A784" />

      <!-- Groom & Bride Family Section -->
      <g transform="translate(0, 71.5)">
        <!-- Vertical Divider -->
        <line x1="46" y1="3" x2="46" y2="17" stroke="#D0C0A8" stroke-width="0.3" />

        <!-- Groom Side (Left, cx = 25.5) -->
        <text class="font-serif-medium" font-size="1.4" fill="#A1835D" text-anchor="middle" x="25.5" y="5.5" letter-spacing="1">신 랑 측</text>
        <text class="font-serif" font-size="1.2" fill="#555555" text-anchor="middle" x="25.5" y="10.2">(故) 김창득 · 이재숙<tspan font-size="1.0" fill="#777777">의 차남</tspan></text>
        <text class="font-serif-bold" font-size="2.5" fill="#222222" text-anchor="middle" x="25.5" y="16" letter-spacing="2">승 현</text>

        <!-- Bride Side (Right, cx = 66.5) -->
        <text class="font-serif-medium" font-size="1.4" fill="#A1835D" text-anchor="middle" x="66.5" y="5.5" letter-spacing="1">신 부 측</text>
        <text class="font-serif" font-size="1.2" fill="#555555" text-anchor="middle" x="66.5" y="10.2">김종문 · 김명임<tspan font-size="1.0" fill="#777777">의 차녀</tspan></text>
        <text class="font-serif-bold" font-size="2.5" fill="#222222" text-anchor="middle" x="66.5" y="16" letter-spacing="2">다 솔</text>
      </g>
    </g>

    <!-- ==================== RIGHT PANEL: Illustrated Map, Date & Location, QR Code (x: 91 to 182, center: 136) ==================== -->
    <g transform="translate(91, 0)">
      <!-- 1. ILLUSTRATED MAP SECTION (Top y: 3 to 51) -->
      <g transform="translate(0, 3)">
        <!-- Roads (Beige / Grey Paths) -->
        <path d="M 8,30 C 16,24 28,13 38,4" fill="none" stroke="#A89F91" stroke-width="3.8" stroke-linecap="round" />
        <path d="M 8,30 C 16,24 28,13 38,4" fill="none" stroke="#FFFFFF" stroke-width="2.0" stroke-linecap="round" />
        
        <path d="M 12,26 C 22,26 38,28 52,26 C 65,24 75,18 85,14" fill="none" stroke="#D3CBBE" stroke-width="3.2" stroke-linecap="round" />
        <path d="M 44,27 C 52,32 65,38 82,30" fill="none" stroke="#D3CBBE" stroke-width="2.8" />

        <path d="M 68,5 L 68,40" fill="none" stroke="#D3CBBE" stroke-width="2.2" />
        <path d="M 52,26 L 52,42" fill="none" stroke="#D3CBBE" stroke-width="2.2" />

        <text class="font-serif" font-size="1.05" fill="#555555" transform="rotate(-32 19 22)" x="19" y="22">도시고속도로</text>
        <text class="font-serif" font-size="0.95" fill="#2E7D32" transform="rotate(-32 14 27)" x="14" y="27">황령터널 방면</text>

        <use href="#warning-icon" x="27" y="20" />
        <g transform="translate(27, 24)">
          <rect x="-18" y="0" width="36" height="6.5" rx="1" fill="#FFFFFF" opacity="0.92" stroke="#E0E0E0" stroke-width="0.2" />
          <text class="font-serif-bold" font-size="1.0" fill="#2E7D32" text-anchor="middle" x="0" y="2.6">직진 시</text>
          <text class="font-serif-bold" font-size="1.0" fill="#2E7D32" text-anchor="middle" x="0" y="4.6">도시고속도로로 진입하오니</text>
          <text class="font-serif-bold" font-size="1.0" fill="#C85A5A" text-anchor="middle" x="0" y="6.3">유의하시기 바랍니다.</text>
        </g>

        <!-- GS Caltex Gas Station -->
        <use href="#gas-icon" x="35" y="30" />
        <text class="font-serif" font-size="0.95" fill="#333333" x="33" y="34.5">GS칼텍스</text>
        <text class="font-serif" font-size="0.95" fill="#333333" x="33" y="36.5">주유소</text>

        <text class="font-serif" font-size="0.95" fill="#666666" x="52" y="20">남천 동원</text>
        <text class="font-serif" font-size="0.95" fill="#666666" x="52" y="22">로얄듀크</text>

        <text class="font-serif" font-size="0.95" fill="#666666" x="45" y="38">대연힐스테이트</text>
        <text class="font-serif" font-size="0.95" fill="#666666" x="45" y="40">푸르지오</text>

        <text class="font-serif" font-size="0.95" fill="#666666" x="71" y="36">대남</text>
        <text class="font-serif" font-size="0.95" fill="#666666" x="71" y="38">교차로</text>

        <!-- Namcheon Station Exits -->
        <g transform="translate(78, 24)">
          <line x1="-10" y1="8" x2="10" y2="-8" stroke="#2E7D32" stroke-width="0.9" />
          <circle cx="8" cy="-6" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="8" y="-5.7">1</text>
          <circle cx="4" cy="-3" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="4" y="-2.7">2</text>
          <circle cx="-3" cy="2" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="-3" y="2.3">3</text>
          <circle cx="-7" cy="5" r="1.1" fill="#2E7D32" /><text class="font-serif" font-size="0.8" fill="#FFF" text-anchor="middle" x="-7" y="5.3">4</text>
          <text class="font-serif-bold" font-size="1.1" fill="#2E7D32" x="-2" y="-8">남천역</text>
        </g>

        <!-- Shuttle Bus Station -->
        <use href="#bus-icon" x="68" y="25" />
        <text class="font-serif" font-size="0.95" fill="#2E7D32" x="60" y="24">셔틀버스</text>
        <text class="font-serif" font-size="0.95" fill="#2E7D32" x="60" y="26">타는곳</text>

        <!-- Main Venue Banner -->
        <g transform="translate(40, 6)">
          <rect x="-1" y="-4.5" width="42" height="9.5" rx="1" fill="#FFFFFF" stroke="#2E7D32" stroke-width="0.4" />
          <text class="font-serif-bold" font-size="1.15" fill="#2E7D32" x="2" y="-2.5">1층 클래식홀</text>
          <text class="font-serif-bold" font-size="1.55" fill="#111111" x="2" y="0.6">그랜드 모먼트</text>
          <text class="font-serif" font-size="0.95" fill="#C85A5A" x="2" y="3.4">오후 5시</text>
          <text class="font-serif" font-size="0.88" fill="#555555" x="19" y="-2.5">부산광역시 남구 황령대로 401-9</text>
        </g>
      </g>

      <!-- 2. DATE & VENUE SUMMARY TEXT (Middle y: 53 to 68) -->
      <g text-anchor="middle" transform="translate(45, 54)">
        <text class="font-serif-bold" font-size="1.65" fill="#222222" x="0" y="0">2026년 10월 31일 토요일 오후 5시</text>
        <text class="font-serif-bold" font-size="1.65" fill="#222222" x="0" y="4.8">그랜드 모먼트 클래식홀</text>
        <text class="font-serif" font-size="1.35" fill="#555555" x="0" y="9.2">부산광역시 남구 황령대로 401-9</text>
      </g>

      <!-- 3. QR CODE & SMARTPHONE SECTION (Bottom y: 68 to 87) -->
      <g transform="translate(0, 68)">
        <path d="M 4,2 L 2,2 L 2,4 M 86,2 L 88,2 L 88,4" stroke="#CCCCCC" stroke-width="0.3" fill="none" />
        
        <g class="font-serif" font-size="1.35" fill="#333333" text-anchor="start" transform="translate(11, 5)">
          <text x="0" y="0">휴대폰 카메라</text>
          <text x="0" y="4.4">앱을 실행하고</text>
          <text x="0" y="8.8">QR코드를</text>
          <text x="0" y="13.2">눌러주세요</text>
        </g>

        <!-- Right Smartphone & QR Illustration -->
        <g transform="translate(62, 1)">
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
    <rect class="guide-line" x="0.1" y="0.1" width="181.8" height="91.8" stroke="#FFB3B3" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FFB3B3" x="2" y="90.8">작업사이즈 외곽선 (Bleed Line: 182 x 92 mm - 도련 1mm)</text>

    <rect class="guide-line" x="1" y="1" width="180" height="90" stroke="#FF4D4D" stroke-dasharray="1 1" stroke-width="0.2" />
    <text class="font-serif" font-size="1.2" fill="#FF4D4D" x="2" y="1.5">재단선 (Trim Line: 180 x 90 mm - 접었을 때 90 x 90 mm)</text>

    <rect class="guide-line" x="4" y="4" width="84" height="84" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />
    <rect class="guide-line" x="94" y="4" width="84" height="84" stroke="#3B82F6" stroke-dasharray="0.5 1" opacity="0.4" stroke-width="0.15" />

    <line class="guide-line" x1="91" y1="1" x2="91" y2="91" stroke="#A1835D" stroke-dasharray="2 1" stroke-width="0.3" />
    <text class="font-serif" font-size="1.2" fill="#A1835D" x="92" y="89.5">접는선 (중앙 폴딩)</text>
  </g>
</svg>'''

with open(os.path.join(base_dir, 'wedding-invitation-inside-182x92.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_inside_182)

print("Generated 182x92mm (1mm Bleed) SVG files successfully!")
