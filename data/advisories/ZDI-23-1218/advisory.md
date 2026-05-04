# ZDI-23-1218: (0Day) LG Simple Editor Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1218
- **ZDI-CAN:** ZDI-CAN-20327
- **Date:** 2023-08-24
- **CVE:** CVE-2023-40516
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** LG
- **Affected Products:** Simple Editor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1218/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of LG Simple Editor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The product sets incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

02/13/23 – The ZDI requested a vendor PSIRT contact. 02/14/23 – The vendor provided PSIRT Contact information. 02/14/23 – The ZDI reported the vulnerability to the vendor. 08/04/23 – The ZDI asked for an update. 08/08/23 – The vendor states that they do not have plans to fix the vulnerability now or in the future. 08/21/23 – The ZDI informed the vendor that we are publishing the case as a zero-day advisory on 08/24/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
