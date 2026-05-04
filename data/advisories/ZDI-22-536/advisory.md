# ZDI-22-536: (0Day) Electronic Arts Origin Web Helper Service Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-536
- **ZDI-CAN:** ZDI-CAN-14470
- **Date:** 2022-03-24
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Electronic Arts
- **Affected Products:** Origin
- **Credit:** brsn (@brsn76945860)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-536/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Electronic Arts Origin. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Web Helper Service. By creating a symbolic link, an attacker can abuse the service to set a permissive DACL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/17/21 – ZDI reported the vulnerability to vendor 08/19/21 – The vendor acknowledged the report 08/29/21 – The vendor requested technical clarification 08/31/21 – ZDI provided additional evidence 02/22/22 – ZDI requested an update 02/22/22 – The vendor indicated the case does not meet the bar for servicing 03/16/22 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 03/24/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-08-18 - Vulnerability reported to vendor
- 2022-03-24 - Coordinated public release of advisory
- 2022-03-29 - Advisory Updated
