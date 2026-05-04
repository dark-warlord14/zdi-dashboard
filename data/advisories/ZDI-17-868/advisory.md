# ZDI-17-868: Foxit Reader XFAScriptObject insert Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-868
- **ZDI-CAN:** ZDI-CAN-5016
- **Date:** 2017-11-14
- **CVE:** CVE-2017-14824
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-868/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the insert method of XFAScriptObject objects. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2017-11-14 - Coordinated public release of advisory
