# ZDI-23-074: Adobe InCopy Font Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-074
- **ZDI-CAN:** ZDI-CAN-18889
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21598
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** InCopy
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-074/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe InCopy. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of embedded fonts. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/incopy/apsb23-08.html

## Disclosure Timeline

- 2022-09-22 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
