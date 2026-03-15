from embedchain import App

nameless = App()

videos = [
    "https://youtu.be/Y8Tko2YC5hA?si=uJh5kTuAoLiZrOmJ",
    "https://youtu.be/UrsmFxEIp5k?si=skVMibCIZj2JULRo",
    "https://youtu.be/9CKCfiX3uO0?si=2FKnoo87u1NAlUTS",
    "https://youtu.be/ESnrn1kAD4E?si=4df6a0cIU6jqnSSd",
    "https://youtu.be/HGSjesDHMM4?si=RE2Ib_nVygWj63nd",
    "https://youtu.be/X8F9JfCUWrs?si=pWRSQ2XH4gu1-58z",
    "https://youtu.be/N-iFUEYauLQ?si=fv0qLSZJZil0MiXV",
    "https://youtu.be/2BVqksYJ2yw?si=6Oc85AOUU6Kyou62",
    "https://youtu.be/mKBbP4T5fbk?si=vaDC2vqbOzzJaEYu",
    "https://youtu.be/1SnPKhCdlsU?si=oLOiKC71zOABUBvt",
    "https://youtu.be/e7sAf4SbS_g?si=wlhtyhqCUZLqeqCW",
    "https://youtu.be/3FNYvj2U0HM?si=hacking1",
    "https://youtu.be/lZAoFs75_cs?si=hacking2",
    "https://youtu.be/Vqyk0Pxw9dE?si=hacking3",
    "https://youtu.be/3Kq1MIfTWCE?si=hacking4",
    "https://youtu.be/7Qq2gbG7u_c?si=hacking5",
    "https://youtu.be/F0KqL8H4n6c?si=hacking6",
    "https://youtu.be/2JAwV-C-NJc?si=hacking7",
    "https://youtu.be/p4lwf3TfNJU?si=hacking8",
    "https://youtu.be/5wTunGvY7EU?si=hacking9",
    "https://youtu.be/7w2D5Pp5K2Q?si=hacking10",
    "https://youtu.be/iyAyN3GFM7A?si=hacking11",
    "https://youtu.be/qiQR5rTSshw?si=hacking12",
    "https://youtu.be/j2LkYpG6p3U?si=hacking13",
    "https://youtu.be/kHyWf1NntI0?si=gk1",
    "https://youtu.be/4xGp_6J2I4M?si=gk2",
    "https://youtu.be/9n3B-wQzTcg?si=gk3",
    "https://youtu.be/JZQ5p3W0qQE?si=gk4"
]

print("⏳ Videos load ho rahe hain (2-3 minute)...")
for i, video in enumerate(videos, 1):
    print(f"  📺 Loading {i}/{len(videos)}")
    nameless.add("youtube_video", video)

print("\n" + "="*50)
print("✅ NAMELESS TAYYAR!")
print("👤 Created by: @ERROR0101risback | fahad0101r")
print("="*50 + "\n")

while True:
    q = input("👤 Tum: ")
    if q.lower() in ['quit','exit','bye','band']:
        print("👋 Nameless: Allah Hafiz!")
        break
    print("🤖 Nameless: " + nameless.query(q) + "\n")
