import pandas as pd

df = pd.read_csv("youtube-ing.csv")

result = df.head(10) # ilk 10 kaydı getirir
result = df[5:10].head(5) # ikinci 5 kaydı getirir
result = df.columns # datasette bulunan kolon isimlerini getirir
result = len(df.columns) # datasette bulunan kolon sayısını verir
df = df.drop(["video_id", "trending_date", "title", "channel_title"],axis=1) # aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyin
result = df
result = df["likes"].mean() # beğenme sayıları
result = df["dislikes"].mean() # beğenmeme sayıları
result = df["likes"].head(50),df["dislikes"].head(50) # ilk 50 videonun like ve dislike oranları "birinci yöntem ayrı ayrı alır"
result = df.head(50)[["likes","dislikes"]] # ilk 50 videonun like ve dislike oranlarını alır "ikinci yöntem"
result = df[(df["views"].max()) == df["views"]] # en cok göruntulenen video
result = df[(df["views"].min()) == df["views"]] # en az göruntulenen video
# result = df.sort_values("views",ascending=False).head(10)[["title","views"]] # en fazla goruntulenen ilk 10 kaydı getirir
result = df.groupby("category_id").mean().sort_values("likes")["likes"] #te kategoriye gore beğeni ortalamalarını sırasıyla getir
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"] # kategoriye gor yourm sayısını sırasıyla getir
result = df["category_id"].value_counts() # her kategoride kac video var goster

# df["title_len"] = df["title"].apply(len) # her videonun title uzunluk bilgisini yeni bir kolonda gosteriniz
# result = df

# df["tags_sayısı"] =df["tags"].apply(lambda x: len(x.split("|"))) # her video için kullanılan tag sayısını yeni kkolonda gosterir "birinci yontem"
# result = df

def tagCount(tag): # ikinci yontem
    return len(tag.split("|"))
df["tags_sayısı"] =df["tags"].apply(tagCount)
result = df


# en popiler videları belirle like dislike oranına göre
def likeDislikeOranı(oran):
    likelist = list(df["likes"]) # listeye cevirdik
    dislikeslist = list(df["dislikes"])
    ziple = zip(likelist,dislikeslist) # beğeni sayısı(10,10) beğenmeme sayısı seklinde sikiştirir

    oranListesi = [] # yeni bir liste oluşturduk
    for like,dislike in ziple:
        if(like + dislike) == 0:
            oranListesi.append(0) # lis ve dislike toplamı sıfır olanlar otomatik 0 değerini alır

        else:
            oranListesi.append(like/(like+dislike)) # like + dislike bolumunden kalan sayıyı alır

    return oranListesi


df["beğeniOranı"]= likeDislikeOranı(df) # yeni bir kolon oluştırduk

print(df.sort_values("beğeniOranı",ascending=False)[["likes","dislikes","beğeniOranı"]]) # ascending tersten sıralar
