# ZDI-16-631: Apple Safari RenderObject Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-631
- **ZDI-CAN:** ZDI-CAN-4010
- **Date:** 2016-12-13
- **CVE:** CVE-2016-7610
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Zheng Huang of the Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-631/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RenderObject objects. By performing actions in JavaScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207421

## Disclosure Timeline

- 2016-09-06 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
