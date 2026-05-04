# ZDI-24-873: (Pwn2Own) Silicon Labs Gecko OS HTTP GET Request Handling Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-873
- **ZDI-CAN:** ZDI-CAN-23396
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23973
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Silicon Labs
- **Affected Products:** Gecko OS
- **Credit:** PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-873/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Silicon Labs Gecko OS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP GET requests. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Silicon Labs has issued an update to correct this vulnerability. More details can be found at: https://community.silabs.com/a45Vm0000000Atp

## Disclosure Timeline

- 2024-03-07 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
