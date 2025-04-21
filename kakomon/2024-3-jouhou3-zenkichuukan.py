import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_image_plot(filename="image.jpg"):
    fig, ax = plt.subplots()

    # --- Layer 0 ---
    # 1つ目の円：中心を (0, 2.6) として半径 0.5
    circle1 = patches.Circle((0, 2.6), 0.5, edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(circle1)
    ax.text(0, 2.6, r'$a_0^{(0)}$', fontsize=14, ha='center', va='center', fontfamily='serif')
    
    # 2つ目の円：中心を (0, 1.4) として半径 0.5
    circle2 = patches.Circle((0, 1.4), 0.5, edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(circle2)
    ax.text(0, 1.4, r'$a_1^{(0)}$', fontsize=14, ha='center', va='center', fontfamily='serif')
    
    # 3つ目の円：中心を (0, 0.2) として半径 0.5
    circle3 = patches.Circle((0, 0.2), 0.5, edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(circle3)
    ax.text(0, 0.2, r'$a_2^{(0)}$', fontsize=14, ha='center', va='center', fontfamily='serif')
    
    # Layer 0 を囲む外枠の長方形（点線）
    rect_x = -0.7   # -0.5 - 0.2
    rect_y = -0.5   # -0.3 - 0.2
    rect_width = 1.4   # 1.0 + 0.4
    rect_height = 3.8  # (3.1+0.2) - (-0.5)
    outer_rect = patches.Rectangle((rect_x, rect_y), rect_width, rect_height,
                                   edgecolor='black', facecolor='none', linewidth=1, linestyle='dashed')
    ax.add_patch(outer_rect)
    
    # Layer 0 の上部中央に "Layer 0"（ゴシック体）
    ax.text(0, rect_y + rect_height + 0.1, "Layer 0", fontsize=14, ha='center', va='bottom', fontfamily='Yu Gothic')
    
    # --- Layer 1 ---
    # Layer 1 の外枠を、Layer 0 の右端（x = 0.7）から 1.5 マス離して配置
    new_rect_x = 0.7 + 1.5  # 2.2
    new_rect_y = 0.1 - 0.2    # -0.1
    new_rect_width = 1.4      
    new_rect_height = (2.5 + 0.2) - (-0.1)  # 2.8
    layer1_rect = patches.Rectangle((new_rect_x, new_rect_y), new_rect_width, new_rect_height,
                                    edgecolor='black', facecolor='none', linewidth=1, linestyle='dashed')
    ax.add_patch(layer1_rect)
    
    # Layer 1 の上部中央に "Layer 1"（ゴシック体）
    ax.text(new_rect_x + new_rect_width/2, new_rect_y + new_rect_height + 0.1, "Layer 1",
            fontsize=14, ha='center', va='bottom', fontfamily='Yu Gothic')
    
    # Layer 1 内の上段の円：中心を (new_rect_x + new_rect_width/2, 2.0)
    layer1_circle_top = patches.Circle((new_rect_x + new_rect_width/2, 2.0), 0.5,
                                       edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(layer1_circle_top)
    ax.text(new_rect_x + new_rect_width/2, 2.0, r'$a_0^{(1)}$', fontsize=14, ha='center', va='center', fontfamily='serif')
    
    # Layer 1 内の下段の円：中心を (new_rect_x + new_rect_width/2, 0.6)
    layer1_circle_bottom = patches.Circle((new_rect_x + new_rect_width/2, 0.6), 0.5,
                                          edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(layer1_circle_bottom)
    ax.text(new_rect_x + new_rect_width/2, 0.6, r'$a_1^{(1)}$', fontsize=14, ha='center', va='center', fontfamily='serif')
    
    # --- 接続線とラベルの追加 ---
    # 左側の円の略称：a, b, c；右側の円の略称：d, e
    a  = (0, 2.6)
    b  = (0, 1.4)
    c  = (0, 0.2)
    # 接続は円の横端から：左側は右端（中心の x + 半径）、右側は左端（中心の x - 半径）
    a_edge = (a[0] + 0.5, a[1])
    b_edge = (b[0] + 0.5, b[1])
    c_edge = (c[0] + 0.5, c[1])
    # Layer 1 の円：中心＝ new_rect_x + new_rect_width/2
    d_center = (new_rect_x + new_rect_width/2, 2.0)   # (2.2+0.7, 2.0) = (2.9, 2.0)
    e_center = (new_rect_x + new_rect_width/2, 0.6)    # (2.9, 0.6)
    d_edge = (d_center[0] - 0.5, d_center[1])
    e_edge = (e_center[0] - 0.5, e_center[1])
    
    def connect_and_label(start_edge, end_edge, label_text, offset_x=0, offset_y=0.1):
        ax.plot([start_edge[0], end_edge[0]], [start_edge[1], end_edge[1]], color='black', linewidth=1)
        mid_x = (start_edge[0] + end_edge[0]) / 2 + offset_x
        mid_y = (start_edge[1] + end_edge[1]) / 2 + offset_y
        ax.text(mid_x, mid_y, label_text, fontsize=12, ha='center', va='bottom', fontfamily='serif')
    
    connect_and_label(a_edge, d_edge, r'$w_{0,0}$')  # 変更なし
    connect_and_label(a_edge, e_edge, r'$w_{1,0}$', offset_x=-0.2, offset_y=0.4)  # 変更なし
    connect_and_label(b_edge, d_edge, r'$w_{0,1}$', offset_x=-0.2, offset_y=-0.2)  # 変更なし
    # w_{1,1} をもっと左上に寄せる（offset_x = -0.4, offset_y = +0.3）
    connect_and_label(b_edge, e_edge, r'$w_{1,1}$', offset_x=-0.4, offset_y=0.2)
    # w_{0,2} をもっと左下に寄せる（offset_x = -0.3, offset_y = -0.2）
    connect_and_label(c_edge, d_edge, r'$w_{0,2}$', offset_x=-0.3, offset_y=-0.4)
    # w_{1,2} をもっと下に寄せる（offset_y を -0.2 に変更）
    connect_and_label(c_edge, e_edge, r'$w_{1,2}$', offset_x=0, offset_y=-0.2)
    
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 5.0)
    ax.set_ylim(-1, 4.5)
    
    ax.axis('off')
    
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == '__main__':
    create_image_plot()