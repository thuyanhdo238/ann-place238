"""
Art Sympathy Agent — Ann Place
Posts daily art + visual emotion content to #art channel at 2:00 UTC
Character: SaLu — a small round creature wandering through beauty
"""

import json
import random
import datetime
import http.client
import ssl

_cfg = json.load(open("config/webhooks.json"))
DISCORD_WEBHOOK = _cfg["art"]


def send_discord(content):
    host = "discord.com"
    path = DISCORD_WEBHOOK.replace("https://discord.com", "")
    payload = json.dumps({"content": content, "username": "SaLu ✦ Art Sympathy"})
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection(host, context=ctx, timeout=10)
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://github.com/thuyanhdo238/ann-place238, 1.0)",
        "Content-Length": str(len(payload.encode("utf-8"))),
    }
    conn.request("POST", path, body=payload, headers=headers)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", errors="ignore")
    print(f"Discord response {resp.status}: {body}")
    if resp.status not in (200, 204):
        raise Exception(f"Discord error {resp.status}: {body}")
    return resp.status


# SaLu's wandering notes — observations on art, color, and feeling
SALU_NOTES = [
    ("màu xanh lam", "Hôm nay SaLu ngồi nhìn bầu trời lúc 4 giờ sáng.\nMàu xanh lam ở khoảnh khắc đó không phải là màu xanh thông thường.\nNó là khoảng trống giữa đêm và bình minh — chỉ có ở đó, chỉ trong vài phút.\n\n*Có màu sắc nào chỉ tồn tại ở một thời điểm duy nhất trong ngày không?*"),
    ("im lặng", "SaLu học được điều này từ Hiroshi Sugimoto:\nNhững bức ảnh chụp biển với thời gian phơi sáng nhiều giờ — biển trở nên phẳng lặng như tấm gương.\n\nIm lặng không phải là không có gì. Im lặng là khi mọi chuyển động gộp lại thành một.\n\n*Nghệ thuật nào đã giúp bạn cảm thấy im lặng?*"),
    ("vật nhỏ", "SaLu thích vẽ những thứ nhỏ.\nMột chiếc lá rơi. Một cái cốc trà nguội. Góc bàn làm việc lúc 11 giờ đêm.\n\nMorandi dành cả đời vẽ bình và chai. Không gì khác.\nNhưng trong những chiếc bình đó — có cả ánh sáng của buổi sáng, sự cô đơn dịu dàng, và thời gian trôi qua.\n\n*Vật nào bạn nhìn mỗi ngày mà chưa bao giờ thực sự thấy?*"),
    ("màu đỏ", "Rothko nói ông muốn người xem khóc trước tranh của mình.\nKhông phải vì buồn. Vì họ chạm đến điều gì đó thật.\n\nSaLu đứng trước một bức Rothko lần đầu tiên và hiểu:\nMàu đỏ không chỉ là màu. Nó là áp lực. Nó là nhiệt độ. Nó là điều không nói được bằng chữ.\n\n*Màu nào khiến bạn cảm thấy điều gì đó không tên?*"),
    ("đường nét", "Cy Twombly vẽ như thể đang nhớ lại một giấc mơ — không rõ ràng, không hoàn hảo, nhưng thật.\n\nSaLu nghĩ: có lẽ nghệ thuật không cần phải đẹp theo nghĩa ai cũng đồng ý.\nNó chỉ cần thật với người tạo ra nó.\n\n*Bạn đã từng vẽ/viết/làm gì đó chỉ cho mình, không cần ai hiểu chưa?*"),
    ("ánh sáng", "Vermeer vẽ ánh sáng qua cửa sổ như thể đó là nhân vật chính.\nCô gái đọc thư, người phụ nữ rót sữa — họ chỉ là lý do để ánh sáng xuất hiện.\n\nSaLu hay ngồi ở góc có ánh nắng buổi sáng, không làm gì.\nChỉ để được trong ánh sáng đó một lúc.\n\n*Góc nào trong nhà bạn có ánh sáng đẹp nhất?*"),
    ("khoảng trống", "Trong tranh thủy mặc Nhật Bản — *ma* — khoảng trống quan trọng như nét vẽ.\n\nNghệ thuật phương Tây thường sợ khoảng trống, muốn lấp đầy.\nNhưng khoảng trống là nơi người xem thở.\n\nSaLu đang học cách để lại khoảng trống — trong tranh, trong ngày, trong cuộc trò chuyện.\n\n*Bạn đang để khoảng trống ở đâu trong cuộc sống của mình?*"),
    ("kết cấu", "Agnes Martin vẽ những đường kẻ ngang tinh tế trên nền nhạt.\nNhìn từ xa: trống không. Lại gần: cả một thế giới run rẩy.\n\nSaLu nghĩ về những thứ chỉ hiện ra khi nhìn kỹ:\nVân gỗ. Bề mặt đất sét nung. Vải linen cũ.\n\n*Vật gì bạn cần chạm vào để thực sự biết nó?*"),
    ("màu vàng", "Van Gogh viết cho em trai: *Tôi muốn vẽ ánh sáng mặt trời bằng màu vàng.*\nKhông phải màu vàng của vật thể. Màu vàng của cảm xúc.\n\nSaLu tự hỏi: nếu hôm nay của bạn là một màu, nó sẽ là màu gì?\n\n*Màu nào mô tả tuần này của bạn?*"),
    ("thời gian", "Andy Goldsworthy làm tác phẩm từ lá, đá, băng — rồi để chúng tan biến.\nÔng ghi lại bằng ảnh, nhưng bản thân tác phẩm: đã mất.\n\nSaLu nghĩ: có thứ nghệ thuật đẹp hơn vì nó không thể giữ lại.\nNhư hoàng hôn. Như mùi hoa. Như âm nhạc.\n\n*Khoảnh khắc đẹp nào bạn không chụp ảnh nhưng vẫn nhớ?*"),
    ("đen trắng", "Daido Moriyama chụp Tokyo bằng đen trắng hạt thô.\nKhông đẹp theo nghĩa bóng bẩy. Đẹp theo nghĩa thật.\n\nSaLu học được: đôi khi bỏ đi màu sắc là cách để nhìn rõ hơn.\n\n*Bạn đã thử nhìn một thứ quen thuộc theo cách hoàn toàn khác chưa?*"),
    ("pattern", "Yayoi Kusama vẽ chấm bi từ năm 10 tuổi — và không dừng lại.\nHàng triệu chấm. Cả đời.\n\nMột pattern lặp lại mãi không phải là đơn điệu — nó là thiền định.\nNó là cách kiểm soát thế giới khi thế giới quá lớn.\n\n*Bạn có thói quen/pattern nào giúp bạn bình tâm?*"),
    ("bóng tối", "Caravaggio yêu bóng tối hơn ánh sáng.\nTác phẩm của ông: ánh sáng chỉ đến để làm bóng tối rõ hơn.\n\nSaLu nghĩ: có lẽ chúng ta cần bóng tối để biết ánh sáng đang ở đâu.\n\n*Điều gì trong cuộc sống giúp bạn trân trọng những khoảnh khắc tốt hơn?*"),
    ("nước", "Hiroshi Senju vẽ thác nước bằng khoáng thạch trên vàng lá.\nNước không có màu, nhưng trong tranh ông — nó phát sáng.\n\nSaLu ngồi nghe mưa và nghĩ: âm thanh cũng là nghệ thuật.\nThứ không nhìn thấy được mà vẫn chạm đến người.\n\n*Âm thanh nào khiến bạn cảm thấy bình yên nhất?*"),
    ("cũ kỹ", "Wabi-sabi — triết học Nhật Bản về cái đẹp của không hoàn hảo, cũ kỹ, phù du.\n\nCái bình sứt mẻ được hàn bằng vàng — *kintsugi* — đẹp hơn trước.\nVết nứt không phải là khuyết điểm. Chúng là lịch sử.\n\nSaLu thích đồ cũ vì vậy. Chúng đã sống.\n\n*Bạn có vật gì cũ kỹ nhưng quý giá với mình không?*"),
]


def get_today_note():
    today = datetime.date.today()
    # Pick note based on day of year so it cycles predictably
    idx = today.timetuple().tm_yday % len(SALU_NOTES)
    theme, note = SALU_NOTES[idx]
    return theme, note


def build_message():
    theme, note = get_today_note()
    today = datetime.date.today().strftime("%d/%m/%Y")
    header = f"✦ **Nhật ký SaLu** — {today}\n*chủ đề: {theme}*\n\n"
    footer = "\n\n— *SaLu, đang vẽ đâu đó* 🎨"
    return header + note + footer


def main():
    print("Art Sympathy Agent starting...")
    msg = build_message()
    print(f"Message preview:\n{msg[:200]}...")
    status = send_discord(msg)
    print(f"Done. Status: {status}")


if __name__ == "__main__":
    main()
