def starrating(score, max_score=10, max_star=5, color=False):
    star_count = round(score / max_score * max_star)
    if color:
        # Renkli yıldızlar
        return "\033[1;33m★" * star_count + "\033[0m" + "☆" * (max_star - star_count)
    else:
        # Normal siyah yıldızlar
        return "★" * star_count + "☆" * (max_star - star_count)

def main():
    try:
        userinput = input("Okuduğun kitap için 0-10 arasında bir sayısal puan girebilir misin?: ")
        score = float(userinput)

        if score < 0 or score > 10:
            print("Lütfen 0 ile 10 arasında bir değer girebilir misin.")
        else:
            star_rating = starrating(score, color=True)
            print("Yıldız puanlaması:", star_rating)
    except ValueError:
        print("Lütfen geçerli bir sayı girebilir misin?")

if __name__ == '__main__':
    main()
