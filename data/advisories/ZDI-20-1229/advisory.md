# ZDI-20-1229: Foxit PhantomPDF U3DBrowser U3D Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1229
- **ZDI-CAN:** ZDI-CAN-11190
- **Date:** 2020-09-29
- **CVE:** CVE-2020-17411
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1229/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of U3D objects embedded in PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2020-06-03 - Vulnerability reported to vendor
- 2020-09-29 - Coordinated public release of advisory
- 2020-10-09 - Advisory Updated
