
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 日本語フォントの設定例（システムにインストールされている日本語フォントを指定）
plt.rcParams['font.family'] = 'Yu Gothic'  # または 'Yu Gothic', 'TakaoPGothic' など

def generate_xy_plot(filename="3.jpg"):
    fig, ax = plt.subplots()

    # x軸の矢印：(-1,0)から(2,0)へ（正の側が長め）
    ax.arrow(-1, 0, 3, 0, head_width=0.1, head_length=0.2, fc='black', ec='black')
    # y軸の矢印：(0,-1)から(0,2)へ（正の側が長め）
    ax.arrow(0, -1, 0, 3, head_width=0.1, head_length=0.2, fc='black', ec='black')

    # 軸のラベル
    ax.text(2.2, -0.1, 'x', fontsize=12, fontfamily='serif')
    ax.text(-0.2, 2.2, 'y', fontsize=12, fontfamily='serif')
    ax.text(0.05, -0.15, 'O', fontsize=12, fontfamily='serif')

    # 原点に小さい黒い丸を描画
    ax.plot(0, 0, marker='o', markersize=6, color='black')

    # レールの追加：y軸正の部分に、x軸に平行な2本線（間隔を広くし、x軸の端まで描画）
    rail_y11 = 0.3
    rail_y12 = rail_y11 + 0.025
    rail_y21 = rail_y11 + 0.5
    rail_y22 = rail_y21 + 0.025
    ax.hlines(rail_y11, xmin=-1, xmax=2, colors='black', linewidth=1)
    ax.hlines(rail_y12, xmin=-1, xmax=2, colors='black', linewidth=1)
    ax.hlines(rail_y21, xmin=-1, xmax=2, colors='black', linewidth=1)
    ax.hlines(rail_y22, xmin=-1, xmax=2, colors='black', linewidth=1)

    # レールのラベル（日本語を使用）
    ax.text(2.05, rail_y21, 'レールA', fontsize=12)
    ax.text(2.05, rail_y11, 'レールB', fontsize=12)

    # 棒の追加：レールA（上）とレールB（下）を端とする縦に細長い長方形
    # ここでは棒は両レールの間を跨ぐように描画します。
    rod_bottom = rail_y11-0.05   # レールBの下側（例としてrail_y11を採用）
    rod_top = rail_y22+0.05      # レールAの下側（例としてrail_y21を採用）
    rod_height = rod_top - rod_bottom  # 高さ1.0
    rod_width = 0.05  # 棒の幅

    # 棒1：左側に配置
    rod1_x = -0.4
    rod1 = patches.Rectangle((rod1_x, rod_bottom), rod_width, rod_height, 
                              linewidth=1, edgecolor='black', facecolor='gray', fill=True)
    ax.add_patch(rod1)
    ax.text(rod1_x + rod_width/2, rod_top + 0.1, '棒1', fontsize=12, ha='center')

    # 棒2：右側に配置
    rod2_x = 1.2
    rod2 = patches.Rectangle((rod2_x, rod_bottom), rod_width, rod_height, 
                              linewidth=1, edgecolor='black', facecolor='gray', fill=True)
    ax.add_patch(rod2)
    ax.text(rod2_x + rod_width/2, rod_top + 0.1, '棒2', fontsize=12, ha='center')

    # 棒2の左上に磁束密度を表す記号を追加
    # 電荷は小さい黒塗り円と、その周囲を囲む白抜き円で表現します
    charge_center = (rod2_x - 0.5, rod_top + 0.5)  # 座標は適宜調整してください
    # 外側の白抜きの円（黒枠付き）
    charge_outer = plt.Circle(charge_center, 0.07, edgecolor='black', facecolor='white', linewidth=1)
    ax.add_patch(charge_outer)
    # 小さい黒塗りの円
    charge_inner = plt.Circle(charge_center, 0.03, color='black')
    ax.add_patch(charge_inner)
    # 棒2の左上に磁束密度を表す記号を追加した部分で、
    # その上にベクトルB→のラベルを配置して、ベクトルであることを示す
    # （例：B→ は LaTeX 記法 r'$B\rightarrow$' を使用）
    ax.text(charge_center[0] + 0.1, charge_center[1] + 0.06, r'$\vec{B}$', 
            fontsize=12, fontfamily='serif', ha='left', va='center')

    # レールのラベルの下（右端）に、レールA（上）とレールB（下）の間の長さを示す上下矢印と
    # その中央に「l」の文字を追加
    arrow_x = 1.9
    ax.annotate(
        "", 
        xy=(arrow_x, rail_y21+0.05), 
        xytext=(arrow_x, rail_y11-0.02),
        arrowprops=dict(arrowstyle="<->", color="black", linewidth=1.5)
    )
    mid_y = (rail_y21 + rail_y11) / 2
    ax.text(arrow_x+0.1, mid_y, 'l', fontsize=12, ha='left', va='center', fontfamily = 'serif')

    # 描画範囲・比率の設定（右上の象限を大きく取る）
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-1.5, 2.5)
    ax.axis('off')  # 目盛りと枠線を非表示に

    # 余白を削いで高解像度で保存
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == "__main__":
    generate_xy_plot()