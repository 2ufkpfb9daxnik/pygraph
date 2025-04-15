import matplotlib.pyplot as plt

def generate_2d_plot(filename="plot.png"):
    fig, ax = plt.subplots()

    # x軸の矢印：(-1,0)から(1,0)へ
    ax.arrow(-1, 0, 2, 0, head_width=0.1, head_length=0.2, fc='black', ec='black')
    # y軸の矢印：(0,-1)から(0,1)へ
    ax.arrow(0, -1, 0, 2, head_width=0.1, head_length=0.2, fc='black', ec='black')
    # z軸の矢印： (1,1)から(-1,-1)へ（y=x線上、左下方向）
    ax.arrow(1, 1, -2, -2, head_width=0.1, head_length=0.2, fc='black', ec='black')

    # 0,0からx軸正方向への太いベクトルv
    ax.arrow(0, 0, 0.8, 0, head_width=0.1, head_length=0.15,
             fc='black', ec='black', lw=3, length_includes_head=True)
    # ベクトルvであることを示すため、中央付近にラベル（上付きの矢印付きv）を配置
    ax.text(0.4, 0.12, r'$\vec{v}$', fontsize=12, ha='center', fontfamily='serif')

    # 各軸のラベル
    ax.text(1.2, -0.1, 'x', fontsize=12, fontfamily='serif')
    ax.text(-0.2, 1.2, 'y', fontsize=12, fontfamily='serif')
    ax.text(-1.25, -1.2, 'z', fontsize=12, fontfamily='serif')
    ax.text(0.05, -0.15, 'O', fontsize=12, fontfamily='serif')

    # 原点0,0に黒塗りの丸を描画（ベクトルの始点を強調）
    ax.plot(0, 0, marker='o', markersize=6, color='black')

    # 軸比を1:1に設定
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    # 目盛りと枠線を非表示にする
    ax.axis('off')

    # 余白を削って高解像度で保存
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == "__main__":
    generate_2d_plot()

    