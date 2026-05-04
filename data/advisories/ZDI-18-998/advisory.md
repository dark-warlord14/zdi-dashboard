# ZDI-18-998: (0Day) Cisco WebEx Network Recording Player Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-998
- **ZDI-CAN:** ZDI-CAN-5623
- **Date:** 2018-09-06
- **CVE:** CVE-2018-0422
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Simon Zuckerbraun of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-998/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Cisco WebEx Network Recording Player. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists in the access control that the product installer sets on the product's binaries. This allows any local user to replace the product's binaries with malicious replacements. An attacker can leverage this vulnerability to escalate privileges to the level of some other user of the system, such as an administrator.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180905-webex-pe https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180905-webex-pe This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/07/18 - ZDI reported vulnerability to Vendor 02/07/18 - Vendor acknowledged and provided ZDI with a tracking number 04/07/18 - Vendor contacted ZDI stating the fix would result on an ETA release for March 2019 and requested accommodating an extension accordingly 05/01/18 - Vendor contacted ZDI requesting a status update 05/15/18 - ZDI replied denying such big extension and provided a workaround to produce a timely fix 05/18/18 - Vendor replied indicating the suggested fix would break certain installations and required additional fixes. Vendor provided a new ETA for August 2018 06/06/18 - ZDI requested the vendor for an update on the precise date 07/03/18 - Vendor provided an update indicating a new ETA of September 2018. 07/19/18 - ZDI contacted the vendor and indicated that the case was overdue and offered an extension until early August 2018 before 0-daying 07/24/18 - Vendor replied indicating the long process and requested a heads-up if we were to 0-day so a statement could be provided 08/17/18 - ZDI contacted the vendor for an update 08/29/18 - ZDI contacted the vendor again for an update 08/30/18 - Vendor replied stating fixes were expected on September 7 and the release ETA is October 3 (2018) 08/31/18 - ZDI notified the vendor that the case will 0-day on September 5 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-02-07 - Vulnerability reported to vendor
- 2018-09-06 - Coordinated public release of advisory
- 2018-09-06 - Advisory Updated
