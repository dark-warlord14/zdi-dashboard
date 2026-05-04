# ZDI-15-643: Foxit Reader Will Print Action Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-643
- **ZDI-CAN:** ZDI-CAN-3311
- **Date:** 2015-12-16
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-643/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Will Print document action. A specially crafted Will Print action can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2015-12-16 - Coordinated public release of advisory
