import pandas as pd
from scipy.stats import ttest_ind

def website_analyse(file_path):
    df = pd.read_csv(file_path)
    
    mean_pages = df['Просмотренные страницы'].mean()
    print(f"1) Среднее количество просмотренных страниц: {mean_pages}")
    
    std_time = df['Время на сайте (сек)'].std()
    print(f"2) Стандартное отклонение: {std_time}")
    
    mean_time = df['Время на сайте (сек)'].mean()
    cv = std_time / mean_time
    
    if cv > 0.25:
        variability = "Высокая вариабельность"
    elif cv > 0.1:
        variability = "Умеренная вариабельность"
    else:
        variability = "Слабая вариабельность"
    
    print(f"3) {variability}: {cv}")
    
    mobile = df[df['Тип устройства'] == 'Мобильное']['Просмотренные страницы']
    desktop = df[df['Тип устройства'] == 'Десктоп']['Просмотренные страницы']
    
    _, p_value = ttest_ind(mobile, desktop, equal_var=False)
    
    if p_value < 0.05:
        result = "Есть статистически значимая разница в количестве страниц"
    else:
        result = "Нет статистически значимой разницы"
    
    print(f"4) {result}: {p_value}")
