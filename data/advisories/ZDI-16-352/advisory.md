# ZDI-16-352: (Pwn2Own) Apple Safari GraphicsContext Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-352
- **ZDI-CAN:** ZDI-CAN-3610
- **Date:** 2016-05-20
- **CVE:** CVE-2016-1859
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Liang Chen and wushi of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-352/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of GraphicsContext objects. By manipulating a document's elements an attacker can force this object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206568

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-20 - Coordinated public release of advisory
