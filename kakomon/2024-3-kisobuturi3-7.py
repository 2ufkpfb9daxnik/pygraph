import matplotlib.pyplot as plt
import math

def create_F_vector_plot(filename="7.jpg"):
    fig, ax = plt.subplots()

    # ベクトル F : 原点から上方向へ（長さ 3）
    ax.arrow(0, 0, 0, 3, head_width=0.025, head_length=0.1,
             fc='black', ec='black', length_includes_head=True)
    ax.text(0.15, 1.5, r'$\vec{F}$', fontsize=12, fontfamily='serif')

    # ベクトル B : 同じ原点から、水平状態から +20°回転した方向（長さ 3）
    angle_B = math.radians(20)
    length = 3
    bx = length * math.cos(angle_B)
    by = length * math.sin(angle_B)
    ax.arrow(0, 0, bx, by, head_width=0.025, head_length=0.1,
             fc='black', ec='black', length_includes_head=True)
    # ベクトル B のラベルを、矢印の先端から少し右側に配置
    ax.text(bx + 0.15, by, r'$\vec{B}$', fontsize=12, fontfamily='serif')

    # ベクトル v : 同じ原点から、水平状態から -20°回転した方向（長さ 3）
    angle_v = math.radians(-20)
    bx_v = length * math.cos(angle_v)
    by_v = length * math.sin(angle_v)
    ax.arrow(0, 0, bx_v, by_v, head_width=0.025, head_length=0.1,
             fc='black', ec='black', length_includes_head=True)
    # ベクトル v のラベルを、矢印の先端から少し右側に配置
    ax.text(bx_v + 0.15, by_v, r'$\vec{v}$', fontsize=12, fontfamily='serif')
    
    # ----- 以下、直角マークの挿入 -----
    seg = 0.1  # 直角マークの各線分の長さ
    
    # (1) Fとvの間の直角マーク
    # F上の点 (0, 0.1)
    p1 = (0, 0.1)
    # p1から、Bと同じ傾き(20°)・方向に seg の線分を引く
    dx1 = seg * math.cos(angle_B)
    dy1 = seg * math.sin(angle_B)
    p2 = (p1[0] + dx1, p1[1] + dy1)
    # p2から垂直下に seg の線分を引く（下方向は y 減少）
    p3 = (p2[0], p2[1] - seg)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='black', linewidth=1)
    ax.plot([p2[0], p3[0]], [p2[1], p3[1]], color='black', linewidth=1)
    
    # (2) FとBの間の直角マーク
    # F上の点 (0, 0.1) を再利用
    q1 = (0, 0.1)
    # q1から、vと同じ傾き(-20°)・方向に seg の線分を引く
    dx2 = seg * math.cos(angle_v)
    dy2 = seg * math.sin(angle_v)
    q2 = (q1[0] + dx2, q1[1] + dy2)
    # q2から垂直下に seg の線分を引く
    q3 = (q2[0], q2[1] - seg)
    ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color='black', linewidth=1)
    ax.plot([q2[0], q3[0]], [q2[1], q3[1]], color='black', linewidth=1)
    # ----- 直角マーク 終了 -----
    
    ax.axis('off')

    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_F_vector_plot()