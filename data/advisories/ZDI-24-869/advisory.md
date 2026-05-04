# ZDI-24-869: (Pwn2Own) Silicon Labs Gecko OS Debug Interface Format String Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-869
- **ZDI-CAN:** ZDI-CAN-23189
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23937
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Silicon Labs
- **Affected Products:** Gecko OS
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-869/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Silicon Labs Gecko OS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the debug interface. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

Silicon Labs has issued an update to correct this vulnerability. More details can be found at: https://community.silabs.com/a45Vm0000000Atp

## Disclosure Timeline

- 2024-02-12 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
