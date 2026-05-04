# ZDI-21-1587: Adobe Premiere Rush MP4 File Parsing Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1587
- **ZDI-CAN:** ZDI-CAN-15278
- **Date:** 2021-12-21
- **CVE:** CVE-2021-43030
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Premiere Rush
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1587/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Premiere Rush. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/premiere_rush/apsb21-101.html

## Disclosure Timeline

- 2021-09-15 - Vulnerability reported to vendor
- 2021-12-21 - Coordinated public release of advisory
