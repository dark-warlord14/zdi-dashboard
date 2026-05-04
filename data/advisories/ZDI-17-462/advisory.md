# ZDI-17-462: (Pwn2Own) Google Chrome Array indexOf Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-462
- **ZDI-CAN:** ZDI-CAN-4587
- **Date:** 2017-07-10
- **CVE:** CVE-2017-5053
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Tencent Security Team Sniper
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-462/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Array.prototype.indexOf method. By performing actions in JavaScript, an attacker can trigger a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2017/03/stable-channel-update-for-desktop_29.html

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-10 - Coordinated public release of advisory
