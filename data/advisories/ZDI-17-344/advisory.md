# ZDI-17-344: Apple Safari RenderLayer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-344
- **ZDI-CAN:** ZDI-CAN-4519
- **Date:** 2017-05-15
- **CVE:** CVE-2017-2525
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Kai Kang(a.k.a 4B5F5F4B) of Tencent's Xuanwu LAB(http://www.tencent.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-344/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RenderLayer objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207798

## Disclosure Timeline

- 2017-03-09 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
