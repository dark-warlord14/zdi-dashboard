# ZDI-25-209: (Pwn2Own) Synology BeeStation BST150-4T Cleartext Transmission of Sensitive Information Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-209
- **ZDI-CAN:** ZDI-CAN-25617
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10445
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-209/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to spoof specific configuration values on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloading of configuration information at boot time. The issue results from the use of an insecure protocol to download a configuration file. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_20

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
