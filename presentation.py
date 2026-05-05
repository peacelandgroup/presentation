import pygame
import sys

# 初始化 pygame
pygame.init()

# 設定視窗與顏色
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("安心置地 - 安心學 建案專屬簡報")

# 顏色定義
BLACK = (20, 20, 25)
WHITE = (245, 245, 245)
GOLD = (212, 175, 55)
GRAY = (150, 150, 150)

# 設定中文字體 (依作業系統自動尋找支援的字體，若顯示方塊請將中文字體檔案 .ttf 放在同目錄並更改路徑)
font_preferences = ['microsoftjhenghei', 'pingfangtc', 'simhei', 'heiti tc']
title_font = pygame.font.SysFont(font_preferences, 56, bold=True)
content_font = pygame.font.SysFont(font_preferences, 32)
small_font = pygame.font.SysFont(font_preferences, 24)

# 簡報資料
slides_data = [
    {
        "title": "安心置地開發集團",
        "content": [
            "秉持『安全、安居、安心』三安理念",
            "為您精心規劃並打造安全舒適的傳家建築。",
            "",
            "► 董事長：林水成",
            "► 資本總額：10,000,000元",
            "► 總部位置：新竹市東區北大路",
            "► 專業領域：不動產開發、投資興建、工程營造"
        ]
    },
    {
        "title": "集團實力與團隊",
        "content": [
            "發跡於科技重鎮新竹市，以全方位工程營建起家，",
            "練就一絲不苟的細膩施工態度。",
            "",
            "旗下專業建築團隊：",
            "• 安心置地開發",
            "• 安心國際投資",
            "• 晉通營造",
            "",
            "長期深耕大台北、桃園與新竹等精華區域。"
        ]
    },
    {
        "title": "2023 精品建案：【安心學】",
        "content": [
            "創造安心成家的願景！楊梅區指標性精品預售案。",
            "",
            "► 建案地點：桃園市楊梅區校前路318巷",
            "► 預期完工：2027年 6月",
            "► 開價區間：約 34～39 萬/坪",
            "► 總價規劃：約 699～1,130 萬元/戶",
            "► 極佳交通：距離五楊高架校前路交流道僅約 150 公尺！"
        ]
    },
    {
        "title": "建築與格局規劃",
        "content": [
            "住戶單純的精緻社區，給您最寧靜的居住品質。",
            "",
            "► 樓層規劃：5 棟 (地上 8/9/13 層，地下 1 層)",
            "► 戶數規劃：64 戶住家，1 戶警衛室 (一層 2~3 戶)",
            "► 坪數與格局：",
            "   - 2 房：約 19.03 坪",
            "   - 2+1 房：約 23.83 坪",
            "   - 3 房：約 24.72～29.78 坪",
            "► 採光通風：全區無暗廳、無暗房，衛浴皆開窗！"
        ]
    },
    {
        "title": "高規精品建材 & 優勢方案",
        "content": [
            "導入日系精工與頂級設備，打造健康智慧宅。",
            "",
            "► 隔音：YKK AP 水氣密隔音窗 + 6+6mm 膠合玻璃",
            "► 廚衛：Panasonic 系統廚具、TOTO 精品衛浴 (G5全自動馬桶)",
            "► 設備：美國 Pentair 淨水、當層排氣系統",
            "► 安全：防火鑄鋁玄關門 + 智慧四合一抗菌電子鎖",
            "",
            "★ 輕鬆成家：推出「結構工程零付款」方案！"
        ]
    }
]

def render_text(surface, text, font, color, x, y):
    """渲染單行文字"""
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def create_slide_surface(slide):
    """將單頁簡報繪製到一個獨立的 Surface 上（用於處理透明度特效）"""
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill(BLACK)
    
    # 畫標題
    render_text(surface, slide["title"], title_font, GOLD, 100, 120)
    
    # 畫裝飾線
    pygame.draw.line(surface, GOLD, (100, 190), (924, 190), 3)
    
    # 畫內容
    y_offset = 240
    for line in slide["content"]:
        if line.startswith("►") or line.startswith("★") or line.startswith("•"):
            render_text(surface, line, content_font, WHITE, 130, y_offset)
        else:
            render_text(surface, line, content_font, GRAY, 100, y_offset)
        y_offset += 50
        
    # 畫頁腳提示
    render_text(surface, "按下 [空白鍵] 或 [滑鼠左鍵] 進入下一頁 | 按 [ESC] 離開", small_font, GRAY, 250, HEIGHT - 50)
    
    return surface

def main():
    clock = pygame.time.Clock()
    current_slide = 0
    alpha = 0
    fading_in = True
    
    # 準備第一張投影片
    slide_surface = create_slide_surface(slides_data[current_slide])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in [pygame.K_SPACE, pygame.K_RIGHT, pygame.K_RETURN]:
                    if current_slide < len(slides_data) - 1:
                        current_slide += 1
                        slide_surface = create_slide_surface(slides_data[current_slide])
                        alpha = 0
                        fading_in = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # 左鍵
                    if current_slide < len(slides_data) - 1:
                        current_slide += 1
                        slide_surface = create_slide_surface(slides_data[current_slide])
                        alpha = 0
                        fading_in = True

        # 處理淡入特效
        if fading_in:
            alpha += 5  # 調整此數值可改變淡入速度
            if alpha >= 255:
                alpha = 255
                fading_in = False

        # 繪製畫面
        screen.fill(BLACK)
        slide_surface.set_alpha(alpha)
        screen.blit(slide_surface, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()