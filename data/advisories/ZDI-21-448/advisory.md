# ZDI-21-448: Schneider Electric C-Bus Toolkit CBZ File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-448
- **ZDI-CAN:** ZDI-CAN-12589
- **Date:** 2021-04-22
- **CVE:** CVE-2021-22718
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-448/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric C-Bus Toolkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CBZ files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

http://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-103-01 https://us-cert.cisa.gov/ics/advisories/icsa-21-105-01

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
