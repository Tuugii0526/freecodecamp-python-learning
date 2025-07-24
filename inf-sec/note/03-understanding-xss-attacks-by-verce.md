---
title: "03 understanding xss attacks by verce"
date: 2025-07-14
---

# 03 understanding xss attacks by vercel

1. Хэрэглэгчийн оролтыг хянаагүй вэб хуудас нь өөрөө xss ийн эмзэг байдалтай болно. Хакер input ээр дамжуулан script оруулах бөгөөд эргээд энэхүү script ийг харуулах үед script ийн код ажиллан session cookie зэрэг мэдээллийг хакерчиний вэб сервер луу явуулдаг .

## Ямар төрлийн xss халдлага байдаг вэ ?

1. Dom-based xss

```
<div id="content">Default content</div>
<script>
   const params = new URLSearchParams(window.location.search);
   document.getElementById('content').innerHTML = params.get('message');
</script>
```

If a user visits a link like http://example.com/index.html?message=<script>alert('Hacked!')</script>, the malicious script would run.

2. Reflected XSS
   Хэрэглэгчийн input ээр дамжуулан халдлага хийдэг . Бид яг сайн ойлгосонгүй . Доор дэлгэрэнгүй тайлбар байна .
   This attack occurs when a malicious script provided by an attacker is reflected off a web server, such as through a search result or error message, and executed immediately without being stored.

Reflected XSS typically requires some form of social engineering, as the victim must be tricked into clicking a specially crafted link that contains the malicious payload. Once the link is clicked, the payload is sent to the vulnerable website which then reflects the attack back to the user's browser, where the malicious script is executed. Due to its non-persistent nature, the attack happens in real time and doesn't affect other users of the site.

Imagine a simple search feature on a website that displays the search query back to the user. If the website fails to properly sanitize the query parameter before reflecting its content back on the page, the script will execute, resulting in an XSS attack.

<div>        
  <!-- Vulnerable Code: Reflects the user input directly without sanitization -->        
  You searched for: <span id="search-result"></span>    
</div>

<script>       
  // Get the query parameter from the URL        
  const params = new URLSearchParams(window.location.search);
  const query = params.get('query');

   // Reflect the query directly into the page (vulnerable!)        
  document.getElementById('search-result').innerHTML = query;
</script>

If a user inputs a script instead of an ID, it'll execute on the browser, leading to a Reflected XSS attack.

3. Stored xss
   Датабазад хортой хадгалагдана гэсэн үг .Энэ нь датабазаас дата авах үед хортой явна гэсэн үг . Хэрэглэгчид датагаа харуулах гэтэл манай хортой код ажиллана гэсэн үг .

## Preventing XSS attacks

1.  Reject unexpected inputs
2.  Validate and sanitize user inputs - use an library like DomPurify .

    [vercel source](https://vercel.com/guides/understanding-xss-attacks)

3.  avoid inline scripts and inline script handlers
4.  set a csp
5.  avoid using dangerouslySetInnerHtml
6.  httpOnly and Secure attributes on cookies
7.  be cautious with third party libraries

Дүгнэхэд :

1. Хэрэглэгчийн оролтонд итгэж болохгүй ажээ .

Бид түрүүнд олон гайхалтай эх сурвалжуудтай таарлаа .
https://portswigger.net/daily-swig/prototype-pollution-the-dangerous-and-underrated-vulnerability-impacting-javascript-applications
https://portswigger.net/daily-swig/javascript
https://owasp.org/www-community/attacks/xss/
https://portswigger.net/web-security/all-topics
