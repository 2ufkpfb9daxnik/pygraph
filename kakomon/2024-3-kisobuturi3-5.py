import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.patches import Arc, Polygon


plt.rcParams['font.family'] = 'Yu Gothic'

def draw_parallelogram():
    # もとの平行四辺形の頂点（ア, イ, ウ, エ）の座標設定
    A = (6, 4)   # ア
    B = (4, 5)   # イ
    C = (0, 3)   # ウ
    D = (2, 2)   # エ
    vertices = [A, B, C, D]
    labels = ['ア', 'イ', 'ウ', 'エ']
    
    plt.figure(figsize=(6,4))
    
    # --- もとの平行四辺形（実線）の描画 ---
    # 辺 A→B, B→C, C→D をそのまま描画
    xs, ys = zip(*[A, B])
    plt.plot(xs, ys, 'k-', lw=2)
    xs, ys = zip(*[B, C])
    plt.plot(xs, ys, 'k-', lw=2)
    xs, ys = zip(*[C, D])
    plt.plot(xs, ys, 'k-', lw=2)
    
    # 辺 D→A を途切れさせる
    dx, dy = A[0] - D[0], A[1] - D[1]  # (6-2, 4-2) = (4,2)
    f = 0.1                           # gap の割合（中央 f%を途切れさせる）
    seg_frac = (1 - f) / 2            # それぞれの描画割合
    # gap開始点 P：D + seg_frac*(A-D)
    P = (D[0] + seg_frac*dx, D[1] + seg_frac*dy)
    # gap終了点 Q：A - seg_frac*(A-D)
    Q = (A[0] - seg_frac*dx, A[1] - seg_frac*dy)
    # 辺 D→A は D→P と Q→A で描画
    xs, ys = zip(*[D, P])
    plt.plot(xs, ys, 'k-', lw=2)
    xs, ys = zip(*[Q, A])
    plt.plot(xs, ys, 'k-', lw=2)
    
    # 次に、両方の gap の端（P と Q）から、辺 B→A と平行な方向へ延長線を描く
    d_vec = (A[0] - B[0], A[1] - B[1])   # = (6-4, 4-5) = (2, -1)
    norm = math.hypot(d_vec[0], d_vec[1])
    u_vec = (d_vec[0]/norm, d_vec[1]/norm)
    L = 1.0  # 延長線の長さ
    ext = (u_vec[0]*L, u_vec[1]*L)
    # 拡張先の座標
    P_ext = (P[0] + ext[0], P[1] + ext[1])
    Q_ext = (Q[0] + ext[0], Q[1] + ext[1])
    xs, ys = zip(*[P, P_ext])
    plt.plot(xs, ys, 'k-', lw=2)
    xs, ys = zip(*[Q, Q_ext])
    plt.plot(xs, ys, 'k-', lw=2)
    
    # 延長線上に三角形（矢印）を描画して電流の流れを示す
    perp = (-u_vec[1], u_vec[0])
    arrow_len = 0.2   # 三角形の高さ
    arrow_half = 0.1  # 三角形の底辺半分の長さ
    
    # D側延長（点エ側）：電流が回路内に入る（矢印は P_ext側から内向き）
    T_P = (P_ext[0] - 0.2*u_vec[0], P_ext[1] - 0.2*u_vec[1])
    tri_P = [
        T_P,
        (T_P[0] + arrow_len*u_vec[0] + arrow_half*perp[0],
         T_P[1] + arrow_len*u_vec[1] + arrow_half*perp[1]),
        (T_P[0] + arrow_len*u_vec[0] - arrow_half*perp[0],
         T_P[1] + arrow_len*u_vec[1] - arrow_half*perp[1])
    ]
    tri_P_x, tri_P_y = zip(*tri_P)
    plt.fill(tri_P_x, tri_P_y, 'k')
    
    # A側延長（点ア側）：電流が回路から出る（矢印は Q_ext側から外向き）
    T_Q = (Q_ext[0] + 0.2*u_vec[0], Q_ext[1] + 0.2*u_vec[1])
    tri_Q = [
        T_Q,
        (T_Q[0] - arrow_len*u_vec[0] + arrow_half*perp[0],
         T_Q[1] - arrow_len*u_vec[1] + arrow_half*perp[1]),
        (T_Q[0] - arrow_len*u_vec[0] - arrow_half*perp[0],
         T_Q[1] - arrow_len*u_vec[1] - arrow_half*perp[1])
    ]
    tri_Q_x, tri_Q_y = zip(*tri_Q)
    plt.fill(tri_Q_x, tri_Q_y, 'k')
    
    plt.text(((P_ext[0]+Q_ext[0])/2), ((P_ext[1]+Q_ext[1])/2) - 0.3,
             "電流の正の向き", fontsize=12, ha='center', fontfamily='Yu Gothic')
    
        # ここから新たにアの下側に半円と矢印を描画
    arc_center = (6, 3.5)
        # --- アの下側に描いた半円の上端に付く矢印（三角形）の描画 ---
    plt.text(arc_center[0] - 0.1, arc_center[1] - 0.05, "⤴", fontsize=12)

    # （元の平行四辺形の頂点ラベル個別設定例）
    # ア：A のラベル（例：右上に配置）
    plt.text(A[0] + 0.1, A[1] + 0.1, "ア", fontsize=12, fontfamily='Yu Gothic')
    # イ：B のラベル（例：右下に配置）
    plt.text(B[0] + 0.1, B[1] + 0.05, "イ", fontsize=12, fontfamily='Yu Gothic')
    # ウ：C のラベル（例：左下に配置）
    plt.text(C[0] - 0.2, C[1] - 0.2, "ウ", fontsize=12, fontfamily='Yu Gothic')
    # エ：D のラベル（例：左上に配置）
    plt.text(D[0] - 0.5, D[1] - 0.1, "エ", fontsize=12, fontfamily='Yu Gothic')
    
    # --- ここから新しい平行四辺形（点線）の描画 ---
    # セット済みの gap の割合（f=0.1 なので seg_frac = (1-f)/2 = 0.45）
    # P, Q はもとの D→A 辺から求めた gap の端点
    # P = (3.8, 2.9), Q = (4.2, 3.1)
    
    # new_D：x座標は D と同じ 2、y 座標は D (2) より上
    new_D = (2, 2.2)
    # new_A：x座標は new_D から基底長を足して求める（ここでは 4.0 を足して 6.0）、
    #     　 new_A の y は A (4) より下
    new_A = (6.0, 3.7556)
    
    # new_B：x 座標は B と同じ 4、新しい平行四辺形の上辺は new_A→new_B とするので
    # new_B = (4, y) で y は new_B_y を調整（ここでは 4.7 とする：B = (4,5) より下）
    new_B = (4, 4.7)
    # new_C：平行四辺形の対辺から、new_C = new_D + (new_B - new_A)
    new_C = (new_D[0] + (new_B[0] - new_A[0]),
             new_D[1] + (new_B[1] - new_A[1]))
    #     = (2 + (4 - 6.0), 2.2 + (4.7 - 3.7556))
    #     = (0, 2.2 + 0.9444)
    #     = (0, 3.1444)
    
    # 新しい平行四辺形の gap 部分は、もとの平行四辺形と同じ割合 seg_frac で途切れる
    P_new = (new_D[0] + seg_frac*(new_A[0]-new_D[0]),
             new_D[1] + seg_frac*(new_A[1]-new_D[1]))
    Q_new = (new_A[0] - seg_frac*(new_A[0]-new_D[0]),
             new_A[1] - seg_frac*(new_A[1]-new_D[1]))
    # ここで P_new = (2 + 0.45*4.0, 2.2 + 0.45*(3.7556-2.2))
    #           = (2 + 1.8, 2.2 + 0.45*1.5556)
    #           = (3.8, 2.2 + 0.7) = (3.8, 2.9)
    # 同様に Q_new = (6.0 - 1.8, 3.7556 - 0.7) = (4.2, 3.0556)（概ねもとの Q と一致）
    
    # 点線で新しい平行四辺形を描画（頂点の順番：new_A, new_B, new_C, new_D）
    # 辺 new_A→new_B, new_B→new_C, new_C→new_D はそのまま、new_D→new_A は gap 部分で途切れる
    xs, ys = zip(*[new_A, new_B])
    plt.plot(xs, ys, 'k--', lw=2)
    xs, ys = zip(*[new_B, new_C])
    plt.plot(xs, ys, 'k--', lw=2)
    xs, ys = zip(*[new_C, new_D])
    plt.plot(xs, ys, 'k--', lw=2)
    xs, ys = zip(*[new_D, P_new])
    plt.plot(xs, ys, 'k--', lw=2)
    xs, ys = zip(*[Q_new, new_A])
    plt.plot(xs, ys, 'k--', lw=2)

        # 平行四辺形内の「ウ」のかなり右上の方向の点（例として [2,3] を採用）
    point_B_start = np.array([2, 3])
    # 真上方向のベクトル（[0, 1.5]）
    vec_B = np.array([0, 1.5])
    # plt.quiver を用いてベクトルを描画
    plt.quiver(point_B_start[0], point_B_start[1],
               vec_B[0], vec_B[1],
               angles='xy', scale_units='xy', scale=1, color='k')
    # 矢印上部に「\vec{B}」のラベルを付加
    plt.text(point_B_start[0] - 0.1, point_B_start[1] + vec_B[1] + 0.05,
             r"$\vec{B}$", fontsize=12, fontfamily='Yu Gothic')
    
    plt.axis('off')
    plt.savefig("5.jpg", dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_parallelogram()