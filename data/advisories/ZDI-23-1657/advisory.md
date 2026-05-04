# ZDI-23-1657: Adobe Audition MP4 File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1657
- **ZDI-CAN:** ZDI-CAN-21685
- **Date:** 2023-11-15
- **CVE:** CVE-2023-47047
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Audition
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1657/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Audition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/audition/apsb23-64.html

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
