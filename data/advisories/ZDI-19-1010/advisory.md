# ZDI-19-1010: (0Day) Advantech WebAccess Node BwOpcBs Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1010
- **ZDI-CAN:** ZDI-CAN-7883
- **Date:** 2019-12-12
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within BwOpcBs.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 02/04/19 – ZDI provided the report to ICS-CERT 02/05/19 - ICS-CERT acknowledged the report and provided an ICS-VU# 03/22/19 - The vendor advised ICS-CERT that the vulnerability was in a 3rd party binary and that because they were missing the source code would not fix it 03/25/19 - ZDI requested the 3rd party vendor name and asked had the vendor reported it to the 3rd party 10/07/19 - ZDI asked ICS-CERT again for some details, including: the 3rd party vendor name and whether the vendor reported it to the 3rd party 10/08/19 - ICS-CERT replied that they "have made multiple requests to <the vendor> for the identity of the 3rd party, but no response" -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-02-04 - Vulnerability reported to vendor
- 2019-12-12 - Coordinated public release of advisory
