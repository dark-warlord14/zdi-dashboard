# ZDI-17-054: Apple Safari SearchInputType Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-054
- **ZDI-CAN:** ZDI-CAN-4121
- **Date:** 2017-01-24
- **CVE:** CVE-2017-2354
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Neymar of Tencent's Xuanwu LAB(http://www.tencent.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within SearchInputType objects. The issue results from the lack of proper validation of user-supplied data which can result in a type confusion condition. An attacker can leverage this vulnerability to achieve remote code execution under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2016-11-10 - Vulnerability reported to vendor
- 2017-01-24 - Coordinated public release of advisory
