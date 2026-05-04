# ZDI-24-191: Schneider Electric EcoStruxure IT Gateway Hard-Coded Credentials Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-191
- **ZDI-CAN:** ZDI-CAN-22087
- **Date:** 2024-02-21
- **CVE:** CVE-2024-0865
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure IT Gateway
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-191/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric EcoStruxure IT Gateway. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2024-044-03&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2024-044-03.pdf

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-02-21 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
