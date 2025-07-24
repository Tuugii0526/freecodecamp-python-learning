---
title: "clickjacking"
date: 2025-07-12
---

# clickjacking

Хэрэглэгчийн вэбсайтыг iframe оруулан css ээр style өгөн дарах ёсгүй товчийг даруулдаг hacker ажээ .
Ийм байлаа гэж бодоход :
[Анхны байрлал](./static/click-jack-ex.png)
`Transfer all money ` хэмээх товчин дээр iframe ашиглан даруулах ажээ . Энэхүү халдлагыг clickjack хэмээдэг .
Эдгээрд 2 арга авж болно:

1. The frame-ancestors directive in a content security policy
2. The X-Frame-Options response header.

Express server :

```
const express=require('express')
const helmet=require('helmet')
const app=express()
app.use(helmet.frameguard({action:'deny'}))
```

Тэгвэл бид үүнийг вэбсайт дээр бас хийх ёстой юу ?

## Эх сурвалжууд

1.  j
