# ZDI-24-855: (Pwn2Own) Phoenix Contact CHARX SEC-3100 OCPP Protocol Improper Log Output Neutralization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-855
- **ZDI-CAN:** ZDI-CAN-23321
- **Date:** 2024-06-21
- **CVE:** CVE-2024-25997
- **CVSS:** 3.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-855/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to injection malicious content into log files on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of logging. The issue results from insufficient neutralization of special characters when writing to logs. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
