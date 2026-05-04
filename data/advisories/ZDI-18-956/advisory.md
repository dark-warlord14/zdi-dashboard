# ZDI-18-956: Microsoft Windows EMF File Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-956
- **ZDI-CAN:** ZDI-CAN-6588
- **Date:** 2018-08-30
- **CVE:** CVE-2018-8394
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lin Wang of Beihang University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-956/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of EMF graphics. Crafted data in an EMF graphic can trigger a read past the end of a data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8394

## Disclosure Timeline

- 2018-07-10 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
