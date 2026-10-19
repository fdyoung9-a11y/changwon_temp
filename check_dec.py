import pandas as pd

df = pd.read_csv('data/changwon_temp.csv', encoding='cp949', skiprows=7)
df.columns = df.columns.str.strip()
df['날짜'] = pd.to_datetime(df['날짜'])
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month

print("컬럼 확인:", df.columns.tolist())
print("행 수:", len(df))

dec_data = df[df['월'] == 12].copy()
dec_data = dec_data.set_index('연도')

col = '평균기온(℃)'
early = dec_data[dec_data.index.isin(range(2000, 2005))][col].mean()
recent = dec_data[dec_data.index.isin(range(2020, 2025))][col].mean()

print(f"2000~2004년 12월 평균: {early:.1f}°C")
print(f"2020~2024년 12월 평균: {recent:.1f}°C")
print(f"차이: {recent - early:+.1f}°C")
