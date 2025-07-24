---
title: "security headers"
date: 2025-07-13
---

# security headers

## what are http headers ?

http хүсэлт хариултаар дамжуулан нэмэлт дата дамжуулахад үүнийг ашигладаг .

## what are security headers ?

Аюулгүй ажилгааг хангах зорилготой http headers ийг хэлнэ .

Security headers :

1. Content security policy
   Баттай эх сурвалжуудыг зааж өгөхөд ашигладаг .

   ```
   script-src	The most important one. Defines valid sources for JavaScript.
   style-src	Defines valid sources for CSS stylesheets.
   img-src	Defines valid sources for images.
   font-src	Defines valid sources for web fonts.
   connect-src	Restricts URLs that can be loaded using APIs like fetch() or XMLHttpRequest.
   frame-src	Restricts URLs that can be embedded as frames (<iframe>).
   frame-ancestors	Specifies which sites can embed the current page, preventing clickjacking.
   default-src	A fallback directive for any other directive that isn't explicitly defined.
   ```

   Дээр харагдаж байгаачлан `script-src` нь javascript баттай эх сурвалж авах газрыг заахад ашиглана . `style-src` нь `style` ийг авах баттай эх сурвалжыг заахад ашиглана . гэх мэт ажээ .
   [nextjs config](./static/content-security-policy-nextjs-config.png)
   [nextjs result](./static/content-security-policy-nextjs-result.png)

2. X-Frame-Options header
   `iframe` , `frame`,`embed` эсвэл `object` хэмээх тагуудад тухайн вэбсайт харуулагдах боломжтой эсэхийг заахад ашигладаг .
3. Permission policy header
   Аль browser api ашиглахыг заахад ашигладаг .
   Жишээ нь , camera , geolocation гэх мэт .
4. Referrer policy
   Та `page A` аас `page B` рүү үсэрхэд `page B` тантай холбоотой мэдүүллүүд хадгалагддаг . Хэрвээ `page A` ийн url д хэрэглэгчийн нэр , чухал мэдээлэл байсан бол энэ нь биднийг аюулд хүргэх магадлалтай .
   Бид referrer-policy д `strict-origin-when-cross-origin` тавьснаар зөвхөн same-origin вэбсайтууд дээр л url хамт явна , бусад тохиолдолд origin эсвэл http байвал хүсэлт явахгүй гэдгийг хэлж байгаа .

## Эх сурвалжууд

[GeeksForGeeks](https://www.geeksforgeeks.org/nextjs/next-js-security-headers/)
