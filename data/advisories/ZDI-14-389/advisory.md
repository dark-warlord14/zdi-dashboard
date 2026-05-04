# ZDI-14-389: ARRIS VAP2500 Management Portal Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-389
- **ZDI-CAN:** ZDI-CAN-2137
- **Date:** 2014-11-25
- **CVE:** CVE-2014-8423
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ARRIS
- **Affected Products:** VAP2500
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-389/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ARRIS VAP2500. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of access to the management portal. The issue lies in the ability to execute arbitrary commands without any sanitization. An attacker can leverage this vulnerability to execute code with root privileges.

## Additional Details

Vendor has released a hotfix to address the issue: FW08.41

## Disclosure Timeline

- 2014-04-29 - Vulnerability reported to vendor
- 2014-11-25 - Coordinated public release of advisory
