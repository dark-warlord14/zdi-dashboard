# ZDI-15-016: Microsoft Internet Explorer TransNavContext Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-016
- **ZDI-CAN:** ZDI-CAN-2305
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0031
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of TransNavContext objects after they have been freed. With control of the freed memory, an attacker may leverage specific instructions to modify memory. An attacker can leverage this vulnerability to leak information within the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-05-08 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
