# ZDI-16-343: (Pwn2Own) Apple Safari ArrayStorage DFG Optimization Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-343
- **ZDI-CAN:** ZDI-CAN-3619
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1857
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Liang Chen of KeenLab Tencent Zhen Feng of KeenLab Tencent wushi of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-343/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ArrayBuffer objects. By triggering certain JavaScript optimizations, an attacker can force an ArrayBuffer in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206568

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
