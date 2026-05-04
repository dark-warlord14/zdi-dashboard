# ZDI-23-310: Adobe Dimension USD File Parsing Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-310
- **ZDI-CAN:** ZDI-CAN-19467
- **Date:** 2023-03-16
- **CVE:** CVE-2023-26344
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Dimension
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-310/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Dimension. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of USD files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/dimension/apsb23-20.html

## Disclosure Timeline

- 2022-11-09 - Vulnerability reported to vendor
- 2023-03-16 - Coordinated public release of advisory
