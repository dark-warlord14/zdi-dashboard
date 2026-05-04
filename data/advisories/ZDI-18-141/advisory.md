# ZDI-18-141: ABB MicroSCADA Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-141
- **ZDI-CAN:** ZDI-CAN-5097
- **Date:** 2018-02-06
- **CVE:** CVE-2018-1168
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:H/Au:S/C:C/I:C/A:C
- **Affected Vendors:** ABB
- **Affected Products:** MicroSCADA
- **Credit:** Fritz Sands - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-141/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of ABB MicroSCADA. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of the access controls for the installed product files. The installation procedure leaves critical files open to manipulation by any authenticated user. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://library.e.abb.com/public/7a88a74b12bb492ea138b1f2365d00f6/ABBVU-PGGA-33888_ABB_SoftwareVulnerabilityHandlingAdvisory_Rev_A.pdf?x-sign=MJfu9cHtRUUubpLAYzyWFTmW5W+mg3kZ/nm7F/Jw5HlFTQf4eNyfLAgE8HozRJEC

## Disclosure Timeline

- 2017-08-18 - Vulnerability reported to vendor
- 2018-02-06 - Coordinated public release of advisory
- 2018-02-07 - Advisory Updated
