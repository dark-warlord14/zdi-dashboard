# ZDI-18-755: Foxit PhantomPDF PDF Parsing Shading Pattern Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-755
- **ZDI-CAN:** ZDI-CAN-6223
- **Date:** 2018-07-19
- **CVE:** CVE-2018-14295
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-755/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF documents. When parsing shading patterns, the process does not properly validate user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-07-19 - Coordinated public release of advisory
- 2018-07-19 - Advisory Updated
