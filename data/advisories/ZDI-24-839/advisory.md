# ZDI-24-839: (Pwn2Own) Wyze Cam v3 Cloud Infrastructure Improper Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-839
- **ZDI-CAN:** ZDI-CAN-22393
- **Date:** 2024-06-21
- **CVE:** CVE-2024-6248
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wyze
- **Affected Products:** Cam v3
- **Credit:** Rafal Goryl
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-839/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Wyze Cam v3 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the run_action_batch endpoint of the cloud infrastructure. The issue results from the use of the device's MAC address as a sole credential for authentication. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Wyze has issued an update to correct this vulnerability. More details can be found at: https://forums.wyze.com/t/security-advisory/289256

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
