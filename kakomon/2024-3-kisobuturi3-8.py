import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Yu Gothic'

def create_vertical_rectangle(filename="8.jpg"):
    fig, ax = plt.subplots()

    # 縦に長い長方形（内部は塗りつぶさない）
    rect = patches.Rectangle((0, 0), 1, 3, angle=0,
                             linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)

    # 長方形の右下の頂点 (1, 0) から水平右方向に矢印を追加（長さ = 長方形の短辺＝1）
    ax.arrow(1, 0, 1, 0, head_width=0.05, head_length=0.1,
             fc='black', ec='black', length_includes_head=True)
    # 長方形の右下から生えている矢印の先（(2,0)）の少し右側に「導体棒の速さ」のテキストを追加
    ax.text(2.05, 0, "導体棒の速さ", fontsize=10, fontfamily='Yu Gothic', va='center', ha='left')
    
    # 長方形の中央に、長方形の長辺の半分（1.5）の長さの、まっすぐ上方向の矢印を追加
    # 始点を (0.5, 1.3) に変更して、矢印が少し下側から生えるようにする
    center_arrow_start = (0.5, 1.3)
    arrow_length = 1.5
    ax.arrow(center_arrow_start[0], center_arrow_start[1], 0, arrow_length,
             head_width=0.05, head_length=0.1, fc='black', ec='black', length_includes_head=True)
    
    # center_arrow_start の位置に、正円（楕円ではない）の円を追加
    small_circle = patches.Circle(center_arrow_start, 0.08, edgecolor='black',
                                  facecolor='white', linewidth=1)
    ax.add_patch(small_circle)
    # 円の内部に "-e" とセリフ体で描画
    ax.text(center_arrow_start[0], center_arrow_start[1], r'$-e$',
            fontsize=10, fontfamily='serif', ha='center', va='center')
    
    # ここで、軸のアスペクトを equal に設定（これにより円が正円に表示されます）
    ax.set_aspect('equal')

    ax.text(0.6, 1.3, "ローレンツ力F\n(電子の流れる方向)", fontsize=10, fontfamily='Yu Gothic',
            ha='left', va='center')
    
    # 長方形の左側に下向きの矢印とテキストを追加
    # 矢印の始点は、長方形の左側中央 (0, 1.5) とする。矢印は下方向に 1.5 の長さ
    ax.arrow(-0.1, 2, 0, -1.5, head_width=0.05, head_length=0.1,
             fc='black', ec='black', length_includes_head=True)
    # 矢印の左側に、「電流の向き」というテキストを配置
    ax.text(-0.1, 1.5 - 0.75, "電流の向き", fontsize=10, fontfamily='Yu Gothic',
            ha='right', va='center')
    
    # 新たに追加：長方形の左上の頂点の、更に左上に、外側の円を追加
    # 長方形の左上の頂点は (0, 3) なので、そこから左上方向にオフセットする
    outer_circle_center = (-0.2, 3.2)
    outer_radius = 0.1
    outer_circle = patches.Circle(outer_circle_center, outer_radius, edgecolor='black',
                                  facecolor='none', linewidth=1)
    ax.add_patch(outer_circle)
    # 外側の円の内側に、黒塗りの内側の円を追加
    inner_radius = 0.04
    inner_circle = patches.Circle(outer_circle_center, inner_radius, edgecolor='black',
                                  facecolor='black', linewidth=1)
    ax.add_patch(inner_circle)
    # 外側の円の左上に "B" のテキストを配置
    ax.text(outer_circle_center[0] - outer_radius, outer_circle_center[1] + outer_radius,
            "B", fontsize=10, fontfamily='serif', ha='center', va='center')
    
    ax.axis('off')

    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_vertical_rectangle()