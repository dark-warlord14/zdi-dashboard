# ZDI-19-169: (0Day) Hewlett Packard Enterprise Intelligent Management Center UrlAccessController Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-169
- **ZDI-CAN:** ZDI-CAN-6769
- **Date:** 2019-02-05
- **CVE:** CVE-2019-5347
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-169/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UrlAccessController servlet. The issue results from the lack of proper filtering of URLs. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/17/18 - ZDI sent the vulnerability report to the vendor 01/25/19 - ZDI notified the vendor if this is not patched that the report will be published as an 0-day on 2/5 01/30/19 - The vendor replied "We are currently checking with engineering to try to get an updated schedule for fixes for all of the outstanding ZDIs we have open. We'll let you know the status as soon as we hear back." -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-08-29 - Vulnerability reported to vendor
- 2019-02-05 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
