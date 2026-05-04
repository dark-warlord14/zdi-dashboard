# ZDI-22-1583: SAP 3D Visual Enterprise Author PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1583
- **ZDI-CAN:** ZDI-CAN-18220
- **Date:** 2022-11-03
- **CVE:** CVE-2022-41181
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Author
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1583/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of SAP 3D Visual Enterprise Author. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. Crafted data in a PDF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://www.sap.com/documents/2022/02/fa865ea4-167e-0010-bca6-c68f7e60039b.html

## Disclosure Timeline

- 2022-08-04 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
