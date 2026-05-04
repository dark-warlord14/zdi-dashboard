# ZDI-17-042: Foxit PhantomPDF ConvertToPDF TIFF Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-042
- **ZDI-CAN:** ZDI-CAN-4327
- **Date:** 2017-01-11
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Juan Pablo Lopez Yacubian
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ConvertToPDF's TIFF parsing. The issue results from the lack of proper validation of user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-12-01 - Vulnerability reported to vendor
- 2017-01-11 - Coordinated public release of advisory
