# ZDI-14-329: Sophos Cyberoam add_guest_user Blind SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-329
- **ZDI-CAN:** ZDI-CAN-2331
- **Date:** 2014-10-01
- **CVE:** CVE-2014-5503
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:C
- **Affected Vendors:** Sophos
- **Affected Products:** Cyberoam
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-329/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary SQL on vulnerable installations of Sophos Cyberoam. Authentication is not required to exploit this vulnerability. The specific flaw exists within the add_guest_user opcode. The issue lies in the failure to properly sanitize the specified mobile number prior to executing a SQL query. A remote attacker can leverage this vulnerability to disclose credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://kb.cyberoam.com/default.asp?id=3049&Lang=1&SID

## Disclosure Timeline

- 2014-06-04 - Vulnerability reported to vendor
- 2014-10-01 - Coordinated public release of advisory
