# ZDI-20-191: (0Day) Hewlett Packard Enterprise Intelligent Management Center powershellConfigContent Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-191
- **ZDI-CAN:** ZDI-CAN-9009
- **Date:** 2020-02-04
- **CVE:** CVE-2020-7186
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the beanName parameter provided to the powershellConfigContent.xhtml endpoint. When parsing the beanName parameter, the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/12/19 - ZDI reported the vulnerabilities to the vendor 10/08/19 - ZDI requested acknowledgement 10/08/19 - The vendor acknowledged and provided IDs 12/12/19 - ZDI requested an update 01/09/20 - The vendor communicated that they plan to address the issues in the next release 01/09/20 - ZDI requested an ETA for the next release 01/14/20 - ZDI requested an update 01/22/20 - ZDI requested an update 01/14/20 - ZDI notified the vendor of the intention to 0-day on 02/04/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-09-12 - Vulnerability reported to vendor
- 2020-02-04 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
