# ZDI-15-524: Foxit Reader Forms Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-524
- **ZDI-CAN:** ZDI-CAN-3267
- **Date:** 2015-10-19
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-524/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within PDF Forms. A specially crafted PDF file can force Foxit Reader to read memory past the end of an allocated object. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2015-10-19 - Coordinated public release of advisory
