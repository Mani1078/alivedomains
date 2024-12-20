import requests

def check_alive_domains(input_file, output_file):
    # خواندن دامین‌ها از فایل ورودی
    with open(input_file, 'r') as file:
        domains = file.readlines()

    alive_domains = []

    for domain in domains:
        domain = domain.strip()  # حذف فاصله‌های اضافی

        # تلاش برای ارسال درخواست HTTP به دامین
        try:
            response = requests.get(f'https://{domain}', timeout=5)
            # اگر کد وضعیت 200 باشد، دامین زنده است
            if response.status_code == 200:
                alive_domains.append(domain)
        except requests.exceptions.RequestException:
            # اگر درخواست موفقیت‌آمیز نبود، دامین را رد می‌کنیم
            continue

    # نوشتن دامین‌های زنده در فایل خروجی
    with open(output_file, 'w') as file:
        for domain in alive_domains:
            file.write(domain + '\n')

# استفاده از تابع
check_alive_domains('domains.txt', 'alive.txt')
