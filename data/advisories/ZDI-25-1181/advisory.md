# ZDI-25-1181: Net-SNMP SnmpTrapd Agent Message Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1181
- **ZDI-CAN:** ZDI-CAN-27507
- **Date:** 2025-12-23
- **CVE:** CVE-2025-68615
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Net-SNMP
- **Affected Products:** Net-SNMP
- **Credit:** buddurid
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Net-SNMP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SnmpTrapd service, which listens on UDP port 162 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Net-SNMP has issued an update to correct this vulnerability. More details can be found at: https://github.com/net-snmp/net-snmp/security/advisories/GHSA-4389-rwqf-q9gq

## Disclosure Timeline

- 2025-07-25 - Vulnerability reported to vendor
- 2025-12-23 - Coordinated public release of advisory
- 2025-12-23 - Advisory Updated
