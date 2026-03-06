# Consciousness Sliding Model Simulation

## 概要
このパッケージは、意識場仮説をもとにした**滑り台モデル**を量子計算で概念的に再現するためのサンプルです。

- 微小管は量子ビットで抽象化
- 意識場 \(C(t)\) は弱測定（Weak Measurement）として表現
- 集団意識（人数 n）、遮蔽 S、距離 r といったパラメータも組み込んでいます

> 注意: これはあくまで**理論モデルの概念実験**です。現実の意識場の証明を意図するものではありません。

## 収録内容
- `sliding_model.pdf` : 滑り台モデル論文（概念説明）
- `consciousness_sim.py` : Qiskitで実行できるシミュレーションコード
- `requirements.txt` : Pythonライブラリの依存関係

## 実行方法
1. Python 3.x と Qiskit をインストール
```bash
pip install -r requirements.txt
2.	コードを実行
python consciousness_sim.py
3.	コヒーレンス (\Gamma(t)) の時間推移がプロットされます

パラメータ変更
	•	集団人数 n、遮蔽 S、距離 r、感情・記憶パラメータは consciousness_sim.py 内で調整可能
	•	これらを変えると、コヒーレンス変化の傾向を観察できます

注意点
	•	優位差や変化が出ても、意識場の存在を証明するものではありません
	•	あくまで概念実験としての計算モデルです
	•	実験条件やパラメータの探索に使用してください

ライセンス

MIT License
