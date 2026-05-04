# ZDI-20-994: Microsoft Windows findBaseLigature TTF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-994
- **ZDI-CAN:** ZDI-CAN-10812
- **Date:** 2020-08-13
- **CVE:** CVE-2020-1577
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-994/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TTF files by GDI routines. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1577

## Disclosure Timeline

- 2020-04-30 - Vulnerability reported to vendor
- 2020-08-13 - Coordinated public release of advisory
