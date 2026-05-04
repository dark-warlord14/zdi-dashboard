# ZDI-25-925: Viessmann Vitogate 300 BN/MB vitogate.cgi form-0-2 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-925
- **ZDI-CAN:** ZDI-CAN-23861
- **Date:** 2025-10-01
- **CVE:** CVE-2025-9494
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Viessmann
- **Affected Products:** Vitogate 300
- **Credit:** adhkr - LuwakLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-925/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Viessmann Vitogate 300 BN/MB devices. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of JSON payload data provided to the vitogate.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Viessmann has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-266-04

## Disclosure Timeline

- 2025-04-29 - Vulnerability reported to vendor
- 2025-10-01 - Coordinated public release of advisory
- 2025-10-01 - Advisory Updated
