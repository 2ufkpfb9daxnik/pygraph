import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.interpolate import splprep, splev

# 日本語フォントの設定例（システムにインストールされている日本語フォントを指定）
plt.rcParams['font.family'] = 'Yu Gothic'

def generate_circuit(filename="4.jpg"):
    fig, ax = plt.subplots(figsize=(8,4))
    
    # 外枠のパラメータ
    left, right, bottom, top = 0, 10, 0, 4
    
    # 外枠の上辺・下辺（部品がある領域は線を描かない）
    ax.plot([left, 1], [top, top], color='black', lw=2)
    ax.plot([9, right], [top, top], color='black', lw=2)
    ax.plot([left, 1], [bottom, bottom], color='black', lw=2)
    ax.plot([3, 4.8], [bottom, bottom], color='black', lw=2)
    ax.plot([5.2, 7], [bottom, bottom], color='black', lw=2)
    ax.plot([9, right], [bottom, bottom], color='black', lw=2)
    ax.plot([left, left], [bottom, top], color='black', lw=2)
    ax.plot([right, right], [bottom, top], color='black', lw=2)
    
    # 内部部品の描画
    # ① ソレノイド（上側）
    # x=1～9 内で各コイルの部分円の端点をすべて集め、スプライン補間で滑らかに連結
    n_coils = 30
    coil_points = 20  # 各部分円で取得する点数
    coil_radius = 0.25
    gap = 0.3  # 各コイルの開始・終了角度に設ける隙間（ラジアン）
    pts = []  # 全ての点を保存
    
    for i in range(n_coils):
        # 各コイルの中心位置（等間隔に配置）
        center_x = 1 + ((9 - 1) / n_coils) * (i + 0.5)
        # ここで中心位置を少し上に寄せる（オフセットを 0.05 に変更）
        center_y = top - coil_radius + 0.1
        # 部分円とするため、gap分だけ角度をカットして描く
        t = np.linspace(gap/2, 2 * np.pi - gap/2, coil_points)
        x_circle = center_x + coil_radius * np.cos(t)
        y_circle = center_y + coil_radius * np.sin(t)
        # 最初のコイルは全点、以降は先頭の点を除いて重複を避ける
        if i == 0:
            for xx, yy in zip(x_circle, y_circle):
                pts.append([xx, yy])
        else:
            for xx, yy in zip(x_circle[1:], y_circle[1:]):
                pts.append([xx, yy])
    pts = np.array(pts)
    # 外枠上辺との接続：最初と最後の点をそれぞれ (1, top) と (9, top) に設定
    pts[0] = [1, top]
    pts[-1] = [9, top]
    
    # スプライン補間で滑らかに連結（s はスムージング係数、値を小さくすると通過に近い）
    tck, u = splprep([pts[:,0], pts[:,1]], s=0.5, per=False)
    u_fine = np.linspace(0, 1, 1000)
    x_smooth, y_smooth = splev(u_fine, tck)
    ax.plot(x_smooth, y_smooth, color='black', lw=2)
    ax.text((1+9)/2, top - coil_radius - 0.3, 'ソレノイド', fontsize=12,
            ha='center', va='top')
    
    # 下側の部品は少し下に配置（offset を追加）
    offset = 0.3
    
    # ② 抵抗 R：左側部品（全辺描画）
    res_left, res_right = 1, 3
    res_bottom = bottom - offset
    res_top = res_bottom + 0.6
    ax.plot([res_left, res_left], [res_bottom, res_top], color='black', lw=2)
    ax.plot([res_right, res_right], [res_bottom, res_top], color='black', lw=2)
    ax.plot([res_left, res_right], [res_bottom, res_bottom], color='black', lw=2)
    ax.plot([res_left, res_right], [res_top, res_top], color='black', lw=2)
    ax.text((res_left+res_right)/2, res_top + 0.3, 'R', fontsize=12, ha='center',
            va='center', fontfamily='serif')
    
    # ③ 電源 V：中央部品（おおむね x=4.8～5.2）
    v_left, v_right = 4.8, 5.2
    ax.plot([v_left, v_left], [bottom - offset, bottom - offset + 0.8], color='black', lw=2)
    ax.plot([v_right, v_right], [bottom - offset + 0.2, bottom - offset + 0.4], color='black', lw=2)
    ax.text((v_left+v_right)/2, bottom - offset + 1, 'V', fontsize=12, ha='center',
            va='top', fontfamily='serif')
    
    # ④ スイッチ S：右側部品（x=7～9）
    sw_left, sw_right = 7, 9
    sw_y = bottom - offset + 0.3
    ax.plot([sw_left, 7.8], [sw_y, sw_y], color='black', lw=2)
    ax.plot([8.2, sw_right], [sw_y, sw_y], color='black', lw=2)
    ax.plot([7.8, 8.2], [sw_y, bottom - offset + 0.8], color='black', lw=2)
    ax.text((sw_left+sw_right)/2, bottom - offset + 0.9, 'S', fontsize=12, ha='center',
            va='bottom', fontfamily='serif')
    
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 5)
    ax.axis('off')
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)

if __name__ == "__main__":
    generate_circuit()