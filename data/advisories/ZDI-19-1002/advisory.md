# ZDI-19-1002: Microsoft Windows Media Player Color Transform Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1002
- **ZDI-CAN:** ZDI-CAN-8029
- **Date:** 2019-12-11
- **CVE:** CVE-2019-1480
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1002/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AVI files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1480

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2019-12-11 - Coordinated public release of advisory
