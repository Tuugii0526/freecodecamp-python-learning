---
title: "04 avoid inferring the response MIME"
date: 2025-07-14
---

# 04 avoid inferring the response MIME

browser нь сэрвэрээс ирж байгаа дата заасан content-type аас өөр тохиолдолд үүнийг харуулдаг . Энэ нь амар болох ч эмзэг байдал үүсгэнэ .
Үүүнээс сэргийлээд `X-Content-Type-Options: nosniff` header ийг сэрвэрээс өгвөл browser яг өгнө гэсэн төрлийн датаг л хүлээж байдаг .
