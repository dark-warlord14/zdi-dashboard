# ZDI-19-293: Advantech WebAccess Node tv_enua Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-293
- **ZDI-CAN:** ZDI-CAN-7909
- **Date:** 2019-03-28
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within tv_enua.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/06/19 – ZDI sent the vulnerability report to ICS-CERT 02/12/19 – ICS-CERT replied with tracking number 03/08/19 – ICS-CERT advised ZDI the vendor was working on a fix for some issues and provided a report, but also advised that this issue would not be fixed 03/13/19 – ZDI notified the vendor that the report will be published as 0-day on 03/28/19 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-01-22 - Vulnerability reported to vendor
- 2019-03-28 - Coordinated public release of advisory
