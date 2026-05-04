# ZDI-19-457: (0Day) Hewlett Packard Enterprise Intelligent Management Center AMF3 Externalizable Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-457
- **ZDI-CAN:** ZDI-CAN-6807
- **Date:** 2019-05-09
- **CVE:** CVE-2019-11944
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-457/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling AMF3 requests to the amf endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/09/19 - ZDI sent the vulnerability report to the vendor 01/09/19 - The vendor replied with tracking number 01/30/19 - The vendor PSIRT mentioned they were working with the engineering team to get an updated schedule 02/27/19 - ZDI asked the vendor again for any ETA for updates for this product 02/27/19 - The vendor replied they would follow up 04/24/19 - ZDI notified the vendor that the reports will be published as 0-day on 05/09 if these are not patched before -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-01-09 - Vulnerability reported to vendor
- 2019-05-09 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
