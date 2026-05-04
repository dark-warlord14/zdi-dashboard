# ZDI-21-1279: Schneider Electric C-Bus Toolkit CONFIG SAVE Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1279
- **ZDI-CAN:** ZDI-CAN-12585
- **Date:** 2021-11-08
- **CVE:** CVE-2021-22748
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric C-Bus Toolkit. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of commands sent to the C-Gate 2 Service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-105-01

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-11-08 - Coordinated public release of advisory
