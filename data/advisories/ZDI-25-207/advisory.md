# ZDI-25-207: (Pwn2Own) Synology BeeStation BST150-4T Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-207
- **ZDI-CAN:** ZDI-CAN-25623
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10443
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** PHP Hooligans / Midnight Blue
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-207/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of websocket requests. When parsing the location property, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_18

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
