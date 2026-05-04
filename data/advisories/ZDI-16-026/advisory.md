# ZDI-16-026: Foxit PhantomPDF WillClose Action Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-026
- **ZDI-CAN:** ZDI-CAN-3493
- **Date:** 2016-01-25
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the WillClose action. A specially crafted PDF with a WillClose action can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
