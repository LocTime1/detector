from PIL import Image, ImageDraw


def draw_map(start, finish):
    anomaly_pwr = {"5b6eb38b": ((24, 21), 60, 5.5),
                   "c00b92ba": ((24, 13), 60, 5.5),
                   "931ede7b": ((13, 4), 60, 5.0),
                   "661c2e66": ((22, 19), 50, 5.9),
                   "c2958c11": ((27, 4), 70, 5.9),
                   "08d55d4f": ((19, 22), 70, 5.9)}
    filename = "static/map.png"
    with Image.open(filename) as img:
        img.load()
        draw = ImageDraw.Draw(img)
    draw.rectangle([(start[0] * 50), (start[1] * 50), (start[0] + 1) * 50, (start[1] + 1) * 50], fill=(98, 99, 155))
    draw.rounded_rectangle([(finish[0] * 50), (finish[1] * 50), (finish[0] + 1) * 50, (finish[1] + 1) * 50],
                           fill=(98, 99, 155))
    draw.ellipse([(24 * 50 - (5.5 * 50)), (21 * 50 - (5.5 * 50)), (24 * 50 + (5.5 * 50)), (21 * 50 + (5.5 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(24 * 50 - 25), (21 * 50 - 25), (24 * 50 + 25), (21 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.ellipse([(24 * 50 - (5.5 * 50)), (13 * 50 - (5.5 * 50)), (24 * 50 + (5.5 * 50)), (13 * 50 + (5.5 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(24 * 50 - 25), (13 * 50 - 25), (24 * 50 + 25), (13 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.ellipse([(13 * 50 - (5.0 * 50)), (4 * 50 - (5.0 * 50)), (13 * 50 + (5.0 * 50)), (4 * 50 + (5.0 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(13 * 50 - 25), (4 * 50 - 25), (13 * 50 + 25), (4 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.ellipse([(22 * 50 - (5.9 * 50)), (19 * 50 - (5.9 * 50)), (22 * 50 + (5.9 * 50)), (19 * 50 + (5.9 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(22 * 50 - 25), (19 * 50 - 25), (22 * 50 + 25), (19 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.ellipse([(27 * 50 - (5.9 * 50)), (4 * 50 - (5.9 * 50)), (27 * 50 + (5.9 * 50)), (4 * 50 + (5.9 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(27 * 50 - 25), (4 * 50 - 25), (27 * 50 + 25), (4 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.ellipse([(19 * 50 - (5.9 * 50)), (22 * 50 - (5.9 * 50)), (19 * 50 + (5.9 * 50)), (22 * 50 + (5.9 * 50))],
                 outline=(72, 6, 7), width=5)
    draw.ellipse([(19 * 50 - 25), (22 * 50 - 25), (19 * 50 + 25), (22 * 50 + 25)], fill=(72, 6, 7), width=5)
    draw.rectangle([(9 * 50), (9 * 50), (9 + 1) * 50, (9 + 1) * 50], fill=(172, 183, 142))
    draw.rectangle([(33 * 50), (9 * 50), (33 + 1) * 50, (9 + 1) * 50], fill=(172, 183, 142))
    draw.rectangle([(9 * 50), (23 * 50), (9 + 1) * 50, (23 + 1) * 50], fill=(172, 183, 142))
    draw.rectangle([(32 * 50), (22 * 50), (32 + 1) * 50, (22 + 1) * 50], fill=(172, 183, 142))

    img2 = img.resize((700, 490))
    img2.save('static/map_2.png')
