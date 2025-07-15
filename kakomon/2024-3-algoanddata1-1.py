from graphviz import Graph
import os

# 無向グラフの定義（format は 'jpg'）
g = Graph('G', filename='graph', format='jpg')

# グラフ属性の設定：左から右への水平レイアウト
g.attr(rankdir='LR')  # Left to Right

# 高解像度画像のための設定
# DPIを300に設定（デフォルトは96程度）
g.attr(dpi='600', shape='circle')

# エッジの追加
g.edge('0', '1')
g.edge('0', '2')
g.edge('1', '2')
g.edge('2', '3')

# render()で画像を生成（dot コマンドが PATH にあるか確認してください）
# Graphviz（dot コマンド）が必要です
try:
    out_file = g.render(cleanup=True)
    print("生成されたファイル名:", out_file)

    # 出力されたファイル名が "graph.jpg" になっていない場合は、以下のように明示的にリネームします
    if not out_file.endswith("graph.jpg"):
        new_name = "graph.jpg"
        os.rename(out_file, new_name)
        print("ファイル名を", new_name, "に変更しました。")
except Exception as e:
    print("エラーが発生しました:", e)
    print("Graphviz（dot コマンド）がインストールされ、PATH に設定されていることを確認してください。")