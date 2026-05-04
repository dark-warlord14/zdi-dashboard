# ZDI-17-893: Foxit Reader clearItems Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-893
- **ZDI-CAN:** ZDI-CAN-5288
- **Date:** 2017-11-14
- **CVE:** CVE-2017-16582
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-893/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the clearItems XFA method. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2017-10-11 - Vulnerability reported to vendor
- 2017-11-14 - Coordinated public release of advisory
