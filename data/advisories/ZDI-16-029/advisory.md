# ZDI-16-029: Foxit Reader GpRuntime::GpLock::GpLock Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-029
- **ZDI-CAN:** ZDI-CAN-3251
- **Date:** 2016-01-25
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Foxit uses the Gdiplus API. A specially crafted PDF can force a dangling pointer to be reused after it has been freed in GpRuntime::GpLock::GpLock. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2015-12-04 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
