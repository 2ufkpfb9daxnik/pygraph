import matplotlib.pyplot as plt

def create_Vt_coordinate_plot(filename="6.jpg"):
    fig, ax = plt.subplots()

    # t軸（横軸）：原点から右方向へ矢印
    ax.arrow(0, 0, 13, 0, length_includes_head=True,
             head_width=0.3, head_length=0.5, fc='black', ec='black')
    # V軸（縦軸）：下から上方向へ矢印
    ax.arrow(0, -6, 0, 12, length_includes_head=True,
             head_width=0.3, head_length=0.5, fc='black', ec='black')

    # t軸正方向に、t = 1～12 の位置に点線グリッドを描画（t=13は除く）
    for t in range(1, 13):
        ax.axvline(x=t, color='gray', linestyle=':', linewidth=0.5)

    # V軸方向に、-5 < V < 5 の整数部分で水平グリッドを描画
    # ※ V=-6, 6は描画しない
    for v in range(-5, 6):  # -4 ～ 4
        ax.axhline(y=v, color='gray', linestyle=':', linewidth=0.5)

    # 表示範囲の設定
    ax.set_xlim(-1, 14)
    ax.set_ylim(-7, 7)

    # 軸など不要なものは非表示に
    ax.axis('off')

    # 軸ラベルの配置
    ax.text(13, -0.8, "t [s]", fontsize=12, ha='right', va='top', fontfamily='serif')
    ax.text(0.4, 7, "V [V]", fontsize=12, ha='left', va='bottom', fontfamily='serif')
    ax.text(-0.5, -0.5, "O", fontsize=12, ha='right', va='top', fontfamily='serif')

    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_Vt_coordinate_plot()