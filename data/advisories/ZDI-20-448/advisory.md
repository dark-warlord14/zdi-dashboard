# ZDI-20-448: (0Day) Advantech WebAccess IOCTL 0x2711 BwPSLink Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-448
- **ZDI-CAN:** ZDI-CAN-10173
- **Date:** 2020-04-08
- **CVE:** CVE-2020-12010
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-448/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x2711, which can be used to invoke BwPSLink.exe. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/28/20 – ZDI reported the vulnerabilities to ICS-CERT 03/06/20 – ICS-CERT provided ZDI with an ICS-VU # 03/26/20 – The vendor communicated that they will rely on existing measures and will add no amendments to the code 03/30/20 – ZDI notified ICS-CERT of the intention to publish the cases as 0-day advisories on 04/08/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-02-28 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
