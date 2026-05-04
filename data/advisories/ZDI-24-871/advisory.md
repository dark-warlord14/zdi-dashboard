# ZDI-24-871: (Pwn2Own) Silicon Labs Gecko OS HTTP Request Handling Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-871
- **ZDI-CAN:** ZDI-CAN-23245
- **Date:** 2024-06-21
- **CVE:** CVE-2025-2837
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Silicon Labs
- **Affected Products:** Gecko OS
- **Credit:** Jack Dates of RET2 Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-871/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Silicon Labs Gecko OS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP requests. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Silicon Labs has issued an update to correct this vulnerability. More details can be found at: https://community.silabs.com/a45Vm0000000Atp

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2025-03-26 - Advisory Updated
