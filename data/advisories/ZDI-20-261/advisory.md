# ZDI-20-261: (0Day) Rockwell Automation FactoryTalk RNADiagnosticsSrv Deserialization Of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-261
- **ZDI-CAN:** ZDI-CAN-9309
- **Date:** 2020-02-20
- **CVE:** CVE-2020-6967
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** FactoryTalk Diagnostics
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation ThinManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RNADiagnosticsSrv endpoint, which listens on TCP port 8082 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/01/19 - ZDI reported a vulnerability to ICS-CERT 10/01/19 - ICS-CERT provided ZDI with an ICS-VU # 01/24/20 - ZDI contacted ICS-CERT requesting a status update 01/27/20 - ICS-CERT shared the vendor's preference to release the fix along with other cases reported in January 2020 01/27/20 - ZDI reminded these were different cases with different due dates and offered an extension for this particular case 02/11/20 - ZDI notified ICS-CERT the intention to publish the case as 0-day on 02/20/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-10-01 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
