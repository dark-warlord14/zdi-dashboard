# ZDI-17-241: Apple Safari RenderBox Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-241
- **ZDI-CAN:** ZDI-CAN-4452
- **Date:** 2017-03-30
- **CVE:** CVE-2017-2463
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Kai Kang(a.k.a 4B5F5F4B) of Tencent's Xuanwu LAB(http://www.tencent.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-241/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within RenderBox objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to achieve remote code execution under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-01-20 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
