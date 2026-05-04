# ZDI-19-229: (0Day) Advantech WebAccess Node spchapi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-229
- **ZDI-CAN:** ZDI-CAN-7878
- **Date:** 2019-02-28
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within spchapi.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 02/04/19 – ZDI sent the vulnerability reports to ICS-CERT 02/04/19 – ICS-CERT replied with tracking number 02/18/19 – ICS-CERT advised ZDI the vendor was working on a fix for some issues and provided a reports, but also advised that 2 issues would not be fixed 02/18/19 – ZDI replied and asked if the vendor was working with the upstream vendor and ICS-CERT agreed to request clarification 02/19/19 – ICS-CERT conveyed the vendor’s reply: “These two installer is already install successfully after installing WebAccess/SCADA installer package. We think these won’t be damage on system so we will ignore these two cases.” 02/21/19 – ZDI notified the vendor if these are not patched that the reports will be published as 0-day on 02/28/19 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-02-04 - Vulnerability reported to vendor
- 2019-02-28 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
