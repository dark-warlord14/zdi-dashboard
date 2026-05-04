# ZDI-14-332: Sophos Cyberoam webclient_portal_settings Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-332
- **ZDI-CAN:** ZDI-CAN-2328
- **Date:** 2014-10-01
- **CVE:** CVE-2014-5502
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Sophos
- **Affected Products:** Cyberoam
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-332/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sophos Cyberoam. Authentication is required to exploit this vulnerability. The specific flaw exists within the webclient_portal_settings opcode. The issue lies in the failure to properly sanitize user-supplied input before executing commands. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://kb.cyberoam.com/default.asp?id=3049&Lang=1&SID

## Disclosure Timeline

- 2014-06-04 - Vulnerability reported to vendor
- 2014-10-01 - Coordinated public release of advisory
