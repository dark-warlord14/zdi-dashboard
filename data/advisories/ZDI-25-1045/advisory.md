# ZDI-25-1045: Schneider Electric PowerChute Serial Shutdown Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1045
- **ZDI-CAN:** ZDI-CAN-27376
- **Date:** 2025-12-09
- **CVE:** CVE-2025-11565 , CVE-2025-11566 , CVE-2025-11567
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** PowerChute Serial Shutdown
- **Credit:** Aleksandar Djurdjevic (https://github.com/revengsmK)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1045/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric PowerChute Serial Shutdown. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additionally, the attacker must authenticate to the application. The specific flaw exists within the web service, which listens on TCP port 6547 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-315-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-315-01.pdf https://www.cisa.gov/news-events/ics-advisories/icsa-25-322-04

## Disclosure Timeline

- 2025-07-03 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
