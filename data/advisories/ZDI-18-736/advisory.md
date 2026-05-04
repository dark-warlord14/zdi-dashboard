# ZDI-18-736: Foxit Reader submitForm Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-736
- **ZDI-CAN:** ZDI-CAN-6039
- **Date:** 2018-07-19
- **CVE:** CVE-2018-14276
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** nsfocus security team.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-736/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the submitForm method. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-04-03 - Vulnerability reported to vendor
- 2018-07-19 - Coordinated public release of advisory
- 2018-07-19 - Advisory Updated
