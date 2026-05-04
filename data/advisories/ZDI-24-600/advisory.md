# ZDI-24-600: Schneider Electric APC Easy UPS Online startRun Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-600
- **ZDI-CAN:** ZDI-CAN-21034
- **Date:** 2024-06-11
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-600/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SchneiderUPS.exe desktop application. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in The APC Easy UPS Online Monitoring Software v2.5-GA-01-23116 https://download.schneider-electric.com/files?p_Doc_Ref=SPD_CCON-APCMONREL_EN&p_enDocType=Quick+start+guide&p_File_Name=APC+Easy+UPS+Online+Monitoring+Software+Release+Notes+-+2.6-GA-01-23116.pdf

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2024-06-11 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
