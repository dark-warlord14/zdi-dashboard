# ZDI-24-872: (Pwn2Own) Silicon Labs Gecko OS DNS Response Processing Infinite Loop Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-872
- **ZDI-CAN:** ZDI-CAN-23392
- **Date:** 2024-06-21
- **CVE:** CVE-2025-2838
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Silicon Labs
- **Affected Products:** Gecko OS
- **Credit:** PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-872/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Silicon Labs Gecko OS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of DNS responses. The issue results from a logic error that can lead to an infinite loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Silicon Labs has issued an update to correct this vulnerability. More details can be found at: https://community.silabs.com/a45Vm0000000Atp

## Disclosure Timeline

- 2024-02-12 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2025-03-26 - Advisory Updated
