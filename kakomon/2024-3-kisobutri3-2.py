import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_rectangle_plot(filename="2.jpg"):
    fig, ax = plt.subplots()

    # 横に長い長方形を追加：左下の座標(0,0), 幅2, 高さ1
    rect = patches.Rectangle((0, 0), 2, 1, angle=0,
                             linewidth=1, edgecolor='black', facecolor='#d3d3d3')
    ax.add_patch(rect)

    # ベクトル v₀:
    # ターゲットは長方形の左下から右方向に長辺の1/3の位置 ⇒ (2/3, 0)
    # 下からその点を指すので、始点は (2/3, -0.8) とし、矢印は上向きに描画
    # length_includes_head=True により、矢印の先端が (2/3, 0) に接する
    v0_start = (2/3, -0.8)
    v0_dx = 0
    v0_dy = 0.8  # v0_start.y + 0.8 = 0
    ax.arrow(v0_start[0], v0_start[1], v0_dx, v0_dy,
             head_width=0.05, head_length=0.1, fc='black', ec='black', length_includes_head=True)
    # ベクトル v₀ のラベル（セリフ体）
    ax.text(v0_start[0] - 0.1, v0_start[1] + v0_dy/2, r'$v_0$', fontsize=8, fontfamily='serif')

    # 半円（点線）を追加：  
    # 矢印の先端の点 A は (2/3, 0)
    # 同じ辺上に、A から右方向に長辺の半分 (=1) の点 B を取る ⇒ B = ((2/3)+1, 0) = (1.6667, 0)
    # A と B の中点が円の中心になるので、中心は ((2/3 + 1.6667)/2, 0) ≒ (1.1667, 0)
    # 円の半径は AB の半分 = 0.5
    center = ((2/3 + (2/3 + 1)) / 2, 0)
    radius = 0.5
    circle = patches.Circle(center, radius, edgecolor='black',
                            facecolor='none', linestyle='dotted', linewidth=1)
    # 長方形のバウンディングボックスでクリッピング（長方形外側は描画されない）
    circle.set_clip_box(rect.get_bbox())
    ax.add_patch(circle)

    # 以下、新たに追加する磁束密度Bを表す図形
    # 円の中心から、半径よりも外、つまり上側に
    # 小さな黒塗りの円（内部極）と、その外側を囲む、塗りつぶされていない円（外枠）を描画
    # ここでは、元の半円の中心 center を基準とし、上方向に (radius + offset) だけずらす
    offset = 0.3
    small_center = (center[0], center[1] + radius + offset)  # 例: (1.1667, 0 + 0.5 + 0.3) = (1.1667, 0.8)
    small_r = 0.04   # 小さい円の半径
    outer_r = 0.1    # 外枠の円の半径

    # 内部の黒く塗りつぶされた小円
    small_circle = patches.Circle(small_center, small_r, edgecolor='black',
                                  facecolor='black')
    ax.add_patch(small_circle)
    # その外側に、塗りつぶされていない円（外枠）
    outer_circle = patches.Circle(small_center, outer_r, edgecolor='black',
                                  facecolor='none', linewidth=1)
    ax.add_patch(outer_circle)
    # Bベクトルのラベルを、円のちょうど右に配置（横方向中央揃え）
    ax.text(small_center[0] + outer_r + 0.05, small_center[1], r'$\vec{B}$',
            fontsize=8, fontfamily='serif', ha='left', va='center')

    # 表示範囲の設定
    ax.set_aspect('equal')
    ax.axis('off')

    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_rectangle_plot()