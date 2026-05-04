# ZDI-23-1059: (0Day) (Pwn2Own) Softing edgeAggregator Permissive Cross-domain Policy with Untrusted Domains Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1059
- **ZDI-CAN:** ZDI-CAN-20542
- **Date:** 2023-08-09
- **CVE:** CVE-2023-38125
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeAggregator
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing edgeAggregator. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of the web server. The issue results from the lack of appropriate Content Security Policy headers. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

02/15/23 – The ZDI reported this vulnerability to the vendor during the Pwn2Own Miami contest. 02/20/23 – The vendor states they would review and report back with the security advisories. 03/08/23 – The vendor requested CVE Numbers. 03/15/23 – ZDI provided the vendor with CVE numbers. 07/31/23 – ZDI asked for an update. 08/03/23 – ZDI asked for an update. 08/07/23 – The ZDI asked for an update and informed the vendor that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
