# ZDI-25-621: (Pwn2Own) Phoenix Contact CHARX SEC-3150 DHCP Configuration Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-621
- **ZDI-CAN:** ZDI-CAN-26350
- **Date:** 2025-07-21
- **CVE:** CVE-2025-25269
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3150
- **Credit:** HT3 Labs (@ht3labs)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-621/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Phoenix Contact CHARX SEC-3150 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration service, which listens on TCP port 5001 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://certvde.com/en/advisories/VDE-2025-019/

## Disclosure Timeline

- 2025-03-04 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated
