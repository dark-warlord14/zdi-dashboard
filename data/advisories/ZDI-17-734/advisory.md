# ZDI-17-734: Microsoft Windows Uniscribe Bidirectional Text Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-734
- **ZDI-CAN:** ZDI-CAN-4845
- **Date:** 2017-09-12
- **CVE:** CVE-2017-8692
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-734/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of Bidirectional Text. Crafted data in a file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8692

## Disclosure Timeline

- 2017-06-01 - Vulnerability reported to vendor
- 2017-09-12 - Coordinated public release of advisory
