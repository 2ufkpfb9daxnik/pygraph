import matplotlib.pyplot as plt
import japanize_matplotlib

fig, ax = plt.subplots(figsize=(8, 2.5))  # 縦方向を圧縮

# 四分位数・中央値・平均・外れ値
whisker_min = 69
box_min = 76
median = 81  # 箱内の中央値
box_max = 83
whisker_max = 90
mean = 80
outliers = [62, 65, 99]

# 箱（76～83）
ax.plot([box_min, box_max], [1, 1], color='black', linewidth=2)  # 箱の上下
ax.plot([box_min, box_min], [0.92, 1.08], color='black', linewidth=2)  # 左端
ax.plot([box_max, box_max], [0.92, 1.08], color='black', linewidth=2)  # 右端
ax.fill_between([box_min, box_max], 0.92, 1.08, color='skyblue', alpha=0.5, zorder=0)

# 箱内の中央値（赤線）
ax.plot([median, median], [0.92, 1.08], color='red', linewidth=2)

# 平均点（ひし形マーク）
ax.scatter(mean, 1, marker='D', color='deepskyblue', s=80, zorder=5)

# ヒゲ（69～76, 83～90）
ax.plot([whisker_min, box_min], [1, 1], color='black', linestyle='-', linewidth=1)
ax.plot([box_max, whisker_max], [1, 1], color='black', linestyle='-', linewidth=1)
# ヒゲの端に縦線
ax.plot([whisker_min, whisker_min], [0.95, 1.05], color='black', linewidth=2)
ax.plot([whisker_max, whisker_max], [0.95, 1.05], color='black', linewidth=2)

# 外れ値（○マーク）
for outlier in outliers:
    ax.scatter(outlier, 1, marker='o', color='purple', s=80, facecolors='none', edgecolors='purple', zorder=5)

# 1点ごとに薄い点線
for x in range(60, 101):
    ax.axvline(x, color='gray', linestyle=':', linewidth=0.7, zorder=0)

# 軸目盛を5点ごとに
ax.set_xticks(range(60, 101, 5))
ax.set_yticks([])

# 箱ひげ図の外側左右に「理科」と表示
ax.text(57, 1, '理科', fontsize=16, fontweight='bold', rotation=90, va='center', fontname='Yu Gothic')
ax.text(102, 1, '理科', fontsize=16, fontweight='bold', rotation=90, va='center', fontname='Yu Gothic')

ax.set_xlim(60, 100)
ax.set_ylim(0.9, 1.1)
ax.set_xlabel('')
ax.set_title('')

plt.tight_layout()
plt.savefig('box.jpg', dpi=300)