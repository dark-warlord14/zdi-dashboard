# ZDI-16-468: Foxit Reader TIFF Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-468
- **ZDI-CAN:** ZDI-CAN-3919
- **Date:** 2016-08-10
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** 5206560A306A2E085A437FD258EB57CE
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within TIFF Parsing. The process does not properly validate user-supplied data which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-07-27 - Vulnerability reported to vendor
- 2016-08-10 - Coordinated public release of advisory
