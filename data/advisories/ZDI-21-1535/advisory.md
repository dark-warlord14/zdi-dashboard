# ZDI-21-1535: McAfee Database Security Improper Access Control Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1535
- **ZDI-CAN:** ZDI-CAN-14792
- **Date:** 2021-12-14
- **CVE:** CVE-2021-31850
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Database Security
- **Credit:** Jokubas Arsoba (ikth)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1535/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of McAfee Database Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the McAfee DBS service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10358

## Disclosure Timeline

- 2021-10-21 - Vulnerability reported to vendor
- 2021-12-14 - Coordinated public release of advisory
