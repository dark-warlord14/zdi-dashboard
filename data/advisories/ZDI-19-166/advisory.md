# ZDI-19-166: (0Day) Hewlett Packard Enterprise Intelligent Management Center SyslogTempletSelectWin Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-166
- **ZDI-CAN:** ZDI-CAN-6767
- **Date:** 2019-02-05
- **CVE:** CVE-2019-5341
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the beanName parameter provided to the SyslogTempletSelectWin.xhtml endpoint. When parsing the beanName parameter, the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/17/18 - ZDI sent the vulnerability report to the vendor 01/25/19 - ZDI notified the vendor if this is not patched that the report will be published as an 0-day on 2/5 01/30/19 - The vendor replied "We are currently checking with engineering to try to get an updated schedule for fixes for all of the outstanding ZDIs we have open. We'll let you know the status as soon as we hear back." -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-08-22 - Vulnerability reported to vendor
- 2019-02-05 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
