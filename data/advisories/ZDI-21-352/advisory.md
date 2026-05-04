# ZDI-21-352: Foxit PhantomPDF JPEG2000 Parsing Out-Of Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-352
- **ZDI-CAN:** ZDI-CAN-12230
- **Date:** 2021-03-22
- **CVE:** CVE-2021-27270
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** cece
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-352/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG2000 images. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-03-22 - Coordinated public release of advisory
