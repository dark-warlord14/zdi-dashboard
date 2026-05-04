# ZDI-16-426: Adobe Flash StyleSheet Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-426
- **ZDI-CAN:** ZDI-CAN-3744
- **Date:** 2016-07-12
- **CVE:** CVE-2016-4174
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Kai Kang (a.k.a 4B5F5F4B)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-426/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the StyleSheet objects. By calling the parseCSS method of the StyleSheet object from within a specific callback function, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-25.html

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
