import pandas as pd

df = pd.read_csv("arquivos/salaries.csv")
job_diff = df["job_title"].unique()
quantidade_jobs_diff = df["job_title"].value_counts()
print(quantidade_jobs_diff)
print(f"temos {len(job_diff)} tipos de trabalho diferentes\nsendo eles: {job_diff}")
print("\n---\n")
print(len(quantidade_jobs_diff))
print("\n---\n")
diretores = 0
for i in df["job_title"]:
    if i == "Director":
        diretores += 1
print(f"temos {diretores} diretores")
