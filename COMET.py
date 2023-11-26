from comet import download_model, load_from_checkpoint

model_path = download_model("Unbabel/wmt22-comet-da")  
model = load_from_checkpoint(model_path)


src = open('/kaggle/input/cometdataset/zh.txt').read().strip().split('\n')
mt = open('/kaggle/input/cometdataset/googletrans.shuffle4G.txt').read().strip().split('\n')
ref = open('/kaggle/input/cometdataset/en.txt').read().strip().split('\n')


data = [{
  "src": s, 
  "mt": t,
  "ref": r
} for s, t, r in zip(src, mt, ref)]


output = model.predict(data)

#print(output.scores) 
print(output.system_score)