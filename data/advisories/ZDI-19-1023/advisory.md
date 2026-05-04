# ZDI-19-1023: (0Day) Microsoft Windows WebDAV Path Parsing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1023
- **ZDI-CAN:** ZDI-CAN-9278
- **Date:** 2019-12-17
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Joshua Graham of TSS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebDAV paths. A crafted WebDAV path can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 08/29/19 – ZDI reported the vulnerability to the vendor 08/29/19 – The vendor acknowledged the report 11/06/19 – the vendor replied that the report did not lead to code execution and did not meet the bar for security servicing 11/11/19 – The vendor requested ZDI agreement 11/26/19 – ZDI indicated to the vendor our disagreement and sent additional evidence demonstrating code execution 11/26/19 – The vendor agreed to view the additional material 12/05/19 – ZDI and the vendor met by phone to discuss multiple cases and the vendor advised ZDI that the attack vector does not meet the bar for security servicing due to user interaction 12/09/19 - ZDI advised the vendor of the intent to publish the report as 0-day on 12/17/19 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-08-29 - Vulnerability reported to vendor
- 2019-12-17 - Coordinated public release of advisory
