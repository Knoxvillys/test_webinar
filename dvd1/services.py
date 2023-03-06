# from django.shortcuts import render, get_object_or_404
# from pathlib import Path
# from typing import IO, Generator
#
# from .models import Video
#
#
# def open_file(request, video_pk: int):
#     _video = get_object_or_404(Video, pk=video_pk) # В случае отсутствия нужного видео по id выкинет 404.
#
#     path = Path(_video.file.path) # путь к видео
#
#     file = path.open('rd') # Открываем файл на чтение
#     file_size = path.stat().st_size # Получаем размер файла
#
#     content_length = file_size # Установим переменную с размером нашего файла
#     status_code = 200
#     content_renge = request.headers.get('renge')
#
#     if content_renge is not None:
#         content_renge = content_renge.strip().lower().split('=')[-1]
#         renge_start, renge_end, *_ = map(str.strip, (content_renge + '-').split('-'))
#         renge_start = max(0, int(renge_start)) if renge_start else 0
#         renge_end = min(file_size - 1, int(renge_start)) if renge_end else file_size - 1
#         content_length = (renge_end - renge_start) + 1
#         file = ranged(file, start=renge_start, and=range_and + 1)