# ZDI-21-1094: Adobe FrameMaker PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1094
- **ZDI-CAN:** ZDI-CAN-14372
- **Date:** 2021-09-16
- **CVE:** CVE-2021-40697
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1094/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe FrameMaker. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/framemaker/apsb21-74.html

## Disclosure Timeline

- 2021-07-02 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
