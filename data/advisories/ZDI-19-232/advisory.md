# ZDI-19-232: Tencent WeChat URL Scheme Handling Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-232
- **ZDI-CAN:** ZDI-CAN-6996
- **Date:** 2019-02-28
- **CVE:** N/A
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Tencent
- **Affected Products:** Wechat
- **Credit:** lilang wu, moony Li and yuchen zhou of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-232/
## Vulnerability Details

This vulnerability allows local attackers to modify requests on vulnerable installations of Tencent WeChat. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of URL schemes. The issue resides in the improper validation if a URL Scheme was acted upon by a malicious application. An attacker can leverage this vulnerability to steal tokens and manipulate requests in the context of current user.

## Additional Details

This issue was resolved and fixed on the server side. Hence, no patch version number is available.

## Disclosure Timeline

- 2018-07-30 - Vulnerability reported to vendor
- 2019-02-28 - Coordinated public release of advisory
