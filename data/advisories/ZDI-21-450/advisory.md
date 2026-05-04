# ZDI-21-450: Schneider Electric C-Bus Toolkit PROJECT RESTORE Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-450
- **ZDI-CAN:** ZDI-CAN-12604
- **Date:** 2021-04-22
- **CVE:** CVE-2021-22720
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-450/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric C-Bus Toolkit. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of commands sent to the C-Gate 2 Service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

http://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-103-01 https://us-cert.cisa.gov/ics/advisories/icsa-21-105-01

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
