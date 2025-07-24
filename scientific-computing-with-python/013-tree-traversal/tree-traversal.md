---
title: Модоор аялах
date: 2025-6-7
---

# Модоор аялах программ

1. Сонсох тэмдэглэл
   Шинээр key нэмэхэд зангилаан доороос нэмэгдэнэ .
   Аль нэг устгахад бүгдээрээ шинэчлэгдэнэ .
2. Хэрхэн зангилаа устгах вэ ?
   Доорх нь 0 болон 1 хүүхэдтэй зангилаанд тохирно хэмээлээ .

   ```
   if node is None:
      return node
   if key < node.key:
      node.left= self._delete(node.left,key)
   elif key > node.key:
      node.right= self._delete(node.right,key)
   ```

   2 хүүхэдтэй зангилаанд яах вэ?
