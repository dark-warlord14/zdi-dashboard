# ZDI-24-1736: (0Day) Paessler PRTG Network Monitor SNMP Cross-Site Scripting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1736
- **ZDI-CAN:** ZDI-CAN-23371
- **Date:** 2024-12-30
- **CVE:** CVE-2024-12833
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Paessler
- **Affected Products:** PRTG Network Monitor
- **Credit:** Andreas Finstad
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1736/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Paessler PRTG Network Monitor. Some user interaction on the part of an administrator is required to exploit this vulnerability. The specific flaw exists within the PRTG Network Monitor web interface. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

03/13/24 – ZDI reported the vulnerability to the vendor 11/19/24 - ZDI asked for updates 12/16/24 - ZDI notified the vendor of the intention to publish the case as 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application On 01/09/24 The vendor addressed the issue in PRTG version 25.1.102.1373 https://www.paessler.com/prtg/history/stable

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2024-12-30 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
