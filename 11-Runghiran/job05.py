def info(**detail):
    print("สวัสดีครับ ผมชื่อ", detail["name"])
    print("อายุ", detail["age"], "ปี")
    print("กำลังศึกษาอยู่ที่", detail["school"])
    print("ระดับชั้น", detail["level"])
    print("สาขา", detail["major"])
    print("งานอดิเรก", detail["hobby"])

info(
    name="รุ่งหิรัณย์ บุญเรือง",
    age=17,
    school="วิทยาลัยอาชีวศึกษานครราชสีมา",
    level="ปวช.2",
    major="เทคโนโลยีธุรกิจดิจิทัล 1",
    hobby="บาสเกตบอล"
)