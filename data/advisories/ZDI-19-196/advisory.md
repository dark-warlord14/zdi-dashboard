# ZDI-19-196: Microsoft Windows EMF File Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-196
- **ZDI-CAN:** ZDI-CAN-7560
- **Date:** 2019-02-12
- **CVE:** CVE-2019-0615
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-196/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of EMF graphics. Crafted data in an EMF graphic can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0615

## Disclosure Timeline

- 2018-11-27 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
