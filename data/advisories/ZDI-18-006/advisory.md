# ZDI-18-006: (0Day) Quest NetVault Backup Server checksession Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-006
- **ZDI-CAN:** ZDI-CAN-4752
- **Date:** 2018-01-16
- **CVE:** CVE-2018-1163
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Quest
- **Affected Products:** NetVault Backup
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-006/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Quest NetVault Backup. The specific flaw exists within JSON RPC Request handling. By setting the checksession parameter to a specific value, it is possible to bypass authentication to critical functions. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/26/17 - ZDI wrote to Dell requesting a disclosure contact for the product 05/29/17 - Dell responded and provided a vendor contact at Quest 05/29/17 - ZDI reached out to the provided contact 05/30/17 - The contact provided a PGP key to accept disclosure 06/20/17 - The contact provided a group mailing list for further disclosures 05/30/17 - 6/22/17 - ZDI reported 25 vulnerabilities to the contact and/or the group list 07/03/17 - The vendor asked clarifying questions 07/03/17 - ZDI responded 07/10/17 - ZDI responded with further information 11/02/17 - ZDI wrote the contact and the group list requesting a status update 11/17/17 - The ZDI PM called and left a message for the contact and emailed the contact and the group list requesting a status update 12/06/17 - The ZDI PM met with the vendor team by phone at their request and explained the intent to 0-day the reports This is now fixed with NetVault v11.4.5.15. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2017-12-06 - Vulnerability reported to vendor
- 2018-01-16 - Coordinated public release of advisory
