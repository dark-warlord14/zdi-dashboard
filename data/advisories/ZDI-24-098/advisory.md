# ZDI-24-098: Schneider Electric Easergy Studio InitializeChannel Deserialization of Untrusted Data Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-098
- **ZDI-CAN:** ZDI-CAN-21065
- **Date:** 2024-02-08
- **CVE:** CVE-2023-7032
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** Easergy Studio
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-098/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric Easergy Studio. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the InitializeChannel method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

https://www.cisa.gov/news-events/ics-advisories/icsa-24-011-05 https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2024-009-02&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2024-009-02.pdf

## Disclosure Timeline

- 2023-06-09 - Vulnerability reported to vendor
- 2024-02-08 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
