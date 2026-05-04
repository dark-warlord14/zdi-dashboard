# ZDI-19-452: (0Day) Hewlett Packard Enterprise Intelligent Management Center iccSelectDevType Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-452
- **ZDI-CAN:** ZDI-CAN-6857
- **Date:** 2019-05-09
- **CVE:** CVE-2019-11941
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-452/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the beanName parameter provided to the iccSelectDevType.xhtml endpoint. When parsing the beanName parameter, the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/20/18 – ZDI sent the vulnerability report to the vendor 01/03/19 – The vendor replied with tracking number 01/09/19 – ZDI requested an update (for this and other related reports) 01/30/19 - The vendor PSIRT replied they were working with the engineering team to get an updated schedule 02/27/19 – ZDI asked the vendor again for any ETA for updates for this product 02/27/19 – The vendor replied they would follow up 04/24/19 – ZDI notified the vendor that the reports will be published as 0-day on 05/09 if these are not patched before -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-12-20 - Vulnerability reported to vendor
- 2019-05-09 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
