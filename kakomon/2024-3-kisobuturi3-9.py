import matplotlib.pyplot as plt
import numpy as np

def create_Vt_coordinate_plot(filename="9.jpg"):
    fig, ax = plt.subplots()

    # t軸（横軸）：原点から右方向へ矢印（t<0は表示しない）
    ax.arrow(0, 0, 13, 0, length_includes_head=True,
             head_width=0.3, head_length=0.5, fc='black', ec='black')
    # V軸（縦軸）：下から上方向へ矢印
    ax.arrow(0, -6, 0, 12, length_includes_head=True,
             head_width=0.3, head_length=0.5, fc='black', ec='black')

    # t軸正方向に、t = 1～12 の位置に点線グリッドを描画
    for t in range(1, 13):
        ax.axvline(x=t, color='gray', linestyle=':', linewidth=0.5)

    # V軸方向に、-5 < V < 5 の整数部分で水平グリッドを描画
    for v in range(-5, 6):
        ax.axhline(y=v, color='gray', linestyle=':', linewidth=0.5)

    # sin(Θ+π) のグラフを追加
    # ω = 2π/周期 = 2π/8 = π/4
    omega = np.pi / 4
    t_values = np.linspace(0, 14, 1000)  # t<0は含めない
    # 振幅2、 sin(ωt + π)
    y_values = 2 * np.sin(omega * t_values + np.pi)
    ax.plot(t_values, y_values, color='red', linewidth=1)

    # t軸上（下部）に、原点から 4マスごとにラベルを配置（t軸に近い位置：y = -0.3)
    ax.text(4, -0.3, r'$\frac{\pi}{\omega}$', fontsize=10, ha='center', va='top', fontfamily='serif')
    ax.text(8, -0.3, r'$\frac{2\pi}{\omega}$', fontsize=10, ha='center', va='top', fontfamily='serif')
    ax.text(12, -0.3, r'$\frac{3\pi}{\omega}$', fontsize=10, ha='center', va='top', fontfamily='serif')

    # V軸の y = 2 と y = -2 に、それぞれ V₀, -V₀ と配置
    ax.text(-0.3, 2, r'$V_0$', fontsize=10, ha='right', va='center', fontfamily='serif')
    ax.text(-0.3, -2, r'$-V_0$', fontsize=10, ha='right', va='center', fontfamily='serif')

    # 表示範囲の設定
    ax.set_xlim(0, 14)
    ax.set_ylim(-7, 7)

    # 軸など不要なものは非表示
    ax.axis('off')

    # 軸ラベルの配置
    ax.text(13, -0.8, "t [s]", fontsize=12, ha='right', va='top', fontfamily='serif')
    ax.text(0.4, 7, "V [V]", fontsize=12, ha='left', va='bottom', fontfamily='serif')
    ax.text(-0.1, -0.5, "O", fontsize=12, ha='right', va='top', fontfamily='serif')

    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_Vt_coordinate_plot()