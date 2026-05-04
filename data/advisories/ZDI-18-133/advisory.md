# ZDI-18-133: (0Day) Belkin Wemo Link syseventd Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-133
- **ZDI-CAN:** ZDI-CAN-5095
- **Date:** 2018-01-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Belkin
- **Affected Products:** Wemo Link
- **Credit:** Dove Chiu and Kenney Lu of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Belkin Wemo Link. Authentication is not required to exploit this vulnerability. The specific flaw exists within the syseventd daemon, which listens on TCP port 52367 by default. The issue results from the lack of authentication prior to allowing alterations to the system configuration. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/18/17 - ZDI reported vulnerability to vendor 01/18/18 - ZDI notified the vendor the intention to 0-day the case -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2017-08-18 - Vulnerability reported to vendor
- 2018-01-23 - Coordinated public release of advisory
