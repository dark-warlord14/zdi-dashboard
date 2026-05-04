# ZDI-18-1095: Foxit PhantomPDF fxhtml2pdf HTML Conversion Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1095
- **ZDI-CAN:** ZDI-CAN-6230
- **Date:** 2018-09-28
- **CVE:** CVE-2018-17706
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** bit - MeePwn team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within fxhtml2pdf. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-05-16 - Vulnerability reported to vendor
- 2018-09-28 - Coordinated public release of advisory
- 2018-09-28 - Advisory Updated
