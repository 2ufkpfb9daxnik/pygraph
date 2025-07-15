from graphviz import Digraph
import os

# 有向グラフの定義（座標指定を活用するため neato エンジンを使用）
g = Digraph('G', filename='tree', format='jpg', engine='neato')

# グラフ属性の設定
g.attr(dpi='300')     # 高解像度設定
g.attr(fontname='Yu Gothic')  # 日本語フォント設定
g.attr(overlap='true')  # ノードの重なりを許可する
g.attr(splines='true')  # エッジを曲線に

# ノードの形状設定（塗りつぶしなし）
g.attr('node', shape='circle', style='solid', fontsize='14')
g.attr('edge', fontname='Yu Gothic')  # エッジのラベルにも日本語フォント設定

# 木構造のノードを配置（座標指定）
# 左から右への配置になるように座標を調整
g.node('1', pos='1,3!')  # 左端
g.node('2', pos='3,3!')  # 1の右側
g.node('4', pos='1,2!')  # 左下
g.node('5', pos='3,2!')  # 4の右側
g.node('6', pos='4.5,2.5!')  # 5の右上
g.node('8', pos='4.5,1.5!')  # 5の右下
g.node('7', pos='6,1.5!')  # 8の右側

# 矢印の追加（位置が指定されているので、エッジは単に接続を示すだけ）
g.edge('1', '2')  # 1から2へ
g.edge('4', '5')  # 4から5へ
g.edge('5', '6')  # 5から6へ
g.edge('5', '8')  # 5から8へ
g.edge('8', '7')  # 8から7へ

# ----- 凡例部分 -----
# 凡例用の角丸長方形
g.node('legend_box', 
       shape='box', 
       style='rounded',
       label='',
       width='3',
       height='2.5',
       color='black',
       fillcolor='none',
       pos='8,2!')

# 凡例ラベル（角丸長方形と同じ座標で重ねて表示）
g.node('legend_title', 
       label='凡例:', 
       shape='none',
       fontname='Yu Gothic', 
       fontsize='14',
       pos='7,3.5!')  # legend_boxと同じ座標

# 凡例内のノード例（意図的に説明ラベルと重ねる）
g.node('example_node', 
       shape='circle', 
       label='10', 
       style='solid',
       pos='7,2.5!')

# ノードの説明ラベル（example_nodeと同じ位置に配置して重ねる）
g.node('node_label', 
       label='ノード\n(円内数字はID)', 
       shape='none',
       fontname='Yu Gothic',
       pos='8,2.5!')  # example_nodeと同じ座標

# 矢印の始点・終点（arrow_start_labelと重ねる）
g.node('arrow_start_point', 
       shape='point', 
       width='0.05', 
       height='0.05',
       label='',
       pos='7,1.5!')  # arrow_start_labelと同じ座標

g.node('arrow_end_point', 
       shape='point', 
       width='0.05', 
       height='0.05',
       label='',
       pos='8.5,1.5!')  # arrow_end_labelと同じ座標

# 矢印を描画
g.edge('arrow_start_point', 'arrow_end_point')

# 矢印の説明ラベル（対応するポイントと重ねる）
g.node('arrow_start_label', 
       label='矢印の元', 
       shape='none',
       fontname='Yu Gothic',
       pos='7,1!')  # arrow_start_pointと同じ座標

g.node('arrow_end_label', 
       label='矢印の先', 
       shape='none',
       fontname='Yu Gothic',
       pos='8.5,1!')  # arrow_end_pointと同じ座標

try:
    # レンダリングして画像生成
    out_file = g.render(cleanup=True)
    print("生成されたファイル名:", out_file)

    # 出力ファイル名がtree.jpgでない場合、リネームする
    if not out_file.endswith("tree.jpg"):
        new_name = "tree.jpg"
        os.rename(out_file, new_name)
        print("ファイル名を", new_name, "に変更しました。")
except Exception as e:
    print("エラーが発生しました:", e)
    print("Graphviz（dot コマンド）がインストールされ、PATH に設定されていることを確認してください。")