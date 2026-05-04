# ZDI-21-908: Adobe Prelude MP4 File Parsing Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-908
- **ZDI-CAN:** ZDI-CAN-13735
- **Date:** 2021-07-28
- **CVE:** CVE-2021-36007
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Prelude
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-908/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Prelude. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/prelude/apsb21-58.html

## Disclosure Timeline

- 2021-04-30 - Vulnerability reported to vendor
- 2021-07-28 - Coordinated public release of advisory
